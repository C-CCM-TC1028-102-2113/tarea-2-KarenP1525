def main():
    import math
    # Escribe el código adecuado para completar el programa
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    


    if(peso>0 and altura>0):
        indice=peso/math.pow(altura,2)
        if(indice<20):
            print("PESO BAJO")
        elif(20<=indice<25):
            print("NORMAL")
        elif(25<=indice<30):
            print("SOBREPESO")
        elif(30<=indice<40):
            print("OBESIDAD")
        else:
             print("OBESIDAD MORBIDA")
    else:
        print("mensaje de error: Revisa tus datos, alguno de ellos es erróneo.")
    pass

if __name__ == '__main__':
    main()
