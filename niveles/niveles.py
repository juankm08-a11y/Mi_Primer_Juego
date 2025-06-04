
niveles = [
    {'nombre':'Demo 1','color':(50,50,100)},
    {'nombre':'Demo 2','color':(100,50,50)},
    {'nombre':'Demo 3','color':(50,100,50)}
]

def obtener_color_nivel(indice):
    return niveles[indice]['color']

def obtener_nombre_nivel(indice):
    return niveles[indice]['nombre']

def siguiente_nivel(indice_actual):
    return (indice_actual + 1) % len(niveles)        
   