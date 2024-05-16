Tema 1 – Práctico Unidad 2
Programación Orientada a Objetos
Año 2024
Resuelva la siguiente situación problemática, utilizando el lenguaje de programación Python.
La empresa “Tarjeta la Sanjuanina”, lo contrata a usted como programador para desarrollar un sistema
para la administración de las tarjetas de crédito que entrega a sus clientes y movimientos que éstos
hacen con las tarjetas.
Para ello cuenta con los datos de:
Los Clientes: 
nombre, apellido, dni, número de tarjeta, saldo anterior.
Los Movimientos: 
número de tarjeta, fecha, descripción, tipo de movimiento (‘C’ – Crédito, ‘P’-Pago), importe
Los datos de los Clientes, están almacenados en un archivo .csv, denominado “ClientesAbril2024.csv”. 
El archivo tiene como separador el carácter “;”.
Los datos de los movimientos, están almacenados en un archivo .csv, denominado
“MovimientosAbril2024.csv”. El archivo tiene como separador el carácter “;”.

Por disposición del área de Sistemas, usted debe escribir el código de las clases, separadas en módulos.
1. Escriba el código de las clases Cliente y Movimiento, con los atributos y métodos necesarios.
2. Escriba el código de un Gestor de Clientes, que permita almacenar los datos de todos los
Clientes de la tarjeta, para el mes de abril del 2024. Este gestor debe basarse en una lista del
lenguaje Python.
3. Escriba el código de un Gestor de Movimientos, que permita leer y almacenar los datos de
todos los Movimientos de las tarjetas de los Clientes, para el mes de abril del 2024. Este gestor
debe basarse en un arreglo Numpy.
4. Leer los datos del archivo “ClientesAbril2024.csv”, y almacenarlos en el Gestor de Clientes.
5. Leer los datos del archivo “MovimientosAbril2024.csv”, y almacenarlos en el Gestor de
Movimientos.
Utilizando exclusivamente los Gestores cargados con los datos de los archivos, escriba un menú de
opciones que permita:
a. Leer por teclado el dni de un Cliente, y actualice el saldo del cliente, sumando los créditos y
restando el pago realizado, éstos últimos datos, obtenidos del Gestor de Movimientos,
emitiendo el siguiente listado:
Cliente: (apellido y nombre)
Número de tarjeta: xxxx-xxxx
Saldo anterior: xxxxxxxx.xx
Movimientos
Fecha        Descripción        Importe            Tipo de movimiento
xx/xx/xx     xxxxxxxxxxxxxxx    xxxxxx.xx          x
xx/xx/xx     xxxxxxxxxxxxxxx    xxxxxx.xx          x
xx/xx/xx xxxxxxxxxxxxxxxxxxx    xxxxxx.xx          x
Saldo actualizado: xxxxxxxx.xx
b. Leer por teclado un número de tarjeta, e informar por pantalla apellido y nombre del Cliente, si
este, no tuvo movimientos durante el mes de abril 2024.
c. Ordenar el Gestor de Movimientos por número de tarjeta, para facilitar el procesamiento del
punto a.
Reglas de negocio:
Los archivos no presentan ningún orden en particular.
Todas las funcionalidades deben resolverse con los Gestores definidos. Tiene prohibido sacar sublistas o
subarreglos para procesar por fuera de los métodos definidos en los Gestores.
Para ordenar el Gestor de Movimientos, debe sobrecargar el método “__lt__” en la clase que
corresponda.