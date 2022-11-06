import cryptocode
from getpass import getpass



def crypto():
    password = getpass("Inserisci la password da cifrare ")
    print()
    passkey = getpass("inserisci la chiave ")
    print()
    str_encoded = cryptocode.encrypt(password, passkey)
    y=input("Seleziona un opzione: \n 1. Visualizza stringa codificata \n 2. Salva stringa codificata su un file \n")
    if(y=="1"):
        print(str_encoded)
    elif(y=="2"):
        try:
            with open('crypted password.txt', 'w') as f:
                f.write(str_encoded)
        except FileNotFoundError:
            print("The 'docs' directory does not exist")
    else:
        print("Scelta non possibile")



def decode():
    keypass= getpass("inserisci la chiave ")
    str_encoded = getpass("inserisci la stringa codificata ")
    print()
    str_decoded = cryptocode.decrypt(str_encoded, keypass)
    print(str_decoded)
    input()





x=input("Benvenuto, scegli una tra le seguenti opzioni \n 1. Cripta la tua password\n 2. Decodifica una stringa codificata \n")
if(x=="1"):
    crypto()
elif(x=="2"):
    decode()


