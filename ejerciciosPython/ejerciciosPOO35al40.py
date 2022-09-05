class Poo:
    def __init__(self, titulo):
            self.titulo=titulo
            print('🔶'*20,titulo,'🔶'*20)

    def video35(self): #Herencia
        class Persona():
        
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombres = nom

            def mostrarNombreCompleto(self):
                txt = "{0} {1}, {2}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

        class Estudiante(Persona):

            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

        estu1 = Estudiante("Torres", "López", "Juan", "Ingeniería Civil")
        print(estu1.mostrarNombreCompleto())
        print(estu1.profesion)

    def video36(self): #Sobreescritura
        class Persona():
    
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombres = nom

            def mostrarNombreCompleto(self):
                txt = "{0} {1}, {2}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

            def datos(self):
                print(self.mostrarNombreCompleto())


        class Estudiante(Persona):

            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

            def datos(self):
                super().datos()
                print("Profesión: {0}".format(self.profesion))


        estu1 = Estudiante("Torres", "López", "Juan", "Ingeniería Civil")
        # print(estu1.mostrarNombreCompleto())
        # print(estu1.profesion)
        estu1.datos()

    def video37(self): #Sustitucion entre Clases
        class Persona():
    
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombres = nom

            def mostrarNombreCompleto(self):
                txt = "{0} {1}, {2}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

            def datos(self):
                print(self.mostrarNombreCompleto())


        class Estudiante(Persona):

            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

            def datos(self):
                super().datos()
                print("Profesión: {0}".format(self.profesion))


        # estu1 = Estudiante("Torres", "López", "Juan", "Ingeniería Civil")
        per1 = Persona("Torres", "López", "Juan")
        # print(estu1.mostrarNombreCompleto())
        # print(estu1.profesion)
        # estu1.datos()

        print(isinstance(per1, Estudiante))

    def video38(self): #Herencia Multiple
        class ClaseA():

            def __init__(self, par1, par2):
                self.parametro1 = par1
                self.parametro2 = par2


        class ClaseB():

            def __init__(self, par3, par4, par5):
                self.parametro3 = par3
                self.parametro4 = par4
                self.parametro5 = par5


        class ClaseX(ClaseA, ClaseB):
            pass


        cX1 = ClaseX(15, 21)
    
    def video39(self): #Polimorfismo

        class Estudiante():

            def describir(self):
                print("Soy un buen estudiante.")


        class Docente():

            def describir(self):
                print("Me dedico a enseñar cursos.")


        class Trabajador():

            def describir(self):
                print("Trabajo dentro de una gran empresa.")


        def describirPersona(persona):
            persona.describir()


        doc1 = Trabajador()
        describirPersona(doc1)

    def video40(self): #Relaciones entre Clases
        class Pais():
    
            def __init__(self, nom, pre):
                self.nombre = nom
                self.presidente = pre

            def __str__(self):
                txt = "País: {0} - Presidente: {1}"
                return txt.format(self.nombre, self.presidente)


        class Ciudad():

            def __init__(self, nom, hab, pai):
                self.nombre = nom
                self.habitantes = hab
                self.pais = pai

            def __str__(self):
                txt = "Ciudad: {0} - N° Habitantes: {1} ({2})"
                return txt.format(self.nombre, self.habitantes, self.pais)


        class Urbanizacion():

            def __init__(self, nom, ciu):
                self.nombre = nom
                self.ciudad = ciu

            def __str__(self):
                txt = "Urbanización: {0} ({1})"
                return txt.format(self.nombre, self.ciudad)


        pais1 = Pais("Perú", "Martín Vizcarra")
        print(pais1)

        ciudad1 = Ciudad("Chiclayo", 150000, pais1)
        print(ciudad1)

        urba1 = Urbanizacion("María de los Angeles", ciudad1)
        print(urba1)