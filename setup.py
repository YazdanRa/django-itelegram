import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

dev_requirements = ["black", "pre-commit", "psycopg2-binary"]

setup(
    name="django-itelegram",
    version="1.2.5",
    description="Developing Telegram bots on Django with extra built-in features",
    long_description=README,
    author="Yazdan Ranjbar",
    url="https://github.com/YazdanRa/django-itelegram",
    download_url="https://pypi.python.org/pypi/django-itelegram",
    license="MIT",
    packages=find_packages(".", include=("itelegram", "itelegram.*")),
    include_package_data=True,
    install_requires=["Django>=3.0", "python-telegram-bot>=13.0"],
    extras_require={"dev": dev_requirements},
    tests_require=dev_requirements,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
