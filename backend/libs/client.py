import os
import json

import requests
from rest_framework import status


class Client(object):

    def __init__(self, base_url, auth=(), *args, **kwargs):
        self.base_url = base_url
        self.auth = auth
        return super().__init__(*args, **kwargs)

    def get_base_url(self, endpoint):
        return self.base_url + endpoint

    def get_auth(self):
        return self.auth

    def get_headers(self, original_headers):
        headers = original_headers.copy()
        headers.setdefault('content-type', 'application/json')
        return headers

    def get(self, endpoint, params=None, headers={}, **kwargs):
        try:
            req = requests.get(self.get_base_url(endpoint), auth=self.get_auth(), params=params,
                               headers=self.get_headers(headers), **kwargs)
            req.raise_for_status()
            return json.loads(req.content)
        except requests.exceptions.HTTPError as e:
            raise ClientError(req.status_code, req.content, str(e))
        except Exception as e:
            raise ClientError(status.HTTP_408_REQUEST_TIMEOUT,
                              'Terjadi Kesalahan Pada Sistem, Silahkan Mencoba Kembali', str(e))

    def post(self, endpoint, headers={}, **kwargs):
        try:
            req = requests.post(self.get_base_url(endpoint), auth=self.get_auth(),
                                headers=self.get_headers(headers), **kwargs)
            req.raise_for_status()
            return json.loads(req.content)
        except requests.exceptions.HTTPError as e:
            raise ClientError(req.status_code, req.content, str(e))
        except Exception as e:
            raise ClientError(status.HTTP_408_REQUEST_TIMEOUT,
                              'Terjadi Kesalahan Pada Sistem, Silahkan Mencoba Kembali', str(e))

    def patch(self, endpoint, headers={}, **kwargs):
        try:
            req = requests.patch(self.get_base_url(endpoint), auth=self.get_auth(),
                                 headers=self.get_headers(headers), **kwargs)
            return json.loads(req.content)
        except requests.exceptions.HTTPError as e:
            raise ClientError(req.status_code, req.content, str(e))
        except Exception as e:
            raise ClientError(status.HTTP_408_REQUEST_TIMEOUT,
                              'Terjadi Kesalahan Pada Sistem, Silahkan Mencoba Kembali', str(e))


class ClientError(Exception):

    def __init__(self, code, message, error):
        Exception.__init__(self, "%d: %s - %s" % (code, message, error))
        self.code = code
        self.message = message
        self.error = error
