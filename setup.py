"""
    Pinterest REST API

    Pinterest's REST API  # noqa: E501

    The version of the OpenAPI document: 5.7.0
    Contact: pinterest-api@pinterest.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301
from pathlib import Path

NAME = "Pinterest Generated Client"
VERSION = "0.1.4"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3==1.26.12",
  "python-dateutil",
]

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    description="Pinterest REST API",
    author="Pinterest, Inc.",
    author_email="pinterest-api@pinterest.com",
    url="https://github.com/pinterest/pinterest-python-generated-api-client",
    keywords=["OpenAPI", "OpenAPI-Generator", "Pinterest REST API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type='text/markdown',
)
