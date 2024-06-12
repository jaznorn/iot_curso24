<a id="presentacion"># iot_curso24
Repositorio del curso [IoT Essencials Developer](https://edu.codigoiot.com/my/courses.php "Ir al curso").

Aqui se guardaran los ejercicios del curso IoT Essentials Developer
| Modulo | Ejercicio | Fecha |
|:------------:|-------------:| -------------:|
| Utilizacion de rasp Pi | Prender LED | 18/Mayo |
| Acceso Vehicular | RFID | 21/Mayo |
</a>

## Contenidos
1. [Introduccion](#presentacion)
2. [Ejercicios incluidos](#ejercicios-incluidos)
3. [To do](#to-do)
4. [Advertencia de uso](#advertencia-de-uso)

<a id="incluidos"> </a>
## Ejercicios incluidos
1. Parpadear LED
    - Circuito sugerido
    - Codigo para prender LED desde python
    ``` python
    # No olvides el import 
    import RPi.GPIO as GPIO
    GPIO=1
    GPIO.setmode(BOARD)
    ```
2. Lectura de tarjeta RFID
    - Requiere crear un ambiente de trabajo con
    ``` python
    python -m venv <nombre_de_ambiente>
    source <nombre_de_ambiente>/bin/activate
    ```
    - Requiere las bibliotecas spidev y mfrc522
    ``` python
    python -m pip install spidev
    python -m pip install mfrc522
    ```

    - Consulta [rfid.py](./RFID/rfid.py) para mas informacion
    - Documents [git](../git)

<a id="pendientes"></a>
## To Do

- [ ] Iniciar documentacion

- [x] Incorporar codigo al LED

- [ ] Hacer notas sobre Git

<a id="Advertencia de uso"> </a>
## Advertencia de uso
__Este codigo es experimental y con fines educativos.__
___Uselos bajo su propio riesgo___