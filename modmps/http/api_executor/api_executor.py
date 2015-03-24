"""A general module to execute web apis.

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

__author__ = 'Akinori Hayashi, Junya Kaneko <junya@mpsamurai.org>'

from urllib import parse, request
import json
import xmltodict
from modmps.http.api_executor import exceptions

class ApiExecutor:
    """Executing web api with GET or POST method."""

    JSON_FORMAT = 0
    XML_FORMAT = 1

    def __init__(self, base_url, parameters):
        self.__base_url = base_url
        self.__parameters = parameters

    @property
    def _base_url(self):
        return self.__base_url

    @property
    def _parameters(self):
        return self.__parameters

    def _get_default_query(self):
        default_query = {}
        for key in self._parameters.keys():
            if self._parameters[key] is not None:
                default_query[key] = self._parameters[key]
        return default_query

    def _update_query(self, parameters, default_query):
        for key in parameters.keys():
            if key in self._parameters.keys():
                default_query[key] = parameters[key]
            else:
                raise exceptions.InvalidApiParameter(self.__class__.__name__, key)
        return default_query

    def _get_query(self, parameters):
        default_query = self._get_default_query()
        query = self._update_query(parameters, default_query)
        return query

    def _get_query_string(self, parameters):
        query = self._get_query(parameters)
        return parse.urlencode(query)

    def _get_url_with_query_string(self, parameters):
        return self._base_url + '?' + self._get_query_string(parameters)

    def _get_response_by_get(self, parameters):
        url = self._get_url_with_query_string(parameters)
        return request.urlopen(url)

    def _get_response_by_post(self, parameters, encode_to='utf-8'):
        url = self._base_url
        query_string = self._get_query_string(parameters)
        request_obj = request.Request(url=url, data=query_string.encode(encode_to))
        return request.urlopen(request_obj)

    def _get_response(self, parameters, method='get', encode_to='utf-8'):
        if method == 'get':
            response = self._get_response_by_get(parameters)
        elif method == 'post':
            response = self._get_response_by_post(parameters, encode_to)
        else:
            raise exceptions.InvalidHttpMethod(self.__class__.__name__, method)
        response_code = response.getcode()
        if response_code == 200 or response_code == 304:
            return response
        else:
            raise exceptions.ApiExecutionFailure(self.__class__.__name__)

    def _check_data_format(self, response):
        content_type = response.info()['Content-Type']
        if content_type.find('json') != -1:
            return self.JSON_FORMAT
        elif content_type.find('xml') != -1:
            return self.XML_FORMAT
        else:
            exceptions.UnknownDataFormat(self.__class__.__name__)

    def _convert_xml_to_json(self, byte_data):
        return xmltodict.parse(byte_data)

    def _execute(self, parameters={}, method='get', encode_to='utf-8', decode_to='utf-8'):
        response = self._get_response(parameters, method, encode_to=encode_to)
        data_format = self._check_data_format(response)
        byte_data = response.read()

        byte_data = byte_data.decode(decode_to)

        if data_format == self.JSON_FORMAT:
            return json.loads(byte_data)
        else:
            return self._convert_xml_to_json(byte_data)

    def get_data(self, parameters={}, decode_to='utf-8'):
        return self._execute(parameters, method='get', decode_to=decode_to)

    def post_data(self, parameters={}, encode_to='utf-8', decode_to='utf-8'):
        return self._execute(parameters, method='post', encode_to=encode_to, decode_to=decode_to)