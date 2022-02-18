ocupacion=["ANALISTA","PROGRAMADOR","ASISTENTE","TECNICO","OPERADOR"]
sueldo=[2500,1500,1000,700,500]
descuento1=[0.12,0.10,0.08,0.06,0.04]
descuento2=[0.1,0.08,0.06,0.04,0.02]
bonificacion1=[0.14,0.12,0.1,0.08,0.06]
bonificacion2=[0.16,0.14,0.12,0.1,0.08]

def vocupacion(categoria):
    if categoria=="A":
        cat= ocupacion[0]
    elif categoria=="B":
        cat= ocupacion[1]
    elif categoria=="C":
        cat= ocupacion[2]
    elif categoria=="D":
        cat= ocupacion[3]
    else:
        cat= ocupacion[4]
    return cat

def vsueldo(categoria):
    if categoria=="A":
        sueld= sueldo[0]
    elif categoria=="B":
        sueld= sueldo[1]
    elif categoria=="C":
        sueld= sueldo[2]
    elif categoria=="D":
        sueld= sueldo[3]
    else:
        sueld= sueldo[4]
    return sueld

def vdescuento1(categoria):
    if categoria=="A":
        d1= vsueldo(categoria)*descuento1[0]
    elif categoria=="B":
        d1= vsueldo(categoria)*descuento1[1]
    elif categoria=="C":
        d1= vsueldo(categoria)*descuento1[2]
    elif categoria=="D":
        d1= vsueldo(categoria)*descuento1[3]
    else:
        d1= vsueldo(categoria)*descuento1[4]
    return str(round(d1,2))

def vdescuento2(categoria):
    if categoria=="A":
        d2= vsueldo(categoria)*descuento2[0]
    elif categoria=="B":
        d2= vsueldo(categoria)*descuento2[1]
    elif categoria=="C":
        d2= vsueldo(categoria)*descuento2[2]
    elif categoria=="D":
        d2= vsueldo(categoria)*descuento2[3]
    else:
        d2= vsueldo(categoria)*descuento2[4]
    return str(round(d2,2))

def vbonificacion1(categoria):
    if categoria=="A":
        b1= vsueldo(categoria)*bonificacion1[0]
    elif categoria=="B":
        b1= vsueldo(categoria)*bonificacion1[1]
    elif categoria=="C":
        b1= vsueldo(categoria)*bonificacion1[2]
    elif categoria=="D":
        b1= vsueldo(categoria)*bonificacion1[3]
    else:
        b1= vsueldo(categoria)*bonificacion1[4]
    return str(round(b1,2))

def vbonificacion2(categoria):
    if categoria=="A":
        b2= vsueldo(categoria)*bonificacion2[0]
    elif categoria=="B":
        b2= vsueldo(categoria)*bonificacion2[1]
    elif categoria=="C":
        b2= vsueldo(categoria)*bonificacion2[2]
    elif categoria=="D":
        b2= vsueldo(categoria)*bonificacion2[3]
    else:
        b2= vsueldo(categoria)*bonificacion2[4]
    return str(round(b2,2))

listado=[]
def IngresoDatos(CATEGORIA,NOMBRES_APELLIDOS,OCUPACION,SUELDO,DESCUENTO_1,DESCUENTO_2, BONIFICACION_1,BONIFICACION_2):
    listado.extend([CATEGORIA,NOMBRES_APELLIDOS,OCUPACION,SUELDO,DESCUENTO_1,DESCUENTO_2, BONIFICACION_1,BONIFICACION_2])


