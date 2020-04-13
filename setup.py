import setuptools
from curac_utils import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="curac_util-pkg-max0r",
    version=__version__,
    author="Max-Heinrich Laves",
    author_email="author@example.com",
    description="A helper package for CURAC lecture.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mlaves/curac_utils",
    packages=setuptools.find_packages(),
    install_requires=[
              'numpy',
              'torch',
              'progressbar',
              'tqdm'
          ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
