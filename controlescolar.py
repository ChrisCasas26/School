from queue import Queue
from alumos import Alumno
from Personas import Persona
import time

#no se te olvide caon que los catalogos sirven para llevar datos o cajitas de datos cuando los necesitas
LISTADEMATERIAS={
    1:["Bloque 1:  Algebra", 
       "Bloque 2:  Programacion 1",
       "Bloque 3:  Administracion"],
    2:["Bloque 1:  Calculo integral", 
       "Bloque 2:  Programacion 2", 
       "Bloque 3:  paginas web"],
    3:["Bloque 1:  Algoritmos", 
       "Bloque 2:  Redes", 
       "Bloque 3:  Calculo diferencial"],
    4:["Bloque 1:  Ciberseguridad",
       "Bloque 2:  Sistemas Operativos", 
       "Bloque 3:  Bases de Datos"],
    5:["Bloque 1:  Inteligencia Artificial", 
       "Bloque 2:  Robótica", 
       "Bloque 3:  Graficación"],
    6:["Bloque 1:  Proyecto Final", 
       "Bloque 2:  Ética Profesional", 
       "Bloque 3:  tesis"]}

al1 = Alumno()
al1.set__nombre("Aldo Antonio de la Cruz")
al1.set__usuario("AAC01")
al1.set__correo("aldoan@outlook.mx")
al1.set__id(12345)
al1.set__numerotelefono(3329342556)
al1.set__semestre(1)
al1.set__materias(LISTADEMATERIAS[1])
al1.set__calificacion1(40)
al1.set__calificacion2(55)
al1.set__calificacion3(50)

al2 = Alumno()
al2.set__nombre("Jessica Hernandez Perez")
al2.set__usuario("JHP02")
al2.set__correo("jessi345@outlook.mx")
al2.set__id(54321)
al2.set__numerotelefono(3329045687)
al2.set__semestre(5)
al2.set__materias(LISTADEMATERIAS[5])
al2.set__calificacion1(85)
al2.set__calificacion2(78)
al2.set__calificacion3(92)

al3 = Alumno()
al3.set__nombre("Catriel Joya Quiroz")
al3.set__usuario("CJQ03")
al3.set__correo("Catrieljoya@outlook.mx")
al3.set__id(12543)
al3.set__numerotelefono(3345876091)
al3.set__semestre(3)
al3.set__materias(LISTADEMATERIAS[3])
al3.set__calificacion1(90)
al3.set__calificacion2(100)
al3.set__calificacion3(88)

al4 = Alumno()
al4.set__nombre("Carlos Gomez Ruiz")
al4.set__usuario("CGR04")
al4.set__correo("carlosg@outlook.mx")
al4.set__id(98765)
al4.set__numerotelefono(3312345678)
al4.set__semestre(2)
al4.set__materias(LISTADEMATERIAS[2])
al4.set__calificacion1(50)
al4.set__calificacion2(60)
al4.set__calificacion3(40)

al5 = Alumno()
al5.set__nombre("Ana Sofia Lopez")
al5.set__usuario("ASL05")
al5.set__correo("anasofia@outlook.mx")
al5.set__id(87654)
al5.set__numerotelefono(3387654321)
al5.set__semestre(6)
al5.set__materias(LISTADEMATERIAS[6])
al5.set__calificacion1(92)
al5.set__calificacion2(95)
al5.set__calificacion3(91)

al6 = Alumno()
al6.set__nombre("Luis Fernando Torres")
al6.set__usuario("LFT06")
al6.set__correo("luisfer@outlook.mx")
al6.set__id(76543)
al6.set__numerotelefono(3355443322)
al6.set__semestre(4)
al6.set__materias(LISTADEMATERIAS[4])
al6.set__calificacion1(88)
al6.set__calificacion2(82)
al6.set__calificacion3(96)

al7 = Alumno()
al7.set__nombre("Mariana Chavez Rios")
al7.set__usuario("MCR07")
al7.set__correo("marianach@outlook.mx")
al7.set__id(65432)
al7.set__numerotelefono(3311223344)
al7.set__semestre(1)
al7.set__materias(LISTADEMATERIAS[1])
al7.set__calificacion1(100)
al7.set__calificacion2(90)
al7.set__calificacion3(95)

al8 = Alumno()
al8.set__nombre("Ricardo Mendiola Silva")
al8.set__usuario("RMS08")
al8.set__correo("ricardoms@outlook.mx")
al8.set__id(23456)
al8.set__numerotelefono(3366778899)
al8.set__semestre(3)
al8.set__materias(LISTADEMATERIAS[3])
al8.set__calificacion1(79)
al8.set__calificacion2(87)
al8.set__calificacion3(83)

al9 = Alumno()
al9.set__nombre("Valeria Ortiz Luna")
al9.set__usuario("VOL09")
al9.set__correo("valeriaol@outlook.mx")
al9.set__id(34567)
al9.set__numerotelefono(3344556677)
al9.set__semestre(5)
al9.set__materias(LISTADEMATERIAS[5])
al9.set__calificacion1(45)
al9.set__calificacion2(50)
al9.set__calificacion3(40)

al10 = Alumno()
al10.set__nombre("Alejandro Ruiz Diaz")
al10.set__usuario("ARD10")
al10.set__correo("alexruiz@outlook.mx")
al10.set__id(45678)
al10.set__numerotelefono(3399887766)
al10.set__semestre(2)
al10.set__materias(LISTADEMATERIAS[2])
al10.set__calificacion1(75)
al10.set__calificacion2(90)
al10.set__calificacion3(86)

al11 = Alumno()
al11.set__nombre("Brandon Alaniz Torres")
al11.set__usuario("BAT11")
al11.set__correo("brandon.al@outlook.mx")
al11.set__id(56789)
al11.set__numerotelefono(3314253647)
al11.set__semestre(1)
al11.set__materias(LISTADEMATERIAS[1])
al11.set__calificacion1(40)
al11.set__calificacion2(60)
al11.set__calificacion3(55)

al12 = Alumno()
al12.set__nombre("Diana Laura Montes")
al12.set__usuario("DLM12")
al12.set__correo("dianamontes@outlook.mx")
al12.set__id(67890)
al12.set__numerotelefono(3398877665)
al12.set__semestre(2)
al12.set__materias(LISTADEMATERIAS[2])
al12.set__calificacion1(95)
al12.set__calificacion2(90)
al12.set__calificacion3(100)

al13 = Alumno()
al13.set__nombre("Eduardo Meza Castro")
al13.set__usuario("EMC13")
al13.set__correo("lalo.meza@outlook.mx")
al13.set__id(78901)
al13.set__numerotelefono(3355667788)
al13.set__semestre(3)
al13.set__materias(LISTADEMATERIAS[3])
al13.set__calificacion1(80)
al13.set__calificacion2(85)
al13.set__calificacion3(78)

al14 = Alumno()
al14.set__nombre("Fernanda Islas Moran")
al14.set__usuario("FIM14")
al14.set__correo("ferislas@outlook.mx")
al14.set__id(89012)
al14.set__numerotelefono(3312233445)
al14.set__semestre(4)
al14.set__materias(LISTADEMATERIAS[4])
al14.set__calificacion1(50)
al14.set__calificacion2(60)
al14.set__calificacion3(45)

al15 = Alumno()
al15.set__nombre("Gabriel Segura Peña")
al15.set__usuario("GSP15")
al15.set__correo("gabysegura@outlook.mx")
al15.set__id(90123)
al15.set__numerotelefono(3344332211)
al15.set__semestre(5)
al15.set__materias(LISTADEMATERIAS[5])
al15.set__calificacion1(90)
al15.set__calificacion2(92)
al15.set__calificacion3(96)

al16 = Alumno()
al16.set__nombre("Hector Morales Vega")
al16.set__usuario("HMV16")
al16.set__correo("hectormv@outlook.mx")
al16.set__id(23412)
al16.set__numerotelefono(3366554433)
al16.set__semestre(6)
al16.set__materias(LISTADEMATERIAS[6])
al16.set__calificacion1(50)
al16.set__calificacion2(55)
al16.set__calificacion3(60)

al17 = Alumno()
al17.set__nombre("Irene Palacios Soto")
al17.set__usuario("IPS17")
al17.set__correo("irene.ps@outlook.mx")
al17.set__id(34523)
al17.set__numerotelefono(3377889900)
al17.set__semestre(4)
al17.set__materias(LISTADEMATERIAS[4])
al17.set__calificacion1(88)
al17.set__calificacion2(91)
al17.set__calificacion3(85)

al18 = Alumno()
al18.set__nombre("Juan Pablo Cisneros")
al18.set__usuario("JPC18")
al18.set__correo("juanpac@outlook.mx")
al18.set__id(45634)
al18.set__numerotelefono(3311992288)
al18.set__semestre(2)
al18.set__materias(LISTADEMATERIAS[2])
al18.set__calificacion1(55)
al18.set__calificacion2(60)
al18.set__calificacion3(45)

al19 = Alumno()
al19.set__nombre("Karla Vazquez Flores")
al19.set__usuario("KVF19")
al19.set__correo("karlavq@outlook.mx")
al19.set__id(56745)
al19.set__numerotelefono(3322883399)
al19.set__semestre(3)
al19.set__materias(LISTADEMATERIAS[3])
al19.set__calificacion1(95)
al19.set__calificacion2(98)
al19.set__calificacion3(94)

al20 = Alumno()
al20.set__nombre("Leonardo Cárdenas")
al20.set__usuario("LCO20")
al20.set__correo("leocardenas@outlook.mx")
al20.set__id(67856)
al20.set__numerotelefono(3344115522)
al20.set__semestre(6)
al20.set__materias(LISTADEMATERIAS[6])
al20.set__calificacion1(85)
al20.set__calificacion2(80)
al20.set__calificacion3(89)

filadeatencion=Queue()

LISTAALUMNOS = [al1, al2, al3, al4, al5, al6, al7, al8, al9, al10, al11, al12, al13, al14, al15, al16, al17, al18, al19, al20]
#le damos el nombre a la fila y le decimos los datos que van a entrar
for Alumno in LISTAALUMNOS:
    filadeatencion.put(Alumno)

print("\nAtendiendo alumnos")
 
time.sleep(5)
#aqui esta lo chido, lit es el motor o la funcion que secciona y jala los datos de la lista individualmente
for i in range(len(LISTAALUMNOS)):
    alumnoactual=filadeatencion.get()

    print(f"\nAlumno: {alumnoactual.get__nombre()} en atencion.")
    time.sleep(2)
#aqui jala los datos de semestre y la materia
    print(f"semestre: {alumnoactual.get__semestre()}")
    print(f"\nMaterias: {alumnoactual.get__materias()}")
    time.sleep(4)
#aqui se trae los datos de cada uno y de cada una de sus calificaciones
    print(f"\nCalificacion bloque 1: {alumnoactual.get__calificacion1()}")
    print(f"\nCalificacion bloque 2: {alumnoactual.get__calificacion2()}")
    print(f"\ncalificacion bloque 3: {alumnoactual.get__calificacion3()}")
    time.sleep(4)
#suma de calificaciones es una bariable 
#lo que hice aqui es darle el valor de un metodo que esta en alumnos y la definicion de alumno actual 
#ademas de sacar el porcentaje de la calificacion
    sumadecalificaciones = alumnoactual.calcular_calificaciones()
    print(f"\npuntos totales: {sumadecalificaciones}")
    porcentajeglobal = sumadecalificaciones / 300 * 100
    print(f"\nCALIFICACION FINAL: {porcentajeglobal}")
    time.sleep (6)
#esta condicion define si aprobo el mono o nel y si le vamos a cobrar o no 
    if porcentajeglobal >= 70:
        print ("APROBADO")
    else:
        print ("REPROBADO")
        print ("Adeudo por materia reprobada: Quinientos pesos MXN ($500)")
    
print("Alumnos atendidos")

