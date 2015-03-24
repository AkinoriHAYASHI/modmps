from distutils.core import setup

setup(
    name='modmps',
    version='0.0.1',
    packages=['modmps', 'modmps.http', 'modmps.http.oauth2', 'modmps.http.oauth2.base', 'modmps.http.oauth2.google',
              'modmps.http.oauth2.google.auth', 'modmps.http.api_executor'],
    url='www.mpsamurai.org',
    license='GNU General Public License version 3',
    author='Junya Kaneko, Akinori Hayashi',
    author_email='junya@mpsamurai.org, akinori@mpsamurai.org',
    description=''
)
