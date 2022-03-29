from setuptools import setup

NAME = 'py-ffmpeg'
DESCRIPTION = 'Python scripts for ffmpeg'
URL = ''
EMAIL = 'enoch@notanemail.com'
AUTHOR = 'Enoch Chu'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'

packages = []

required = [ ]

test_requirements = []

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=packages,
    install_requires= required,
    tests_require = test_requirements
)