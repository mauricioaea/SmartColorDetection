import cv2
import numpy as np

# Capturar el video
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: no se pudo abrir la cámara")
    exit()

while True:
    # Leer un fotograma
    ret, frame = cap.read()
    if not ret:
        print("Error: no se pudo leer el fotograma")
        break

    # Convertir a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definir el rango de color rojo en el espacio HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Crear una máscara para los colores en el rango definido
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Encontrar contornos en la máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar un rectángulo verde alrededor de cada contorno
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Filtrar por área para evitar ruido
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el resultado en la ventana
    cv2.imshow('Detección de color', frame)

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar la captura y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()