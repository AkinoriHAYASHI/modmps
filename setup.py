from distutils.core import setup

setup(
    name='modmps',
    version='0.0.1',
    packages=['modmps', 'modmps.http', 'modmps.http.oauth2', 'modmps.http.api_executor', 'modmps.http.extra_services',
              'modmps.http.extra_services.google', 'modmps.http.extra_services.google.oauth2'],
    url='www.mpsamurai.org',
    license='GNU General Public Lisence version 3',
    author='Junya Kaneko, Akinori Hayashi',
    author_email='junya@mpsamurai.org, akinori@mpsamurai.org',
    description=''
)
