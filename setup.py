from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import sys

# Custom install class untuk menjalankan post-install script
class CustomInstall(install):
    def run(self):
        # Jalankan instalasi normal
        install.run(self)

        # Jalankan post-install script untuk pyfiglet
        self.reinstall_pyfiglet()

    def reinstall_pyfiglet(self):
        try:
            # Uninstall pyfiglet
            subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", "pyfiglet"])
            # Install ulang pyfiglet
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyfiglet"])
            print("pyfiglet has been reinstalled successfully.")
        except Exception as e:
            print(f"Failed to reinstall pyfiglet: {e}")

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
        "pyfiglet",  # Pastikan versi pyfiglet yang digunakan
        "prettytable",  # Library untuk menampilkan tabel font
        "colorama",  # Library untuk warna terminal
        "pyperclip"
    ],
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
    python_requires=">=3.6",
    cmdclass={
        'install': CustomInstall,  # Gunakan custom install class
    },
)
