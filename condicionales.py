''' En este script vamos a probar como funcionan los condicionales
y como funciona el bucle while.

Un condicional es un tipo de estructura que va a chequear cuantas
condiciones nosotros pongamos adentro, luego de probar la primera, si resulta
en falsa (False), seguira con las siguientes hasta tanto, una condicion se cumpla
como verdadera (True), en ese caso, ingresara al siguiente escalon de las condiciones
para seguir probando, o terminara el proceso.

Por ejemplo, en el siguiente ejemplo, vamos a chequear que la temperatura
del mate este en un determinada temperatura, para luego, en caso que el agua
este muy caliente, el codigo quedara encerrado en un bucle While hasta tanto
la temperatura baje a 80 grados, dentro de cada iteracion del bucle While, la
variable temperatura ira decreciendo en 1 grado hasta alcanzar la temperatura
de 80 grados.

En el otro segmento de la condicion else, se repite exactamente la misma estructura
pero en este caso, ingresara a esa condicion si la temperatura es mayor a 80 grados
entonces, en este caso, mismo que el anterior, el proceso quedara encerrado dentro
de otro bucle While, hasta tanto, luego de restarle 1 a la temperatura, esta alcance
la de objetivo que es de 80 grados.

Los grados de temperatura estaran guardados en un cajon o variable que contendra
ese dato, la variable se llamara temperatura y se le asignara el valor de 15 grados
digamos la temperatura ambiente del agua, luego de probar si la temperatura
esta a ese nivel, se incrementara de 5 en 5 hasta alcanzar la temperatura.

Como pueden ver, en este codigo importamos dos librerias, la libreria random, y la libreria
time.

La libreria random la usaremos para chequear de manera aleatoria, eligiendo un valor random
entre 15 y 100 grados, para ver en varias ejecuciones si funcionan las dos condiciones
tanto si la temperatura arranca por encima de 80 grados, como si la temperatura arranca
en un valor inferior.

La libreria time, la usamos en este caso, solo para establecer un tiempo en segundos que la
condicion se ejecutara, solo a titulo de ilustrar de manera mas amena como va incrementando
o decreciendo la temperatura.

temperatura = 15

Veamos como funciona
'''

import random
import time
temperatura = random.randint(15, 100)

if temperatura < 80:
    print("El agua esta muy fria para tomar mates! :( \n")

    while temperatura < 80:
        print("Calentando agua...\n")
        temperatura += 1
        print(temperatura)
        time.sleep(2)


elif temperatura > 80:
    print("El agua esta muy caliente para tomar mates! :( \n")

    while temperatura > 80:
        temperatura -= 1
        print("Enfriando agua...\n")
        print(temperatura)
        time.sleep(2)

print(f"El agua ya esta a {temperatura} grados, y esta al punto justo!\nTomando matecitos! :)")





