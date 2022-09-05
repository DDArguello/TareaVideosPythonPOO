from math import dist, factorial
from multiprocessing.sharedctypes import Value
from xmlrpc.client import boolean


class Ejercicios:
    def __init__(self, titulo):
        self.titulo=titulo
        print('🔶'*20,titulo,'🔶'*20)

    def video4(self): #Variables
        nombre="UskoKruM2010"
        print(nombre)
        edad=25
        print(edad)
        edad=True
        print(edad)

        sueldo=205.10
        print(sueldo)
    
    def video5(self): #Conversiones
        numero1="35"
        numero2="18"
        print(numero1+numero2)

        num1=int(numero1)
        num2=int(numero2)
        print(num1+num2)

        sueldo=1200.43
        sueldoEntero=int(sueldo)
        print(sueldoEntero)

        valor= "4500.89"
        valorDecimal = float(valor)
        print(valorDecimal + 3)

        edad=100
        print(len(str(edad)))

    def video6(self): #Numeros .opMatematicas 
        entero=23
        decimal=31.78
        complejo=12+5j
        booleano=True

        print(entero)
        print(decimal)
        print(complejo)
        print(booleano)

        num1=20
        num2=4
        print("suma: ", (num1+num2))
        print("resta: ", (num1-num2))
        print("multiplicacion: ", (num1*num2))
        print("division: ", (num1/num2))
        print("division exacta: ", (num1//num2))
        print("potencia: ", (num1**num2))


    def video7(self): #Concatenacion
        texto1="hola"
        texto2="mundo"
        textoFinal= texto1 + " " + texto2
        print(textoFinal)

        print("El saludo es: %s %s" % (texto1, texto2))

        saludoFinal= "saludo: {0} {1}".format(texto1,texto2)
        print(saludoFinal)
        saludoFinal2 = "saludo: {x} {y}".format(x=texto1,y=texto2)

    def video8(self): #Funiones cadenas
        texto ="bienveNIdos al canal de uskokru2010"
        print(texto)
        print(texto.lower())
        print(texto.upper())
        print(texto.title())
        print(texto.find("al"))
        print(texto.count("e"))
        textoFinal =texto.replace("a","3")
        print(textoFinal)
        valor=texto.isnumeric()
        print(valor)
        cadenasSeparadas=texto.split(" ")
        print(cadenasSeparadas)

    def video9(self): #Tuplas
        tupla=(1,2,3)
        print(tupla)
        tupla2=(7,"Oscar",True,450.1,16+7j)
        print(tupla2)
        tupla3=(9,3,(4,5,6))
        print(tupla3)
        print(tupla2[1])
        print(tupla2[-1])
        print(tupla2[0:4])
        print(tupla2[-2])
        a,b,c=tupla
        print(a)
        print(b)
        print(c)

        tuplaFinal=tupla+tupla3
        print(tuplaFinal)

        print(tuplaFinal.count(3))
        print(tuplaFinal.index(3))

    def video10(self): # Listas
        lista1=["Oscar",25,98.3,True,"Flavio",53.3]
        print(lista1)
        print(lista1[:])
        print(lista1[2])
        print(lista1[-1])

        print(lista1[0:3])
        print(lista1[:2])
        print(lista1[3:])

        lista1.append("UskoKruM2010")
        print(lista1)

        lista1.insert(4, "Peru")
        print(lista1)

        lista1.extend(["Alejandro",110,False])
        print(lista1)

        print(lista1.index("Flavio"))

        lista1.remove(98.3)
        print(lista1)

        lista1.pop()
        print(lista1)

        lista2=["Chiclayo","Irma"]
        lista3=lista1+lista2
        print(lista3)

        print(lista2*4)
        print("UskoKruM2010" in lista1)
        
    def video11(self): #Diccionarios
        miDiccionario={"España":"Madrid","Peru":"Lima","Alemania":"Berlin"}
        print(miDiccionario["Peru"])
        print(miDiccionario)

        miDiccionario["Venezuela"] = "Caracas"
        print(miDiccionario)

        miDiccionario["España"]= "Barcelona"
        print(miDiccionario)

        del miDiccionario["España"]
        print(miDiccionario)

        dic2={"Garcia":"Oscar",25:True, "Sueldo":150.00}
        print(dic2[25])

        llaves=("España","Francia","Inglaterra")
        dicPaises={llaves[0]:"Madrid",llaves[1]:"Paris",llaves[2]:"Londres"}
        print(dicPaises)

        datosPersonales={"Apellidos":"Garcia","Anios":(2010,2011,2012,2013,2014)}
        print(datosPersonales)
        print(datosPersonales["Anios"])

        print(datosPersonales.get("Apellidos","Oscar"))

        print(datosPersonales.keys())
        print(datosPersonales.values())
        valores=list(datosPersonales.values())
        print(valores)

    def video12(self): #Lectura de Datos
        nombre=input("Ingrese su nombre")
        edad=int(input("Ingrese su edad"))
        sueldo=float(input("Ingrese su sueldo"))

        print("Hola, " + nombre)
        edadFutura = edad+20
        print("Tu edad es: ", edad)
        print("Tu edad (dentro de 20 anios) sera: ", edadFutura)
        print("Tu sueldo es: ", sueldo)

    def video13(self): #IF - ELSE - ELIF
        edad=int(input("ingrese su edad: "))
        if edad>18:
            print("Eres mayor de edad.")
        elif edad == 18:
            print("Tienes 18 años!")
        else:
            print("No eres mayor de edad.")

    def video14(self): #Funciones
        class Funciones:
            def saludar():
                print("Garcia")
                print("Oscar")
                print("UskoKruM2010")
                return "hola"

            def evaluarSueldominimo(sueldo):
                if sueldo>=850:
                    print("Cumple con el sueldo")
                else:
                    print("Ganas menos que el sueldo minimo")
        
        print(Funciones.saludar())
        Funciones.evaluarSueldominimo(900)
    
    def video15(self): # Operadores Logicos
        distancia=1200
        numeroHermanos=3
        salarioPadres=1500

        tieneBeneficios=False

        if (distancia>100 and numeroHermanos>2) or salarioPadres<2000:
            tieneBeneficios=True
        
        print(not tieneBeneficios)

        if (5>3) or (8<15):
            print("Verdad")
        else:
            print("Es mentira...")
    
    def video16(self): #Operador Ternario
        sexos=("Hombre", "Mujer")

        posicion=True
        sexo=sexos[posicion]
        print(sexo)
        sexo=sexos[not posicion]
        print(sexo)

    def video17(self): #IF con Tuplas
        print("---Cursos---")
        print("Matematica - Biologia - Lenguaje - Ciencias")
        curso=input("Ingrese el curso deseado")

        if curso in ("Matematicas", "Biologia", "Lenguaje", "Ciencias"):
            print("Curso {0} seleccionado".format(curso))
        else:
            print("No existe ese Curso")

    def video18(self): #Funcion Range
        numeros=range(5)
        print(numeros[1])

        numeros1=range(4,10)
        print(numeros1[5])

        numeros2=range(10,100, 8)
        print(numeros2[9])

    def video19(self): #For
        for num in range(0,20,2):
            print("Valor actual: {0}".format(num))

        for i in range(1,13):
            print("{0} x {1} es: {2}".format(i,i,(i*i)))
        
        for num in ["Karen", "Oscar", "Hector", "Leonardo"]:
            print("Cantidad de letras de {0} es: {1}".format(num,len(num)))
    
    def video20(self): #Factorial
        numero=int(input("Ingrese un numero: "))
        factorial=1
        for n in range(1,(numero+1)):
            factorial=factorial*n
        print("El factorial de {0} es {1}".format(numero,factorial))

    def video21(self): #While
        indice=1
        while indice<10:
            print("valor actual: {0}".format(indice))
            indice+=1
        print("Hemos terminado el bucle while")

        inicio=2

        while inicio<=20:
            print("Numero par: {0}".format(inicio))
            inicio+=2
        print("Hemos terminado el bucle while")

    def video22(self): #Sentencias Break - Continue - Pass
        for numero in range(1,6):
            if numero==3:
                break
            print("El numero es: {0}".format(numero))

        print("Bucle Terminado")

        for numero in range(1,6):
            if numero==3:
                continue
            print("El numero es: {0}".format(numero))

        print("Bucle Terminado")

        for numero in range(1,6):
            if numero<=3:
                pass
            else:
                print("El siguiente valor es mayor a 3: ")
            print("El numero es: {0}".format(numero))

        print("Bucle Terminado")

    def video23(self): #Generadores - Yield
        def generarMultiplos7(limite):
            numero=1
            listaNumeros=[]
            while numero<=limite:
                listaNumeros.append(numero*7)
                numero+=1
            return listaNumeros
        
        print(generarMultiplos7(5))

        def generarMultiplos7(limite):
            numero=1
            while numero<=limite:
                yield numero*7
                numero+=1
        obtieneMultiplos7=generarMultiplos7(5)
        for n in obtieneMultiplos7:
            print(n)

    def video24(self): #Generadores - Yieldfrom
        # def devuelveLenguajes(self,*lenguajes):
        #     for leng in lenguajes:
        #         for letra in leng:
        #             yield letra
        def devuelveLenguajes(self,*lenguajes):
            for leng in lenguajes:
                yield from leng
        lenguajesObtenidos=devuelveLenguajes("python","java","php","Ruby","javascript")
        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))

    def video25(self): #Excepciones TRY EXCEPT
        numero1=20
        numero2=0
        #print("La divisioin es {0} entre {1} es: {2}".format(numero1,numero2,(numero1/numero2)))
        try:
            resultado=numero1/numero2
        except ZeroDivisionError:
            print("No se puede dividir entre 0...")
        finally:
            print("Yo siempre aparezco")

        print("Aqui termina mi programa")
    
    def video26(self): #Sentencia RISE
        def evaluarNota(nota):
            if nota<0:
                raise ValueError("Valor incorrecto...")
                #raise ZeroDivisionError("no se permiten valores negativos...")
            elif nota>=16:
                print("Excelente")
            elif nota>=11:
                print("Aprobado")
            else:
                print("Desaprobado")
        evaluarNota(16)
        print("Este es el fin de mi programa")
    
    def video27(self): #Modulos - importacion
        print("Este video era explicacion de modulos en python")

    def video28(self): #paquetes python
        print("En este video se explico sobre los paquetes de python __init__.py")

    def video29(self): #POO
        class Persona():
            apellidos=""
            nombres=""
            edad=0
            despierta=False
            def despertar(self):
                self.despierta=True
                print("Buen Dia")
        persona1=Persona()
        persona1.apellidos="Garcia Fuentes"
        print(persona1.apellidos)
        persona1.despertar()
        print(persona1.despierta)

    def video30(self): #Constructutres
        class Curso():
            #nombre="Matematica"
            #creditos=5
            #profesion="Ingenieria civil"

            def __init__(self,nom,cre,pro):
                self.nombre=nom
                self.creditos=cre
                self.profesion=pro
        curso1=Curso("Matematicas",5,"Ingenieria Civil")
        print(curso1.nombre)

    def video31(self): #Encapsulamiento de Variables
        class Curso():
            #nombre="Matematica"
            #creditos=5
            #profesion="Ingenieria civil"

            def __init__(self,nom,cre,pro):
                self.nombre=nom
                self.creditos=cre
                self.profesion=pro
                self.__imparticion="Precencial"
            
            def mostrarDatos(self):
                dat="Nombre: {0} / Creditos: {1} / imparticion: {2}"
                print(dat.format(self.nombre,self.creditos,self.__imparticion))

        curso1=Curso("Matematicas",5,"Ingenieria Civil")
        print(curso1.nombre)
        curso1.mostrarDatos()

    def video32(self): #Encapsulamiento de Metodos
        class Curso():
            #nombre="Matematica"
            #creditos=5
            #profesion="Ingenieria civil"

            def __init__(self,nom,cre,pro):
                self.nombre=nom
                self.creditos=cre
                self.profesion=pro
                self.__imparticion="Precencial"
            
            def mostrarDatos(self):
                dat="Nombre: {0} / Creditos: {1} / imparticion: {2}"
                print(dat.format(self.nombre,self.creditos,self.__imparticion))
                docenteAsignado=self.__verificarDocente()
                if docenteAsignado:
                    print("Existe docente asignado...")
                else:
                    print("No es necesario asignar un docente...")

            def __verificarDocente(self):
                print("Verificando si existe docente asignado...")
                if self.__imparticion=="Presencial":
                    return True
                else:
                    return False

        curso1=Curso("Matematicas",5,"Ingenieria Civil")
        print(curso1.nombre)
        curso1.mostrarDatos()
    
    def video33(self): #Metodos GET - SET
        class Cuenta():
            def __init__(self,pro,sal,mon):
                self.__propietario=pro
                self.__saldo=sal
                self.__moneda=mon

            #Metodo Get
            def get_Saldo(self):
                return self.__saldo
            def get_Propietario(self):
                return self.__propietario
            def get_Moneda(self):
                return self.__moneda

            #Metodo Set
            def set_Moneda(self,moneda):
                self.__moneda=moneda
        
        cuenta1=Cuenta("Oscar Garcia",1500,"Soles")
        print(cuenta1.get_Saldo())
        print(cuenta1.get_Moneda())
        cuenta1.set_Moneda("Dolares")
        print(cuenta1.get_Moneda())

    def video34(self): #Metodo de Clase __str__
        class Curso():
            #nombre="Matematica"
            #creditos=5
            #profesion="Ingenieria civil"

            def __init__(self,nom,cre,pro):
                self.nombre=nom
                self.creditos=cre
                self.profesion=pro
                self.__imparticion="Precencial"
            
            def mostrarDatos(self):
                dat="Nombre: {0} / Creditos: {1} / imparticion: {2}"
                print(dat.format(self.nombre,self.creditos,self.__imparticion))
                docenteAsignado=self.__verificarDocente()
                if docenteAsignado:
                    print("Existe docente asignado...")
                else:
                    print("No es necesario asignar un docente...")

            def __verificarDocente(self):
                print("Verificando si existe docente asignado...")
                if self.__imparticion=="Presencial":
                    return True
                else:
                    return False

            def __str__(self):
                texto="Nombre: {0} - Creditos: {1}"
                return texto.format(self.nombre, self.creditos)

        curso1=Curso("Matematicas",5,"Ingenieria Civil")
        print(curso1)
        curso1.mostrarDatos()
