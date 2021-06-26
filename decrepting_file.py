import tkinter

from cryptography.fernet import Fernet, InvalidToken
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from tkinter import messagebox, filedialog


def decrypting(path):
    root = tkinter.Tk()
    root.title('Encrypting')
    tkinter.Label(root, text="Enter the Password").pack()
    password = tkinter.Entry(root,show="*",width=50)
    password.pack()


    def actual_decryption(path,password):
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
        key1 = base64.urlsafe_b64encode(kdf.derive(password))
        file = open('key.key', 'rb')
        key = file.read()
        file.close()
        if (key1 == key):
            input_file = 'your_encrypted_file.encrypted'
            output_file = path

            with open(input_file, 'rb') as f:
                data = f.read()  # Read the bytes of the encrypted file

            fernet = Fernet(key)
            try:
                decrypted = fernet.decrypt(data)

                with open(output_file, 'wb') as f:
                    f.write(decrypted)  # Write the decrypted bytes to the output file


            except InvalidToken as e:
                print("Invalid Key - Unsuccessfully decrypted")
            messagebox.showwarning('Decrpyting Files', 'Decryption is successful')

        else :
            messagebox.showwarning('incorrect password','INCORRECT PASSWORD')
        root.destroy()

    tkinter.Button(root, text="Enter", command=lambda: actual_decryption(path,password.get())).pack()
    root.mainloop()
    os.remove('your_encrypted_file.encrypted')
    os.remove('key.key')

