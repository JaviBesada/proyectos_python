def multiTable(n): 
    i = 1
    
    tabla = ""

    while i < 11:
        if i==10:
            tabla += str(i) + " * " + str(n) + " = " + str(i * n)
        else:
            tabla += str(i) + " * " + str(n) + " = " + str(i * n) + "\n"
        i += 1
    return tabla
  

print(multiTable(5))
