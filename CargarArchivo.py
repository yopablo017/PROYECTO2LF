from tkinter import *
from tkinter import messagebox as MessageBox
noterminales=""
terminales=""
terminalinicial=""
contador=0
Terminales=[]
Noterminales=[]
Terminalinicial=[]
Titulos=[]
Produccion=[]
Cantidad1=[]
Cantidad2=[]
Cantidad3=[]
Validos=[]
NoValidos=[]
ContadorCantidad=0
Validar=False
def analizar(cadena):
	global contador
	global ContadorCantidad
	global Validar

	inicio=cadena[0]
	final=cadena[-1]
	if inicio=="G":
		ContadorCantidad += 1
		Nombre(cadena)

	paso2=";" in cadena
	if paso2==True:
		Automatas(cadena)

	paso3=">" in cadena
	if paso3==True:
		Producciones(cadena)

	paso4="*" in cadena
	if paso4==True:
		if Validar==True:
			Validos.append(ContadorCantidad)
		else:
			Eliminar()
			NoValidos.append(ContadorCantidad)	
		contador=0
		Validar=False

			
def Nombre(cadena):
	global ContadorCantidad
	Titulos.append(cadena)
	Cantidad1.append(ContadorCantidad)

def Automatas(cadena):
	global ContadorCantidad
	global terminales
	global noterminales
	global terminalinicial
	Alfabeto=cadena.split(";")
	noterminales=Alfabeto[0]
	terminales=Alfabeto[1]
	terminalinicial=Alfabeto[2]
	Terminales.append(terminales)
	Noterminales.append(noterminales)
	Terminalinicial.append(terminalinicial)
	Cantidad2.append(ContadorCantidad)


def Producciones(cadena):
	global ContadorCantidad
	global contador
	global terminales
	global noterminales
	global terminalinicial
	global Validar
	contadorterminales=0
	contadornoterminales=0
	paso1=True
	paso2=False
	Paso3=False
	for i in cadena:
		caracter=i
		if paso1==True:
			if caracter==">":
				paso2=True
				paso1=False
			else:
				pass
		elif paso2==True:
			ter=caracter in terminales
			noter=caracter in noterminales
			if ter==True:
				contadorterminales += 1
			elif noter==True:
				contadornoterminales += 1
	if contadorterminales==2 and contadornoterminales==1:
		Validar=True

	Cantidad3.append(ContadorCantidad)	
	contador += 1
	Produccion.append(str(contador)+": "+cadena)


def Eliminar():
	global ContadorCantidad
	ultimo=Titulos[-1]
	MessageBox.showwarning("Alerta","La gramatica "+ultimo+" es  Regular asi que no se agregara.")
	tamaño1=Cantidad1.count(ContadorCantidad)
	for i in range(0,tamaño1):
		Titulos.pop()
		Cantidad1.pop()


	tamaño2=Cantidad2.count(ContadorCantidad)
	for i in range(0,tamaño2):
		Noterminales.pop()
		Terminalinicial.pop()
		Terminales.pop()
		Cantidad2.pop()

	tamaño3=Cantidad3.count(ContadorCantidad)
	for i in range(0,tamaño3):
		Produccion.pop()
		Cantidad3.pop()