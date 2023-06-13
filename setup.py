# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="半自動センサー校正器「コウセイくん☆」Web API",
    author_email="yuma140902@gmail.com",
    url="",
    keywords=["OpenAPI", "半自動センサー校正器「コウセイくん☆」Web API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    情報工学実験1A 実世界センシングで作成した半自動センサー校正器「コウセイくん☆」のWeb APIです。このWeb APIを利用することにより、Webページ、LINE、Discordなど様々なフロントエンドからコウセイくん☆を利用することができます。
    """
)

