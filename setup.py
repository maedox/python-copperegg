from distutils.core import setup

setup(
    name='python-copperegg',
    version='0.1',
    description='Python wrapper for the CopperEgg Client API',
    author='maedox',
    author_email='paal.nilsen@gmail.com',
    url='http://github.com/maedox/python-copperegg',
    packages=['copperegg']
)

package_dir = {'copperegg': 'lib'}
