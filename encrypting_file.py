import base64
import os
import tkinter
from tkinter import messagebox
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
def encrypting(dir_name):
    root = tkinter.Tk()
    root.title('Encrypting')
    tkinter.Label(root, text="Enter the Password").pack()
    password = tkinter.Entry(root, width= 50)
    password.pack()
    def actual_encryption(password,dir_name):
        password_provided = password
        password = password_provided.encode()  # Convert to type bytes
        salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        print(key)
        file = open('key.key', 'wb')  # Open the file as wb to write bytes
        file.write(key)  # The key is type bytes still
        file.close()

        # Can only use kdf once
        dir_name = dir_name + ".zip"
        input_file = f"C:/Users/91922/PycharmProjects/file_manager/{dir_name}"
        output_file = 'your_encrypted_file.encrypted'

        with open(input_file, 'rb') as f:
            data = f.read()  # Read the bytes of the input file

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        with open(output_file, 'wb') as f:
            f.write(encrypted)  # Write the encrypted bytes to the output file
        os.remove(input_file)
        tkinter.messagebox.showinfo('Encrypting A File','Encryption Successful')
        root.destroy()

    tkinter.Button(root,text="Enter",command=lambda : actual_encryption(password.get(),dir_name)).pack()
    root.mainloop()
