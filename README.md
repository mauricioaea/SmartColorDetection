# Hola Chicos aqui les dejo la expliación del codigo, el cual puede resultar util para sus proyectos
Antes de inciar crear una carpeta en tus archivos. despues de esto la debes abrir en visual studio code o tu ide de preferecia.
# 1  activa el entorno virtual=> .\env\Scripts\activate      


 El código que he programado para detectar colores en objetos usando la cámara de tu computadora tiene muchas aplicaciones interesantes. Aquí te dejo algunas ideas de proyectos en los que podrías utilizarlo:


 1. ---Sistema de Clasificación de Objetos--- => (Desarrolla un sistema que clasifique objetos en función de su color. Por ejemplo, podrías usarlo para clasificar frutas y verduras en una línea de producción.)
 2. ---Sistema de Control de Acceso por Color--- => (Desarrolla un sistema de control de acceso que permita el acceso a ciertas áreas o funciones basándose en el color de un objeto que se presenta a la cámara.)
 3. ---Aplicación de Monitoreo de Plantas--- => (Crea una aplicación que monitoree el crecimiento de plantas y detecte el color de las hojas para determinar su salud.)
 4. ---Sistema de Seguimiento de Objetos--- => (Crea un sistema que pueda seguir un objeto de un color específico en movimiento, como un balón o un juguete.)
 5. ---Sistema de Alerta de Seguridad--- => (Crea un sistema de seguridad que envíe alertas cuando detecte un objeto de un color específico en un área restringida.)

# iniciamos instalando las librerias 

pip install opencv-python
pip install numpy

Incio y explicacion del codigo.

El codigo incia importando las librearias:

    import cv2 = esta la usamos para lsa herramientas de visón por computador
    import numpy as np => esta nos sirve par los arreglos y operacines matematicas

# aqui cargamos el video
    
    cap = cv2.VideoCapture(0)

en esta linea de codigo declaramosla variable 'cap', donde almacenaremos la información y utilizamos la herramienta cv2... de opencv para captura nuestro camara principal del pc, o puedes cambiar a 1 si tienes conectada otra camara por usb.

    
# aqui leemos el video
    while True: 
      ret, frame = cap.read()

mediante un ciclo while, estaremos leyendo los fotogramas del video, utilizamos la palabra reservada 'ret' el cual indica que es un boleano, 'frame' haciendo referencia a los frame del video, 'cap' como vimos arriba fue la variable donde almacenamos niestro video y 'read' para leer el video. 

    

# aqui cambio de color

    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

La imagenes capturadas por una camara normalmente vienen en formato 'RGB' (R=RED, G=GREN, B=BLUE) si bien son colores establecidos, en vision por computador los colores pueden tener direrentes tonalides, talvez un rojo mas intenso que otro y asi con toda la gama de colores que se puedan generar, es por eso que usaremos 'HSV' donde (H= los colores de RGB, S= Saturación. V=Luminocidad), en ese orden de ideas con estos parametros, y teneniendo diferentes saturaciones y exposiciones de un color a la luz, en visión por computador (VC) Será mas facil identificar la gama de colores.
explicaré cada parte de la linea del código.

1. asignamos una variable llamada 'hsv' donde quedaran almacenado nuestranueva lectura de color.
2. utilizamos la herramienta de opencv 'cv2.cvtColor' la cual recibira los argumentos par hacer el cambio de lectura de los colores.
3. llamamos a 'frame' haciendo referencia sobre que queremos aplicar el cambio
4. utiliamos la herramienta de opncv 'cv2.COLOR_RGB_HSV, donde estamos odenando se realice la correccion de color de RGB a HSV

        
     
     
# definimos los rangos de color, se ajusta segun el color a detectar

      lower_red =  np.array[0,100,100]
      upper_red =  np.array[10,255,255]

1. cramos 2 variables llamadas 'lower_red y upper_red' en las cuales almacenaremos la informacion de los colores que queremos detectar en nuestra visión por computador.

2. utilizamos la herramienta de la biblioteca Numpy, (np.array) la cual se encarga de realizar entre otras cosas operaciones matematicas, y las cuales contienen los numeros que hacen referencia a [0,100,100] como rojo intenso y [10,255,255] como otras variedades de rojo. para obtener estos numeros es necesaio revisar la paleta de colores (lo vereos en otra exlicación como extraer nuemeros para los colores o lo puedes buscar en chatgpt)
    
# creamos una mascara.      
       mask = cv2.inRange(hsv,lower_red,upper_red)

la mascara se encargara de extraer los pixeles de cada imagen que corresponden a nuestro color que hemos elegiodo en el paso anterior

- esta línea de código crea una máscara  "mask"binaria donde los píxeles blancos corresponden a los píxeles de la 
- imagen original que tienen un color dentro del rango de rojo definido por lower_red y upper_red
- cv2.inRange: Esta función de OpenCV es la encargada de crear la máscara. Toma tres argumentos
- hsv: La imagen en el espacio de color HSV que queremos analizar.
- lower_red: El límite inferior del rango de color que queremos detectar (en este caso, el rojo).
- upper_red: El límite superior del rango de color que queremos detectar.



# detectamos los contornos.

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

En resumen, esta línea de código encuentra todos los contornos en la imagen binaria mask, que representa las áreas donde se ha detectado un color específico. La función devuelve una lista de contornos y una jerarquía que describe la relación entre ellos. Esto es útil para realizar operaciones posteriores, como dibujar rectángulos alrededor de los objetos detectados.

- cv2.findContours:
Esta es la función de OpenCV que se utiliza para detectar contornos en una imagen. Devuelve una lista de contornos encontrados y otros parámetros relacionados.
- mask:
Este es el argumento de entrada para la función. mask es una imagen binaria (en blanco y negro) donde los píxeles blancos (valor 255) representan las áreas donde se ha detectado el color que estás buscando, y los píxeles negros (valor 0) representan el fondo.
- cv2.RETR_TREE:
Este es el segundo argumento de la función. Especifica el modo de recuperación de contornos. cv2.RETR_TREE recupera todos los contornos y construye una jerarquía de contornos. Esto significa que no solo se obtienen los contornos principales, sino también los contornos anidados (contornos dentro de otros contornos).
- cv2.CHAIN_APPROX_SIMPLE:
Este es el tercer argumento de la función. Especifica el método de aproximación de contornos. cv2.CHAIN_APPROX_SIMPLE significa que se almacenarán solo los puntos extremos de los contornos, lo que reduce la cantidad de memoria utilizada. Por ejemplo, si un contorno es un rectángulo, solo se almacenarán los cuatro vértices en lugar de todos los puntos que forman el contorno.
- contours, _:
La función findContours devuelve dos valores: una lista de contornos y una jerarquía de contornos (que describe la relación entre los contornos). En este caso, solo estamos interesados en los contornos, así que usamos _ para ignorar el segundo valor.

# Dibujar un rectángulo verde alrededor de cada contorno
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Filtrar por área para evitar ruido
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

Este fragmento de código recorre todos los contornos detectados en la imagen y dibuja un rectángulo verde alrededor de aquellos que cumplen con un criterio específico (en este caso, un área mínima). Esto es útil para resaltar los objetos detectados en la imagen.
Componentes del Código
for contour in contours::
Este es un bucle for que itera sobre cada contorno en la lista contours. Cada contour es una serie de puntos que representan la forma del objeto detectado.
- if cv2.contourArea(contour) > 500::
Esta línea utiliza la función cv2.contourArea para calcular el área del contorno actual.
El valor 500 es un umbral que se utiliza para filtrar los contornos. Si el área del contorno es mayor que 500, se considera que es un objeto significativo y se procede a dibujar el rectángulo. Esto ayuda a evitar el ruido, es decir, contornos pequeños que podrían ser causados por cambios menores en la imagen o por objetos no deseados.
- x, y, w, h = cv2.boundingRect(contour):
Esta línea utiliza la función cv2.boundingRect para calcular el rectángulo delimitador (bounding box) que rodea el contorno.
La función devuelve cuatro valores:
- x: la coordenada x de la esquina superior izquierda del rectángulo.
- y: la coordenada y de la esquina superior izquierda del rectángulo.
- w: el ancho del rectángulo.
- h: la altura del rectángulo.
Este rectángulo es el más pequeño que puede contener completamente el contorno.
- cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2):
Esta línea dibuja el rectángulo en el fotograma original (frame).
Los parámetros de la función cv2.rectangle son:
- frame: la imagen sobre la que se dibuja el rectángulo.
- (x, y): la esquina superior izquierda del rectángulo.
- (x + w, y + h): la esquina inferior derecha del rectángulo (calculada sumando el ancho y la altura a las coordenadas x y y).
- (0, 255, 0): el color del rectángulo en formato BGR (en este caso, verde).
- 2: el grosor del borde del rectángulo en píxeles.


# Muestramsos el resultado

     
    cv2.imshow('Detección de color', frame)

con la herramienta de la biblioteca de opencv cv2.imshow mostramos una ventana donde observaremos la deteccion de los colores
     
- Esta función de OpenCV se utiliza para mostrar una imagen en una ventana. Toma dos argumentos:
- 'frame': Este es el nombre que se le asigna a la ventana donde se mostrará la imagen. Puedes cambiar este nombre por cualquier otro que   prefieras.
- mask: Esta es la variable que contiene la imagen que queremos mostrar, en este caso, la máscara binaria que hemos creado.
     
     
# Salir si se presiona la tecla 'q'

finalmene, ecribimos la siguinte liena de codigo que basicamente nos permite cerar la ventana que estaras observando precionando la tecla 'q'
     
      if cv2.waitKey(1) & 0xFF == ord('q'):
               break

# Liberar la captura y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
 
""" Finalmente en tu terminal ejecuta el comando (python detection_color.py)  para ver el codigo en ejecución 

finalmente si tienes dudas no dudes en contactarme. [MauricioErazoArango] (https://github.com/mauricioaea)(https://www.tiktok.com/@mauricioa.erazo?_t=8oquUxmJ1Mc&_r=1)

[Simpler-smarter-Futher] 


si deseas detectar otro tipo de colores aqui te dejo el codigo:

Ejemplo de Rangos de Colores Comunes
Aquí tienes algunos rangos de colores comunes en el espacio HSV:
# Rojo:
Rango bajo: [0, 100, 100]
Rango alto: [10, 255, 255] (también necesitas un rango para el rojo más oscuro)
Rango bajo: [170, 100, 100]
Rango alto: [180, 255, 255]
# Verde:
Rango bajo: [40, 100, 100]
Rango alto: [80, 255, 255]
# Azul:
Rango bajo: [100, 100, 100]
Rango alto: [140, 255, 255]

# Amarillo:
Rango bajo: [20, 100, 100]
Rango alto: [30, 255, 255]


Paso 2: Ajustar el Código para Detectar el Nuevo Color

Si deseas detectar solo el color verde, puedes reemplazar la línea de la máscara anterior (que detectaba rojo) con la nueva máscara para verde.
1. Definir los Nuevos Rangos de Color
Supongamos que deseas detectar el color verde. Debes agregar los nuevos rangos en tu código. Aquí hay un ejemplo de cómo hacerlo:

# Definir el rango de color verde en el espacio HSV
lower_green = np.array([40, 100, 100])
upper_green = np.array([80, 255, 255])

# Crear una máscara para el color verde
mask = cv2.inRange(hsv, lower_green, upper_green)


# Si deseas detectar múltiples colores, puedes combinar las máscaras.

lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])

# Crear máscaras para los colores
   
# Definir el rango de color verde
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([80, 255, 255])

# Crear máscaras para los colores
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

# Combinar las máscaras
    mask = cv2.bitwise_or(mask_red1, mask_red2)
    mask = cv2.bitwise_or(mask, mask_green)


De aqui en adelante continua con el codigo normal: 
# Encontrar contornos en la máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)....
