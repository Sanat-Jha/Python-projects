import string
aToz = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'," ", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
def encrypt(text):
    text = [char for char in text]
    newText=[]
    for i in text:
        position = aToz.index(i)
        newText.append(aToz[position+2])
    newTextstr = ""
    for i in newText:
        newTextstr += i
    return newTextstr

def decrypt(text):
    text = [char for char in text]
    newText=[]
    for i in text:
        position = aToz.index(i)
        newText.append(aToz[position-2])
    newTextstr = ""
    for i in newText:
        newTextstr += i
    return newTextstr

if __name__ == "__main__":
    print("What you want to do?\nEncrypt Text[1]\nor \nDecrypt Text[2]")
    Work = input("Enter 1 or 2:  ")
    if Work == "1":
        text = input("Enter the text you want to Encrypt: ")
        print("Your encrypted text is-\n",encrypt(text))
    elif Work == "2":
        text = input("Enter the text you want to Decrypt: ")
        print("Your decrypted text is-\n",decrypt(text))
    else:
        print("You entered something wrong and not 1 or 2. \nEnding Task..")