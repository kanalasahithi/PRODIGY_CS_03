from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Encrypt the image by applying a simple XOR operation with the key
    encrypted_array = image_array ^ key
    
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image_path = image_path.split('.')[0] + '_encrypted.png'
    encrypted_image.save(encrypted_image_path)
    print(f"Encrypted image saved to {encrypted_image_path}")

def decrypt_image(encrypted_image_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_image)
    
    # Decrypt the image by applying the XOR operation with the key again
    decrypted_array = encrypted_array ^ key
    
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image_path = encrypted_image_path.split('_encrypted')[0] + '_decrypted.png'
    decrypted_image.save(decrypted_image_path)
    print(f"Decrypted image saved to {decrypted_image_path}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Encrypt or Decrypt an image using pixel manipulation.")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("image_path", help="Path to the image file")
    parser.add_argument("key", type=int, help="Encryption/Decryption key (integer)")
    
    args = parser.parse_args()
    
    if args.mode == "encrypt":
        encrypt_image(args.image_path, args.key)
    elif args.mode == "decrypt":
        decrypt_image(args.image_path, args.key)
