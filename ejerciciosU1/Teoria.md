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

**Estructuras de control secuencial.**

```
Inicio
    Instrucción1
    …
    Instrucción
Fin
```

**Estructuras de control condicional.**

*Vamos a utilizar 3 tipos: simple, doble y múltiple.*

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
