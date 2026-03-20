class Material:
    def __init__(self,idcosa,nombre,anio,estado=True):
        self.id_material=idcosa
        self.titulo=nombre
        self.anio_publicacion=anio
        self.disponible=estado
    def mostrar_info(self):
        return f"Material: {self.titulo} | Año: {self.anio_publicacion} | Disponible: {self.disponible}"

class Libro(Material):
    def __init__(self,idcosa,nombre,anio,escritor,codigo,tipo,estado=True):
        super().__init__(idcosa,nombre,anio,estado)
        self.autor=escritor
        self.isbn=codigo
        self.genero=tipo
    def mostrar_info(self):
        return f"Libro: {self.titulo} | Autor: {self.autor} | Disponible: {self.disponible}"

class Revista(Material):
    def __init__(self,idcosa,nombre,anio,num,frecuencia,estado=True):
        super().__init__(idcosa,nombre,anio,estado)
        self.edicion=num
        self.periodicidad=frecuencia
    def mostrar_info(self):
        return f"Revista: {self.titulo} | Edicion: {self.edicion} | Cada: {self.periodicidad} | Disponible: {self.disponible}"

class MaterialDigital(Material):
    def __init__(self,idcosa,nombre,anio,archivo,link,peso,estado=True):
        super().__init__(idcosa,nombre,anio,estado)
        self.tipo_archivo=archivo
        self.url_descarga=link
        self.tamano_mb=peso
    def mostrar_info(self):
        return f"Digital: {self.titulo} | Tipo: {self.tipo_archivo} | Tamaño: {self.tamano_mb} MB | Link: {self.url_descarga} | Disponible: {self.disponible}"

class Persona:
    def __init__(self,nom):
        self.nombre=nom
    def mostrar_info(self):
        return f"Persona: {self.nombre}"

class Usuario(Persona):
    def __init__(self,nom,limite=3):
        super().__init__(nom)
        self.limite_prestamos=limite
        self.lista_activa=[]
        self.bloqueado=False
    def puede_prestar(self):
        return self.bloqueado==False and len(self.lista_activa)<self.limite_prestamos
    def mostrar_info(self):
        return f"Usuario: {self.nombre} | Limite: {self.limite_prestamos} | Activos: {len(self.lista_activa)} | Bloqueado: {self.bloqueado}"

class Bibliotecario(Persona):
    def __init__(self,nom):
        super().__init__(nom)
    def gestionar_prestamo(self,persona,objeto,folio,inicio,fin):
        if persona.puede_prestar() and objeto.disponible:
            prestamoNuevo=Prestamo(folio,inicio,fin,persona,objeto)
            persona.lista_activa.append(prestamoNuevo)
            objeto.disponible=False
            return f"Prestamo hecho a {persona.nombre} del material '{objeto.titulo}'"
        return "No se pudo hacer el prestamo"
    def transferir_material(self,objeto,salida,llegada):
        if objeto in salida.catalogo_local:
            salida.catalogo_local.remove(objeto)
            llegada.catalogo_local.append(objeto)
            return f"Material '{objeto.titulo}' movido de {salida.nombre} a {llegada.nombre}"
        return "No se encontro el material"
    def mostrar_info(self):
        return f"Bibliotecario: {self.nombre}"

class Sucursal:
    def __init__(self,clave,nom):
        self.id_sucursal=clave
        self.nombre=nom
        self.catalogo_local=[]
    def agregar_material(self,cosa):
        self.catalogo_local.append(cosa)
    def mostrar_catalogo(self):
        if not self.catalogo_local:
            return f"{self.nombre} no tiene materiales"
        texto=f"Catalogo de {self.nombre}:\n"
        for item in self.catalogo_local:
            texto+=f"- {item.mostrar_info()}\n"
        return texto

class Prestamo:
    def __init__(self,folio,inicio,fin,persona,objeto):
        self.id_prestamo=folio
        self.fecha_inicio=inicio
        self.fecha_devolucion=fin
        self.usuario=persona
        self.material=objeto
    def devolver_material(self):
        self.material.disponible=True
        if self in self.usuario.lista_activa:
            self.usuario.lista_activa.remove(self)
        return f"Material '{self.material.titulo}' devuelto"
    def mostrar_info(self):
        return f"Prestamo #{self.id_prestamo} | Usuario: {self.usuario.nombre} | Material: {self.material.titulo} | Inicio: {self.fecha_inicio} | Entrega: {self.fecha_devolucion}"

class Penalizacion:
    def __init__(self,dinero,razon,pagada=False):
        self.monto=dinero
        self.motivo=razon
        self.pagada=pagada
    def calcular_multa(self,dias):
        self.monto=dias*10
        return f"Multa: ${self.monto}"
    def bloquear_usuario(self,persona):
        persona.bloqueado=True
        return f"Usuario {persona.nombre} bloqueado"
    def mostrar_info(self):
        return f"Penalizacion | Monto: ${self.monto} | Motivo: {self.motivo} | Pagada: {self.pagada}"

class Catalogo:
    def __init__(self,sedes):
        self.sucursales=sedes
    def buscar_por_autor(self,nombre):
        lista=[]
        for sede in self.sucursales:
            for item in sede.catalogo_local:
                if isinstance(item,Libro) and item.autor.lower()==nombre.lower():
                    lista.append((sede.nombre,item.titulo))
        return lista
    def buscar_en_todas_sucursales(self,texto):
        lista=[]
        for sede in self.sucursales:
            for item in sede.catalogo_local:
                if texto.lower() in item.titulo.lower():
                    lista.append((sede.nombre,item.titulo))
        return lista
