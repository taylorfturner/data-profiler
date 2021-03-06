"""
A setuptools for the Data Profiler Application and Python Libraries
"""

# To use a consistent encoding
from codecs import open
import os
from os import path
from datetime import datetime

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

MAJOR               = 0
MINOR               = 3
MICRO               = 0
ISRELEASED          = True

VERSION             = '%d.%d.%d' % (MAJOR, MINOR, MICRO)


# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# Get the install_requirements from requirements.txt
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    required_packages = f.read().splitlines()

nightly_schema = "%y%m%d"
try:
    # Obtain version number, based on git commit
    os.system('git log -1 --format=%cd > tmp')
    last_commit = open('tmp', 'r').read()
    os.remove('tmp')
    last_commit = ' '.join(last_commit.split(' ')[:-1])
    NIGHTLY = datetime.strptime(last_commit, '%a %b %d %H:%M:%S %Y').strftime(nightly_schema)
except:
    # If fail, use current time
    NIGHTLY = datetime.now().strftime(nightly_schema)


if not ISRELEASED: 
    VERSION += '.dev+' + NIGHTLY
    
    
resource_dir = 'resources/'
default_labeler_files = [(d, [os.path.join(d, f) for f in files])
                         for d, folders, files in os.walk(resource_dir)]


DESCRIPTION = "What is in your data? Detect schema, statistics and entities in almost any file."

setup(
    name='DataProfiler',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',

    # The project's main homepage.
    url='https://github.com/capitalone/data-profiler',

    # Author details
    author='Jeremy Goodsitt, Austin Walters, Anh Truong, Grant Eden',

    # Choose your license
    license='Apache License, Version 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',

        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Security',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 3 or both.
        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords='Data Investigation',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['src/test', 'src/sample']),
    packages=find_packages(exclude=["tests", "examples"]),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=required_packages,

    # # If there are data files included in your packages that need to be
    # # installed, specify them here.  If using Python 2.6 or less, then these
    # # have to be included in MANIFEST.in as well.
    # package_data={
    #     'data': [],
    # },
    #
    # # Although 'package_data' is the preferred approach, in some case you may
    # # need to place data files outside of your packages. See:
    # # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=default_labeler_files,
    include_package_data=True,
)

print("find_packages():", find_packages())
