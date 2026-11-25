def saludar(nombre_completo):
    """
    Muestra un saludo personalizado.
    Recibe el nombre completo de una persona.
    """
    if not nombre_completo or not nombre_completo.strip():
        return "Error: el nombre no puede estar vacío"

    return f"Hola {nombre_completo}"

print(saludar("GitHub"))