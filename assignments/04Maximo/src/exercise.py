def main():
    # Escribe el código adecuado para completar el programa
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))

    if(num1+num2>num2+num3):
        if(num1>num2):
            print(num1)
        else:
            print(num2)
    else:
        if(num2>num3):
            print(num2)
        else:
            print(num3)

    pass

if __name__ == '__main__':
    main()
