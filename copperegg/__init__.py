# -*- coding: utf-8 -*-

"""Python wrapper for the CopperEgg API
"""

__author__ = "Pål Nilsen (@maedox)"
__version__ = "0.1"


import json

try:
    import requests
except ImportError:
    print("""The requests module is required. """
          """See http://docs.python-requests.org/ for instructions.""")
    raise


class CopperEgg(object):

    def __init__(self):
        self.api_url = "https://api.copperegg.com"
        self.probes_list_path = "/v2/revealuptime/probes.json"
        self.probes_path = "/v2/revealuptime/probes"

    class APIError(Exception):

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return self.value

    def call_api(self, method, url_path, data=None):
        if method not in ("get", "post", "put", "delete"):
            raise self.APIError(
                """Unsupported request method: {0}\n"""
                """Must be one of: get, post, put""".format(method))

        url = "{0}{1}".format(self.api_url, url_path)
        timeout = 20  # seconds

        if method in ("get", "delete"):
            req = requests.request(method, url, timeout=timeout)
        else:
            headers = {'content-type': 'application/json'}
            req = requests.request(method, url, data=json.dumps(data),
                                   headers=headers, timeout=timeout)

        if req.status_code == 200:
            return req.json() or None
        else:
            raise self.APIError(req.text)

    def get_probe_path(self, probe_id):
        return "{0}/{1}.json".format(self.probes_path, probe_id)

    def get_probe(self, probe_id):
        path = self.get_probe_path(probe_id)
        return self.call_api("get", path)

    def list_probes(self):
        return self.call_api("get", self.probes_list_path)

    def update_probe(self, probe_id, data):
        path = self.get_probe_path(probe_id)
        return self.call_api("put", path, data)

    def add_probe(self, data):
        for param in ('probe_desc', 'type', 'probe_dest'):
            if param not in data:
                raise self.APIError("probe_desc, type and probe_dest are "
                                    "required parameters when adding a probe.")
        return self.call_api("post", self.probes_list_path, data)

    def delete_probe(self, probe_id):
        path = self.get_probe_path(probe_id)
        return self.call_api("delete", path)
