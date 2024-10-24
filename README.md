# El Codigo Enigma: Sistema de Cifrado y Descifrado

Este proyecto implementa un sistema de cifrado y descifrado utilizando el método de Vigenère. Permite a los usuarios cifrar y descifrar mensajes de texto usando una clave específica. Es solo un pequeño homenaje a Alan Turing. me sorprende que en una hora puedo hacer lo que les tomo meses a los analistas en la II guerra mundial. Estaba viendo la pelicula de el codigo enigma y me pregunte si yo hubiese podido hacer algo asi. Este es el resultado.

## Funciones

### `enigma(message, key)`

Cifra un mensaje utilizando una clave mediante el método de Vigenère.

#### Parámetros:
- `message`: El mensaje que se desea cifrar (debe ser una cadena de texto).
- `key`: La clave utilizada para cifrar el mensaje (debe ser una cadena de texto).

#### Excepciones:
- Lanza un `ValueError` si:
  - `message` o `key` son `None`.
  - La longitud de `message` o `key` es 0.
  - `message` o `key` no son cadenas de texto.

#### Retorno:
- Devuelve el mensaje cifrado como una cadena de texto.

#### Ejemplo de uso:
```python
encrypted_message = enigma("hola mundo", "clave")
print(encrypted_message)  # Salida: mensaje cifrado
```

USO: 

```python
Python Enigma.py
```
