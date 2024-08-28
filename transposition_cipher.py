import random
import string
import sys

def generate_fixed_mapping(seed=42):
    """Generate a fixed random mapping for the characters using a seed."""
    random.seed(seed)  # Set the seed for reproducibility
    chars = string.ascii_letters + string.digits + string.punctuation + ' '
    mapping = list(chars)
    random.shuffle(mapping)
    return dict(zip(chars, mapping))

def encrypt(plaintext, encoding_map):
    """Encrypt the plaintext using the encoding_map."""
    return ''.join(encoding_map.get(char, char) for char in plaintext)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 transposition_cipher.py 'plaintext'")
        sys.exit(1)
    
    plaintext = sys.argv[1]
    
    # Generate fixed mapping
    encoding_map = generate_fixed_mapping(seed=42)
    
    # Encrypt
    encrypted_message = encrypt(plaintext, encoding_map)
    print(encrypted_message)

if __name__ == "__main__":
    main()
