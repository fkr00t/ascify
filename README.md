
# **Advanced ASCII Banner Maker**

![Banner Maker](https://img.shields.io/badge/ASCII-BannerMaker-blue?style=flat-square)
![Python Version](https://img.shields.io/badge/Python-3.x-green?style=flat-square)
![License](https://img.shields.io/github/license/fkr00t/ascify?style=flat-square)

## **Overview**
The **Advanced ASCII Banner Maker** is a Python-based tool designed to generate customizable ASCII art banners. With a library of hundreds of fonts, an easy-to-use interface, and the ability to save results to files, it’s the perfect solution for creating stylish ASCII banners for your projects.

---

## **Features**
- 🚀 **Hundreds of Fonts**: Choose from a comprehensive library of fonts to customize your banner.
- 💡 **Interactive Interface**: Font selection displayed in a neatly organized table.
- 📝 **Save to File**: Option to save your ASCII banner to a file with your chosen filename.
- 📋 Copy to Clipboard: Copy the generated banner directly to your clipboard for easy sharing (uses xclip on Linux).
- 🎨 Customizable Output: Preview and customize your banner before saving or copying.

---

## **Requirements**
- Python 3.x
- Dependencies:
  - [`pyfiglet`](https://pypi.org/project/pyfiglet/)
  - [`prettytable`](https://pypi.org/project/prettytable/)
  - [`colorama`](https://pypi.org/project/colorama//)

## **How to Use**
1. Clone the repository:
   ```bash
   git clone https://github.com/fkr00t/ascify.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ascify
   ```
3. Run the application:
   ```bash
   pip install .
   ```
   
**Linux Users**: Ensure `xclip` is installed for clipboard functionality:
   ```bash
     sudo apt-get install xclip
   ```

## **How to Run**
```bash
   ascify 
   ```