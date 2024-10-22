def enigma(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    if message is None or key is None:
        raise ValueError("Message or key cannot be null")
    if len(message) == 0 or len(key) == 0:
        raise ValueError("Message or key cannot be empty")
    if not isinstance(message, str) or not isinstance(key, str):
        raise ValueError("Message or key must be a string")
    message = ''.join(c for c in message.lower() if c.isalpha())
    key = key.lower()
    key_index = 0
    for char in message:
        encrypted += alphabet[(alphabet.index(char) + alphabet.index(key[key_index])) % 26]
        key_index = (key_index + 1) % len(key)
    return encrypted

def decripta(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = ''
    if message is None or key is None:
        raise ValueError("Message or key cannot be null")
    if len(message) == 0 or len(key) == 0:
        raise ValueError("Message or key cannot be empty")
    if not isinstance(message, str) or not isinstance(key, str):
        raise ValueError("Message or key must be a string")
    message = ''.join(c for c in message.lower() if c.isalpha())
    key = key.lower()
    key_index = 0
    for char in message:
        decrypted += alphabet[(alphabet.index(char) - alphabet.index(key[key_index])) % 26]
        key_index = (key_index + 1) % len(key)
    return decrypted

def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = ''.join(c for c in input("Ingrese el mensaje a encriptar: ").lower() if c.isalpha())
    key = "aleman"
    encrypted = enigma(message, key)
    print("El mensaje encriptado es: " + encrypted)
    desc_key = input("Ingrese la palabra de desencriptacion: ")
    if desc_key == key:
        decrypted = decripta(encrypted, key)
        print("El mensaje desencriptado es: " + decrypted)
    else:
        print("La palabra de desencriptacion no coincide con la llave de encriptacion")

if __name__ == "__main__":
    main()
