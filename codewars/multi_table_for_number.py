def multiTable(multiplicando): 
    UNO = 1
    DIEZ = 10
    
    tabla_de_multiplicar = ""

    for multiplicador in range(UNO, DIEZ + UNO):
            tabla_de_multiplicar += f"{multiplicador} * {multiplicando} = {multiplicador * multiplicando}\n"
    
    return tabla_de_multiplicar [:-1]
    

print(multiTable(5))
