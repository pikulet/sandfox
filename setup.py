import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sandfox",
    version="0.0.1",
    author="pikulet",
    author_email="jycyeo@yahoo.com.sg",
    description="Python engine for Beyond.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pikulet/sandfox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
