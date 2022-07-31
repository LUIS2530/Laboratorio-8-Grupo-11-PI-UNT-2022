import speech_recognition as sr
import pyttsx3
import wikipedia

#iniciar y cambiar el idioma del modulo de audio
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
#===========FUNCIONES PARA EL PROGRAMA==============
#funcion para inicializar el modulo de voz
def hablar(texto):
    print(texto)
    engine.say(texto)
    engine.runAndWait()

#funcion para buscar informacion en wikipedia
def buscador(pregunta):
    wikipedia.set_lang("es")
    respuesta = wikipedia.summary(pregunta, sentences=3)
    print(respuesta)
    hablar(respuesta)

#funcion para el microfono
def microfono():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        mensaje = recognizer.recognize_google(audio, language='es')
        print(mensaje)
        return mensaje   
    except:
        hablar("Lo siento, no entendi lo que dijiste")
#==========INICIO DEL PROGRAMA=========
hablar("Desea que busque informacion en internet")
voz = microfono()
if "sí" in voz.lower():
    hablar("Que busco en wikipedia")
    mensaje = microfono()
    buscador(mensaje)
elif "no" in voz.lower():
    hablar("Hasta luego")