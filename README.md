# Password Complexity Checker

## Description
The Password Complexity Checker is a Python-based application designed to determine the complexity of a password. Users can input a password to perform compelxity checker. This tool uses zxcvbn, which is a password strength estimation library. This helps determine the time it takes for a hacker to get access. This tool also provides suggestions on how to improve the password's complexity to be less susceptible to perpetrators.

## Features
- Encrypt Text: Encrypt messages using the Caesar cipher with a specified shift value.
- Decrypt Text: Decrypt messages that were encrypted with the Caesar cipher.
- Web Interface: A user-friendly web application allows for easy text input and shift value specification.
- Result Display: View the encrypted or decrypted message directly on the web page.

## Requirements
- Python 3.x

### Install Dependencies
Install the required Python packages by running:
```
$ pip install flask
$ pip install zxcvbn-python
```

### Running the Web App Locally
To run the web application locally and open it in your browser:
```
$ python app.py
```


After running the above command, open the program by clicking [here](http://127.0.0.1:9090/).

## DEMO
### Encrypt
![PRODIGY_CS_01_encrypt](https://github.com/user-attachments/assets/89f372dd-5e54-4f63-bf79-3c5fec6ca9dd)
### Decrypt
![PRODIGY_CS_01_decrypt](https://github.com/user-attachments/assets/51c78606-e9de-4efc-9431-962a2e673415)


## Web App Features
- **Text Encryption**:  Input your message and shift value to encrypt the text.
- **Text Decryption**: Input your encrypted message and shift value to decrypt the text.
- **User Interface**: A simple form allows for text input, shift value specification, and action selection (encrypt/decrypt).
