"""
Objetivo: Crear un simulador de cuota mensual de préstamos hipotecarios

1. Crea una clase llamada LoanSimulator 
que modele el proceso de calcular el pago total de un préstamo hipotecario, 
incluyendo tanto el capital inicial como los intereses generados 
a lo largo del plazo del préstamo.

2. La clase toma como parámetros detalles_prestamo, 
un número complejo cuya parte real será la entrada proporcionada 
para la hipoteca y la parte imaginaria el tipo de interés.

3. También tomará como parámetro opcional los años del préstamos hipotecario (por defecto 30) 
y el precio de la vivienda (por defecto para este ejercicio 300_000).

4. Deben almacenarse en el método constructor de la clase al menos los siguientes atributos de instancia:
4.1 tasa_mensual: Tasa de interés (parte imaginaria de detalles_prestamo) dividida entre 12 para convertirla a mensual y dividida entre 100
4.2 numero_pagos: Numero de pagos totales (número de años * 12).
4.3 entrada: Parte real del parámetro detalles_prestamo.
4.4 prestamo: Precio de la vivienda restando la entrada.
4.5 cuota_mensual: Parámetro a calcular en el programa (inicialmente 0).

5. Implementa un método llamado calcular_pago_total que realice 
el cálculo de la cuota mensual a pagar del préstamo hipotecario 
y que actualice el atributo cuota_mensual. 
El cálculo de la cuota mensual se realiza mediante la siguiente fórmula:
Cuota mensual = prestamo * (tasa de interés mensual * (1 + tasa de interés mensual)**número de pagos) / ((1 + tasa de interés mensual)**snúmero de pagos - 1)

6. Implementa otro método mostrar_resultados que imprima la simulación de la hipoteca: 
el precio de la vivienda, la entrada, los años y finalmente la cuota mensual.

7. Instancia la clase con un número complejo representativo y ejecuta los métodos para calcular el pago total y mostrar los resultados.
"""

"""
Resultado esperado
----- Simulación Hipoteca -----
Para una vivienda de 300000 euros, aportando una entrada de 50000.0 euros y con una tasa de interés del 2.5% anual durante 30 años:
Cuota mensual a pagar: 987.8022470442972 euros
----- Fin de la Simulación -----
"""

import os
from loan import LoanSimulator


def main():
    # os.system("cls")
    
    loan = LoanSimulator(3 * 1e6, 5 * 1e5)
    loan.print_loan()


if __name__ == "__main__":
    main()