"""A module to be authenticated by google through OAuth2.

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

from modmps.http.oauth2.base import base

class AuthRequester(base.AuthRequester):
    def __init__(self, client_id, redirect_uri, scope, response_type='code', state=None,
                 access_type='online', approval_prompt='auto', login_hint=None, include_granted_scopes='false'):
        base_url = 'https://accounts.google.com/o/oauth2/auth'

        extra_params = {
            'access_type': access_type,
            'approval_prompt': approval_prompt,
            'login_hint': login_hint,
            'include_granted_scopes': include_granted_scopes,
        }

        super(AuthRequester, self).__init__(base_url,
                                            client_id, response_type, redirect_uri, scope, state, extra_params)


class AccessTokenRequester(base.AccessTokenRequester):
    def __init__(self, code, client_id, client_secret, redirect_uri, grant_type='authorization_code'):
        base_url = 'https://www.googleapis.com/oauth2/v3/token'
        extra_params = {
            'client_secret': client_secret
        }
        super(AccessTokenRequester, self).__init__(base_url, code, redirect_uri, client_id, grant_type, extra_params)

class AccessTokenRefreshRequester(base.AccessTokenRefreshRequester):
    def __init__(self, refresh_token, client_id, client_secret, grant_type='refresh_token'):
        base_url = 'https://www.googleapis.com/oauth2/v3/token'
        extra_params = {
            'client_id': client_id,
            'client_secret': client_secret
        }
        super(AccessTokenRefreshRequester, self).__init__(base_url, refresh_token,
                                                          grant_type=grant_type, extra_params=extra_params)