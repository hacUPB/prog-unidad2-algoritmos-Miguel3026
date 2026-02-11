Pseudocodigo
inicio

Leer ID, S1,S2,S3,S4,S5,S6

Total= S1+S2+S3+S4+S5+S6

Prom= Total/6

Mostrar ID, Total, Prom

Fin

## Ejercicio 1
Un acuario necesita determinar cuantos litros o galones de agua caben en un acuario, pero solo dispone de una cinta metrica. Diseña un algoritmo para solucionr el problema.

**Datos de entrada:**
- **Largo:**Largo del tanque en cm
- **Ancho:** Ancho del tanque en cm 
- **Alto:** Alto del tanque en cm
- **Unidad:** Unidad de medida, litro o galón 

**Datos de salida:**

- **Volumen_lt:**Total del tanque en litros 
- **Volumen_gal:**Total del tanque en galones 

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
| nombre | tipo | descripción |
| ------- | ---- | -----------| 





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
