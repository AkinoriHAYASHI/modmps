"""Modules to request to https://www.googleapis.com/plus/v1/people

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

class PeopleApiExecutor(ApiExecutor):
    def __init__(self, user_id, callback=None, fields=None, key=None, access_token=None, prettyPring=None, userIp=None):
        base_url = 'https://www.googleapis.com/plus/v1/people/%s' % user_id

        if key is None and access_token is None:
            raise Exception('Either key or access_token should be specified.')
        elif key is not None and access_token is not None:
            raise Exception('Only either key or access_token should be specified.')

        params = {
            'callback': callback,
            'fields': fields,
            'key': key,
            'access_token': access_token,
            'prettyPring': prettyPring,
            'userIp': userIp,
        }

        super(PeopleApiExecutor, self).__init__(base_url, params)