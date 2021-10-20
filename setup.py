import codecs
import os
from os import path

from setuptools import setup


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


description = (
    "Django package that provides Cloudinary storages for both media and "
    "static files as well as management commands for removing unnecessary "
    "files. "
)


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dj3-cloudinary-storage",
    version="0.0.6",
    author="Tiago Cordeiro",
    author_email="tiago@mulhergorila.com",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/tiagocordeiro/dj3-cloudinary-storage",
    keywords="django cloudinary storage",
    packages=[
        "cloudinary_storage",
        "cloudinary_storage.templatetags",
        "cloudinary_storage.management",
        "cloudinary_storage.management.commands",
    ],
    include_package_data=True,
    install_requires=["requests>=2.26.0", "cloudinary>=1.26.0"],
    extras_require={"video": ["python-magic>=0.4.24"]},
    classifiers=[
        "Framework :: Django",
        "Environment :: Web Environment",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
