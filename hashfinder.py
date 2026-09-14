#typer af hash den skal kunne finde
#md5, sha1 sha256, sha512, bycrypt, scrypt, argon2, PBKDF2, 

def find_hash_type(hash_string):
    strip_hash = hash_string.strip()

    if strip_hash.startswith("$2a$") or strip_hash.startswith("$2b$") or strip_hash.startswith("$2y$"):
        print("your hash is BYCRYPT (hashcat value: -m 0 -a [attack-mode] [options])")
    elif strip_hash.startswith("$7$") or strip_hash.startswith("$scrypt$"):
        print("your hash is SCRYPT (hashcat value: -m 8900 -a [attack-mode] [options])")
    elif strip_hash.startswith('$argon2'):
        print("your hash is ARAGON (hashcat value: -m 34000 -a [attack-mode] [options])")
    elif strip_hash.startswith("PBKDF2$"):
        print("your hash is PBKDF2 (hashcat value: -m 10900 -a [attack-mode] [options])")
    
    
    elif len(strip_hash) == 32:
        print("your hash is MD5 (hashcat value: -m 0 -a [attack-mode] [options])" )
    elif len(strip_hash) == 40:
        print("your hash is SHA1 (hashcat value: hashcat -m 100 -a [attack-mode] [options])")
    elif len(strip_hash) == 64:
        print("your hash is SHA256 (hashcat value: hashcat -m 1400 -a [attack-mode] [options])")
    elif len(strip_hash) == 128:
        print("your hash is SHA512 (hashcat value: hashcat -m 1700 -a [attack-mode] [options])")
    else:
        print("unknown hash format")

def main():
    while True:
        option = input("please enter your hash (or 'exit' to quit)")

        if 'exit' in option.lower():
            print("goodbye")
            break

        find_hash_type(option)
       


main()

