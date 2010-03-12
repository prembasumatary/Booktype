from setuptools import setup, find_packages

import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('AUTHORS.txt')
    )


setup(
    name = "booki",
    version = "0.1",

    packages = find_packages('lib', 'lib/redis.py'),  # include all packages under src
    package_dir = {'':'lib'},   # tell distutils packages are under src

    author = "Aleksandar Erkalovic",
    author_email = "aerkalov@gmail.com",

    description = "FLOSS Manuals collaborative book writing tool",
    long_description = long_description,

    url = "http://booki-dev.flossmanuals.net/",
    include_package_data = True,
    package_data = {
        # If any package contains *.txt or *.rst files, include them
        '': ['*.txt', '*.rst'],
    },
    install_requires = ['setuptools', 'simplejson', 'django' ],
    classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
      ],
      keywords='collaborative book writing sprint',
      license='GPL',

)

