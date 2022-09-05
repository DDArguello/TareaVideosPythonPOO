from ejercicios4al34  import Ejercicios
from ejerciciosPOO35al40 import Poo
import os

x=True
while x:
    print("*"*51)
    print("*                                                 *")
    print("*  ¡Bienvenidos a la revision de los ejercicios!  *")
    print("*                                                 *")
    print("*"*51)

    opc=input("\nIngrese el número del ejercicio a realizar, entre [1-37]: ")
    if opc=='1':
        tarea=Ejercicios("Video 4")
        tarea.video4()
        c=1
    elif opc=='2':
        tarea=Ejercicios("Video 5")
        tarea.video5()
    elif opc=='3':
        tarea=Ejercicios("Video 6")
        tarea.video6()
    elif opc=='4':
        tarea=Ejercicios("Video 7")
        tarea.video7()
    elif opc=='5':
        tarea=Ejercicios("Video 8")
        tarea.video8()
    elif opc=='6':
        tarea=Ejercicios("Video 9")
        tarea.video9()
    elif opc=='7':
        tarea=Ejercicios("Video 10")
        tarea.video10()
    elif opc=='8':
        tarea=Ejercicios("Video 11")
        tarea.video11()
    elif opc=='9':
        tarea=Ejercicios("Video 12")
        tarea.video12()
    elif opc=='10':
        tarea=Ejercicios("Video 13")
        tarea.video13()
    elif opc=='11':
        tarea=Ejercicios("Video 14")
        tarea.video14()
    elif opc=='12':
        tarea=Ejercicios("Video 15")
        tarea.video15()
    elif opc=='13':
        tarea=Ejercicios("Video 16")
        tarea.video16()
    elif opc=='14':
        tarea=Ejercicios("Video 17")
        tarea.video17()
    elif opc=='15':
        tarea=Ejercicios("Video 18")
        tarea.video18()
    elif opc=='16':
        tarea=Ejercicios("Video 19")
        tarea.video19()
    elif opc=='17':
        tarea=Ejercicios("Video 20")
        tarea.video20()
    elif opc=='18':
        tarea=Ejercicios("Video 21")
        tarea.video21()
    elif opc=='19':
        tarea=Ejercicios("Video 22")
        tarea.video22()
    elif opc=='20':
        tarea=Ejercicios("Video 23")
        tarea.video23()
    elif opc=='21':
        tarea=Ejercicios("Video 24")
        tarea.video24()
    elif opc=='22':
        tarea=Ejercicios("Video 25")
        tarea.video25()
    elif opc=='23':
        tarea=Ejercicios("Video 26")
        tarea.video26()
    elif opc=='24':
        tarea=Ejercicios("Video 27")
        tarea.video27()
    elif opc=='25':
        tarea=Ejercicios("Video 28")
        tarea.video28()
    elif opc=='26':
        tarea=Ejercicios("Video 29")
        tarea.video29()
    elif opc=='27':
        tarea=Ejercicios("Video 30")
        tarea.video30()
    elif opc=='28':
        tarea=Ejercicios("Video 31")
        tarea.video31()
    elif opc=='29':
        tarea=Ejercicios("Video 32")
        tarea.video32()
    elif opc=='30':
        tarea=Ejercicios("Video 33")
        tarea.video33()
    elif opc=='31':
        tarea=Ejercicios("Video 34")
        tarea.video34()
    elif opc=='32':
        tarea=Poo("Video 35")
        tarea.video35()
    elif opc=='33':
        tarea=Poo("Video 36")
        tarea.video36()
    elif opc=='34':
        tarea=Poo("Video 37")
        tarea.video37()
    elif opc=='35':
        tarea=Poo("Video 38")
        tarea.video38()
    elif opc=='36':
        tarea=Poo("Video 39")
        tarea.video39()
    elif opc=='37':
        tarea=Poo("Video 40")
        tarea.video40()
    else:
        print("\nOpcion incorrecta! Vuelva a intentar: ")
    while True:
        opc=input("\nDesea acceder a otro ejercicio? [s/n]")
        if opc=='s':
            os.system("cls")
            break
        elif opc=='n':
            os.system("cls")
            print("\nGracias por revisar los ejercicios <3")
            x=False
            break
        else:
            os.system("cls")