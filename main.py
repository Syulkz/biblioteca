import models

# ---------------------------
# CREACIÓN DE MATERIALES
# ---------------------------
libro1 = models.Libro(1, "Cien Años de Soledad", 1967, "Gabriel García Márquez", "1111", "Novela")
libro2 = models.Libro(2, "Don Quijote", 1605, "Miguel de Cervantes", "2222", "Clásico")
libro3 = models.Libro(3, "Python Básico", 2020, "Juan Pérez", "3333", "Tecnología")

revista1 = models.Revista(4, "National Geographic", 2024, 120, "Mensual")
revista2 = models.Revista(5, "Muy Interesante", 2023, 85, "Mensual")

digital1 = models.MaterialDigital(6, "Manual de IA", 2025, "PDF", "www.ejemplo.com/ia", 15.7)
digital2 = models.MaterialDigital(7, "Curso de Python", 2025, "EPUB", "www.ejemplo.com/python", 9.2)

# ---------------------------
# CREACIÓN DE USUARIOS
# ---------------------------
usuario1 = models.Usuario("Carlos López", 2)
usuario2 = models.Usuario("María Hernández", 3)

bibliotecario1 = models.Bibliotecario("Laura Sánchez")

# ---------------------------
# CREACIÓN DE SUCURSALES
# ---------------------------
sucursal1 = models.Sucursal(1, "Centro")
sucursal2 = models.Sucursal(2, "Norte")

# Agregar materiales
sucursal1.agregar_material(libro1)
sucursal1.agregar_material(revista1)
sucursal1.agregar_material(digital1)

sucursal2.agregar_material(libro2)
sucursal2.agregar_material(libro3)
sucursal2.agregar_material(revista2)
sucursal2.agregar_material(digital2)

# ---------------------------
# CATÁLOGO GLOBAL
# ---------------------------
catalogo = models.Catalogo([sucursal1, sucursal2])

# ---------------------------
# PRUEBAS
# ---------------------------
print("========== EVIDENCIA DE INSTANCIACIÓN ==========")
print(libro1.mostrar_info())
print(libro2.mostrar_info())
print(libro3.mostrar_info())
print(revista1.mostrar_info())
print(revista2.mostrar_info())
print(digital1.mostrar_info())
print(digital2.mostrar_info())
print(usuario1.mostrar_info())
print(usuario2.mostrar_info())
print(bibliotecario1.mostrar_info())

print("\n========== CATÁLOGOS ==========")
print(sucursal1.mostrar_catalogo())
print(sucursal2.mostrar_catalogo())

print("========== PRUEBA DE MÉTODOS INDIVIDUALES ==========")
print("Buscar por autor 'Juan Pérez':")
resultado_autor = catalogo.buscar_por_autor("Juan Pérez")
for sucursal, titulo in resultado_autor:
    print(f"- {titulo} en sucursal {sucursal}")

print("\nBuscar material con título 'Python':")
resultado_titulo = catalogo.buscar_en_todas_sucursales("Python")
for sucursal, titulo in resultado_titulo:
    print(f"- {titulo} en sucursal {sucursal}")

print("\n========== PRUEBA DE PRÉSTAMO ==========")
resultado_prestamo = bibliotecario1.gestionar_prestamo(
    usuario1,
    libro3,
    101,
    "2026-03-18",
    "2026-03-25"
)
print(resultado_prestamo)
print(usuario1.mostrar_info())
print(libro3.mostrar_info())

if usuario1.lista_activa:
    print(usuario1.lista_activa[0].mostrar_info())

print("\n========== PRUEBA DE DEVOLUCIÓN ==========")
if usuario1.lista_activa:
    print(usuario1.lista_activa[0].devolver_material())
print(usuario1.mostrar_info())
print(libro3.mostrar_info())

print("\n========== PRUEBA DE TRANSFERENCIA ==========")
print(bibliotecario1.transferir_material(revista1, sucursal1, sucursal2))
print(sucursal1.mostrar_catalogo())
print(sucursal2.mostrar_catalogo())

print("========== PRUEBA DE PENALIZACIÓN ==========")
penalizacion1 = models.Penalizacion(0, "Retraso en devolución")
print(penalizacion1.calcular_multa(5))
print(penalizacion1.bloquear_usuario(usuario2))
print(usuario2.mostrar_info())
print(penalizacion1.mostrar_info())