"""A general module to use OAuth2.

(c) 2015 Morning Project Samurai

This file is part of modmps.
modmps is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.

modmps is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = 'Junya Kaneko <junya@mpsamurai.org>'

from modmps.http.api_executor import ApiExecutor

class StateGenerator:
    def gen(self):
        return 0

class AuthRequester(ApiExecutor):
    def __init__(self,
                 base_url, client_id, response_type='code', redirect_uri=None, scope=None, state=None, extra_params={}, state_generator=StateGenerator()):
        params = {
            'response_type': response_type,
            'client_id': client_id,
            'redirect_uri': redirect_uri,
            'scope': scope,
            'state': state,
        }

        if params['state'] is None:
            params['state'] = state_generator.gen()

        params.update(extra_params)
        super(AuthRequester, self).__init__(base_url, params)

    @property
    def state(self):
        return self._parameters['state']

    def get_url(self, parameters={}):
        return self._get_url_with_query_string(parameters)

class AccessTokenRequester(ApiExecutor):
    def __init__(self, base_url, code, redirect_uri, client_id, grant_type='authorization_code', extra_params={}):
        params = {
            'grant_type': grant_type,
            'code': code,
            'redirect_uri': redirect_uri,
            'client_id': client_id
        }
        params.update(extra_params)
        super(AccessTokenRequester, self).__init__(base_url, params)

    def get_token(self, parameters={}):
        return self.post_data(parameters)

class AccessTokenRefreshRequester(ApiExecutor):
    def __init__(self, base_url, refresh_token, scope=None, grant_type='refresh_token', extra_params={}):
        params = {
            'grant_type': grant_type,
            'refresh_token': refresh_token,
            'scope': scope,
        }
        params.update(extra_params)
        super(AccessTokenRefreshRequester, self).__init__(base_url, params)

    def get_token(self, parameters={}):
        return self.post_data(parameters)