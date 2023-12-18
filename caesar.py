def cifrar_mensaje(mensaje, desplazamiento):
    mensaje_cifrado = ''
    for letra in mensaje:

        if letra.isalpha():
            codigo = ord(letra)

            if letra.isupper():
                codigo_crifrado = (codigo - 65 + desplazamiento) % 26 + 65
            else:
                codigo_crifrado = (codigo - 97 + desplazamiento) % 26 + 97
            
            letra_cifrada = chr(codigo_crifrado)
            mensaje_cifrado += letra_cifrada
        else:
            mensaje_cifrado += letra

    return mensaje_cifrado

def descifrar_mensaje(mensaje_cifrado, desplazamiento):
    mensaje_descifrado = ''
    for letra in mensaje_cifrado:

        if letra.isalpha():
            codigo = ord(letra)

            if letra.isupper():
                codigo_descrifrado = (codigo - 65 - desplazamiento) % 26 + 65
            else:
                codigo_descrifrado = (codigo - 97 - desplazamiento) % 26 + 97
            
            letra_descifrada = chr(codigo_descrifrado)
            mensaje_descifrado += letra_descifrada
        else:
            mensaje_descifrado += letra

    return mensaje_descifrado
