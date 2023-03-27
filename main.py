import sys

characters_dict = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10,
        "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20,
        "V":21, "W":22, "X":23, "Y":24, "Z":25 }

abeceda = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def dotazy() -> str: 
    dotazy_whileloop = 1
    while dotazy_whileloop < 2:
        print("If you want to enter the text to be encrypted manually press m and if you want insert a file press f")
        answer = input()
        if answer == "m":
            dotazy_whileloop =+ 1
            print("Enter the text to be encrypted:")
            text = input()
            return text
        elif answer == "f":
            dotazy_whileloop =+ 1
            with open("Text k sifrovani.txt") as f:
                text = f.read()
                return text
        else:
            print("Wrong character try again")

def Encrypt(text: str, encrypted_text: str, encrypted_text1: str) -> None:
    for char in text:
        if char == " ":
            encrypted_text.append(char)
        else:
            upperChar = char.upper()
            cisloPismena = characters_dict.get(upperChar) + 3
            encrypted_text.append(cisloPismena)
    for cislo in encrypted_text:
        if cislo == " ":
            encrypted_text1.append(cislo)

        elif cislo >= 26 :
            encryptedPismeno = abeceda[cislo - 26]
            encrypted_text1.append(encryptedPismeno)

        else:
            encryptedPismeno = abeceda[cislo]
            encrypted_text1.append(encryptedPismeno)
    string_from_list = "".join(encrypted_text1)
    print(string_from_list) 

def Decrypt(text: str,decrypted_text: str, decrypted_text1: str) -> None:
    for char in text:
        if char == " ":
            decrypted_text1.append(char)
        else:
            upperChar = char.upper()
            cisloPismena = characters_dict.get(upperChar) 
            decrypted_text1.append(cisloPismena)
    for cislo in decrypted_text1:
        if cislo == " ":
            decrypted_text.append(cislo)
        elif cislo <= 2:
            cislo += 23
            decrypted_pismeno = abeceda[cislo]
            decrypted_text.append(decrypted_pismeno)
        else:
            cislo -= 3
            decrypted_pismeno = abeceda[cislo]
            decrypted_text.append(decrypted_pismeno)
    decrypted_text3 = "".join(decrypted_text)
    print(decrypted_text3)
    


def main():
    while 1 < 2:
        encrypted_text = []
        encrypted_text1 = []
        decrypted_text = []
        decrypted_text1 = []
        print("If you want to encrypt press e and if you want decrypt press d otherwise press q to exit")
        answer = input()
        if answer == "e":
            text = dotazy()
            Encrypt(text, encrypted_text, encrypted_text1)
        elif answer == "d":
            text = dotazy()
            Decrypt(text, decrypted_text, decrypted_text1)
        elif answer == "q":
            sys.exit()
        else:
            print("Wrong character try again")

if __name__ == "__main__":
   main()
