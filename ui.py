import streamlit as st
from queue import Queue
from alumos import Alumno
from Personas import Persona

# --- CONFIGURACIÓN DE LA PÁGINA WEB ---
st.set_page_config(page_title="Control Escolar Pro v1.0", layout="centered")

# Estilos personalizados para emular el diseño (cuadros celestes en modo claro)
st.markdown("""
    <style>
    .reportview-container .main .block-container{ max-width: 560px; }
    /* Estilo para las tarjetas informativas */
    .stAlert { border-radius: 15px; }
    </style>
""", unsafe_allow_html=True)

st.title("MI SEMESTRE")

# --- CATALOGO DE MATERIAS ---
LISTADEMATERIAS={
    1:["Bloque 1:  Algebra", "Bloque 2:  Programacion 1", "Bloque 3:  Administracion"],
    2:["Bloque 1:  Calculo integral", "Bloque 2:  Programacion 2", "Bloque 3:  paginas web"],
    3:["Bloque 1:  Algoritmos", "Bloque 2:  Redes", "Bloque 3:  Calculo diferencial"],
    4:["Bloque 1:  Ciberseguridad", "Bloque 2:  Sistemas Operativos", "Bloque 3:  Bases de Datos"],
    5:["Bloque 1:  Inteligencia Artificial", "Bloque 2:  Robótica", "Bloque 3:  Graficación"],
    6:["Bloque 1:  Proyecto Final", "Bloque 2:  Ética Profesional", "Bloque 3:  tesis"]}

# --- INICIALIZACIÓN DE DATOS EN LA SESIÓN WEB ---
# En la web, para que las colas no se reinicien en cada clic, usamos st.session_state
if "filas_por_semestre" not in st.session_state:
    # Registro oficial de los 20 alumnos
    al1 = Alumno(); al1.set__nombre("Aldo Antonio de la Cruz"); al1.set__usuario("AAC01"); al1.set__correo("aldoan@outlook.mx"); al1.set__id(12345); al1.set__numerotelefono(3329342556); al1.set__semestre(1); al1.set__materias(LISTADEMATERIAS[1]); al1.set__calificacion1(40); al1.set__calificacion2(55); al1.set__calificacion3(50)
    al2 = Alumno(); al2.set__nombre("Jessica Hernandez Perez"); al2.set__usuario("JHP02"); al2.set__correo("jessi345@outlook.mx"); al2.set__id(54321); al2.set__numerotelefono(3329045687); al2.set__semestre(5); al2.set__materias(LISTADEMATERIAS[5]); al2.set__calificacion1(85); al2.set__calificacion2(78); al2.set__calificacion3(92)
    al3 = Alumno(); al3.set__nombre("Catriel Joya Quiroz"); al3.set__usuario("CJQ03"); al3.set__correo("Catrieljoya@outlook.mx"); al3.set__id(12543); al3.set__numerotelefono(3345876091); al3.set__semestre(3); al3.set__materias(LISTADEMATERIAS[3]); al3.set__calificacion1(90); al3.set__calificacion2(100); al3.set__calificacion3(88)
    al4 = Alumno(); al4.set__nombre("Carlos Gomez Ruiz"); al4.set__usuario("CGR04"); al4.set__correo("carlosg@outlook.mx"); al4.set__id(98765); al4.set__numerotelefono(3312345678); al4.set__semestre(2); al4.set__materias(LISTADEMATERIAS[2]); al4.set__calificacion1(50); al4.set__calificacion2(60); al4.set__calificacion3(40)
    al5 = Alumno(); al5.set__nombre("Ana Sofia Lopez"); al5.set__usuario("ASL05"); al5.set__correo("anasofia@outlook.mx"); al5.set__id(87654); al5.set__numerotelefono(3387654321); al5.set__semestre(6); al5.set__materias(LISTADEMATERIAS[6]); al5.set__calificacion1(92); al5.set__calificacion2(95); al5.set__calificacion3(91)
    al6 = Alumno(); al6.set__nombre("Luis Fernando Torres"); al6.set__usuario("LFT06"); al6.set__correo("luisfer@outlook.mx"); al6.set__id(76543); al6.set__numerotelefono(3355443322); al6.set__semestre(4); al6.set__materias(LISTADEMATERIAS[4]); al6.set__calificacion1(88); al6.set__calificacion2(82); al6.set__calificacion3(96)
    al7 = Alumno(); al7.set__nombre("Mariana Chavez Rios"); al7.set__usuario("MCR07"); al7.set__correo("marianach@outlook.mx"); al7.set__id(65432); al7.set__numerotelefono(3311223344); al7.set__semestre(1); al7.set__materias(LISTADEMATERIAS[1]); al7.set__calificacion1(100); al7.set__calificacion2(90); al7.set__calificacion3(95)
    al8 = Alumno(); al8.set__nombre("Ricardo Mendiola Silva"); al8.set__usuario("RMS08"); al8.set__correo("ricardoms@outlook.mx"); al8.set__id(23456); al8.set__numerotelefono(3366778899); al8.set__semestre(3); al8.set__materias(LISTADEMATERIAS[3]); al8.set__calificacion1(79); al8.set__calificacion2(87); al8.set__calificacion3(83)
    al9 = Alumno(); al9.set__nombre("Valeria Ortiz Luna"); al9.set__usuario("VOL09"); al9.set__correo("valeriaol@outlook.mx"); al9.set__id(34567); al9.set__numerotelefono(3344556677); al9.set__semestre(5); al9.set__materias(LISTADEMATERIAS[5]); al9.set__calificacion1(45); al9.set__calificacion2(50); al9.set__calificacion3(40)
    al10 = Alumno(); al10.set__nombre("Alejandro Ruiz Diaz"); al10.set__usuario("ARD10"); al10.set__correo("alexruiz@outlook.mx"); al10.set__id(45678); al10.set__numerotelefono(3399887766); al10.set__semestre(2); al10.set__materias(LISTADEMATERIAS[2]); al10.set__calificacion1(75); al10.set__calificacion2(90); al10.set__calificacion3(86)
    al11 = Alumno(); al11.set__nombre("Brandon Alaniz Torres"); al11.set__usuario("BAT11"); al11.set__correo("brandon.al@outlook.mx"); al11.set__id(56789); al11.set__numerotelefono(3314253647); al11.set__semestre(1); al11.set__materias(LISTADEMATERIAS[1]); al11.set__calificacion1(40); al11.set__calificacion2(60); al11.set__calificacion3(55)
    al12 = Alumno(); al12.set__nombre("Diana Laura Montes"); al12.set__usuario("DLM12"); al12.set__correo("dianamontes@outlook.mx"); al12.set__id(67890); al12.set__numerotelefono(3398877665); al12.set__semestre(2); al12.set__materias(LISTADEMATERIAS[2]); al12.set__calificacion1(95); al12.set__calificacion2(90); al12.set__calificacion3(100)
    al13 = Alumno(); al13.set__nombre("Eduardo Meza Castro"); al13.set__usuario("EMC13"); al13.set__correo("lalo.meza@outlook.mx"); al13.set__id(78901); al13.set__numerotelefono(3355667788); al13.set__semestre(3); al13.set__materias(LISTADEMATERIAS[3]); al13.set__calificacion1(80); al13.set__calificacion2(85); al13.set__calificacion3(78)
    al14 = Alumno(); al14.set__nombre("Fernanda Islas Moran"); al14.set__usuario("FIM14"); al14.set__correo("ferislas@outlook.mx"); al14.set__id(89012); al14.set__numerotelefono(3312233445); al14.set__semestre(4); al14.set__materias(LISTADEMATERIAS[4]); al14.set__calificacion1(50); al14.set__calificacion2(60); al14.set__calificacion3(45)
    al15 = Alumno(); al15.set__nombre("Gabriel Segura Peña"); al15.set__usuario("GSP15"); al15.set__correo("gabysegura@outlook.mx"); al15.set__id(90123); al15.set__numerotelefono(3344332211); al15.set__semestre(5); al15.set__materias(LISTADEMATERIAS[5]); al15.set__calificacion1(90); al15.set__calificacion2(92); al15.set__calificacion3(96)
    al16 = Alumno(); al16.set__nombre("Hector Morales Vega"); al16.set__usuario("HMV16"); al16.set__correo("hectormv@outlook.mx"); al16.set__id(23412); al16.set__numerotelefono(3366554433); al16.set__semestre(6); al16.set__materias(LISTADEMATERIAS[6]); al16.set__calificacion1(50); al16.set__calificacion2(55); al16.set__calificacion3(60)
    al17 = Alumno(); al17.set__nombre("Irene Palacios Soto"); al17.set__usuario("IPS17"); al17.set__correo("irene.ps@outlook.mx"); al17.set__id(34523); al17.set__numerotelefono(3377889900); al17.set__semestre(4); al17.set__materias(LISTADEMATERIAS[4]); al17.set__calificacion1(88); al17.set__calificacion2(91); al17.set__calificacion3(85)
    al18 = Alumno(); al18.set__nombre("Juan Pablo Cisneros"); al18.set__usuario("JPC18"); al18.set__correo("juanpac@outlook.mx"); al18.set__id(45634); al18.set__numerotelefono(3311992288); al18.set__semestre(2); al18.set__materias(LISTADEMATERIAS[2]); al18.set__calificacion1(55); al18.set__calificacion2(60); al18.set__calificacion3(45)
    al19 = Alumno(); al19.set__nombre("Karla Vazquez Flores"); al19.set__usuario("KVF19"); al19.set__correo("karlavq@outlook.mx"); al19.set__id(56745); al19.set__numerotelefono(3322883399); al19.set__semestre(3); al19.set__materias(LISTADEMATERIAS[3]); al19.set__calificacion1(95); al19.set__calificacion2(98); al19.set__calificacion3(94)
    al20 = Alumno(); al20.set__nombre("Leonardo Cárdenas"); al20.set__usuario("LCO20"); al20.set__correo("leocardenas@outlook.mx"); al20.set__id(67856); al20.set__numerotelefono(3344115522); al20.set__semestre(6); al20.set__materias(LISTADEMATERIAS[6]); al20.set__calificacion1(85); al20.set__calificacion2(80); al20.set__calificacion3(89)

    lista_completa = [al1, al2, al3, al4, al5, al6, al7, al8, al9, al10, al11, al12, al13, al14, al15, al16, al17, al18, al19, al20]
    
    st.session_state.filas_por_semestre = {1: Queue(), 2: Queue(), 3: Queue(), 4: Queue(), 5: Queue(), 6: Queue()}
    for al in lista_completa:
        semestre_alumno = al.get__semestre()
        st.session_state.filas_por_semestre[semestre_alumno].put(al)
        
    st.session_state.alumno_actual = None

# --- PANEL DE CONTROLES (SEMESTRE ACTIVO Y CONTADOR) ---
col_combobox, col_contador = st.columns([2, 1])

with col_combobox:
    opcion_semestre = st.selectbox("Semestre en curso:", ["1 Semestre", "2 Semestre", "3 Semestre", "4 Semestre", "5 Semestre", "6 Semestre"])
    semestre_seleccionado = int(opcion_semestre.split()[0])

total_en_fila = st.session_state.filas_por_semestre[semestre_seleccionado].qsize()

with col_contador:
    st.write("") # Espaciador estético
    st.markdown(f"<h4 style='color: #3b82f6; text-align: right;'>{total_en_fila} alumnos activos</h4>", unsafe_allow_html=True)

# --- BOTÓN DE ATENCIÓN DE ALUMNOS ---
if st.button("Atender Siguiente Alumno", use_container_width=True):
    fila_actual = st.session_state.filas_por_semestre[semestre_seleccionado]
    if not fila_actual.empty():
        st.session_state.alumno_actual = fila_actual.get()
        st.rerun()
    else:
        st.error(f"¡No quedan más alumnos en la fila de {semestre_seleccionado}° semestre!")
        st.session_state.alumno_actual = None

# --- PANEL CENTRAL DE DATOS (TARJETA) ---
with st.container(border=True):
    al_actual = st.session_state.alumno_actual
    
    if al_actual is not None:
        st.markdown(f"### Alumno: {al_actual.get__nombre()}")
        st.markdown(f"#### `{{{al_actual.get__id()}}}`")
        st.write(f"**Semestre:** {al_actual.get__semestre()}° Semestre")
        
        st.write("---")
        
        # Estructura Mitad y Mitad (Materias a la izquierda, Calificaciones a la derecha)
        col_mat, col_cal = st.columns(2)
        
        with col_mat:
            st.write("**Materias Asignadas:**")
            materias_lista = al_actual.get__materias()
            for mat in materias_lista:
                st.write(f"• {mat}")
                
        with col_cal:
            st.write("**Calificaciones:**")
            st.write(f"Calificación: {al_actual.get__calificacion1()}")
            st.write(f"Calificación: {al_actual.get__calificacion2()}")
            st.write(f"Calificación: {al_actual.get__calificacion3()}")
            
        st.write("---")
        
        sumadecalificaciones = al_actual.calcular_calificaciones()
        porcentajeglobal = (sumadecalificaciones / 300) * 100
        
        st.write(f"**Puntuación Total:** {sumadecalificaciones} / 300 pts")
        st.markdown(f"#### PROMEDIO GLOBAL: {porcentajeglobal:.1f}%")
        
        if porcentajeglobal >= 70:
            st.success("ESTADO: APROBADO")
            st.info("Adeudo financiero: $0.00 MXN")
        else:
            st.error("ESTADO: REPROBADO")
            st.warning("Adeudo generado: $500 Quinientos pesos MXN  \nFavor de pasar a caja")
            
    else:
        st.write("Selecciona un semestre y presiona Atender...")
