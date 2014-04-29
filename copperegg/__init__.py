# -*- coding: utf-8 -*-

"""Python wrapper for the CopperEgg API
"""

__author__ = "Pål Nilsen (@maedox)"
__version__ = "0.1"


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
        if method not in ("get", "post", "put"):
            raise self.APIError(
                """Unsupported request method: {0}\n"""
                """Must be one of: get, post, put""".format(method))

        url = "{0}{1}".format(self.api_url, url_path)

        if method is "get":
            req = requests.request(method, url)
        else:
            req = requests.request(method, url, data=data)

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
