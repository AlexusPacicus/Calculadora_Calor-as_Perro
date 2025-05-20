##
def introducir_datos_perro():


    
    nombre = input('Introducir el nombre del perro')

    edad = int (input('Edad'))

    peso = float (input('Peso en kg'))

    opciones_validas = ['Bajo', 'Medio', 'Alto']
    nivel_actividad_fisica = ''
    while nivel_actividad_fisica not in opciones_validas:
        nivel_actividad_fisica = input('Nivel de actividad física: Bajo / Medio / Alto: ').capitalize()
                                    
        if nivel_actividad_fisica not in opciones_validas:
            print('Opciones válidas: Bajo / Medio / Alto')
    return nombre, edad, peso, nivel_actividad_fisica        
# DEFINIMOS UNA FUNCIÓN EN LA QUE CALCULAMOS EL GASTO CALÓRICO EN REPOSO (RER)#  
   
def calcular_rer(peso):

    rer = 70 * (peso ** 0.75)

    return (rer)


rango_actividad= {
    'Bajo': 1.2,
    'Medio': 1.4,
    'Alto': 1.6
}                                                                               

def calorias_totales (peso, nivel_actividad_fisica):
    
    rer = calcular_rer(peso)
    niveles = rango_actividad.get(nivel_actividad_fisica, 1.0)


    return rer * niveles

if __name__ == '__main__':