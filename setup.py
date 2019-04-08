import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="matontools",
    version="0.0.1",
    description="A set of functions to speed up Data Science workflows",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader", #replace this
    author="Nathan Maton", #replace this
    author_email="office@realpython.com", #replace this
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["matontools"],
    include_package_data=True,
    install_requires=["pandas", "numpy"],
    # entry_points={
    #     "console_scripts": [
    #         "realpython=reader.__main__:main",
    #     ]
    # },
)