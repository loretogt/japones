# japones
Se trata de una aplicación que corre en terminal para poder practicar y aprender palabras en japonés

## Importante ‼️
No es una versión final, donde se encuentran los datos ("datos.jason") se está constantemente actualizando según voy aprendiendo palabras. 

## Requisitos
Es necesario tener instalado alguna version de python en el ordenador

## Como ejecutarlo 
Desde la terminal tienes que irte a la carpeta donde este almacenado el codigo, y para poder ejecutarlo simplemente escribir
```bash
python3 main.py 
```
Una vez ejecutado el codigo se ofrecen 5 opciones distintas, para poder seleccioar una de las opciones simplemente hay que escirbir por teclado el numero de la opción que quieras ejecutar

## Opiones que hay

### 1. De japonés a Español
Sirve para repasar, ya que te ofrece una palabra en japonés de la que tendrás que escribir su traducción en español.  
Antes de empezar debes seleccionar sobre que grupo de palabras quieres repasar (para seleccionarlo debes escribir), o si quieres una bateria con todas las palabras disponibles selecciona 1 ("sobre todo")  
Una vez seleccionado el tema aparecerá por terminal una palabra en japonés de la que deberás escirbir su traducción en español y pulsar intro. Te dirá si es correcto o incorrecto (y su correcta traducción). Ojo que algunas palabras tienen dos posibles traducciones, solo tendra en cuenta una de ellas. 
#### Para parar
Para volver al menu principal debes escribir la palabra
```bash
stop
```

### 2. De español a japonés
Sirve para repasar, ya que te ofrece una palabra en español de la que tendrás que escribir su traducción en japonés.  
Antes de empezar debes seleccionar sobre que grupo de palabras quieres repasar (para seleccionarlo debes escribir), o si quieres una bateria con todas las palabras disponibles selecciona 1 "sobre todo"  
Una vez seleccionado el tema aparecerá por terminal una palabra en español de la que deberás escirbir su traducción en japones y pulsar intro. 
La pablabra en japones debe estar escrita en hiragana (tambien da como correcta su escritura en kanji) o si así es la palabra en katakana
Te dirá si es correcto o incorrecto (y su correcta traducción). Ojo que algunas palabras tienen dos posibles traducciones, solo tendra en cuenta una de ellas. 
#### Para parar
Para volver al menu principal debes escribir la palabra
```bash
stop
```

### 3. Mostrar vocabulario
Te muestra todas las palabras pertenecientes a cada uno de los grupos de pablabras, debes seleccionar el grupo del que quieras (para seleccionarlo debes escribir).
El orden en el que muestra las pablabras es Español-Hiragana-Kanji(si tiene)

### 4. Diccionario Español-Japones
De una palabra en español que tu escribas te muestra su traduccion en japonés.  Ojo que algunas palabras tienen dos posibles traducciones, solo tendra en cuenta una de ellas. 
#### Para parar
Para volver al menu principal debes escribir la palabra
```bash
stop
```

### 5. Diccionario Japones-Español
De una palabra en japonés que tu escribas te muestra su traduccion en español.  Ojo que algunas palabras tienen dos posibles traducciones, solo tendra en cuenta una de ellas. 
#### Para parar
Para volver al menu principal debes escribir la palabra
```bash
stop
```