#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import django_itelegram

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = django_itelegram.__version__

if sys.argv[-1] == "publish":
    try:
        import wheel
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()

if sys.argv[-1] == "tag":
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")

setup(
    name="django-itelegram",
    version=version,
    description="It's a library for building Telegram bot on Django with extra built-in features",
    long_description=readme + "\n\n" + history,
    author="django-itelegram",
    author_email="yazdan_ra@icloud.com",
    url="https://github.com/YazdanRa/django-itelegram",
    packages=[
        "django_itelegram",
    ],
    include_package_data=True,
    install_requires=[
        "django>=2.2",
        "python-telegram-bot>=6.0.1",
    ],
    license="MIT",
    zip_safe=False,
    keywords="django-itelegram",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
