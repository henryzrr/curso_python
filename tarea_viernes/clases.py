class Estudiante:
    def __init__(self,nombre,ci,correo,direccion):
        self.nombre_completo=nombre
        self.correo=correo
        self.direccion=direccion
        self.ci=ci

    def get_nombre(self):
        return self.nombre

    def get_ci(self):
        return self.ci

    def get_correo(self):
        return self.correo
    
    def get_direccion(self):
        return self.direccion
    
    def get_datos(self):
        str = "nombre: "+self.nombre+"\nci: "+self.ci+"\ncorreo: "+self.correo+"\ndireccion: "+direccion
        return str

class Curso:
    def __init__(self,nombre_curso,inicio,duracion,cod_curso,estudiantes={}):
        self.nombre_curso=nombre_curso
        self.inicio=inicio
        self.duracion=duracion
        self.cod_curso=cod_curso
        self.estudiante_nota=estudiantes
        self.ls_aprobados=[]
        self.ls_reprobados=[]
        self.exelencia=[]
    def inscribir_estudiante(self,cod_estudiante):
        self.estudiante_nota[cod_estudiante]=0

    def set_notas(self,cod_estudiante,nota):
        self.estudiante_nota[cod_estudiante]=nota
    
    def get_lista_estudiantes(self):
        return self.estudiante_nota

    def get_nombre_curso(self):
        return self.nombre_curso

    def get_inicio_cuso(self):
        return self.inicio

    def get_duracion_curso(self):
        return self.duracion
    
    def get_cod_curso(self):
        return self.cod_curso
    
    def get_nro_inscritos(self):
        return len(self.estudiante_nota)

    def clasificar_estudiante(self):
        promedio=0
        for k,v in estudiante_nota:
            if v>51: 
                ls_aprobados.append(k)
            else:
                ls_reprobados.append(k)
            promedio+=v
        
        prom = float(promedio)/len(estudiante_nota)

        for k,v in estudiante_nota:
            if double(v)>=prom:
                exelencia.append(k)

    def get_aprobados(self):
        return self.ls_aprobados

    def get_reprobados(self):
        return self.ls_reprobados

    def get_lista_exelencia(self):
        return self.exelencia

    def __str__(self):
        str = "nombre: "+self.nombre_curso+"\n"+"cod_curso: "+self.cod_curso+"\n"+"inicio: "+self.inicio+"\n"+"duracion: "+self.duracion
        return str

class instituto:
    def __init__(self,nombre,cod_instituto,cursos=[]):
        self.nombre=nombre
        self.cod_instituto=cod_instituto
        self.cursos=cursos



    