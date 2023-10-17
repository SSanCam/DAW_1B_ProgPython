# Programación, 
## Curso 2023/24, IES Rafael Alberti.

### <ul><li>Tema 1.</li></ul>
<u>**Pseudocódigo.**</u>

Inicio

    Escribe "un texto a escribir".
    Lee X
    _______________________
    Si (condición) entonces
        Instrucciones.
    _______________________
    Si (condición) entonces
        Instrucciones.
    Sino
        Instrucciones.
    _______________________
    Según (valor) entonces
        opción 1:
            Instrucciones.
        opción N:
            Instrucciones.
    _______________________
    Mientras (condición) hacer
        Instrucciones
    _______________________
    Para X en (1..N) hacer
        Instrucciones.
    

Fin
<br>
<hr>

<ol>
<li>Operadores matemáticos básicos: +, -, *, / y % (módulo).

<li>Operadores relacionales: == (igual), >, <, >=, <= y != (distinto).

<li>Operadores lógicos: and, or y not (negación).

<li>La asignación de valores a una variable la realizaremos con el símbolo =

</ol>

<hr>

# **Estructuras de control secuencial.**

```
Inicio
    Instrucción1
    …
    Instrucción
Fin
```

# **Estructuras de control condicional.**

*Vamos a utilizar 3 tipos de condicionales: simple, doble y múltiple.*

<ol>
<li>Condicional simple:</li>

```
Si (condición) entonces
    Instrucción1
    …
    InstrucciónN
```

<li>Condicional doble:</li>

```
Si (condición) entonces
    Instrucción1
    …
    InstrucciónN
Sino
    Instrucción1
    …
    InstrucciónN
```
<li>Condicional múltiple:</li>

```
Según valor_selector entonces 
    opcion1:
        Instrucción1
        …
        InstrucciónI  
    opcion2:
        InstrucciónJ
        …
        InstrucciónN
```

<li>Estructuras anidadas:

```
Si (condición) entonces
    Instrucciones1
Sino
    Si (condición) entonces
        InstruccionesI
    Sino
        Si (condición) entonces
            InstruccionesJ
        Sino
            InstruccionesN
```

</ol>

# <u>**Estructuras de control iterativa.**</u>

<ul><li>ESTRUCTURA ITERATIVA <b>MIENTRAS:</b></li></ul>

<p>Iteración con salida al principio (Mientras): primero se evalúa la condición y en caso de cumplirse ejecuta el bloque de instrucciones. Las instrucciones contenidas deben actuar sobre los valores usados en la condición para evitar bucles infinitos.</p>

```
Mientras (condición) hacer
    Instrucción1
    …
    InstrucciónN
```

```
Mientras (cont > 0) hacer
    Escribe cont
    cont = cont - 1
```

<ul><li>ESTRUCTURA ITERATIVA <b>PARA:</b></li></ul>
<p>Ejecutará el bloque de instrucciones un número determinado de veces. Hace uso de una variable que irá incrementando o decrementando su valor de uno en uno en función de un rango de valores.</p>

```
Para i en (1…N) hacer
    Instrucción1
    …
    InstrucciónN
```

```Para i en (N…0) hacer
    Instrucción1
    …
    InstrucciónN
```
```
Inicio
    suma = 0 
    Para i en (1…10) hacer
        suma = suma + 1
    Escribe “La suma de los primeros 10 números enteros es ” + suma
Fin
```