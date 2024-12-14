from setuptools import setup, find_packages

setup(
    name="ascify",  # Nama package
    version="1.0.0",  # Versi package
    description="A tool to generate ASCII banners with customizable fonts and colors",
    long_description=open("README.md").read(),  # Deskripsi panjang dari README.md
    long_description_content_type="text/markdown",  # Format README.md
    author="fkr00t",  # Nama penulis
    author_email="fkr00t@duck.com",  # Email penulis
    url="https://github.com/your_username/ascify",  # URL repositori
    packages=find_packages(),  # Otomatis menemukan folder package
    include_package_data=True,  # Sertakan data non-Python
    install_requires=[
        "pyfiglet",
        "prettytable",
        "colorama"
    ],  # Dependencies
    entry_points={
        "console_scripts": [
            "ascify=ascify.main:main",  # Membuat command-line script 'ascify'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Versi Python minimum
)
