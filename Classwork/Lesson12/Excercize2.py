

def strogo_narascajoce(lista_stevil):
    retval = False
    for i in range(1, len(lista_stevil)):
        # print ""str(lista_stevil[i]) + " " + str(lista_stevil[i-1])
        if lista_stevil[i] > lista_stevil[i-1]:
            retval = True
        else:
            retval = False
    return retval

lista1 = [3,2,3,4,5,6]

print strogo_narascajoce(lista1)
