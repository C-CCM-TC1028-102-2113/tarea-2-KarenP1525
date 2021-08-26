def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))

    if(x<y and x<z):
       min=x
       if(y<z):
           med=y
           max=z
       else:
           med=z
           max=y
    elif(y<x and y<z):
       min=y 
       if(x<z):
           med=x
           max=z
       else:
           med=z
           max=x
    else:
        min=z
        if(x<y):
           med=x
           max=y
        else:
           med=y
           max=x

    print(min)
    print(med)
    print(max)

if __name__ == '__main__':
    main()
