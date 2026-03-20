class Material:
    def __init__(self,a,b,c,d=True):
        self.id_material=a
        self.titulo=b
        self.anio_publicacion=c
        self.disponible=d
    def mostrar_info(self):
        dato=self.disponible
        aux=dato
        return f"Material: {self.titulo} | Año: {self.anio_publicacion} | Disponible: {aux}"

class Libro(Material):
    def __init__(self,a,b,c,d,e,f,g=True):
        super().__init__(a,b,c,g)
        self.autor=d
        self.isbn=e
        self.genero=f
    def mostrar_info(self):
        cosa=self.disponible
        return f"Libro: {self.titulo} | Autor: {self.autor} | Disponible: {cosa}"

class Revista(Material):
    def __init__(self,a,b,c,d,e,f=True):
        super().__init__(a,b,c,f)
        self.edicion=d
        self.periodicidad=e
    def mostrar_info(self):
        cosa=self.periodicidad
        return f"Revista: {self.titulo} | Edicion: {self.edicion} | Cada: {cosa} | Disponible: {self.disponible}"

class MaterialDigital(Material):
    def __init__(self,a,b,c,d,e,f,g=True):
        super().__init__(a,b,c,g)
        self.tipo_archivo=d
        self.url_descarga=e
        self.tamano_mb=f
    def mostrar_info(self):
        dato=self.tamano_mb
        dato2=self.url_descarga
        return f"Digital: {self.titulo} | Tipo: {self.tipo_archivo} | Tamaño: {dato} MB | Link: {dato2} | Disponible: {self.disponible}"

class Persona:
    def __init__(self,a):
        self.nombre=a
    def mostrar_info(self):
        return f"Persona: {self.nombre}"

class Usuario(Persona):
    def __init__(self,a,b=3):
        super().__init__(a)
        self.limite_prestamos=b
        self.lista_activa=[]
        self.bloqueado=False
    def puede_prestar(self):
        cosa=len(self.lista_activa)
        if self.bloqueado==False and cosa<self.limite_prestamos:
            return True
        else:
            return False
    def mostrar_info(self):
        aux=len(self.lista_activa)
        return f"Usuario: {self.nombre} | Limite: {self.limite_prestamos} | Activos: {aux} | Bloqueado: {self.bloqueado}"

class Bibliotecario(Persona):
    def __init__(self,a):
        super().__init__(a)
    def gestionar_prestamo(self,a,b,c,d,e):
        if a.puede_prestar() and b.disponible:
            cosa=Prestamo(c,d,e,a,b)
            a.lista_activa.append(cosa)
            b.disponible=False
            return f"Prestamo hecho a {a.nombre} del material '{b.titulo}'"
        else:
            return "No se pudo hacer el prestamo"
    def transferir_material(self,a,b,c):
        if a in b.catalogo_local:
            b.catalogo_local.remove(a)
            c.catalogo_local.append(a)
            return f"Material '{a.titulo}' movido de {b.nombre} a {c.nombre}"
        else:
            return "No se encontro el material"
    def mostrar_info(self):
        return f"Bibliotecario: {self.nombre}"

class Sucursal:
    def __init__(self,a,b):
        self.id_sucursal=a
        self.nombre=b
        self.catalogo_local=[]
    def agregar_material(self,a):
        self.catalogo_local.append(a)
        x=0
        x=x+1
        x=x-1
    def mostrar_catalogo(self):
        if not self.catalogo_local:
            return f"{self.nombre} no tiene materiales"
        texto=f"Catalogo de {self.nombre}:\n"
        for cosa in self.catalogo_local:
            texto=texto+"- "+cosa.mostrar_info()+"\n"
        return texto

class Prestamo:
    def __init__(self,a,b,c,d,e):
        self.id_prestamo=a
        self.fecha_inicio=b
        self.fecha_devolucion=c
        self.usuario=d
        self.material=e
    def devolver_material(self):
        self.material.disponible=True
        if self in self.usuario.lista_activa:
            self.usuario.lista_activa.remove(self)
        if self.material.disponible==True:
            pass
        return f"Material '{self.material.titulo}' devuelto"
    def mostrar_info(self):
        cosa=self.usuario.nombre
        cosa2=self.material.titulo
        return f"Prestamo #{self.id_prestamo} | Usuario: {cosa} | Material: {cosa2} | Inicio: {self.fecha_inicio} | Entrega: {self.fecha_devolucion}"

class Penalizacion:
    def __init__(self,a,b,c=False):
        self.monto=a
        self.motivo=b
        self.pagada=c
    def calcular_multa(self,a):
        self.monto=a*10
        dato=self.monto
        return f"Multa: ${dato}"
    def bloquear_usuario(self,a):
        a.bloqueado=True
        return f"Usuario {a.nombre} bloqueado"
    def mostrar_info(self):
        return f"Penalizacion | Monto: ${self.monto} | Motivo: {self.motivo} | Pagada: {self.pagada}"

class Catalogo:
    def __init__(self,a):
        self.sucursales=a
    def buscar_por_autor(self,a):
        lista=[]
        for cosa in self.sucursales:
            for dato in cosa.catalogo_local:
                if isinstance(dato,Libro):
                    if dato.autor.lower()==a.lower():
                        lista.append((cosa.nombre,dato.titulo))
        return lista
    def buscar_en_todas_sucursales(self,a):
        lista=[]
        for cosa in self.sucursales:
            for dato in cosa.catalogo_local:
                if a.lower() in dato.titulo.lower():
                    lista.append((cosa.nombre,dato.titulo))
        return lista
