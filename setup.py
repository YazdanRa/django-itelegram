#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import find_packages

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
    os.system("python setup.py bdist_wheel")
    os.system("twine upload dist/*")
    os.system("git tag v{}".format(version))
    os.system("git push --tags")
    sys.exit()

README = open("README.rst", "r", encoding="UTF-8").read()
DEV_REQ = open("requirements_dev.txt", "r", encoding="UTF-8").read()
TEST_REQ = open("requirements-test.txt", "r", encoding="UTF-8").read()

setup(
    name="Django-iTelegram",
    version=version,
    description="It's a library for building Telegram bot on Django with extra built-in features",
    long_description=README,
    author="Yazdan Ranjbar",
    author_email="yazdan_ra@icloud.com",
    url="https://github.com/YazdanRa/django-itelegram",
    download_url="https://pypi.python.org/pypi/django-itelegram",
    packages=find_packages(".", include=("django-itelegram", "django-itelegram.*")),
    include_package_data=True,
    install_requires=["django>=3.0", "python-telegram-bot>=6.0.1"],
    extras_require={"dev": DEV_REQ, "test": TEST_REQ},
    license="MIT",
    zip_safe=False,
    keywords=["django-itelegram", "django", "telegram", "django-telegrambot", "python-telegram-bot"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
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
