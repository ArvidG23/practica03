import pytest
from src.procesador import Analizador

# Ruta del archivo CSV usado por todas las pruebas
ARCHIVO = "datos/sri_ventas_2024.csv"

def test_retorna_diccionario():
    """La función ventas_totales_por_provincia debe retornar un diccionario."""
    analizador = Analizador(ARCHIVO)
    resultado = analizador.ventas_totales_por_provincia()
    assert isinstance(resultado, dict), "El resultado debe ser un diccionario"


def test_numero_de_provincias_coherente():
    """El número de provincias debe ser razonable (al menos 10 y no más de 30)."""
    analizador = Analizador(ARCHIVO)
    resultado = analizador.ventas_totales_por_provincia()
    cantidad = len(resultado)

    assert 10 <= cantidad <= 30, f"Número incoherente de provincias: {cantidad}"


def test_valores_numericos_y_no_negativos():
    """Todas las ventas deben ser números y no pueden ser negativas."""
    analizador = Analizador(ARCHIVO)
    resultado = analizador.ventas_totales_por_provincia()

    for prov, total in resultado.items():
        assert isinstance(total, (int, float)), f"El valor de {prov} no es numérico"
        assert total >= 0, f"El valor de {prov} es negativo, lo cual es incorrecto"


def test_provincia_existente():
    """La función ventas_por_provincia debe reconocer provincias existentes."""
    analizador = Analizador(ARCHIVO)
    
    provincias = analizador.ventas_totales_por_provincia().keys()
    
    # Elegimos 3 provincias que SI existen en tu CSV
    provincias_a_probar = ["LOJA", "PICHINCHA", "GUAYAS"]

    for prov in provincias_a_probar:
        assert prov in provincias, f"La provincia {prov} debería existir en el archivo"


def test_valores_de_provincias_correctos():
    """Verificar que las 3 provincias tengan ventas mayores a cero."""
    analizador = Analizador(ARCHIVO)

    # Provincias reales que sabemos que existen
    provincias = ["LOJA", "PICHINCHA", "GUAYAS"]

    for prov in provincias:
        valor = analizador.ventas_por_provincia(prov)
        assert valor > 0, f"La provincia {prov} debería tener ventas mayores a cero"
        

def test_exportaciones_totales_por_mes():
    analizador = Analizador("datos/sri_ventas_2024.csv")
    resultado = analizador.exportaciones_totales_por_mes()

    # Debe ser diccionario
    assert isinstance(resultado, dict)

    # Los meses deben ser enteros
    assert all(isinstance(mes, int) for mes in resultado.keys())

    # Los valores deben ser numéricos y no negativos
    assert all(isinstance(total, float) for total in resultado.values())
    assert all(total >= 0 for total in resultado.values())


def test_provincia_con_mayor_importaciones():
    analizador = Analizador("datos/sri_ventas_2024.csv")
    provincia, total = analizador.provincia_con_mayor_importaciones()

    # provincia debe ser texto
    assert isinstance(provincia, str)

    # total debe ser número positivo
    assert isinstance(total, float)
    assert total >= 0

    # La provincia debe existir en el dataset
    provincias_existentes = {fila["PROVINCIA"].strip().upper() for fila in analizador.datos}
    assert provincia in provincias_existentes
