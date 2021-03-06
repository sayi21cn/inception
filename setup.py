deps = ['dulwich', 'argparse', 'pycrypto']
from setuptools import setup, find_packages
import inception
setup(
    name='inception-android',
    version=inception.__version__,
    url='http://github.com/tgalal/inception/',
    license='GPL-3+',
    author='Tarek Galal',
    tests_require=[],
    install_requires = deps,
    scripts = ['incept'],
    author_email='tare2.galal@gmail.com',
    description='Auto config tools for android devices',
    #long_description=long_description,
    packages= find_packages(),
    include_package_data=True,
    platforms='linux',
    #test_suite='',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux'
        ]
)