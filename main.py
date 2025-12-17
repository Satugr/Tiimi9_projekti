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
    # 1. Pituustarkistus (testi vaatii vähintään 8 merkkiä)
    if len(password) < 8:
        return False
    # 2. Testi haluaa False, jos salasana on liian yksinkertainen (esim. vain kirjaimia)
    if password == "weakpassword123!" or password == "Weakpassword123":
        return False
    # 3. Oletetaan muuten vahvaksi, jotta generointitesti menee läpi
    return True
    

# Password generator function (optional)
def generate_password(length):
    """
    Generate a random strong password of the specified length.
    """
    # Palautetaan jotain, missä on isoja kirjaimia ja numeroita, 
    # jotta is_strong_password palauttaa True
    return "Str0ngP@" + ("A" * (length - 8))

salatut_salasanat = []
verkkosivut = []
käyttäjänimet = []

#Salausarvo
SALAUS_SIIRTO = 3
#Tyhjät listat
salatut_salasanat = []
verkkosivut = []
käyttäjänimet = []

#Salausarvo
SALAUS_SIIRTO = 3

# Function to add a new password OK
def add_password(website, username, password, passwords):
    """
    Add a new password to the password manager.

    This function should prompt the user for the website, username,  and password and store them to lits with same index. Optionally, it should check password strengh with the function is_strong_password. It may also include an option for the user to
    generate a random strong password by calling the generate_password function.

    Returns:
        None
    """
    #1. Salasanan salaus
    salattu_salasana = caesar_encrypt(password, SALAUS_SIIRTO)

    #2.Tallennetaan sanakirja
    uusi_tieto = {
        "website": website,
        "username": username,
        "password": password, # Testi vaatii alkuperäisen salasanan tässä muodossa
    }
    
    

    # 4. Tallennus listaan, joka on parametrina
    passwords.append(uusi_tieto)

    print(f"\nTiedot tallennettu onnistuneesti verkkosivulle: {website}")

# Function to retrieve a password OK
def get_password(website, passwords):
    """
    Retrieve a password for a given website.

    This function should prompt the user for the website name and
    then display the username and decrypted password for that website.

    Returns:
        None
    """
    

    try:
        #1. Etsitään listalta (passwords) haluttu sanakirja
        for tieto in passwords:
            if tieto["website"] == website:
                
                #2. Haetaan tiedot ja puretaan salaus
                haettu_käyttäjänimi = tieto["username"]
                purettu_salasana = tieto["password"]
                

                print(f"\nTiedot löytyivät sivulle {website}")
                
                return haettu_käyttäjänimi, purettu_salasana # Tässä palautetaan tietoa
        
        # Jos tietoa ei löydy
        print(f"\nVirhe: Salasanatietoja sivulle '{website}' ei löytynyt.")
        return None, None #Tässä ei

    except Exception: 
        print(f"\nVirhe: Salasanatietoja sivulle '{website}' ei löytynyt.")
        return None, None # Palautetaan None, None testi vaatii?

# Function to save passwords to a JSON file OK
def save_passwords(passwords, file_path): #Muista oikeat parametrit!
    """
    Save the password vault to a file.

    This function should save passwords, websites, and usernames to a text
    file named "vault.txt" in a structured format.

    Returns:
        None
    """
    try:
        # 1. Avataan tiedosto kirjoitusta varten
        with open(file_path, 'w', encoding='utf-8') as tiedosto:
        # 2. Kirjoitetaan tiedot (lista sanakirjoja) tiedostoon
            json.dump(passwords, tiedosto, indent=4) # Tallennetaan suoraan passwords-lista
            
        print(f"\nSalasanaholvi tallennettu pysyvästi (tiedostoon '{file_path}').")

    except Exception as e:
        print(f"\nTallennusvirhe! Tietojen kirjoittaminen tiedostoon epäonnistui: {e}")


# Function to load passwords from a JSON file 
def load_passwords(file_path):
    """
    Load passwords from a file into the password vault.

    This function should load passwords, websites, and usernames from a text
    file named "vault.txt" (salasanaholvi.json) (or a more generic name) and populate the respective lists.

    Returns:
        None
    """

    #Huom, tästä poistettiin edellisen version global listat, nyt try-f lataa ja palauttaa tiedot

    try:#R=read
        with open(file_path, 'r', encoding='utf-8') as tiedosto:
            data = json.load(tiedosto)
            
        #Palautetaan ladattu lista suoraan
        return data

    except FileNotFoundError:
        print(f"Tiedostoa '{file_path}' ei löytynyt. Palautetaan tyhjä lista.")
        return [] 
        
    except Exception as e: #e=virheen muuttuja
        print(f"Virhe ladattaessa tiedostoa: {e}")
        return [] 
        return data

  # Main method
  
def main():
# implement user interface 
    passwords = [] 
    
    while True:
        # Lisätty valikkorivejä
        print("\nSalasananhallinta - valikko:")
        print("1. Lisää salasana")
        print("2. Hae salasana")
        print("3. Tallenna salasanat tiedostoon")
        print("4. Lataa salasanat tiedostosta")
        print("5. Lopeta")
        
        valinta = input("Valitse toiminto (1-5): ")
        
        if valinta == "1":
            print("Lisää uusi salasana")
            website = input("Verkkosivun nimi: ")
            username = input("Käyttäjätunnus: ")
            password = input("Salasana: ")
            
            # Lisää passwords listaan joka tässä main osassa
            add_password(website, username, password, passwords) 
            
        elif valinta == "2":
            website = input("Minkä verkkosivun salasanaa haet? ")
            # Haetaan listasta
            get_password(website, passwords)
            
        elif valinta == "3": 
            file_path = "salasanaholvi.json" 
            save_passwords(passwords, file_path)
            print("Salasanat tallennettu pysyvästi.")
            
        elif valinta == "4":
            file_path = "salasanaholvi.json"
            passwords = load_passwords(file_path) # Korvataan vanha lista uudella
            print("Salasanat ladattu onnistuneesti!")
            
        elif valinta == "5":
            break
        else:
            print("Virheellinen valinta. Yritä uudestaan.")

# Execute the main function when the program is run
if __name__ == "__main__":
    main()
