nombres="""'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David', 'Diego', 'Dolores',
 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Facundo', 'FEDERICO', 'FEDERICO', 'GONZALO', 'Gregorio',
 'Ignacio', 'Jonathan', 'Jonathan', 'Jorge', 'JOSE', 'JUAN', 'Juan', 'Juan', 'Julian', 'Julieta', 'LAUTARO',
 'Leonel', 'LUIS', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'NICOLÁS', 'Noelia', 'Pablo', 'Priscila',
 'TOMAS', 'Tomás', 'Ulises', 'Yanina' """

eval1="""81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12, 77, 13, 86, 48, 65, 51, 41, 87,
 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74"""

eval2="""30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64, 13, 8, 87, 14, 14, 49, 27, 55,
 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10"""

def convertur_string(cadena):
    cadena2=cadena
    for i in set(cadena) :
        if not i.isalpha() and i != " " :
            cadena2=cadena2.replace(i," ")
    return cadena2.split()


"""nombres=nombres.replace("'"," ")
nombres=nombres.replace(","," ")
nombres=nombres.replace("\n"," ")
nombres_estudiantes=nombres.split()"""

eval1=eval1.replace(","," ")
eval1=eval1.replace("\n"," ")
eval1_lista=eval1.split()

eval2=eval2.replace(","," ")
eval2=eval2.replace("\n"," ")
eval2_lista=eval2.split()

nombres_estudiantes=convertur_string(nombres)


notas=zip(eval1_lista,eval2_lista)

suma_eval=[]

for i in notas :
    suma_eval.append(int(i[0])+int(i[1]))

alumnos_notas=zip(nombres_estudiantes,suma_eval)

def calcular_promedio(lista_alumnos) :
    suma_de_notas=0
    cant=0
    for i in lista_alumnos :
        suma_de_notas=suma_de_notas+i[1]
        cant=cant+1
    return suma_de_notas/cant

promedio=calcular_promedio(alumnos_notas)



for i in zip(nombres_estudiantes,suma_eval) :
    if i[1] < promedio :
        print(i[0])



