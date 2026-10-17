"""Módulo de cálculo de descuentos con validaciones corregidas."""

def aplicar_descuento(precio, porcentaje):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    return precio * (1 - porcentaje / 100)

def calcular_descuento(precio, porcentaje):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    return precio * porcentaje / 100

def calcular_precio_final(precio, impuesto, descuento):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if impuesto < 0:
        raise ValueError("El impuesto no puede ser negativo")
    if descuento < 0 or descuento > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")
    precio_con_descuento = aplicar_descuento(precio, descuento)
    impuesto_monto = precio_con_descuento * (impuesto / 100)
    return precio_con_descuento + impuesto_monto

def descuento_por_volumen(cantidad, precio_unitario):
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa")
    if precio_unitario < 0:
        raise ValueError("El precio unitario no puede ser negativo")
    subtotal = cantidad * precio_unitario
    if cantidad >= 100:
        descuento = 20
    elif cantidad >= 50:
        descuento = 15
    elif cantidad >= 20:
        descuento = 10
    elif cantidad >= 10:
        descuento = 5
    else:
        descuento = 0
    return aplicar_descuento(subtotal, descuento)

def descuento_cumulativo(precio, descuentos):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if not descuentos:
        return precio
    precio_actual = precio
    for desc in descuentos:
        if desc < 0 or desc > 100:
            raise ValueError("Cada descuento debe estar entre 0 y 100")
        precio_actual = aplicar_descuento(precio_actual, desc)
    return precio_actual

def descuento_apilado(precio, descuentos):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if not descuentos:
        return precio
    if any(desc < 0 or desc > 100 for desc in descuentos):
        raise ValueError("Cada descuento debe estar entre 0 y 100")
    total_descuento = sum(descuentos)
    if total_descuento > 100:
        raise ValueError("La suma de descuentos no puede superar el 100%")
    return aplicar_descuento(precio, total_descuento)
