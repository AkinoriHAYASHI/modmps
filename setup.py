from distutils.core import setup

setup(
    name='modmps',
    version='0.0.1',
    packages=['modmps', 'modmps.http', 'modmps.http.oauth2', 'modmps.http.api_executor',
              'modmps.http.web_service_client', 'modmps.http.web_service_client.com',
              'modmps.http.web_service_client.com.google', 'modmps.http.web_service_client.com.google.accounts',
              'modmps.http.web_service_client.com.google.accounts.o',
              'modmps.http.web_service_client.com.google.accounts.o.oauth2',
              'modmps.http.web_service_client.com.google.googleapis',
              'modmps.http.web_service_client.com.google.googleapis.www',
              'modmps.http.web_service_client.com.google.googleapis.www.plus',
              'modmps.http.web_service_client.com.google.googleapis.www.plus.v1',
              'modmps.http.web_service_client.com.google.googleapis.www.oauth2',
              'modmps.http.web_service_client.com.google.googleapis.www.oauth2.v2',
              'modmps.http.web_service_client.com.google.googleapis.www.oauth2.v3',
              'modmps.http.web_service_client.google', 'modmps.http.web_service_client.google.oauth2'],
    url='www.mpsamurai.org',
    license='GNU General Public Lisence version 3',
    author='Junya Kaneko, Akinori Hayashi',
    author_email='junya@mpsamurai.org, akinori@mpsamurai.org',
    description=''
)
