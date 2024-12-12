
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

---

## **Requirements**
- Python 3.x
- Dependencies:
  - [`pyfiglet`](https://pypi.org/project/pyfiglet/)
  - [`prettytable`](https://pypi.org/project/prettytable/)

Install the required libraries using the following command:
```bash
pip install pyfiglet prettytable
```

---

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
   python ascify.py
   ```
4. Follow the on-screen instructions:
   - Enter the text you want to convert into an ASCII banner.
   - Select a font from the table by entering its corresponding number.
   - View the generated banner in your terminal.
   - Optionally save the banner to a file.

---

## **Example**
### **Input**
- **Text**: `Hello`
- **Font**: `slant`

### **Generated ASCII Banner**
```
  _   _      _ _
 | | | |    | | |
 | |_| | ___| | | ___
 |  _  |/ _ \ | |/ _ \
 | | | |  __/ | | (_) |
 \_| |_/\___|_|_|\___/
```

### **Saving to File**
If you choose to save:
```bash
Do you want to save the result to a file? (yes/no): yes
Enter the file name (e.g., output.txt): hello_banner.txt
```
The file `hello_banner.txt` will now contain your ASCII banner.

---

## **Screenshots**
### **Font Selection Table**
### ***Images 1***
![Images 1](https://github.com/user-attachments/assets/88b64c1c-660e-4845-a92a-d2a23a74fac8)

### ***Images 2***
![Images 2](https://github.com/user-attachments/assets/3d9b8e0a-7ec5-4f63-8874-7fa812095b8e)

---
## **License**
This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it as per your needs.

---