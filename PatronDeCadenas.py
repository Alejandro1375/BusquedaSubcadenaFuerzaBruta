def buscar(cadena, patron):
    for i in range(len(cadena)):
        for j in range(len(patron)):
            if i + j >= len(cadena):
                break
            if cadena[i + j] != patron[j]:
                break
        else:
            print(f'El patrón {patron} comienza en el index {i}')
            return True
    print('No se encontro patrón')        
    return False

print(buscar('1110010001101110100011001111000110001110001110001110100011010001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001101000111110101010100111100011000',
'1010101'))