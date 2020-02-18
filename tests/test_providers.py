#!/usr/bin/env python

import pathlib
import json
import unittest
from optimade.models import InfoResponse, LinksResponse

TOP_DIR = pathlib.Path(__file__).parent.parent

class ProvidersValidator(unittest.TestCase):

    def test_info(self):
        """ Validates the index.html json fudge as a `BaseInfoResource` object. """
        info_dir = TOP_DIR / 'src' / 'info'
        versions = [v.parts[-1] for v in info_dir.iterdir() if v.is_dir() and v.parts[-1].startswith('v')]
        for v_ind, version in enumerate(versions):
            path = pathlib.Path(f"/{TOP_DIR}/src/info/{version}/info.json").resolve()
            with open(path, 'r') as f:
                json_rep = json.load(f)
            InfoResponse(**json_rep)

    def test_providers(self):
        """ Validates the providers.json as a list of `Provider`s objects. """
        links_dir = TOP_DIR / 'src' / 'links'
        versions = [v.parts[-1] for v in links_dir.iterdir() if v.is_dir() and v.parts[-1].startswith('v')]
        for v_ind, version in enumerate(versions):
            path = pathlib.Path(f"{TOP_DIR}/src/links/{version}/providers.json").resolve()
            with open(path, 'r') as f:
                json_rep = json.load(f)
            LinksResponse(**json_rep)
        
