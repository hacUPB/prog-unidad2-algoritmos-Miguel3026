# Taller Algoritmos
1. **Verificación de peso de despegue**
    
    En una pista de pruebas de aeronaves, el sistema debe verificar si el peso total de la aeronave, incluyendo combustible y carga, supera el límite máximo permitido para el despegue. Dependiendo del resultado, el sistema deberá indicar si la aeronave está lista para despegar o si debe reducir carga o combustible.

**Datos de entrada**
|nombre|tipo|descripción|
|------|-----|----------|
|Peso_maximo|PF|Peso maximo de despegue|
|peso_aeronave|PF|peso de la aeronave en vacio|
|carga_pasajeros|PF|peso de la carga y pasajeros|
|peso_combustible|PF| peso del combustible|

**Datos intermedios**

|nombre|tipo|descripción|
|------|-----|----------|
|peso_total|PF|La suma de los pesos|

**Datos de salida**
|nombre|tipo|descripción|
|------|-----|----------|
|Situación_aeronave|Str|Dice si la aeronave puede despegar o no|

2. **Control de combustible en pruebas**
    
    Durante un ensayo en banco de un motor a reacción, se mide el nivel de combustible cada minuto y se detiene el registro cuando el combustible baja del 10%. Mostrar el tiempo total de operación antes de llegar a ese punto

 **Datos de entrada**
|nombre|tipo|descripción|
|------|-----|----------|
|nivel_combustible|PF|Nivel del combustible|

## Pseudocodigo 
````
Inicio

i = 0

mostrar("Ingrese el nivel de combustible:")

leer nivel_combustible

ND = nivel_combustible * 0.10

mientras nivel_combustible > ND

Leer valor_actual
i += 1

Fin mientras 

mostrar ("ha trasncurrido" i)

Fin 
````