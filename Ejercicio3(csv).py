
#Escribir un programa que que lea un archivo csv e imprima la información de forma
#agradable en la consola.
import pandas as pd

data=pd.read_csv("C:\\Users\\HP\\Downloads\\futbol.csv",header=0,delimiter=";")
print(data)
