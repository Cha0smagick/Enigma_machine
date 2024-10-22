import time

def enigma(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    encrypted = ''
    
    if message is None or key is None:
        raise ValueError("Message or key cannot be null")
    if len(message) == 0 or len(key) == 0:
        raise ValueError("Message or key cannot be empty")
    if not isinstance(message, str) or not isinstance(key, str):
        raise ValueError("Message or key must be a string")
    
    message = message.replace(" ", "")
    key = key.lower()
    key_index = int(time.time() * 1000) % len(key)
    
    for char in message:
        encrypted += alphabet[(alphabet.index(char) + alphabet.index(key[key_index])) % len(alphabet)]
        key_index = (key_index + 1) % len(key)
    
    return encrypted

def decripta(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    decrypted = ''

    if message is None or key is None:
        raise ValueError("Message or key cannot be null")
    if len(message) == 0 or len(key) == 0:
        raise ValueError("Message or key cannot be empty")
    if not isinstance(message, str) or not isinstance(key, str):
        raise ValueError("Message or key must be a string")
    
    key = key.lower()
    key_index = int(time.time() * 1000) % len(key)
    
    for char in message:
        decrypted += alphabet[(alphabet.index(char) - alphabet.index(key[key_index])) % len(alphabet)]
        key_index = (key_index + 1) % len(key)
    
    return decrypted

def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    message = input("Ingrese el mensaje a encriptar: ")
    key = "aleman"
    encrypted = enigma(message, key)
    
    print("El mensaje encriptado es: " + encrypted)
    
    desc_key = input("Ingrese la palabra de desencriptacion: ")
    
    while desc_key != key:
        print("La palabra de desencriptacion no coincide con la llave de encriptacion")
        desc_key = input("Ingrese la palabra de desencriptacion de nuevo: ")

    decrypted = decripta(encrypted, key)
    print("El mensaje desencriptado es: " + decrypted)

if __name__ == "__main__":
    main()
