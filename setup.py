from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='robin_stocks',
      version='0.1',
      description='Made to interact with the Robinhood API',
      long_description=long_description,
      url='https://github.com/jmfernandes/Robinhood',
      author='Josh Fernandes',
      author_email='joshfernandes@mac.com',
      license='MIT',
      python_requires='>=3',
      packages=['robin_stocks'],
      requires=['requests'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)