import json
import re
import random
import string

# Caesar cipher encryption and decryption functions (pre-implemented)
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Password strength checker function (optional)
def is_strong_password(password):
    # ...

# Password generator function (optional)
def generate_password(length):
     """
    Generate a random strong password of the specified length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: A random strong password.
    """

# Initialize empty lists to store encrypted passwords, websites, and usernames
salatut_salasanat = []
verkkosivut = []
käyttäjänimet = []

#Salausarvo
SALAUS_SIIRTO = 3

# Function to add a new password OK
def add_password():
    """
    Add a new password to the password manager.

    This function should prompt the user for the website, username,  and password and store them to lits with same index. Optionally, it should check password strengh with the function is_strong_password. It may also include an option for the user to
    generate a random strong password by calling the generate_password function.

    Returns:
        None
    """


    print("\nLisää uusi salasana")

    #1.Kysytään syötteet käyttäjältä
    verkkosivu_syote = input("Verkkosivun nimi: ")
    käyttäjänimi_syote = input("Käyttäjätunnus: ")
    salasana_syote = input("Salasana: ")

    #2. Salasanan salaus
    salattu_salasana = caesar_encrypt(salasana_syote, SALAUS_SIIRTO)

    #3. Tallennus listoihin
    verkkosivut.append(verkkosivu_syote)
    käyttäjänimet.append(käyttäjänimi_syote)
    salatut_salasanat.append(salattu_salasana)

    print(f"\nTiedot tallennettu onnistuneesti verkkosivulle: {verkkosivu_syote}")

# Function to retrieve a password OK
def get_password():
    """
    Retrieve a password for a given website.

    This function should prompt the user for the website name and
    then display the username and decrypted password for that website.

    Returns:
        None
    """
    print("\n Hae salasana")
    haettava_sivu=input("Anna sen verkkosivun nimi, jonka salasanan haluat hakea: ")

    try:
        #1.Etsi syötetyn verkkosivun indeksi verkkosivut-listalta
        indeksi=verkkosivut.index(haettava_sivu)

        #2. Hae tiedot käyttäjänimet ja salasanat -listoilta
        haettu_käyttäjänimi=käyttäjänimet[indeksi]
        salattu_salasana=salatut_salasanat[indeksi]

        #3. Pura salaus
        purettu_salasana=caesar_decrypt(salattu_salasana, SALAUS_SIIRTO)

        print(f"\nTiedot löytyivät sivulle {haettava_sivu}")
        print(f"Käyttäjänimi: {haettu_käyttäjänimi}")
        print(f"Salasana: {purettu_salasana}")

    except ValueError: 
        # Käsittelee ja kertoo jos sivua ei löydy
        print(f"\nVirhe: Salasanatietoja sivulle '{haettava_sivu}' ei löytynyt.")

# Function to save passwords to a JSON file OK
def save_passwords():
 """
    Save the password vault to a file.

    This function should save passwords, websites, and usernames to a text
    file named "vault.txt" in a structured format.

    Returns:
        None
    """

    Returns:
        None
    """
    print("\nTallennetaan salasanaholvi tiedostoon")

    #1. Kootaan listat sanakirjaksi
    data = {
        "verkkosivut": verkkosivut,
        "kayttajanimet": käyttäjänimet,
        "salatut_salasanat": salatut_salasanat
        }

    tiedostonimi="salasanaholvi.json"

    try:
        #2.Avataan tiedosto kirjoitusta varten
        with open(tiedostonimi, 'w', encoding='utf-8') as tiedosto:
            #3. Kirjoitetaan tiedot tiedostoon
            json.dump(data, tiedosto, indent=4)

        #4. Onnistunut tulos kerrotaan käyttäjälle
        print(f"\nSalasanaholvi tallennettu pysyvästi (tiedostoon '{tiedostonimi}').")

    except Exception as e:
        #5.Ilm oitetaan jos tapahtui virhe
    print(f"\nTallennusvirhe! Tietojen kirjoittaminen tiedostoon epäonnistui: {e}"))


# Function to load passwords from a JSON file 
def load_passwords():
     """
    Load passwords from a file into the password vault.

    This function should load passwords, websites, and usernames from a text
    file named "vault.txt" (salasanaholvi.json) (or a more generic name) and populate the respective lists.

    Returns:
        None
    
    global salatut_salasanat, verkkosivut, käyttäjänimet
    tiedostonimi = "salasanaholvi.json"

    try:
        # 1. Avataan tiedosto lukemista varten ('r')
        with open(tiedostonimi, 'r', encoding='utf-8') as tiedosto:
            # 2. Ladataan tiedot sanakirjaksi
            data = json.load(tiedosto)
            
        # 3. Tyhjennetään nykyiset listat
        verkkosivut.clear()
        käyttäjänimet.clear()
        salatut_salasanat.clear()
        
        # 4. Lisätään ladatut tiedot listoihin
        verkkosivut.extend(data.get("verkkosivut", []))
        käyttäjänimet.extend(data.get("kayttajanimet", []))
        salatut_salasanat.extend(data.get("salatut_salasanat", []))

    except FileNotFoundError:
        print(f"Tiedostoa '{tiedostonimi}' ei löytynyt.")
        
    except Exception as e:
        print(f"Virhe ladattaessa tiedostoa '{tiedostonimi}': {e}")
    
    return None

  # Main method
  
def main():
# implement user interface 

  while True:
    print("\nSalasananhallinta - valikko:")
    print("1. Lisää salasana")
    print("2. Hae salasana")
    print("3. Tallenna salasanat tiedostoon")
    print("4. Lataa salasanat tiedostosta")
    print("5. Lopeta")
    
    valinta = input("Valitse toiminto (1-5): ")
    
    if valinta == "1":
        add_password()
    elif valinta == "2":
        get_password()
    elif valinta == "3":
        save_passwords()
    elif valinta == "4":
        passwords = load_passwords()
        print("Salasanat ladattu onnistuneesti!")
    elif valinta == "5":
        break
    else:
        print("Virheellinen valinta. Yritä uudestaan.")

# Execute the main function when the program is run
if __name__ == "__main__":
    main()
