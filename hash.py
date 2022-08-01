import hashlib

def hash_string ():
    hash_object = hashlib.sha256(b"Python Bootcamp")
    hex_digit = hash_object.hexdigest()
    print(hex_digit)
def main():
    hash_string()

if __name__ =="__main__":
    main()
