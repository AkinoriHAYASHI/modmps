"""Modules to request to https://www.googleapis.com/oauth2/v3/token

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

from modmps.http import oauth2

class AccessTokenRequester(oauth2.AccessTokenRequester):
    def __init__(self, code, client_id, client_secret, redirect_uri, grant_type='authorization_code'):
        base_url = 'https://www.googleapis.com/oauth2/v3/token'
        extra_params = {
            'client_secret': client_secret
        }
        super(AccessTokenRequester, self).__init__(base_url, code, redirect_uri, client_id, grant_type, extra_params)

class AccessTokenRefreshRequester(oauth2.AccessTokenRefreshRequester):
    def __init__(self, refresh_token, client_id, client_secret, grant_type='refresh_token'):
        base_url = 'https://www.googleapis.com/oauth2/v3/token'
        extra_params = {
            'client_id': client_id,
            'client_secret': client_secret
        }
        super(AccessTokenRefreshRequester, self).__init__(base_url, refresh_token,
                                                          grant_type=grant_type, extra_params=extra_params)