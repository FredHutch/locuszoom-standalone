# Copyright 2019 Fred Hutchinson Cancer Research Center
# from distutils.core import setup

from setuptools import setup, find_packages


packages = find_packages(exclude=['tests']);


setup(name='locuszoom',
      author='Original authors: Ryan Welch, Randall Pruim',
      description='Create regional plots from genome-wide association studies',
      license='License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
      version='1.5',
      url='https://github.com/FredHutch/locuszoom-standalone/',
      classifiers=[
          'Development Status :: 1 - Alpha',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3.5'
          ],
      keywords=None,
      packages=packages,
      install_requires=['numpy', 'pandas', 'matplotlib'],
      python_requires='>=3.5.3',
      scripts = [ 
          "scripts/locuszoom.py",
          "scripts/lzupdate.py",
      ])

