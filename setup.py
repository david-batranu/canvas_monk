from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='canvas_monk',
      version=version,
      description="drawing pymunk data using html5 canvas",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='pymunk canvas html5',
      author='David Batranu',
      author_email='dbatranu@gmail.com',
      url='http://github.com/hman/canvas_monk',
      license='Beerware',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      package_data = {'': [
            'templates/*.*',
            'static/js/*.*',
      ]},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'pymunk',
            'werkzeug',
            'mako',
          # -*- Extra requirements: -*-
      ],
      entry_points= {
          'console_scripts': ['canvas_monk = canvas_monk.manage:main']
          }
      )
