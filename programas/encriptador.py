txtinput = input("Escribe aqui lo que quiereas encriptar (solo letras): ")

txtinput = list(txtinput)
print(txtinput)

# Diccionario que muestra el abecedario con la letra/numero que corresponda para hacer la encriptacion
dic_encrypted_abc = {
    'a': "X",
    'b': "R",
    'c': "B",
    'd': "I",
    'e': "L",
    'f': "V",
    'g': "N",
    'h': "Q",
    'i': "Y",
    'j': "U",
    'k': "E",
    'l': "Z",
    'm': "H",
    'n': "K",
    'o': "C",
    'p': "J",
    'q': "M",
    'r': "T",
    's': "G",
    't': "D",
    'u': "A",
    "v": "O",
    "w": "F",
    'x': 9,
    'y': 7,
    'z': 10
}

 # Cuenta las letras que hay en el input

counttxtinput = len(txtinput)
print(counttxtinput)

# Cambia las letras para encriptarlo

print(f"Se va a encriptar la palabra siguiente: {txtinput}")

encrypted_txt = []

for letter in txtinput:
  if letter in dic_encrypted_abc:
    encrypted_txt.append(dic_encrypted_abc[letter])
  else:
    encrypted_txt.append(letter)

print(f"Texto encriptado: {encrypted_txt}")
