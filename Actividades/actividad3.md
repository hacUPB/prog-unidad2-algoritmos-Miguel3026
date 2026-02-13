## Pseudocodigo
````
inicio

Leer ID, S1,S2,S3,S4,S5,S6

Total= S1+S2+S3+S4+S5+S6

Prom= Total/6

Mostrar ID, Total, Prom

Fin
````
## Ejercicio 1
Un acuario necesita determinar cuantos litros o galones de agua caben en un acuario, pero solo dispone de una cinta metrica. Diseña un algoritmo para solucionr el problema.

**Datos de entrada:**
- **Largo:** Largo del tanque en cm
- **Ancho:** Ancho del tanque en cm 
- **Alto:** Alto del tanque en cm
- **Unidad:** Unidad de medida, litro o galón 

**Datos de salida:**

- **Volumen_lt:** Total del tanque en litros 
- **Volumen_gal:** Total del tanque en galones 

## Pseudocodigo

````
inicio 

mostrar "Por favor ingrese las medidas del tanque"

Leer Largo, Ancho, Alto, Unidad

mostrar "ingrese L para litros y G para galones"

Leer Unidad

volumen= Largo * Ancho * Alto // volumen en cm°3 - equivalente a mL

Volumen_lt = volumen/1000 // en litros

si Unidad= "G"

volumen_gl= Volumen_lt * 0.26

mostrar volumen_gl 

sino

mostrar volumen_lt

Fin si
Fin

````

## Ejercicio 2
Realice un algoritmo para determinar cuanto se debe pagar por equis cantidad de lapices considerando que si son 1000 o mas el costo es de 85$ cada uno; de lo contrario, el precio es de 90$. 

**Datos de entrada:**
- **cantidad_lapices:** cantidad de lapices a comprar 

**Datos de salida:** 
- **total_1:** $85 si la cantidad es mayor o igual a 1000
- **total_2:** $90 si la cantidad es menor a 1000




## Pseudocodigo

````
Inicio

mostrar "ingrese la cantidad de lapices a comprar"

Leer cantidad_lapices

si

cantidad_lapices >= 1000

 total_1 = cantidad_lapices * 85

 mostrar "total_1" 

 si no 

 total_2 = cantidad_lapices *  90 

 mostrar "total_2"

 Fin si

 Fin 

````

## Ejercicio 3
Un almacén de ropa tiene una promoción: por compras superiores a $250 000 se les aplicará un descuento de 15%, de caso contrario, sólo se aplicará un 8% de descuento. Realice un algoritmo para determinar el precio final que debe pagar una persona por comprar en dicho almacén y de cuánto es el descuento que obtendrá. 

**Datos de entrada:**
- **valor_compra:** Valor total de la compra

**Datos de salida:**
- **descuento_1:** descuento si el valor de la compra es mayor a 250000
- **descuento_2:** descuento si el valor de la compra es menor o igual a 250000
- **valor_venta1:** valor total de la compra con el descuento del 15% aplicado 
- **valor_venta2:** valor total de la compra con el descuento del 8% aplicado


## Pseudocodigo
````
Inicio 

mostrar("ingrese el valor de su compra")

Leer valor_compra

si 

valor_compra > 250000

descuento_1 = valor_compra*0.15

valor_venta1 = valor_compra - descuento_1

mostrar("El valor de su compra es:", valor_venta1)

sino

descuento_2 = valor_compra*0.08 

valor_venta2 = valor_compra - descuento_2

mostrar("El valor de su compra es:", valor_venta2)

Fin si 

Fin
````
## Ejercicio 4
El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de $65.00; de 50 a 99 alumnos, el costo es de $70.00, de 30 a 49, de $95.00, y si son menos de 30, el costo de la renta del autobús es de $4000.00, sin importar el número de alumnos.


## Datos de Entrada

- **alumnos:** Cantidad de alumnos que irán al viaje.

## Datos de Salida

- **total_pagar1:** Total del viaje si alumnos >= 100
- **total_pagar2:** Total del viaje si alumnos >= 50 y alumnos <= 99
- **total_pagar3:** Total del viaje si alumnos >= 30 y alumnos <= 49
- **total_pagar4:** Total del viaje si alumnos < 30



## Pseudocodigo
````
Inicio

Mostrar ("Ingrese la cantidad de alumnos que iran al viaje")

Leer alumnos

Si

alumnos >= 100 

total_pagar1 = alumnos * 65.00

Mostrar ("Total del viaje: ", total_pagar1)

Sino Si 

alumnos >= 50 Y alumnos <= 99 

total_pagar2 = alumnos * 70.00

Mostrar ("El total del viaje es: ", total_pagar2)

Sino Si 
 
alumnos >= 30 Y alumnos <= 49 Entonces

total_pagar3 = alumnos * 95.00

Mostrar ("El total del viaje es: ", total_pagar3)

Sino

total_pagar4 = 4000.00

Mostrar ("El total del viaje es: ", total_pagar4)

Fin si

Fin

````