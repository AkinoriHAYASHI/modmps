"""A module containing exceptions raised by modmps.http.api_executor.ApiExecutor class.

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

class ApiExecutionFailure(Exception):
    def __init__(self, api_executor_name):
        self.message = 'Api %s fails to execute.' % api_executor_name

    def __str__(self):
        return repr(self.message)

class InvalidApiParameter(Exception):
    def __init__(self, api_executor_name, param_name):
        self.message = 'Api %s does not have parameter %s.' % (api_executor_name, param_name)

    def __str__(self):
        return repr(self.message)

class UnknownDataFormat(Exception):
    def __init__(self, api_executor_name):
        self.message = 'Api %s cannot recognize the received data format.' % api_executor_name

    def __str__(self):
        return repr(self.message)

class InvalidHttpMethod(Exception):
    def __init__(self, api_executor_name, method):
        self.message = 'Api %s cannot use the http method %s.' % (api_executor_name, method)

    def __str__(self):
        return repr(self.message)