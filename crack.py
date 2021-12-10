import pikepdf
# optional, just display a progress bar
from tqdm import tqdm

# load password from a pre defined file
passwords = [ line.strip() for line in open("passwd.txt") ]

# here we iterate trogh file
for password in tqdm(passwords, "processing"):
    try:
        # open PDF file
        with pikepdf.open("file.pdf", password=password) as pdf:
            # Password decrypted successfully, break out 
            print("Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, go on
        continue