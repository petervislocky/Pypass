## Pypass

Password manager written for the terminal in Python. Made with simplicity in mind, the program is buildable using pip or your favorite python package/project manager. So it can be straightforward and easy to use, without dealing with compiling for different operating systems.

### Features
- Easy to use, command style UI
- Secure selection of password characters with secrets library
- Customizable length and character type
- Supports Windows, Mac, Linux, and anything else you can run Python on
- Automatically copies to clipboard unless set not to

### Installation
- Clone this repository
```bash
git clone https://github.com/petervislocky/Pypass.git
cd Pypass
pip install .
```
  - Or to install in editable mode if you want to add or change code
```bash
pip install -e .
```

### Usage
```bash
# To specify the length of the password
pypass -L <length>

# Specify to include letters
pypass -l
# Numbers
pypass -n
# And punctuation
pypass -p

# Disable auto copy to clipboard
pypass --no-copy
```

