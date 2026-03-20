class Material:
    def __init__(self, id_material, titulo, anio_publicacion, disponible=True):
        self.id_material = id_material
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible

    def mostrar_info(self):
        return f"Material: {self.titulo} ({self.anio_publicacion}) - Disponible: {self.disponible}"


class Libro(Material):
    def __init__(self, id_material, titulo, anio_publicacion, autor, isbn, genero, disponible=True):
        super().__init__(id_material, titulo, anio_publicacion, disponible)
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

    def mostrar_info(self):
        return (
            f"Libro: {self.titulo} | Autor: {self.autor} | ISBN: {self.isbn} | "
            f"Género: {self.genero} | Disponible: {self.disponible}"
        )


class Revista(Material):
    def __init__(self, id_material, titulo, anio_publicacion, edicion, periodicidad, disponible=True):
        super().__init__(id_material, titulo, anio_publicacion, disponible)
        self.edicion = edicion
        self.periodicidad = periodicidad

    def mostrar_info(self):
        return (
            f"Revista: {self.titulo} | Edición: {self.edicion} | "
            f"Periodicidad: {self.periodicidad} | Disponible: {self.disponible}"
        )


class MaterialDigital(Material):
    def __init__(self, id_material, titulo, anio_publicacion, tipo_archivo, url_descarga, tamano_mb, disponible=True):
        super().__init__(id_material, titulo, anio_publicacion, disponible)
        self.tipo_archivo = tipo_archivo
        self.url_descarga = url_descarga
        self.tamano_mb = tamano_mb

    def mostrar_info(self):
        return (
            f"Material Digital: {self.titulo} | Tipo: {self.tipo_archivo} | "
            f"Tamaño: {self.tamano_mb} MB | URL: {self.url_descarga} | Disponible: {self.disponible}"
        )


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return f"Persona: {self.nombre}"


class Usuario(Persona):
    def __init__(self, nombre, limite_prestamos=3):
        super().__init__(nombre)
        self.limite_prestamos = limite_prestamos
        self.lista_activa = []
        self.bloqueado = False

    def puede_prestar(self):
        return not self.bloqueado and len(self.lista_activa) < self.limite_prestamos

    def mostrar_info(self):
        return (
            f"Usuario: {self.nombre} | Límite: {self.limite_prestamos} | "
            f"Préstamos activos: {len(self.lista_activa)} | Bloqueado: {self.bloqueado}"
        )


class Bibliotecario(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def gestionar_prestamo(self, usuario, material, id_prestamo, fecha_inicio, fecha_devolucion):
        if usuario.puede_prestar() and material.disponible:
            prestamo = Prestamo(id_prestamo, fecha_inicio, fecha_devolucion, usuario, material)
            usuario.lista_activa.append(prestamo)
            material.disponible = False
            return f"Préstamo realizado correctamente a {usuario.nombre} del material '{material.titulo}'"
        return "No se pudo realizar el préstamo"

    def transferir_material(self, material, sucursal_origen, sucursal_destino):
        if material in sucursal_origen.catalogo_local:
            sucursal_origen.catalogo_local.remove(material)
            sucursal_destino.catalogo_local.append(material)
            return (
                f"Material '{material.titulo}' transferido de "
                f"{sucursal_origen.nombre} a {sucursal_destino.nombre}"
            )
        return "El material no se encontró en la sucursal de origen"

    def mostrar_info(self):
        return f"Bibliotecario: {self.nombre}"


class Sucursal:
    def __init__(self, id_sucursal, nombre):
        self.id_sucursal = id_sucursal
        self.nombre = nombre
        self.catalogo_local = []

    def agregar_material(self, material):
        self.catalogo_local.append(material)

    def mostrar_catalogo(self):
        if not self.catalogo_local:
            return f"La sucursal {self.nombre} no tiene materiales"
        texto = f"Catálogo de {self.nombre}:\n"
        for material in self.catalogo_local:
            texto += "- " + material.mostrar_info() + "\n"
        return texto


class Prestamo:
    def __init__(self, id_prestamo, fecha_inicio, fecha_devolucion, usuario, material):
        self.id_prestamo = id_prestamo
        self.fecha_inicio = fecha_inicio
        self.fecha_devolucion = fecha_devolucion
        self.usuario = usuario
        self.material = material

    def devolver_material(self):
        self.material.disponible = True
        if self in self.usuario.lista_activa:
            self.usuario.lista_activa.remove(self)
        return f"Material '{self.material.titulo}' devuelto correctamente"

    def mostrar_info(self):
        return (
            f"Préstamo #{self.id_prestamo} | Usuario: {self.usuario.nombre} | "
            f"Material: {self.material.titulo} | Inicio: {self.fecha_inicio} | "
            f"Devolución: {self.fecha_devolucion}"
        )


class Penalizacion:
    def __init__(self, monto, motivo, pagada=False):
        self.monto = monto
        self.motivo = motivo
        self.pagada = pagada

    def calcular_multa(self, dias_retraso):
        self.monto = dias_retraso * 10
        return f"Multa calculada: ${self.monto}"

    def bloquear_usuario(self, usuario):
        usuario.bloqueado = True
        return f"Usuario {usuario.nombre} bloqueado por penalización"

    def mostrar_info(self):
        return f"Penalización | Monto: ${self.monto} | Motivo: {self.motivo} | Pagada: {self.pagada}"


class Catalogo:
    def __init__(self, sucursales):
        self.sucursales = sucursales

    def buscar_por_autor(self, autor):
        resultados = []
        for sucursal in self.sucursales:
            for material in sucursal.catalogo_local:
                if isinstance(material, Libro) and material.autor.lower() == autor.lower():
                    resultados.append((sucursal.nombre, material.titulo))
        return resultados

    def buscar_en_todas_sucursales(self, titulo):
        resultados = []
        for sucursal in self.sucursales:
            for material in sucursal.catalogo_local:
                if titulo.lower() in material.titulo.lower():
                    resultados.append((sucursal.nombre, material.titulo))
        return resultados




