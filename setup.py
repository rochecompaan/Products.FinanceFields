from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='Products.FinanceFields',
      version=version,
      description="Archetypes field for the proper handling of monetary and fixed point values",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='financial money fixed-point',
      author='RC Compaan',
      author_email='roche at upfrontsystems dot co dot za',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      tests_require=[],
      extras_require={
        'test': [
          'plone.app.testing',
        ],
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
