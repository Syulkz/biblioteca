class Material:
    def __init__(self,a,b,c,d=True):
        self.id_material=a
        self.titulo=b
        self.anio_publicacion=c
        self.disponible=d
    def mostrar_info(self):
        x=self.disponible
        return f"Material: {self.titulo} ({self.anio_publicacion}) - Disponible: {x}"

class Libro(Material):
    def __init__(self,a,b,c,d,e,f,g=True):
        super().__init__(a,b,c,g)
        self.autor=d
        self.isbn=e
        self.genero=f
    def mostrar_info(self):
        x=self.disponible
        return f"Libro: {self.titulo} | Autor: {self.autor} | ISBN: {self.isbn} | Género: {self.genero} | Disponible: {x}"

class Revista(Material):
    def __init__(self,a,b,c,d,e,f=True):
        super().__init__(a,b,c,f)
        self.edicion=d
        self.periodicidad=e
    def mostrar_info(self):
        x=self.disponible
        return f"Revista: {self.titulo} | Edición: {self.edicion} | Periodicidad: {self.periodicidad} | Disponible: {x}"

class MaterialDigital(Material):
    def __init__(self,a,b,c,d,e,f,g=True):
        super().__init__(a,b,c,g)
        self.tipo_archivo=d
        self.url_descarga=e
        self.tamano_mb=f
    def mostrar_info(self):
        x=self.tamano_mb
        return f"Material Digital: {self.titulo} | Tipo: {self.tipo_archivo} | Tamaño: {x} MB | URL: {self.url_descarga} | Disponible: {self.disponible}"

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
        x=len(self.lista_activa)
        return self.bloqueado==False and x<self.limite_prestamos
    def mostrar_info(self):
        x=len(self.lista_activa)
        return f"Usuario: {self.nombre} | Límite: {self.limite_prestamos} | Préstamos activos: {x} | Bloqueado: {self.bloqueado}"

class Bibliotecario(Persona):
    def __init__(self,a):
        super().__init__(a)
    def gestionar_prestamo(self,a,b,c,d,e):
        if a.puede_prestar() and b.disponible:
            x=Prestamo(c,d,e,a,b)
            a.lista_activa.append(x)
            b.disponible=False
            return f"Préstamo realizado correctamente a {a.nombre} del material '{b.titulo}'"
        return "No se pudo realizar el préstamo"
    def transferir_material(self,a,b,c):
        if a in b.catalogo_local:
            b.catalogo_local.remove(a)
            c.catalogo_local.append(a)
            return f"Material '{a.titulo}' transferido de {b.nombre} a {c.nombre}"
        return "El material no se encontró en la sucursal de origen"
    def mostrar_info(self):
        return f"Bibliotecario: {self.nombre}"

class Sucursal:
    def __init__(self,a,b):
        self.id_sucursal=a
        self.nombre=b
        self.catalogo_local=[]
    def agregar_material(self,a):
        self.catalogo_local.append(a)
    def mostrar_catalogo(self):
        if not self.catalogo_local:
            return f"La sucursal {self.nombre} no tiene materiales"
        x=f"Catálogo de {self.nombre}:\n"
        for a in self.catalogo_local:
            x=x+"- "+a.mostrar_info()+"\n"
        return x

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
        return f"Material '{self.material.titulo}' devuelto correctamente"
    def mostrar_info(self):
        x=self.usuario.nombre
        y=self.material.titulo
        return f"Préstamo #{self.id_prestamo} | Usuario: {x} | Material: {y} | Inicio: {self.fecha_inicio} | Devolución: {self.fecha_devolucion}"

class Penalizacion:
    def __init__(self,a,b,c=False):
        self.monto=a
        self.motivo=b
        self.pagada=c
    def calcular_multa(self,a):
        self.monto=a*10
        x=self.monto
        return f"Multa calculada: ${x}"
    def bloquear_usuario(self,a):
        a.bloqueado=True
        return f"Usuario {a.nombre} bloqueado por penalización"
    def mostrar_info(self):
        return f"Penalización | Monto: ${self.monto} | Motivo: {self.motivo} | Pagada: {self.pagada}"

class Catalogo:
    def __init__(self,a):
        self.sucursales=a
    def buscar_por_autor(self,a):
        r=[]
        for b in self.sucursales:
            for c in b.catalogo_local:
                if isinstance(c,Libro) and c.autor.lower()==a.lower():
                    r.append((b.nombre,c.titulo))
        return r
    def buscar_en_todas_sucursales(self,a):
        r=[]
        for b in self.sucursales:
            for c in b.catalogo_local:
                if a.lower() in c.titulo.lower():
                    r.append((b.nombre,c.titulo))
        return r
