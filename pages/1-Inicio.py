import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi App", layout="wide")

# Menú lateral principal
st.sidebar.title("Menu de Navegacion")
opcion = st.sidebar.radio(
    "Selecciona una opcion:",
    ("Inicio", "Analisis de Datos", "Calculadora", "Configuracion", "Ayuda")
)

# Contenido principal segun la opcion seleccionada
if opcion == "Inicio":
    st.title("Pagina de Inicio")
    st.write("Bienvenido a la aplicacion multifuncional.")
    
    # Tabs de ejemplo
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://static.streamlit.io/examples/cat.jpg", caption="Gato", use_container_width=True)
    with col2:
        st.image("https://static.streamlit.io/examples/dog.jpg", caption="Perro", use_container_width=True)
    with col3:
        st.image("https://static.streamlit.io/examples/owl.jpg", caption="Búho", use_container_width=True)

elif opcion == "Analisis de Datos":
    st.title("Analisis de Datos")
    st.info("Modulo en desarrollo... Proximamente podras analizar tus datos aqui.")

elif opcion == "Calculadora":
    st.title("Calculadora")
    
    # Crear columnas para organizar la calculadora
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Entrada de numeros (enteros)
        num1 = st.number_input("Ingrese el primer numero:", value=0, step=1, format="%d")
        num2 = st.number_input("Ingrese el segundo numero:", value=0, step=1, format="%d")
        
        # Operaciones basicas
        st.markdown("### Operaciones Basicas")
        col_op1, col_op2, col_op3, col_op4 = st.columns(4)
        
        with col_op1:
            if st.button("Sumar", use_container_width=True):
                resultado = num1 + num2
                st.success(f"Resultado: {num1} + {num2} = {resultado}")
                if 'historial' in st.session_state:
                    st.session_state.historial.append(f"{num1} + {num2} = {resultado}")
        
        with col_op2:
            if st.button("Restar", use_container_width=True):
                resultado = num1 - num2
                st.success(f"Resultado: {num1} - {num2} = {resultado}")
                if 'historial' in st.session_state:
                    st.session_state.historial.append(f"{num1} - {num2} = {resultado}")
        
        with col_op3:
            if st.button("Multiplicar", use_container_width=True):
                resultado = num1 * num2
                st.success(f"Resultado: {num1} x {num2} = {resultado}")
                if 'historial' in st.session_state:
                    st.session_state.historial.append(f"{num1} x {num2} = {resultado}")
        
        with col_op4:
            if st.button("Dividir", use_container_width=True):
                if num2 != 0:
                    resultado = num1 // num2 if num1 % num2 == 0 else num1 / num2
                    if resultado == int(resultado):
                        resultado = int(resultado)
                    st.success(f"Resultado: {num1} / {num2} = {resultado}")
                    if 'historial' in st.session_state:
                        st.session_state.historial.append(f"{num1} / {num2} = {resultado}")
                else:
                    st.error("Error: No se puede dividir entre cero")
        
        st.markdown("---")
        
        # Operaciones avanzadas
        st.markdown("### Operaciones Avanzadas")
        col_adv1, col_adv2, col_adv3 = st.columns(3)
        
        with col_adv1:
            if st.button("Potencia", use_container_width=True):
                resultado = num1 ** num2
                st.success(f"Resultado: {num1}^{num2} = {resultado}")
                if 'historial' in st.session_state:
                    st.session_state.historial.append(f"{num1}^{num2} = {resultado}")
        
        with col_adv2:
            if st.button("Raiz cuadrada", use_container_width=True):
                if num1 >= 0:
                    resultado = num1 ** 0.5
                    if resultado == int(resultado):
                        resultado = int(resultado)
                    st.success(f"Resultado: √{num1} = {resultado}")
                    if 'historial' in st.session_state:
                        st.session_state.historial.append(f"√{num1} = {resultado}")
                else:
                    st.error("Error: No se puede calcular raiz cuadrada de numero negativo")
        
        with col_adv3:
            if st.button("Porcentaje", use_container_width=True):
                resultado = (num1 * num2) / 100
                if resultado == int(resultado):
                    resultado = int(resultado)
                st.success(f"Resultado: {num1}% de {num2} = {resultado}")
                if 'historial' in st.session_state:
                    st.session_state.historial.append(f"{num1}% de {num2} = {resultado}")
    
    with col2:
        st.markdown("### Historial")
        
        if 'historial' not in st.session_state:
            st.session_state.historial = []
        
        if st.button("Limpiar historial", use_container_width=True):
            st.session_state.historial = []
            st.rerun()
        
        if st.session_state.historial:
            for item in reversed(st.session_state.historial[-5:]):
                st.text(item)
        else:
            st.info("No hay operaciones registradas")

elif opcion == "Configuracion":
    st.title("Configuracion")
    
    notificaciones = st.checkbox("Activar notificaciones", value=True)
    auto_guardar = st.checkbox("Auto guardar cambios", value=True)
    
    if st.button("Guardar configuracion"):
        st.success("Configuracion guardada exitosamente")

elif opcion == "Ayuda":
    st.title("Centro de Ayuda")
    
    with st.expander("Como usar la calculadora"):
        st.write("""
        1. Ingresa los numeros en los campos correspondientes
        2. Selecciona la operacion que deseas realizar
        3. El resultado aparecera automaticamente
        4. Puedes ver el historial de operaciones en el panel derecho
        """)
    
    with st.expander("Funcionalidades"):
        st.write("""
        - Suma, resta, multiplicacion y division
        - Potencia y raiz cuadrada
        - Calculo de porcentajes
        - Historial de operaciones
        """)