class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def __eq__(self, other):
        return self.dni == other.dni

    def __contains__(self, dni):
        return dni == self.dni


# Crear una lista de personas
persona_list = [Persona("Juan", "12345678"), Persona("María", "87654321"), Persona("Pedro", "13579246")]

# Verificar si un DNI específico está en la lista de personas
dni_buscado = "87654321"
if dni_buscado in persona_list:
    print(f"Se encontró una persona con DNI {dni_buscado}.")
else:
    print(f"No se encontró ninguna persona con DNI {dni_buscado}.")
