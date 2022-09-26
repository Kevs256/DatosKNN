import pandas as pd
import random
import matplotlib.pyplot as plot

#leemos el csv
file = "wine.csv"
datacsv = pd.read_csv(file, sep=',', decimal=".")

columnas =[
    'categoria',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13'
]

datacsv.columns = columnas

# en el csv las categorias estan disparejas, entonces debemos
#balancearlas en cantidad:

# la categoria con la menor cantidad de datos es la numero 3
# 48 filas

#declaramos el dataframe que contedra los 48 filas de categoria 3

data3 = pd.DataFrame(columns=[
    'categoria',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13'
])
contador3 = 0
for i in range(len(datacsv)):
    if datacsv['categoria'][i] == 3 and contador3 < 40:
        data3.loc[i] = list(datacsv.iloc[i])
        contador3=contador3+1
#declaramos el dataframe que contedra los 48 filas de categoria 2

#esta linea corresponde a resetear los indices para qe no conserve los iniciales
data3.reset_index(drop=True, inplace=True)

data2 = pd.DataFrame(columns=[
    'categoria',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13'
])
contador = 0
for i in range(len(datacsv)):
    if datacsv['categoria'][i] == 2 and contador < 40:
        data2.loc[i] = list(datacsv.iloc[i])
        contador=contador+1

#esta linea corresponde a resetear los indices para qe no conserve los iniciales
data2.reset_index(drop=True, inplace=True)

#declaramos el dataframe que contedra los 48 filas de categoria 1

data1 = pd.DataFrame(columns=[
    'categoria',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13'
])
contador2 = 0
for i in range(len(datacsv)):
    if datacsv['categoria'][i] == 1 and contador2 < 40:
        data1.loc[i] = list(datacsv.iloc[i])
        contador2=contador2+1

#esta linea corresponde a resetear los indices para qe no conserve los iniciales
data1.reset_index(drop=True, inplace=True)

#terminamos de crear los 3 dataframes, uno por cada categoria

#generamos una lista de los indices que ya se han usado
#generamos una lista de los datos de prueba actuales
listausados=[]

def listaprueba():
    listagenerados=[]
    while(len(listagenerados)<12):
        numeroramdom = random.randint(0, 119)
        if numeroramdom in listausados:
            hola=0
        else:
            listausados.append(numeroramdom)
            listagenerados.append(numeroramdom)
    return listagenerados

#creamos un dataframe que sean los 3 dataframes unidos nuevamente, con el fin
#practico de extraer de ahi los puntos de prueba, que en realidad no hay problema
#en escogerlos aleatorios porque son los de prueba

dataframetotal=pd.concat([data1, data2, data3], axis=0)
#esta linea corresponde a resetear los indices para qe no conserve los iniciales
dataframetotal.reset_index(drop=True, inplace=True)

#generamos las comparaciones entre las coordenadas de cada una de los puntos 
#generamos la lista de prueba

def clasificacion(dataframetotal,dataframe1,dataframe2,dataframe3):
    #esta funcion genera los 12 puntos a probar, en cada prueba son aleatorios
    #y diferentes a los anteriores
    listaPR = listaprueba()

    #aca guardamos la categoria original del punto
    #y la categoria obtenida por el modelo
    categoriaPunto=0
    categoriaResultado=0

    #aca vamos acumulando los fp,fn y tp
    PrecisionGeneral=0

    Tp1 = 0
    Tp1N=0
    Tp2 = 0
    Tp2N=0
    Tp3 = 0
    Tp3N=0

    Fp1 = 0
    Fp1N = 0
    Fp2 = 0
    Fp2N = 0
    Fp3 = 0
    Fp3N = 0

    Fn1 = 0
    Fn2 = 0
    Fn3 = 0

    #este for recorre cada uno de los puntos
    for i in range(12):
        resultado1=0
        resultado2=0
        resultado3=0

        #establecemos un k = 40, correpondiente a acompararse con 40 puntos, 
        for j in range(40):
            resultado1=((dataframetotal['2'][listaPR[i]]-dataframe1['2'][j])**2 + (dataframetotal['9'][listaPR[i]]-dataframe1['9'][j])**2 + (dataframetotal['4'][listaPR[i]]-dataframe1['4'][j])**2 + (dataframetotal['10'][listaPR[i]]-dataframe1['10'][j])**2 + (dataframetotal['11'][listaPR[i]]-dataframe1['11'][j])**2 + (dataframetotal['12'][listaPR[i]]-dataframe1['12'][j])**2)**0.5
            resultado2=((dataframetotal['2'][listaPR[i]]-dataframe2['2'][j])**2 + (dataframetotal['9'][listaPR[i]]-dataframe2['9'][j])**2 + (dataframetotal['4'][listaPR[i]]-dataframe2['4'][j])**2 + (dataframetotal['10'][listaPR[i]]-dataframe2['10'][j])**2 + (dataframetotal['11'][listaPR[i]]-dataframe2['11'][j])**2 + (dataframetotal['12'][listaPR[i]]-dataframe2['12'][j])**2)**0.5
            resultado3=((dataframetotal['2'][listaPR[i]]-dataframe3['2'][j])**2 + (dataframetotal['9'][listaPR[i]]-dataframe3['9'][j])**2 + (dataframetotal['4'][listaPR[i]]-dataframe3['4'][j])**2 + (dataframetotal['10'][listaPR[i]]-dataframe3['10'][j])**2 + (dataframetotal['11'][listaPR[i]]-dataframe3['11'][j])**2 + (dataframetotal['12'][listaPR[i]]-dataframe3['12'][j])**2)**0.5
            #acumulamos las distacias para sumarlas
            resultado1 = resultado1 + resultado1
            resultado2 = resultado2 + resultado2
            resultado3 = resultado3 + resultado3
        
        #clasificamos el punto en su categoria ORIGINAL de acuerdo a la posicion
        #porque sabemos que fueron añadidos en orden, primeros 40 categoria uno
        if listaPR[i] < 40:
            categoriaPunto = 1
        if listaPR[i] < 80 and listaPR[i] >= 40:
            categoriaPunto = 2
        if listaPR[i] < 120 and listaPR[i] >= 80:
            categoriaPunto = 3

        #clasificamos el resultado (de la diferencia entre distancias) por categoria
        #categoria que fue predecida
        if resultado1*100 < resultado2*100 and resultado1*100 < resultado3*100:
            categoriaResultado = 1
        if resultado2*100 < resultado1*100 and resultado2*100 < resultado3*100:
            categoriaResultado = 2
        if resultado3*100 < resultado1*100 and resultado3*100 < resultado2*100:
            categoriaResultado = 3
        
        #aca cada categoria tiene un tp, fp y fn (no se pueden acumular, es uno por categoria)
        #acumulamos los tp
        #acumulamos tambien la precision general que si se puede sumar, definida como 
        #sumatoria de los tp sobre la cantidad de muestras, en este caso 12
        if categoriaPunto == 1 and categoriaResultado == 1:
            Tp1=Tp1+1
            PrecisionGeneral = PrecisionGeneral + 1
        if categoriaPunto == 2 and categoriaResultado == 2:
            Tp2=Tp2+1
            PrecisionGeneral = PrecisionGeneral + 1
        if categoriaPunto == 3 and categoriaResultado == 3:
            Tp3=Tp3+1
            PrecisionGeneral = PrecisionGeneral + 1
        
        #acumulamos los fp
        if categoriaResultado != categoriaPunto and categoriaResultado == 1:
            Fp1 = Fp1+1
        if categoriaResultado != categoriaPunto and categoriaResultado == 2:
            Fp2 = Fp2+1
        if categoriaResultado != categoriaPunto and categoriaResultado == 3:
            Fp3 = Fp3+1

        #acumulamos los fn
        if categoriaResultado != categoriaPunto and categoriaPunto == 1:
            Fn1 = Fn1 + 1
        if categoriaResultado != categoriaPunto and categoriaPunto == 2:
            Fn2 = Fn2 + 1
        if categoriaResultado != categoriaPunto and categoriaPunto == 3:
            Fn3 = Fn3 + 1

        #presentamos las categorias obtenidas
        print("resultados")
        print(categoriaPunto, 'esta es la categoria original')
        print(categoriaResultado, 'esta es la categoria resultado')

    #presetnamos los true positive, false positive y false negative
    print("tp y esa weas")
    print(Tp1, "tp 1")
    print(Fp1, "fp 1")
    print(Fn1, "fn 1")

    print(Tp2, "tp 2")
    print(Fp2, "fp 2")
    print(Fn2, "fn 2")

    print(Tp3, "tp 3")
    print(Fp3, "fp 3")
    print(Fn3, "fn 3")

    #presicion general de la prueba
    print("precision general") 
    print(PrecisionGeneral/12)

    #sensiblidad por cada categoria
    #tiene problemas al dividir por cero
    #en el caso que tp y fn/ tp y fp sumen cero
    
    #en caso de dar ceros, no se genera el calculo y se descarta esa estadistica en la prueba
    #pero se suman cuantos se han incluido correctamente

    if Tp1+Fn1 != 0:
        sensibilidadPruebaCAT1=Tp1/(Tp1+Fn1)
        Tp1N=Tp1N + 1
    else:
        print("dividio en cero ptm")
        sensibilidadPruebaCAT1= "esta ronda no hubo"

    if Tp2+Fn2 != 0:
        sensibilidadPruebaCAT2=Tp2/(Tp2+Fn2)
        Tp2N=Tp2N + 1
    else:
        print("dividio en cero ptm")
        sensibilidadPruebaCAT2= "esta ronda no hubo"
    
    if Tp3+Fn3 != 0:
        sensibilidadPruebaCAT3=Tp3/(Tp3+Fn3)
        Tp3N=Tp3N + 1
    else:
        print("dividio en cero ptm")
        sensibilidadPruebaCAT3= "esta ronda no hubo"
    
    #en caso de dar ceros, no se genera el calculo y se descarta esa estadistica en la prueba
    #pero se suman cuantos se han incluido correctamente

    if Tp1+Fp1 != 0:
        precisionPruebaCAT1=Tp1/(Tp1+Fp1)
        Fp1N=Fp1N + 1
    else:
        print("dividio en cero ptm")
        precisionPruebaCAT1="esta ronda no hubo"
    
    if Tp2+Fp2 != 0:
        precisionPruebaCAT2=Tp2/(Tp2+Fp2)
        Fp2N=Fp2N + 1
    else:
        print("dividio en cero ptm")
        precisionPruebaCAT2="esta ronda no hubo"

    if Tp3+Fp3 != 0:
        precisionPruebaCAT3=Tp3/(Tp3+Fp3)
        Fp3N=Fp3N + 1
    else:
        print("dividio en cero ptm")
        precisionPruebaCAT3="esta ronda no hubo"


    print("sensibilidades")
    print(sensibilidadPruebaCAT1, "cat 1")
    print(sensibilidadPruebaCAT2, "cat 2")
    print(sensibilidadPruebaCAT3, "cat 3")
    print("Precisiones")
    print(precisionPruebaCAT1, "cat 1")
    print(precisionPruebaCAT2, "cat 2")
    print(precisionPruebaCAT3, "cat 3")

    return PrecisionGeneral/12


precisiontotal = 0
for i in range(10):
    precision = clasificacion(dataframetotal,data1,data2,data3)
    print("revisa aqui")
    print(precision)
    precisiontotal = precisiontotal + precision

print("he aqui la invariable precision acumulada")
print(precisiontotal/10)


#generaremos un scatter entre cada una de las variables
#para ahcer un inspeccion visual de las relaciones entre ellas
#y escoger las menos relacionadas

# fig = plot.figure()
# plot.scatter(data1['12'], data3['12'])
# plot.show()

#concluimos en la inspeccion visual que se debe usar la columna C y J
#para aumentar la presicion incluimos la columna 10 y 4
