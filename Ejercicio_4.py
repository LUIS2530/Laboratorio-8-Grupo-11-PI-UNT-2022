#Escribir un programa en el que el usuario pueda establecer una hora y minuto del
#día, y sea alertado mediante una notificación ó sonido 5 minutos antes.
import datetime as dt
import os
from time import time
from win10toast import ToastNotifier

date_new = dt.datetime(2022, 7, 30, int(input("Ingrese la hora: ")), int(input("ingrese el minuto: "))-5)
print("Se te notificará a las ", date_new.strftime("%X"))
date=dt.datetime.now()
while date<date_new:
    date=dt.datetime.now()

    if date.minute==date_new.minute:

        def notificacion():
                os.chdir(os.path.dirname(os.path.realpath(__file__)))
                toast= ToastNotifier()
                titulo ="Alerta de notificación"
                mensaje ="Hola!, en 5 minutos se cumplira la hora que has establecido"
                time = 5
                icon = None
                toast.show_toast(titulo, mensaje, icon_path=icon, duration=time, threaded=True)
        notificacion()
   
