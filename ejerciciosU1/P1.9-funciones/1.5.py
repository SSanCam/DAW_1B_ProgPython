"""1.5 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, 
sino que se imprime desde dentro de la función."""

def precio_final(importe: float, iva: int) : 
    importe = float(input("Cuanto cuesta el articulo?: "))
    iva = float(input("Que porcentaje de IVA debe aplicarse?: "))
    if (iva < 0 or iva > 100):
        iva =20
        iva_aplicar = (iva / 100) * importe
        print ("ERROR.")
    else:
        iva_aplicar = (iva / 100) * importe
        importe_total = importe + iva_aplicar
        print(f"Precio de articulo: {importe}\nIVA a aplicar: {iva_aplicar}\nEl precio final es de: {importe_total} €.") 

print(precio_final())