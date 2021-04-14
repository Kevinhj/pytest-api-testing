from wooapitest.src.configs.hosts_config import API_HOSTS
from requests_oauthlib import OAuth1
from wooapitest.src.utilities.credentialsUtility import CredentialsUtility
import requests
import os
import json
import logging as logger


class RequestUtility(object):

    def __init__(self):
        wc_creds = CredentialsUtility.get_wc_api_keys()

        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secret'])

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, F"Bad Status code." \
            F"Expected {self.expected_status_code}, Actual status code is: {self.status_code}" \
            F"URL: {self.url}, Response Json: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API response: {self.rs_json}")

        return self.rs_json

    def get(self):
        pass
