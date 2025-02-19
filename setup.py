from setuptools import setup, find_packages

setup(
    name="ascify",
    version="1.1.0",
    description="A tool to generate ASCII banners with customizable fonts and colors",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="fkr00t",
    author_email="fkr00t@duck.com",
    url="https://github.com/fkr00t/ascify",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pyfiglet",  # Library for generating ASCII art
        "prettytable",  # Library for displaying font tables
        "colorama"  # Library for terminal colors
    ],
    entry_points={
        "console_scripts": [
            "ascify=ascify.main:main",  # Create a command-line script 'ascify'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)