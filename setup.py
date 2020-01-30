# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(  
    name='sap2012', 
    version='0.0.1',  
    author='Steven K Firth',  # Optional
    author_email='s.k.firth@lboro.ac.uk',  # Optional
    description='Python package implementing the SAP2012 domestic building energy calculations',  # Required
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/stevenkfirth/sap2012',  # Optional
    packages=find_packages(), # Required
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    )
