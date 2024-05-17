**Programación Orientada a Objetos**
Año 2024	Tema 1 	– 	Recuperatorio Práctico Unidad 2
Resuelva la siguiente situación problemática, utilizando el lenguaje de programación Python.
El complejo de cabañas “El soleado”, lo contrata para desarrollar un sistema que permita
administrar las reservas de cabañas. Para ello cuenta con los datos de:
Cada Cabaña: número, cantidad de habitaciones, cantidad de camas grandes, cantidad de camas chicas e importe por día.
Cada Reserva: número de reserva, nombre de la persona que reservó, número de cabaña asignada,
fecha de inicio del hospedaje, cantidad de huéspedes, cantidad de días, importe de la seña.
Los datos de las cabañas están en el archivo “Cabañas.csv”. Las reservas recibidas vigentes están
registradas en el archivo “Reservas.csv”. Ambos archivos tienen como separador el carácter “;”.
El equipo de desarrollo ha acordado que cada clase debe estar en un módulo, y usted debe
implementar en Python:
1. Las clases Cabaña y Reserva, con los atributos y métodos necesarios.
2. Una clase Gestor de cabañas que almacene instancias de la clase Cabaña. Cada una de estas
instancias se creará con los datos registrados en el archivo “Cabañas.csv”. Este gestor debe
basarse en un arreglo Numpy teniendo en cuenta que el complejo tiene 10 cabañas.
3. Una clase Gestor de reservas que almacene instancias de la clase Reserva. Cada una de estas
instancias se creará con los datos registrados en el archivo “Reservas.csv”. Este gestor debe
basarse en una lista Python.
4. La carga de cada gestor con los datos respectivos.
5. Utilizando exclusivamente los Gestores cargados con los datos de los archivos, implemente
un menú de opciones que permita:
    a. Ingresar por teclado una cantidad de huéspedes y mostrar el o los números de las cabañas
que tienen una capacidad igual o mayor a la cantidad ingresada y no tienen ninguna reserva
registrada.
    Reglas:
           Para esta funcionalidad debe definir la sobrecarga del operador __ge__ en la clase
Cabaña y usar la sobrecarga definida.
           La capacidad de una cabaña se calcula como:
capacidad de una cabaña = cantidad de camas grandes * 2 + cantidad de camas chicas.
    
    b. Ingresar una fecha y emitir un listado con las reservas cuya fecha de inicio del hospedaje sea
igual a la ingresada. El listado debe tener el siguiente formato:
Reservas para la fecha: xx/xx/xx
N° de cabaña   Importe diario    Cantidad días    Seña       Importe a cobrar
xx             xxxxxx.xx         x                xxxxxx.xx  xxxxxx.xx
xx             xxxxxx.xx         x                xxxxxx.xx  xxxxxx.xx
xx             xxxxxx.xx         x                xxxxxx.xx  xxxxxx.xx
xx             xxxxxx.xx         x                xxxxxx.xx  xxxxxx.xx

Regla: El importe a cobrar se calcula:
Importe a cobrar = Cantidad de días * importe por día de la cabaña – importe de la seña
Reglas de negocio generales:
 Los archivos no presentan ningún orden en particular.
 Todas las funcionalidades deben resolverse con los Gestores definidos. Tiene prohibido sacar
sublistas o subarreglos para procesar por fuera de los métodos definidos en los Gestores.
 El manejo del dato fecha debe hacerse como un string.