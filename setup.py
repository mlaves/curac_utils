import codecs
import os.path
import setuptools


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="curac_utils-pkg-max0r",
    version=get_version("curac_utils/_version.py"),
    author="Max-Heinrich Laves",
    author_email="author@example.com",
    description="A helper package for CURAC lecture.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mlaves/curac_utils",
    packages=setuptools.find_packages(),
    install_requires=[
              'numpy>=1.16.4',
              'torch>=1.4.0',
              'progressbar>=2.5',
              'tqdm>=4.32.1',
              'skimage>=0.15.0',
              'matplotlib>=3.1.0',
              'scipy>=1.3.0',
          ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
