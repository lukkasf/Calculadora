from funciones import *
from time import sleep

def continuar():
    input("Presione una tecla para continuar...")
def enter():
    print()

num_A = None
num_B = None
flag_num_B = False
flag_num_A = False
flag_operaion = False
salir = True

limpiar_terminal()
while salir:
        print("-------Menú de opciones---------")
        if num_A == None:
            print("1. Ingresar 1er operando (A=x)")
        else: 
            print(f"1. Ingresar 1er operando (A = {num_A})")
        if num_B == None:
            print("2. Ingresar 2do operando (B=y)")
        else: 
            print(f"2. Ingresar 2do operando (B = {num_B})")
        print("3. Eliga la operacion a realizar")
        print("4. Informar Resultado")
        print("5. Salir")
        enter()
        while True :
            aux = int(input("Elige una opción: "))
            if aux > 5:
                print("ERROR:Seleccione una opcion valida")
            else:
                opcion = aux
                break
            enter()

        match opcion:
            case 1:
                while True:
                    num_A = input("Ingresar 1er operando (A=x): ")
                    if not num_A.isdigit():
                        print("ERROR:Lo ingresado no es un NUMERO")
                        enter()
                    else:
                        num_A = int(num_A)
                        break
                continuar()
                enter()
                flag_num_A = True
                limpiar_terminal()
            case 2:
                while True:
                    num_B = input("Ingresar 2do operando (B=y): ")
                    if not num_B.isdigit():
                        print("ERROR:Lo ingresado no es un NUMERO")
                        enter()
                    else:
                        num_B = int(num_B)
                        break
                continuar()
                enter()
                flag_num_B = True
                limpiar_terminal()
            case 3:
                while True:
                    limpiar_terminal()
                    if not flag_num_A or not flag_num_B:
                        print("ERROR:Debe elegir Ambos valores con los cuales operar")
                        continuar()
                    else:
                        print("1. Calcular la suma (A+B)")
                        print("2. Calcular la resta (A-B)")
                        print("3. Calcular la división (A/B)")
                        print("4. Calcular la multiplicación (A*B)")
                        print("5. Calcular factorial (A!,B!)")
                        enter()
                        operacion = int(input("Eliga operacion: "))
                        if operacion > 5:
                            enter()
                            print("ERROR:Debe seleccionar una operacion valida")
                            continuar()
                            enter()
                        else:
                            continuar()
                            enter()
                            flag_operaion = True
                            limpiar_terminal()
                            break
                        
            case 4:
                while True:
                    if not flag_num_A or not flag_num_B:
                        print("ERROR:Debe elegir Ambos valores con los cuales operar")
                        continuar()
                        limpiar_terminal()
                    elif not flag_operaion == True:
                        print("ERROR:Debe seleccionar la operacion que desea realizar ")
                        continuar()
                        limpiar_terminal()
                    else:
                        match operacion:
                            case 1:
                                print(f"El resultado de Sumar {num_A} + {num_B} = {sumar(num_A,num_B)}")
                                continuar()
                                limpiar_terminal()
                        match operacion:
                            case 2:
                                print(f"El resultado de Restar {num_A} - {num_B} = {restar(num_A,num_B)}")
                                continuar()
                                limpiar_terminal()
                        match operacion:
                            case 3:
                                print(f"El resultado de Dividir {num_A} / {num_B} = {dividir(num_A,num_B)}")
                                continuar()
                                limpiar_terminal()
                        match operacion:
                            case 4:
                                print(f"El resultado de Multiplicar {num_A} * {num_B} = {multiplicar(num_A,num_B)}")
                                continuar()
                                limpiar_terminal()
                        match operacion:
                            case 5:
                                print(f"El resultado de factorisar {num_A}! y {num_B}! = {calc_factorial(num_A,num_B)}")
                                continuar()
                                limpiar_terminal()
                    break
            case 5:
                abandonar = True
                while abandonar:
                    salir= input("Desea abandonar? y/n: ")
                    if salir != "y" and salir != "n":
                        print("ERROR:No se a seleccionado ninguna opcion valida (y/n)")
                        enter()
                    elif salir == "n":
                        print("Gracias por quedarse <3")
                        continuar()
                        enter()
                        abandonar = False
                    else :
                        print("Cerrando")
                        sleep(1)
                        print(".")
                        sleep(1)
                        print(".")
                        sleep(1)
                        print(".")
                        sleep(1)
                        salir = False
                        break
                        
                        
                
                           
                    