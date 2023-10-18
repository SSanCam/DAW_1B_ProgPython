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

# <u>Cadenas:</u>
<ol>

<li>Métodos de Formato:</li>

<ul>
<li>upper(): Convierte la cadena a mayúsculas.</li>
<li>lower(): Convierte la cadena a minúsculas.</li>
<li>capitalize(): Convierte la primera letra de la cadena a mayúscula y las demás a minúsculas.</li>
<li>title(): Convierte la primera letra de cada palabra en la cadena a mayúsculas.</li>
</ul>

<li>Métodos de Búsqueda y Reemplazo:</li>

<ul>
<li>find(subcadena): Devuelve el índice de la primera aparición de la subcadena (o -1 si no se encuentra).</li>
<li>replace(subcadena, nueva_subcadena): Reemplaza todas las apariciones de la subcadena con la nueva_subcadena.</li>
<li>count(subcadena): Cuenta cuántas veces aparece la subcadena en la cadena.</li>
<li>startswith(prefijo): Comprueba si la cadena comienza con el prefijo especificado.</li>
<li>endswith(sufijo): Comprueba si la cadena termina con el sufijo especificado.</li>
</ul>

<li>Métodos de Modificación:</li>
<ul>
<li>strip(): Elimina espacios en blanco al principio y al final de la cadena.</li>
<li>lstrip(): Elimina espacios en blanco del lado izquierdo de la cadena.</li>
<li>rstrip(): Elimina espacios en blanco del lado derecho de la cadena.</li>
</ul>

<li>Métodos de División y Unión:</li>

<ul>
<li>split(delimitador): Divide la cadena en una lista de subcadenas usando el delimitador especificado.</li>
<li>join(iterable): Une las cadenas de un iterable en una sola cadena utilizando la cadena como separador.</li>
</ul>

<li>Métodos de Validación:</li>
<ul>
<li>isalpha(): Comprueba si la cadena contiene solo letras.</li>
<li>isdigit(): Comprueba si la cadena contiene solo dígitos.</li>
<li>isalnum(): Comprueba si la cadena contiene solo letras y/o dígitos.</li>
<li>isupper(): Comprueba si todos los caracteres en la cadena están en mayúsculas.</li>
<li>islower(): Comprueba si todos los caracteres en la cadena están en minúsculas.</li>
</ul>

<li>Otros Métodos:</li>
<ul></ul>
<li>len(cadena): Devuelve la longitud de la cadena.</li>
<li>index(subcadena): Devuelve el índice de la primera aparición de la subcadena (genera una excepción si no se encuentra).</li>
<li>startswith(prefijo): Comprueba si la cadena comienza con el prefijo especificado.</li>
<li>endswith(sufijo): Comprueba si la cadena termina con el sufijo especificado.</li>
</ul>

</ol>

## EJEMPLOS:

Para contar cuantas veces sale cada palabra en un texto: 
```
# Texto de ejemplo
texto = "Este es un ejemplo de un texto de ejemplo. El ejemplo muestra cómo contar palabras."

# Dividir el texto en palabras utilizando el espacio como delimitador
palabras = texto.split()

# Inicializar un diccionario para el conteo de palabras
conteo_palabras = {}

# Contar las palabras
for palabra in palabras:
    # Limpiar la palabra de signos de puntuación y convertirla a minúsculas
    palabra = palabra.strip(".,!?:;").lower()
    # Contar la palabra en el diccionario
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

# Mostrar el conteo de palabras
for palabra, frecuencia in conteo_palabras.items():
    print(f"'{palabra}': {frecuencia}")
```

Para contar una única palabra podemos usar *count():*
```
# Texto de ejemplo
texto = "Este es un ejemplo de un texto de ejemplo. El ejemplo muestra cómo contar palabras."

# Palabra a contar en una variable
palabra_a_contar = "ejemplo"

# Usar count() con la variable
contador = texto.count(palabra_a_contar)

print(f"La palabra '{palabra_a_contar}' se repite {contador} veces en el texto.")
```

