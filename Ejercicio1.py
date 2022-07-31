import pyttsx3
import csv
#iniciar y cambiar el idioma del modulo de audio
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
#funcion para inicializar el modulo de voz
def hablar(texto):
    print(texto)
    engine.say(texto)
    engine.runAndWait()

#intenta verificar si el archivo tiene la fila principal(primera fila) 
try:
    with open("data.csv", "r", newline="") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader: 
            cabecera = row[1] #al no haber primera fila o el primer dato se genera un error
            dato_uno = row[2] #porque no se le puede asignar nada a la variable
            print(row)
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        hablar('Escriba los datos de la persona')
        hablar("Separelo con comas y no deje espacios porfavor")
        datos = input()
        data = datos.split(',')
        writer.writerow(data)
#si no la primera fila la agrega y almacena el dato de una persona
except:
    hablar("Escriba la descripcion de los datos que desea agregar")
    hablar("Separelo con comas porfavor y no deje espacios")
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        descripcion = input()
        reader = descripcion.split(',')
        writer.writerow(reader)
        
        hablar('Escriba los datos de la persona')
        hablar("Separelo con comas y no deje espacios porfavor")
        datos = input()
        data = datos.split(',')
        writer.writerow(data)