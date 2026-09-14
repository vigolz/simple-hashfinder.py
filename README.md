# Simple HashFinder

A small Python script to quickly identify the type of a given hash string based on its prefix or length, and suggest the corresponding Hashcat mode (`-m`).

## Supported Hashes
The script can identify the following formats:
- **Bcrypt** (`$2b$`, `$2a$`, `$2y$`)
- **Scrypt** (`$7$`, `$scrypt$`)
- **Argon2** (`$argon2$`)
- **PBKDF2** (`$PBKDF2$`)
- **MD5** (length 32)
- **SHA1** (length 40)
- **SHA256** (length 64)
- **SHA512** (length 128)

## How to Use
1. Make sure you have Python installed.
2. Run the script in your terminal:
   ```bash
   python hashfinder.py
