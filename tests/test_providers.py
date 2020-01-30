#!/usr/bin/env python

import pathlib
import json
import unittest
from optimade.models import InfoResponse, LinksResponse

TOP_DIR = pathlib.Path(__file__).parent.parent
VERSIONS = [v.parts[-1] for v in TOP_DIR.iterdir() if v.is_dir() and v.parts[-1].startswith('v')]


class ProvidersValidator(unittest.TestCase):

    def test_info(self):
        """ Validates the index.html json fudge as a `BaseInfoResource` object. """
        for v_ind, version in enumerate(VERSIONS):
            path = pathlib.Path(f"/{TOP_DIR}/{version}/info/index.html").resolve()
            with open(path, 'r') as f:
                json_rep = json.load(f)
            InfoResponse(**json_rep)

    def test_providers(self):
        """ Validates the providers.json as a list of `Provider`s objects. """
        for v_ind, version in enumerate(VERSIONS):
            path = pathlib.Path(f"{TOP_DIR}/src/{version}/providers.json").resolve()
            with open(path, 'r') as f:
                json_rep = json.load(f)
            LinksResponse(**json_rep)
