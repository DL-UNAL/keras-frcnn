#!/usr/bin/env python

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(name='keras-frcnn',
      version='0.2.0',
      description='Keras implementation of Faster R-CNN',
      maintainer='Juan Navarro',
      maintainer_email='jsnavarroa@unal.edu.co',
      url='https://github.com/vvc-unal/keras-frcnn',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required,
     )
