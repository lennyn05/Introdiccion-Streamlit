import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  

# ─── Configuración de la página ─────────────────────────────────────
st.set_page_config(
    page_title="Introducción a Streamlit",
    page_icon="🦖",
    layout="wide"
)

# ─── Encabezado ─────────────────────────────────────────────────────
st.title("🦖 Introducción a Streamlit")

st.markdown("""
Streamlit es un framework de Python que permite crear aplicaciones web de forma sencilla y rápida.  
Es ideal para la **visualización de datos**, el **análisis** y el desarrollo de **prototipos interactivos**.
""")

# ─── Sección con columnas ───────────────────────────────────────────
col1, col2 = st.columns([2,1])

with col1:
    st.subheader("🚀 Ventajas de Streamlit")
    st.markdown("""
    - ✅ **Facilidad de uso:** No necesitas saber HTML, CSS o JavaScript  
    - 🎯 **Interactividad:** Widgets como botones, sliders y selectores  
    - 🔗 **Integración:** Compatible con Pandas, Matplotlib, Plotly  
    - ☁️ **Despliegue sencillo:** Fácil de compartir en la web  
    """)

with col2:
    st.image(
        "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
        use_container_width=True
    )

# ─── Separador ──────────────────────────────────────────────────────
st.markdown("---")

# ─── Tabla ──────────────────────────────────────────────────────────
st.subheader("📊 Características principales")

data = {
    "Característica": [
        "Facilidad de uso",
        "Interactividad",
        "Integración",
        "Despliegue"
    ],
    "Descripción": [
        "No requiere conocimientos avanzados de desarrollo web",
        "Permite crear apps dinámicas con widgets",
        "Compatible con múltiples librerías de Python",
        "Fácil publicación en la nube"
    ]
}

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# ─── Gráfico ────────────────────────────────────────────────────────
st.subheader("📈 Ejemplo de gráfico")

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Función seno")

st.pyplot(fig)

# ─── Información adicional ──────────────────────────────────────────
st.markdown("""
💡 **¿Para quién es Streamlit?**  
Ideal para científicos de datos, analistas y desarrolladores que quieren crear aplicaciones web sin complicarse con frontend.
""")

# ─── Footer ─────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "👩‍💻 Creado por **Luz Eliana Martínez** | [GitHub](https://github.com/tu-usuario)"
)