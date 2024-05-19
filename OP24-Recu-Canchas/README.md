Programación Orientada a Objetos
Año 2024
Tema 2 – Recuperatorio Práctico Unidad 2
Resuelva la siguiente situación problemática, utilizando el lenguaje de programación Python.
El complejo de canchas de fútbol “Un partidito”, lo contrata para desarrollar un sistema que permita administrar el alquiler diario de las canchas de fútbol que dispone.
Para ello cuenta con los datos de:
Cada Cancha: identificador, tipo de piso, importe por hora.
Cada Alquiler: nombre de la persona que alquiló, identificador de la cancha alquilada, hora y minutos para la cual se alquiló (ejemplo: para las 15hs y 30 minutos), duración de alquiler en minutos (60, 90, 120).
Los datos de las canchas están en el archivo “Canchas.csv”, y tiene como separador el carácter “;”.
Los alquileres están en el archivo “Alquiler.csv”, que también tiene como separador el carácter “;”.
El equipo de desarrollo ha acordado que cada clase debe estar en un módulo, y usted debe implementar:

	1. Las clases Cancha y Alquiler, con los atributos y métodos necesarios.
	2. Una clase Gestor de canchas que almacene instancias de la clase Cancha. Cada una de estas instancias se creará con los datos registrados en el archivo “Cancha.csv”. Este gestor debe basarse en un arreglo Numpy teniendo en cuenta que el complejo tiene 6 canchas.
	3. Una clase Gestor de alquileres que almacene instancias de la clase Alquiler. Cada una de estas instancias se creará con los datos registrados en el archivo “Alquiler.csv”. Este gestor debe basarse en una lista Python.
	4. La carga de cada gestor con los datos correspondientes.
	5. Utilizando exclusivamente los Gestores cargados con los datos de los archivos, implemente un menú de opciones que permita:

			a. Emitir un listado ordenado por hora y minutos con todos los alquileres registrados y con el siguiente formato:
	Hora	Id de Cancha Duración alquiler	Importe por hora	Importe alquiler
	xx:xx	x			xx				xxxxxx.xx		xxxxxx.xx

	xx:xx	x			xxx				xxxxxx.xx		xxxxxx.xx
	xx:xx	x			xxx				xxxxxx.xx		xxxxxx.xx

	Total recaudado		xxxxxx.xx

Reglas:
- En esta funcionalidad debe definir la sobrecarga del operador __gt__ en la clase Alquiler
y usar la sobrecarga definida.
- La duración en minutos del alquiler se debe dividir en 60 para obtener la cantidad de
horas del alquiler.

		b. Ingresar el identificador de una cancha y mostrar la cantidad total de minutos que estuvo alquilada.
Reglas de negocio generales:
- Los archivos no presentan ningún orden en particular.
- Todas las funcionalidades deben resolverse con los Gestores definidos. Tiene prohibido sacar sublistas o subarreglos para procesar por fuera de los métodos definidos en los Gestores.
- El manejo del dato hora debe hacerse como un string.