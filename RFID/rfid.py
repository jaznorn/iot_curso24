import RPi.GPIO as GPIO 
from mfrc522 import SimpleMFRC522 
ledVerde =35 #GPIO 19 
ledRojo = 37 #GPIO 26
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(ledVerde,GPIO.OUT) 
GPIO.output(ledVerde, GPIO.LOW) 
GPIO.setup(ledRojo,GPIO.OUT) 
GPIO.output(ledRojo,GPIO.LOW) 
reader = SimpleMFRC522() 
while True: 
   try: 
       id, text = reader.read() 
       print(id) 
       if id==20608395188: 
           print("Estas autorizado") 
           GPIO.output(ledVerde,GPIO.HIGH)
           GPIO.output(ledRojo,GPIO.LOW) 
       else: 
           GPIO.output(ledRojo,GPIO.HIGH)
           GPIO.output(ledVerde, GPIO.LOW)
   except KeyboardInterrupt: #Que pasa cuando ctrl+c
          GPIO.cleanup()
          exit()
