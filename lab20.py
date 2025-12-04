# TAREA 20
# Autora: Brigitte Karolay Velasquez Puma

import math
from typing import List, Dict, Tuple, Optional


# EJERCICIO 3
def calcular_salario(salario_base: float,
                     horas_extras: float,
                     pago_hora_extra: float,
                     bono: float,
                     afp_porcentaje: float,
                     salud_porcentaje: float) -> Dict[str, float]:
    
    salario_bruto = salario_base + (horas_extras * pago_hora_extra) + bono
    descuento_afp = salario_base * (afp_porcentaje / 100.0)
    descuento_salud = salario_base * (salud_porcentaje / 100.0)
    descuentos_totales = descuento_afp + descuento_salud
    salario_neto = salario_bruto - descuentos_totales

    return {
        "salario_bruto": round(salario_bruto, 2),
        "descuento_afp": round(descuento_afp, 2),
        "descuento_salud": round(descuento_salud, 2),
        "descuentos_totales": round(descuentos_totales, 2),
        "salario_neto": round(salario_neto, 2)
    }


# EJERCICIO 4
def calcular_impuesto_progresivo(ingreso_mensual: float) -> Dict[str, object]:
    
    ingreso_anual = ingreso_mensual * 14.0

    tramos = [
        (0, 20000, 0.0),
        (20000, 50000, 0.10),
        (50000, 100000, 0.20),
        (100000, math.inf, 0.30)
    ]

    impuesto_por_tramo = []
    total_impuesto = 0.0

    for inferior, superior, tasa in tramos:
        if ingreso_anual <= inferior:
            base = 0.0
        else:
            base = min(ingreso_anual, superior) - inferior
            if base < 0:
                base = 0.0

        impuesto_tramo = base * tasa
        impuesto_por_tramo.append((
            f"{int(inferior)} - {'INF' if superior == math.inf else int(superior)}",
            round(base, 2),
            tasa,
            round(impuesto_tramo, 2)
        ))
        total_impuesto += impuesto_tramo

    tasa_efectiva = (total_impuesto / ingreso_anual * 100.0) if ingreso_anual > 0 else 0.0

    return {
        "ingreso_anual": round(ingreso_anual, 2),
        "impuesto_por_tramo": impuesto_por_tramo,
        "total_impuesto": round(total_impuesto, 2),
        "tasa_efectiva_pct": round(tasa_efectiva, 4)
    }


# EJERCICIO 5
def generar_espiral(n: int) -> List[List[int]]:
    
    if not isinstance(n, int) or n < 3:
        raise ValueError("N debe ser entero >= 3")

    matriz = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1
    max_num = n * n

    while num <= max_num:
        
        for j in range(left, right + 1):
            matriz[top][j] = num
            num += 1
        top += 1

        
        for i in range(top, bottom + 1):
            matriz[i][right] = num
            num += 1
        right -= 1

        
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matriz[bottom][j] = num
                num += 1
            bottom -= 1

       
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matriz[i][left] = num
                num += 1
            left += 1

    return matriz


# EJERCICIO 6
def normalizar(lista: List[float], modo: str) -> List[float]:
    
    if modo not in ("minmax", "zscore", "unit"):
        raise ValueError("Modo inválido. Use 'minmax', 'zscore' o 'unit'.")

    if not lista:
        return []

    vals = [float(x) for x in lista]

    if modo == "minmax":
        vmin = min(vals)
        vmax = max(vals)
        denom = (vmax - vmin)
        if denom == 0:
            
            return [0.0 for _ in vals]
        return [ (x - vmin) / denom for x in vals ]

    if modo == "zscore":
        n = len(vals)
        mean = sum(vals) / n
        var = sum((x - mean) ** 2 for x in vals) / n  
        std = math.sqrt(var)
        if std == 0:
            return [0.0 for _ in vals]
        return [ (x - mean) / std for x in vals ]

    norm = math.sqrt(sum(x * x for x in vals))
    if norm == 0:
        return [0.0 for _ in vals]
    return [ x / norm for x in vals ]


# EJERCICIO 7

def agregar_estudiante(lista: List[Dict], nombre: str, edad: int, promedio: float) -> None:
    """
    AGREGA UN ESTUDIANTE (diccionario) A LA LISTA
    """
    lista.append({"nombre": nombre, "edad": edad, "promedio": promedio})

def mostrar_estudiantes(lista: List[Dict]) -> List[Tuple[str, int, float]]:
    """
    RETORNA UNA LISTA DE TUPLAS (nombre, edad, promedio)
    """
    return [(e["nombre"], e["edad"], e["promedio"]) for e in lista]

def mejor_promedio(lista: List[Dict]) -> Optional[Dict]:
    """
    RETORNA EL ESTUDIANTE CON MEJOR PROMEDIO O None SI LISTA VACIA
    """
    if not lista:
        return None
    return max(lista, key=lambda e: e["promedio"])

def buscar_por_nombre(lista: List[Dict], nombre: str) -> Optional[Dict]:
    """
    BUSCA ESTUDIANTE POR NOMBRE (COINCIDENCIA EXACTA, CASE SENSITIVE)
    """
    for e in lista:
        if e["nombre"] == nombre:
            return e
    return None

def eliminar_por_nombre(lista: List[Dict], nombre: str) -> bool:
    """
    ELIMINA PRIMERA OCURRENCIA POR NOMBRE. RETORNA True SI SE ELIMINO.
    """
    for i, e in enumerate(lista):
        if e["nombre"] == nombre:
            lista.pop(i)
            return True
    return False

def registro_estudiantes():
    """
    MENU PARA GESTIONAR ESTUDIANTES.
    
    """
    estudiantes = []
    while True:
        print("\nMENU - REGISTRO DE ESTUDIANTES")
        print("1) Agregar estudiante")
        print("2) Mostrar estudiantes")
        print("3) Mostrar estudiante con mejor promedio")
        print("4) Buscar por nombre")
        print("5) Eliminar por nombre")
        print("6) Salir")
        opcion = input("Elija una opcion [1-6]: ").strip()
        if opcion == "1":
            nombre = input("Nombre: ").strip()
            try:
                edad = int(input("Edad: ").strip())
                promedio = float(input("Promedio (0-20): ").strip())
            except ValueError:
                print("Entrada invalida. Edad o promedio no numerico.")
                continue
            agregar_estudiante(estudiantes, nombre, edad, promedio)
            print("Estudiante agregado.")
        elif opcion == "2":
            lista = mostrar_estudiantes(estudiantes)
            if not lista:
                print("No hay estudiantes registrados.")
            else:
                for t in lista:
                    print(f"- {t[0]} | Edad: {t[1]} | Promedio: {t[2]}")
        elif opcion == "3":
            m = mejor_promedio(estudiantes)
            if m is None:
                print("No hay estudiantes registrados.")
            else:
                print(f"Mejor promedio: {m['nombre']} -> {m['promedio']}")
        elif opcion == "4":
            nombre = input("Nombre a buscar: ").strip()
            res = buscar_por_nombre(estudiantes, nombre)
            if res:
                print(f"Encontrado: {res['nombre']} | Edad: {res['edad']} | Promedio: {res['promedio']}")
            else:
                print("No se encontro estudiante con ese nombre.")
        elif opcion == "5":
            nombre = input("Nombre a eliminar: ").strip()
            ok = eliminar_por_nombre(estudiantes, nombre)
            if ok:
                print("Estudiante eliminado.")
            else:
                print("No se encontro estudiante con ese nombre.")
        elif opcion == "6":
            print("Saliendo del registro.")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")

# EJECUCION

if __name__ == "__main__":

    # Ejercicio 3
    print("EJERCICIO 3")
    try:
        res3 = calcular_salario(
            salario_base=3000.0,
            horas_extras=10,
            pago_hora_extra=15.0,
            bono=200.0,
            afp_porcentaje=10.0,
            salud_porcentaje=3.0
        )
        print(res3)
    except NameError:
        print("ERROR: calcular_salario NO definida.")

    # Ejercicio 4
    print("\nEJERCICIO 4")
    while True:
        try:
            s = input("Ingrese ingreso mensual: ").strip()
            ingreso_mensual = float(s)
            break
        except ValueError:
            print("ENTRADA NO VALIDA")
    try:
        resultado4 = calcular_impuesto_progresivo(ingreso_mensual=ingreso_mensual)
        print("Ingreso anual:", resultado4["ingreso_anual"])
        for tramo in resultado4["impuesto_por_tramo"]:
            print("Tramo:", tramo[0], "Base:", tramo[1], "Tasa:", tramo[2], "Impuesto tramo:", tramo[3])
        print("Total impuesto:", resultado4["total_impuesto"])
        print("Tasa efectiva %:", resultado4["tasa_efectiva_pct"])
    except NameError:
        print("ERROR")

    # Ejercicio 5
    print("\nEJERCICIO 5")
    while True:
        try:
            s = input("Ingrese N (entero >= 3): ").strip()
            n = int(s)
            if n < 3:
                print("N DEBE SER >= 3.")
                continue
            break
        except ValueError:
            print("ENTRADA NO VALIDA")
    try:
        matriz = generar_espiral(n)
        for fila in matriz:
            print(fila)
    except NameError:
        print("ERROR")
    except Exception as e:
        print("ERROR AL GENERAR LA ESPIRAL:", e)

    # Ejercicio 6
    print("\nEJERCICIO 6")
    while True:
        s = input("Ingrese numeros: ").strip()
        if s == "":
            print("LISTA VACIA. INTENTE DE NUEVO.")
            continue
        try:
            lista = [float(x.strip()) for x in s.split(",") if x.strip() != ""]
            if not lista:
                print("LISTA VACIA. INTENTE DE NUEVO.")
                continue
            break
        except ValueError:
            print("ENTRADA NO VALIDA")
    while True:
        modo = input("Ingrese modo (minmax / zscore / unit) [minmax]: ").strip().lower() or "minmax"
        if modo not in ("minmax", "zscore", "unit"):
            print("MODO INVALIDO. ESCRIBA minmax, zscore o unit.")
            continue
        break
    try:
        resultado6 = normalizar(lista, modo)
        print("Original:", lista)
        print(f"{modo}:", resultado6)
    except NameError:
        print("ERROR")
    except Exception as e:
        print("ERROR AL NORMALIZAR:", e)

    # Ejercicio 7 
    print("\nEJERCICIO 7")
    try:
        registro_estudiantes() 
    except NameError:
        print("ERROR")

 