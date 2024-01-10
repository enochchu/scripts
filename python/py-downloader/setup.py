from setuptools import setup

NAME = 'py-downloader'
DESCRIPTION = ''
URL = ''
EMAIL = ''
AUTHOR = 'Enoch Chu'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'

packages = [
   'enoch'
]

required = [
    'requests',
    'tqdm'
]

test_requirements = [
]

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