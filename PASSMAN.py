# password manager PASSMAN
import art
import random
from cryptography.fernet import Fernet

art.tprint("PASSMAN")

while True:
    print("""
    chosse options :-:>
    1 = add passwords
    2 = show passwords
    """)
    print()
    print()
    CHO = int(input("----------> "))
    if CHO == 1:
        passlist = []
        passinp = input("your password -> ")
        key = Fernet.generate_key()
        KE = Fernet(key)
        encpass = KE.encrypt(passinp.encode())
        passlist.append(encpass)
        ranname = random.randrange(1 , 5000)
        ranext = random.randrange(1 , 1000)
        filEe = open(f"{ranname}.{ranext}" , "w")
        for WRI in passlist:
            filEe.write(f"{WRI}\n")
        filEe.close()
    elif CHO == 2:
        for SHO in passlist:
            SHODEC = KE.decrypt(SHO).decode()
            print(f"your passwords !!!    > {SHODEC}\n")
    else:
        print("error")
