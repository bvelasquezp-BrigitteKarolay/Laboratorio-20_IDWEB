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



# EJECUCION 
if __name__ == "__main__":

    # ejercicio 3 
    print("EJERCICIO 3 ")
    res3 = calcular_salario(salario_base=3000.0,
                            horas_extras=10,
                            pago_hora_extra=15.0,
                            bono=200.0,
                            afp_porcentaje=10.0,
                            salud_porcentaje=3.0)
    print(res3) 

    # ejercicio 4
    print("\nEJERCICIO 4 ")
    ejemplo4 = calcular_impuesto_progresivo(ingreso_mensual=5000.0) 
    print("Ingreso anual:", ejemplo4["ingreso_anual"])
    for tramo in ejemplo4["impuesto_por_tramo"]:
        print("Tramo:", tramo[0], "Base:", tramo[1], "Tasa:", tramo[2], "Impuesto tramo:", tramo[3])
    print("Total impuesto:", ejemplo4["total_impuesto"])
    print("Tasa efectiva %:", ejemplo4["tasa_efectiva_pct"])

    # ejercicio 5 
    print("\nEJERCICIO 5")
    matriz_espiral_5 = generar_espiral(5)
    for fila in matriz_espiral_5:
        print(fila)

    
