#!/usr/bin/env python

import pathlib
import json
import ssl
import unittest
import urllib.request
import urllib.parse

from optimade.models import InfoResponse, LinksResponse

TOP_DIR = pathlib.Path(__file__).parent.parent

apply_v0_workarounds = True # To be disabled if/when we do not wish to allow to point to v0 endpoints

def query_optimade(url):
    """Perform a URL request to the given URL endpoint.

    However, for requests to `providers.optimade.org`, uses the local files
    rather than going to fetch it on the web.
    This is important to allow testing of new endpoints before the PR
    is merged in GitHub (and only after things are merged in the main branch,
    they will appear on `providers.optimade.org`)
    
    :param url: a string with the URL to fetch
    :return: the raw content.
    :raise urllib.error.HTTPError: if the page is not found. Note that this exception
        is raised also when emulating a request from the local disk for
        `providers.optimade.org` and the file is not found; in this case the code is 404.
    """
    # Set to True for now - we might want to decide that this is a problem instead
    # and set this to False
    ignore_SSL_errors = True

    # Create the context, possibly ignoring SSL errors
    ctx = ssl.create_default_context()
    if ignore_SSL_errors:
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.netloc == 'providers.optimade.org':
        # Strip initial /
        path = parsed_url.path[1:] if parsed_url.path.startswith('/') else parsed_url.path
        # Remove any pending slashes
        path =  path[:-1] if path.endswith('/') else path
        # Append the .json extension
        path += ".json"
        # Create the abs path to the file
        file_path = TOP_DIR / 'src' / path
        try:
            with open(file_path) as fhandle:
                response_content = fhandle.read()
        except FileNotFoundError:
            raise urllib.error.HTTPError(
                url=url, code=404, msg="HTTP Error 404: Not Found", hdrs="", fp="")
    else:
        with urllib.request.urlopen(url, context=ctx) as url_response:
            response_content = url_response.read()
    
    return response_content


class ProvidersValidator(unittest.TestCase):

    def test_info(self):
        """ Validates the index.html json fudge as a `BaseInfoResource` object. """
        info_dir = TOP_DIR / 'src' / 'info'
        versions = [
            v.parts[-1] for v in info_dir.iterdir()
            if v.is_dir() and v.parts[-1].startswith('v')
        ]
        for version in versions:
            path = pathlib.Path(f"/{TOP_DIR}/src/info/{version}/info.json").resolve()
            with open(path, 'r') as f:
                json_rep = json.load(f)
            InfoResponse(**json_rep)


    def test_providers(self):
        """ Validates the providers.json as a list of `Provider`s objects. """
        links_dir = TOP_DIR / 'src' / 'links'
        versions = [v.parts[-1] for v in links_dir.iterdir() if v.is_dir() and v.parts[-1].startswith('v')]
        for version in versions:
            path = pathlib.Path(f"{TOP_DIR}/src/links/{version}/providers.json").resolve()
            with open(path, 'r') as f:
                json_rep = json.load(f)
            LinksResponse(**json_rep)

 
    def test_index_metadb(self):
        """ Validates that all (non-null) entries in providers.json point to an index meta-db. """
        # We collect all errors and report all of them at the end, see below
        problems = []

        links_dir = TOP_DIR / 'src' / 'links'
        versions = [v.parts[-1] for v in links_dir.iterdir() if v.is_dir() and v.parts[-1].startswith('v')]
        for version in versions:
            path = pathlib.Path(f"{TOP_DIR}/src/links/{version}/providers.json").resolve()
            with open(path, 'r') as f:
                json_rep = json.load(f)
            response = LinksResponse(**json_rep)
            for entry in response.data:
                if entry.attributes.base_url is not None:
                    # the provider has a non-null base_url

                    # I check the /info endpoint
                    info_endpoint = f'{entry.attributes.base_url}/{version}/info'
                    tested_info_endpoints = [info_endpoint]                    
                    try:
                        try:
                            response_content = query_optimade(info_endpoint)
                        except urllib.error.HTTPError as exc:
                            if apply_v0_workarounds and version == 'v1' and exc.code == 404:
                                try:
                                    # Temporary workaround for optimade-python-tools while v1 is released
                                    info_endpoint = f'{entry.attributes.base_url}/v0.10/info'
                                    tested_info_endpoints.append(info_endpoint)
                                    response_content = query_optimade(info_endpoint)
                                except urllib.error.HTTPError as exc:
                                    # Temporary workaround for nomad that uses v0 as a prefix
                                    info_endpoint = f'{entry.attributes.base_url}/v0/info'
                                    tested_info_endpoints.append(info_endpoint)
                                    response_content = query_optimade(info_endpoint)                              
                            else:
                                raise
                    except urllib.error.HTTPError as exc:
                        fallback_string = "" if len(tested_info_endpoints) == 1 else f" (I tried all these URLs: {tested_info_endpoints})"
                        problems.append(f'[ERROR] Provider "{entry.id}" {info_endpoint} endpoint is not reachable{fallback_string}. Error: {str(exc)}')
                        continue

                    try:
                        info_response = InfoResponse(**json.loads(response_content))
                    except Exception as exc:
                        problems.append(f'[ERROR] Provider "{entry.id}": {info_endpoint} endpoint has problems during validation. Error:\n{str(exc)}')
                        continue

                    # If unspecified, it should be assumed as False, according to the OPTIMADE specs
                    is_index = info_response.data.attributes.dict().get('is_index', False)
                    if not is_index:
                        print(f"[ERROR]  > PROBLEM DETECTED with provider '{entry.id}'.")
                        print(response_content)
                        problems.append(f'[ERROR] Provider "{entry.id}" is NOT providing an index meta-database at {info_endpoint}')
                        continue
                
                    print(f'[INFO] Provider "{entry.id}" ({version}) validated correctly ({info_endpoint})')
                                
        # I am collecting all problems and printing at the end because in this way we get a full overview
        # of the 
        if problems:
            print("[ERROR] PROBLEMS DETECTED!\n\n" + "\n".join(problems))
            raise AssertionError("[ERROR] PROBLEMS DETECTED!\n\n" + "\n".join(problems))
