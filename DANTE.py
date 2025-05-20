
def introducir_datos_perro():


    
    Nombre = input('Introducir el nombre del perro')

    Edad = int (input('Edad'))

    Peso = float (input('Peso en kg'))

    opciones_validas = ['Bajo', 'Medio', 'Alto']
    Nivel_Actividad_Fisica = ''
    while Nivel_Actividad_Fisica not in opciones_validas:
        Nivel_Actividad_Fisica = input('Nivel de actividad física: Bajo / Medio / Alto: ').capitalize()
                                    
        if Nivel_Actividad_Fisica not in opciones_validas:
            print('Opciones válidas: Bajo / Medio / Alto')
    