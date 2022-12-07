import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'sewell'
AUTHOR = 'Sankaran Vaidyanathan'
AUTHOR_EMAIL = 'sankaranv@cs.umass.edu'
URL = 'https://github.com/sankaranv/sewell'

LICENSE = 'MIT'
DESCRIPTION = 'A package for causal inference, implemented in PyTorch for GPUs'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'numpy',
      'torch',
      'networkx'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )