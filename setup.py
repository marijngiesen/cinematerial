from distutils.core import setup
# from cinematerial import _VERSION_

setup(
    name='cinematerial',
    version='0.0.5',
    packages=['cinematerial'],
    url='',
    license='MIT',
    author='Marijn Giesen',
    author_email='marijn@studio-donder.nl',
    description='Wrapper for CineMaterial API',
    requires=['requests']
)
