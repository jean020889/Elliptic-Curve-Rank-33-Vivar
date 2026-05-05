import mpmath
from mpmath import mp

# Configuración Vivar Research (2000 dps)
mp.dps = 2000

def encontrar_puntos_vivar(a_val, b_val, limite_busqueda):
    """
    Busca puntos racionales (x, y) donde x = p/q.
    Procedimiento base para localizar generadores.
    """
    a = mp.mpf(a_val)
    b = mp.mpf(b_val)
    puntos_hallados = []

    print(f"Buscando puntos para la curva de Rango 33...")
    
    for q in range(1, limite_busqueda):
        for p in range(-limite_busqueda, limite_busqueda):
            x = mp.mpf(p) / mp.mpf(q)
            
            # Ecuación: y^2 = x^3 + ax + b
            z = x**3 + a*x + b
            
            if z >= 0:
                y = mp.sqrt(z)
                # Validación del residuo para confirmar el punto
                residuo = abs(y**2 - z)
                
                if residuo < mp.mpf('1e-1900'):
                    punto = (x, y)
                    if punto not in puntos_hallados:
                        puntos_hallados.append(punto)
                        print(f"Punto P{len(puntos_hallados)} hallado:")
                        print(f"x = {p}/{q}")
                        print(f"y = {y}")
            
            if len(puntos_hallados) >= 33:
                return puntos_hallados
                
    return puntos_hallados

# Ejecución con tus parámetros de récord
A_COEFF = "852223"
B_COEFF = "1847"

# Nota: Inicia con un límite pequeño (p.ej. 500) para probar velocidad
lista_puntos = encontrar_puntos_vivar(A_COEFF, B_COEFF, 500)
