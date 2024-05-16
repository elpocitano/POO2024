Tema 2 – Práctico Unidad 2
Programación Orientada a Objetos. Año 2024

Resuelva la siguiente situación problemática, utilizando el lenguaje de programación Python.
La farmacia “FarmaCiudad”, lo contrata a usted como programador para desarrollar un sistema para la
administración las cuentas corrientes que lleva para los Clientes.
Para ello cuenta con los datos de:
Los Clientes: 
nombre, apellido, dni, número de cuenta, saldo anterior.
Los Movimientos: 
número de cuenta, fecha, descripción, tipo de movimiento (‘C’ – Crédito, ‘P’-Pago), importe

Los datos de los Clientes, están almacenados en un archivo .csv, denominado
“ClientesFarmaCiudad.csv”. El archivo tiene como separador el carácter “;”.
Los datos de los movimientos, están almacenados en un archivo .csv, denominado
“MovimientosAbril2024.csv”. El archivo tiene como separador el carácter “;”. 
Cada vez que el Cliente compra un artículo en la Farmacia o hace un pago, se genera una línea con los datos del movimiento en
el archivo.
Por disposición del área de Sistemas, usted debe escribir el código de las clases, separadas en módulos.
1. Escriba el código de las clases Cliente y Movimiento, con los atributos y métodos necesarios.
2. Escriba el código de un Gestor de Clientes, que permita almacenar los datos de todos los
Clientes de la farmacia, para el mes de abril del 2024. Este gestor debe basarse en una lista del
lenguaje Python.
3. Escriba el código de un Gestor de Movimientos, que permita leer y almacenar los datos de
todos los Movimientos de las cuentas de los Clientes, para el mes de abril del 2024. Este gestor
debe basarse en un arreglo Numpy.
4. Leer los datos del archivo “ClientesFarmaCiudad.csv”, y almacenarlos en el Gestor de Clientes.
5. Leer los datos del archivo “MovimientosAbril2024.csv”, y almacenarlos en el Gestor de
Movimientos.
Utilizando exclusivamente los Gestores cargados con los datos de los archivos, escriba un menú de
opciones que permita:
a. Leer por teclado el dni de un Cliente, y actualice el saldo del cliente, sumando los créditos y
restando los pagos realizados, éstos últimos datos, obtenidos del Gestor de Movimientos,
emitiendo el siguiente listado:
   6. 
   Cliente: (apellido y nombre)   Número de Cuenta: xxxx-xxxx      Saldo anterior: xxxxxxxx.xx
   Movimientos
   Fecha        Descripción         Importe     Tipo de movimiento
   xx/xx/xx xx  xxxxxxxxxxxxxxxxx   xxxxxx.xx   x
   xx/xx/xx xx  xxxxxxxxxxxxxxxxx   xxxxxx.xx   x
   xx/xx/xx xx  xxxxxxxxxxxxxxxxx   xxxxxx.xx   x
   Saldo actualizado: xxxxxxxx.xx
5. 
   b. Leer por teclado un dni, e informar por pantalla apellido y nombre del Cliente, si este, no tuvo
   movimientos durante el mes de abril 2024.
   c. Ordenar el Gestor de Movimientos por número de cuienta, para facilitar el procesamiento del
   punto a.
   Reglas de negocio:
   Los archivos no presentan ningún orden en particular.
   Todas las funcionalidades deben resolverse con los Gestores definidos. Tiene prohibido sacar sublistas o
   subarreglos para procesar por fuera de los métodos definidos en los Gestores.
   Para ordenar el Gestor de Movimientos, debe sobrecargar el método “__lt__” en la clase que
   corresponda.
6. 