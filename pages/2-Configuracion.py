import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Mi App", layout="wide")

# Inicializar session state para configuración
if 'config' not in st.session_state:
    st.session_state.config = {
        'tema': 'Claro',
        'color_primario': '#FF4B4B',
        'fuente': 'Normal',
        'animaciones': True,
        'notificaciones': True,
        'sonidos': False,
        'idioma': 'Español',
        'auto_guardar': True,
        'mostrar_historial': 5,
        'precision_decimales': 0,
        'tamaño_botones': 'Mediano',
        'vista': 'Normal'
    }

# Menú lateral principal renovado
st.sidebar.markdown("# Navegacion")
st.sidebar.markdown("---")

menu_principal = st.sidebar.selectbox(
    "Selecciona una seccion:",
    ["Dashboard", "Calculadora", "Datos", "Configuracion", "Soporte"]
)

st.sidebar.markdown("---")

# Mostrar estado actual en sidebar
st.sidebar.caption(f"Tema: {st.session_state.config['tema']}")
st.sidebar.caption(f"Idioma: {st.session_state.config['idioma']}")

# ==================== DASHBOARD ====================
if menu_principal == "Dashboard":
    st.title("Dashboard")
    st.markdown("---")
    
    # Metricas principales
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Usuarios Activos", "1,234", "+12%")
    with col2:
        st.metric("Operaciones Hoy", "456", "+8%")
    with col3:
        st.metric("Tasa de Exito", "98.5%", "+2.3%")
    with col4:
        st.metric("Tiempo Promedio", "2.3s", "-0.5s")
    
    st.markdown("---")
    
    # Contenido principal del dashboard
    col_izq, col_der = st.columns([2, 1])
    
    with col_izq:
        st.subheader("Actividad Reciente")
        datos_actividad = {
            'Ene': 120,
            'Feb': 135,
            'Mar': 148,
            'Abr': 162,
            'May': 178,
            'Jun': 195
        }
        st.bar_chart(datos_actividad)
    
    with col_der:
        st.subheader("Notificaciones")
        st.info("Bienvenido al dashboard principal")
        st.success("Sistema operando correctamente")
        st.warning("Nueva actualizacion disponible")
    
    st.markdown("---")
    
    # Seccion de inicio rapido
    st.subheader("Acceso Rapido")
    col_q1, col_q2, col_q3 = st.columns(3)
    with col_q1:
        if st.button("Abrir Calculadora", use_container_width=True):
            menu_principal = "Calculadora"
            st.rerun()
    with col_q2:
        if st.button("Ver Datos", use_container_width=True):
            menu_principal = "Datos"
            st.rerun()
    with col_q3:
        if st.button("Configurar App", use_container_width=True):
            menu_principal = "Configuracion"
            st.rerun()

# ==================== CALCULADORA ====================
elif menu_principal == "Calculadora":
    st.title("Calculadora")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Configurar precision segun preferencias
        if st.session_state.config['precision_decimales'] == 0:
            num1 = st.number_input("Primer numero:", value=0, step=1, format="%d")
            num2 = st.number_input("Segundo numero:", value=0, step=1, format="%d")
        else:
            num1 = st.number_input("Primer numero:", value=0.0, step=0.1, format=f"%.{st.session_state.config['precision_decimales']}f")
            num2 = st.number_input("Segundo numero:", value=0.0, step=0.1, format=f"%.{st.session_state.config['precision_decimales']}f")
        
        st.markdown("### Operaciones")
        
        # Botones de operaciones
        col_op1, col_op2, col_op3, col_op4 = st.columns(4)
        
        with col_op1:
            if st.button("Sumar", use_container_width=True):
                resultado = num1 + num2
                st.success(f"{num1} + {num2} = {resultado}")
                if 'historial_calc' not in st.session_state:
                    st.session_state.historial_calc = []
                st.session_state.historial_calc.append(f"{num1} + {num2} = {resultado}")
        
        with col_op2:
            if st.button("Restar", use_container_width=True):
                resultado = num1 - num2
                st.success(f"{num1} - {num2} = {resultado}")
                if 'historial_calc' not in st.session_state:
                    st.session_state.historial_calc = []
                st.session_state.historial_calc.append(f"{num1} - {num2} = {resultado}")
        
        with col_op3:
            if st.button("Multiplicar", use_container_width=True):
                resultado = num1 * num2
                st.success(f"{num1} x {num2} = {resultado}")
                if 'historial_calc' not in st.session_state:
                    st.session_state.historial_calc = []
                st.session_state.historial_calc.append(f"{num1} x {num2} = {resultado}")
        
        with col_op4:
            if st.button("Dividir", use_container_width=True):
                if num2 != 0:
                    resultado = num1 / num2
                    st.success(f"{num1} / {num2} = {resultado}")
                    if 'historial_calc' not in st.session_state:
                        st.session_state.historial_calc = []
                    st.session_state.historial_calc.append(f"{num1} / {num2} = {resultado}")
                else:
                    st.error("No se puede dividir entre cero")
        
        st.markdown("---")
        st.markdown("### Operaciones Avanzadas")
        
        col_adv1, col_adv2, col_adv3 = st.columns(3)
        
        with col_adv1:
            if st.button("Potencia", use_container_width=True):
                resultado = num1 ** num2
                st.success(f"{num1} ^ {num2} = {resultado}")
                if 'historial_calc' not in st.session_state:
                    st.session_state.historial_calc = []
                st.session_state.historial_calc.append(f"{num1} ^ {num2} = {resultado}")
        
        with col_adv2:
            if st.button("Raiz Cuadrada", use_container_width=True):
                if num1 >= 0:
                    resultado = num1 ** 0.5
                    st.success(f"√{num1} = {resultado}")
                    if 'historial_calc' not in st.session_state:
                        st.session_state.historial_calc = []
                    st.session_state.historial_calc.append(f"√{num1} = {resultado}")
                else:
                    st.error("Numero negativo no tiene raiz real")
        
        with col_adv3:
            if st.button("Porcentaje", use_container_width=True):
                resultado = (num1 * num2) / 100
                st.success(f"{num1}% de {num2} = {resultado}")
                if 'historial_calc' not in st.session_state:
                    st.session_state.historial_calc = []
                st.session_state.historial_calc.append(f"{num1}% de {num2} = {resultado}")
    
    with col2:
        st.markdown("### Historial de Operaciones")
        
        if 'historial_calc' not in st.session_state:
            st.session_state.historial_calc = []
        
        if st.button("Limpiar Historial", use_container_width=True):
            st.session_state.historial_calc = []
            st.rerun()
        
        mostrar = st.session_state.config['mostrar_historial']
        if st.session_state.historial_calc:
            for item in reversed(st.session_state.historial_calc[-mostrar:]):
                st.code(item)
        else:
            st.info("No hay operaciones registradas")

# ==================== DATOS ====================
elif menu_principal == "Datos":
    st.title("Analisis de Datos")
    st.markdown("---")
    
    # Selector de tipo de datos
    tipo_datos = st.selectbox(
        "Selecciona tipo de datos:",
        ["Ventas", "Usuarios", "Productos", "Metricas"]
    )
    
    if tipo_datos == "Ventas":
        st.subheader("Reporte de Ventas")
        
        col1, col2 = st.columns(2)
        with col1:
            datos_ventas = {
                'Enero': 12500,
                'Febrero': 14800,
                'Marzo': 16200,
                'Abril': 17800,
                'Mayo': 19500,
                'Junio': 21200
            }
            st.dataframe(datos_ventas, use_container_width=True)
        
        with col2:
            st.bar_chart(datos_ventas)
    
    elif tipo_datos == "Usuarios":
        st.subheader("Estadisticas de Usuarios")
        
        col1, col2 = st.columns(2)
        with col1:
            usuarios = {
                'Activos': 1234,
                'Nuevos': 345,
                'Inactivos': 567,
                'Total': 2146
            }
            st.dataframe(usuarios, use_container_width=True)
        
        with col2:
            st.metric("Crecimiento Mensual", "+12%")
            st.metric("Retencion", "78%")
    
    elif tipo_datos == "Productos":
        st.subheader("Inventario de Productos")
        
        productos = [
            {"Producto": "Producto A", "Stock": 150, "Ventas": 45},
            {"Producto": "Producto B", "Stock": 89, "Ventas": 67},
            {"Producto": "Producto C", "Stock": 234, "Ventas": 123},
            {"Producto": "Producto D", "Stock": 45, "Ventas": 23}
        ]
        st.dataframe(productos, use_container_width=True)
    
    else:
        st.subheader("Metricas de Rendimiento")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Tiempo Respuesta", "1.2s", "-0.3s")
        with col2:
            st.metric("Disponibilidad", "99.9%", "+0.1%")
        with col3:
            st.metric("Errores", "0.5%", "-0.2%")

# ==================== CONFIGURACION ====================
elif menu_principal == "Configuracion":
    st.title("Configuracion")
    st.markdown("---")
    
    # Crear tabs para organizar configuracion
    tab_general, tab_visual, tab_funcional = st.tabs(["General", "Visual", "Funcional"])
    
    with tab_general:
        st.subheader("Preferencias Generales")
        
        col1, col2 = st.columns(2)
        
        with col1:
            idioma = st.selectbox(
                "Idioma de la interfaz",
                ["Español", "Ingles", "Portugues"],
                index=["Español", "Ingles", "Portugues"].index(st.session_state.config['idioma'])
            )
            st.session_state.config['idioma'] = idioma
            
            notificaciones = st.checkbox("Activar notificaciones", value=st.session_state.config['notificaciones'])
            st.session_state.config['notificaciones'] = notificaciones
            
            auto_guardar = st.checkbox("Auto guardar configuracion", value=st.session_state.config['auto_guardar'])
            st.session_state.config['auto_guardar'] = auto_guardar
        
        with col2:
            sonidos = st.checkbox("Activar sonidos", value=st.session_state.config['sonidos'])
            st.session_state.config['sonidos'] = sonidos
            
            animaciones = st.checkbox("Activar animaciones", value=st.session_state.config['animaciones'])
            st.session_state.config['animaciones'] = animaciones
    
    with tab_visual:
        st.subheader("Apariencia")
        
        col1, col2 = st.columns(2)
        
        with col1:
            tema = st.radio(
                "Tema de la aplicacion",
                ["Claro", "Oscuro"],
                index=0 if st.session_state.config['tema'] == "Claro" else 1
            )
            st.session_state.config['tema'] = tema
            
            if tema == "Oscuro":
                st.markdown("""
                <style>
                .stApp {
                    background-color: #1e1e1e;
                }
                </style>
                """, unsafe_allow_html=True)
            
            color_primario = st.color_picker(
                "Color principal",
                st.session_state.config['color_primario']
            )
            st.session_state.config['color_primario'] = color_primario
            
            # Aplicar color personalizado
            st.markdown(f"""
            <style>
            .stButton > button {{
                background-color: {color_primario};
                border-color: {color_primario};
            }}
            </style>
            """, unsafe_allow_html=True)
        
        with col2:
            fuente = st.selectbox(
                "Tamaño de fuente",
                ["Pequeño", "Normal", "Grande"],
                index=["Pequeño", "Normal", "Grande"].index(st.session_state.config['fuente'])
            )
            st.session_state.config['fuente'] = fuente
            
            tamano_botones = st.selectbox(
                "Tamaño de botones",
                ["Pequeño", "Mediano", "Grande"],
                index=["Pequeño", "Mediano", "Grande"].index(st.session_state.config['tamaño_botones'])
            )
            st.session_state.config['tamaño_botones'] = tamano_botones
            
            vista = st.selectbox(
                "Vista predeterminada",
                ["Normal", "Compacta", "Amplia"],
                index=["Normal", "Compacta", "Amplia"].index(st.session_state.config['vista'])
            )
            st.session_state.config['vista'] = vista
    
    with tab_funcional:
        st.subheader("Ajustes de Funcionalidad")
        
        col1, col2 = st.columns(2)
        
        with col1:
            historial = st.slider(
                "Operaciones en historial",
                1, 20, st.session_state.config['mostrar_historial']
            )
            st.session_state.config['mostrar_historial'] = historial
            
            precision = st.select_slider(
                "Decimales en calculos",
                options=[0, 1, 2, 3, 4],
                value=st.session_state.config['precision_decimales']
            )
            st.session_state.config['precision_decimales'] = precision
        
        with col2:
            st.write("**Opciones Avanzadas**")
            
            if st.button("Restablecer valores predeterminados", use_container_width=True):
                st.session_state.config = {
                    'tema': 'Claro',
                    'color_primario': '#FF4B4B',
                    'fuente': 'Normal',
                    'animaciones': True,
                    'notificaciones': True,
                    'sonidos': False,
                    'idioma': 'Español',
                    'auto_guardar': True,
                    'mostrar_historial': 5,
                    'precision_decimales': 0,
                    'tamaño_botones': 'Mediano',
                    'vista': 'Normal'
                }
                st.success("Configuracion restablecida")
                st.rerun()
            
            if st.button("Exportar configuracion", use_container_width=True):
                st.json(st.session_state.config)
    
    st.markdown("---")
    if st.button("Guardar todos los cambios", type="primary", use_container_width=True):
        st.success("Configuracion guardada correctamente")
        st.balloons()

# ==================== SOPORTE ====================
elif menu_principal == "Soporte":
    st.title("Soporte Tecnico")
    st.markdown("---")
    
    tab_faq, tab_contacto, tab_ayuda = st.tabs(["Preguntas Frecuentes", "Contacto", "Ayuda Rapida"])
    
    with tab_faq:
        st.subheader("Preguntas Frecuentes")
        
        with st.expander("Como cambio el tema de la aplicacion?"):
            st.write("Dirigete a la seccion de Configuracion, luego a la pestaña Visual y selecciona entre tema Claro u Oscuro.")
        
        with st.expander("Como guardo mis calculos?"):
            st.write("Todas las operaciones se guardan automaticamente en el historial de la calculadora. Puedes configurar cuantas operaciones mostrar en Configuracion > Funcional.")
        
        with st.expander("Puedo personalizar los colores?"):
            st.write("Si, en Configuracion > Visual puedes usar el selector de color para personalizar el color principal de la interfaz.")
        
        with st.expander("La configuracion se guarda automaticamente?"):
            st.write("Si activaste la opcion 'Auto guardar configuracion' en Configuracion > General, tus cambios se guardaran automaticamente.")
    
    with tab_contacto:
        st.subheader("Contactanos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Email de soporte:**")
            st.code("soporte@miapp.com")
            
            st.write("**Telefono:**")
            st.code("+57 300 123 4567")
        
        with col2:
            st.write("**Horario de atencion:**")
            st.code("Lunes a Viernes")
            st.code("8:00 AM - 6:00 PM")
        
        st.markdown("---")
        st.subheader("Envia un mensaje")
        
        nombre = st.text_input("Nombre completo")
        email = st.text_input("Correo electronico")
        asunto = st.text_input("Asunto")
        mensaje = st.text_area("Mensaje", height=100)
        
        if st.button("Enviar mensaje", type="primary"):
            if nombre and email and mensaje:
                st.success("Mensaje enviado. Te responderemos pronto.")
            else:
                st.error("Por favor completa todos los campos.")
    
    with tab_ayuda:
        st.subheader("Guia Rapida")
        
        st.write("**Atajos de teclado:**")
        st.code("""
        - Dashboard: Presiona D
        - Calculadora: Presiona C
        - Configuracion: Presiona S
        - Soporte: Presiona H
        """)
        
        st.write("**Consejos utiles:**")
        st.info("Puedes personalizar completamente la apariencia desde Configuracion")
        st.success("El historial de calculos se mantiene mientras la aplicacion este abierta")
        st.warning("Recuerda guardar tu configuracion para mantener tus preferencias")