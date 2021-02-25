import hashlib

flag = 0
print("Welcome To Hash Cracker. Supported Hash Formats Are MD5, Sha1, Sha224, Sha256, Sha384, Sha512")

Orignal_Hash = input("Enter Hash: ")
Hash_Number = input("1 For MD5\n2 For Sha1\n3 For Sha224\n4 For Sha256\n5 For Sha384\n6 For Sha512" + "\nEnter Hash Number: ")
Orignal_Wordlist = input("Enter Full Path To Wordlist: ")

try:
    open_wordlist = open(Orignal_Wordlist, "r")
except:
    print("No Wordlist Found!")
    quit()

if Hash_Number == "1":
    print("\nCracking...")
    for Password in open_wordlist:
        Encoding = Password.encode('utf-8')
        Digest = hashlib.md5(Encoding.strip()).hexdigest()
        if Digest == Orignal_Hash:
            print("Password Found: " + Password)
            flag = 1
            break

elif Hash_Number == "2":
    print("\nCracking...")
    for Password in open_wordlist:
        Encoding = Password.encode('utf-8')
        Digest = hashlib.sha1(Encoding.strip()).hexdigest()
        if Digest == Orignal_Hash:
            print("Password Found: " + Password)
            flag = 1
            break

elif Hash_Number == "3":
    print("\nCracking...")
    for Password in open_wordlist:
        Encoding = Password.encode('utf-8')
        Digest = hashlib.sha224(Encoding.strip()).hexdigest()
        if Digest == Orignal_Hash:
            print("Password Found: " + Password)
            flag = 1
            break

elif Hash_Number == "4":
    print("\nCracking...")
    for Password in open_wordlist:
        Encoding = Password.encode('utf-8')
        Digest = hashlib.sha256(Encoding.strip()).hexdigest()
        if Digest == Orignal_Hash:
            print("Password Found: " + Password)
            flag = 1
            break

elif Hash_Number == "5":
    print("\nCracking...")
    for Password in open_wordlist:
        Encoding = Password.encode('utf-8')
        Digest = hashlib.sha384(Encoding.strip()).hexdigest()
        if Digest == Orignal_Hash:
            print("Password Found: " + Password)
            flag = 1
            break
        
elif Hash_Number == "6":
    print("\nCracking...")
    for Password in open_wordlist:
        Encoding = Password.encode('utf-8')
        Digest = hashlib.sha512(Encoding.strip()).hexdigest()
        if Digest == Orignal_Hash:
            print("Password Found: " + Password)
            flag = 1
            break

if flag == 0:
    print("\nError! Password Not Found")
    print("Tip1: Try Changing The Wordlist")
    print("Tip2: Check If The Hash_Number Is Correct")
    print("Tip3: Check If The Hash Is Case Sensitive")
    quit()
