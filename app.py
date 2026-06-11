# app.py
import streamlit as st
import streamlit.components.v1 as components
import datetime
import random

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Para mi reina ❤️",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# VARIABLES DE CONFIGURACIÓN (¡Edita esto!)
# ==========================================
# Reemplaza con la URL de una foto tuya o de ustedes (puede ser local o web)
URL_FOTO = "https://images.unsplash.com/photo-1518199266791-5375a83190b7?auto=format&fit=crop&w=300&q=80" 
# Fecha en la que comenzaron a salir (Año, Mes, Día)
FECHA_INICIO = datetime.datetime(2023, 5, 14) 
# URL de música romántica (mp3). Déjalo vacío si no quieres música.
URL_MUSICA = "https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Tours/Enthusiast/Tours_-_01_-_Enthusiast.mp3"

# ==========================================
# INICIALIZACIÓN DEL ESTADO (SESSION STATE)
# ==========================================
if "page" not in st.session_state:
    st.session_state.page = 1
if "selected_plan" not in st.session_state:
    st.session_state.selected_plan = None
if "selected_date" not in st.session_state:
    st.session_state.selected_date = None
if "selected_time" not in st.session_state:
    st.session_state.selected_time = None
if "reason" not in st.session_state:
    st.session_state.reason = ""

# Función para cambiar de pantalla
def set_page(page_num):
    st.session_state.page = page_num

# ==========================================
# ESTILOS CSS PERSONALIZADOS (UX/UI Romántica)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    /* Ocultar elementos predeterminados de Streamlit para efecto App */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Fondo general - Tonos rosa vieja y malva para mejor contraste */
    .stApp {
        background: linear-gradient(135deg, #e0aeb9 0%, #c9a7b9 100%);
        font-family: 'Poppins', sans-serif;
    }

    /* Tarjetas blancas con sombra */
    .card {
        background-color: rgba(255, 255, 255, 0.90); /* Un poco más opaca para resaltar el texto */
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 40px 0 rgba(0, 0, 0, 0.15); /* Sombra más pronunciada */
        backdrop-filter: blur(10px);
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.6);
    }

    /* Estilo de los textos - Morado más oscuro y profundo */
    h1, h2, h3, p {
        color: #4a2e4b; 
        text-align: center;
    }

    /* Imagen circular */
    .profile-pic {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
        border: 4px solid #ffb6c1;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        display: block;
        margin: 0 auto;
    }

    /* Estilo general para los botones nativos de Streamlit */
    div.stButton > button:first-child {
        background-color: #f77085; /* Rosa un poco más fuerte */
        color: white;
        border-radius: 25px;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(247, 112, 133, 0.4);
        width: 100%;
    }

    div.stButton > button:first-child:hover {
        background-color: #e8556c;
        transform: translateY(-2px);
        color: white;
        box-shadow: 0 6px 15px rgba(232, 85, 108, 0.5);
        border: none;
    }

    /* Contador de tiempo */
    .counter {
        font-size: 14px;
        color: #c04860; /* Tono más oscuro para el contador */
        text-align: center;
        margin-bottom: 20px;
        font-weight: 600;
    }

    /* Animación de corazones flotantes */
    .heart-bg {
        position: fixed;
        font-size: 20px;
        color: #ff758c;
        opacity: 0.5;
        animation: float 8s infinite linear;
        z-index: 0;
        pointer-events: none;
    }
    
    @keyframes float {
        0% { transform: translateY(100vh) scale(0.5); opacity: 0; }
        20% { opacity: 0.6; }
        100% { transform: translateY(-10vh) scale(1.2); opacity: 0; }
    }
</style>

<div class="heart-bg" style="left: 10%; animation-delay: 0s;">❤️</div>
<div class="heart-bg" style="left: 30%; animation-delay: 2s;">💕</div>
<div class="heart-bg" style="left: 50%; animation-delay: 4s;">🌸</div>
<div class="heart-bg" style="left: 70%; animation-delay: 1s;">❤️</div>
<div class="heart-bg" style="left: 90%; animation-delay: 3s;">✨</div>
""", unsafe_allow_html=True)

# ==========================================
# FUNCIONES AUXILIARES
# ==========================================
def mostrar_contador():
    """Calcula y muestra el tiempo desde la fecha de inicio"""
    ahora = datetime.datetime.now()
    diferencia = ahora - FECHA_INICIO
    dias = diferencia.days
    horas, resto = divmod(diferencia.seconds, 3600)
    minutos, _ = divmod(resto, 60)
    st.markdown(f"<div class='counter'>⏳ Tiempo siendo el más feliz: {dias} días, {horas} horas y {minutos} minutos.</div>", unsafe_allow_html=True)

def reproducir_musica():
    """Muestra el reproductor de música opcional si hay una URL"""
    if URL_MUSICA:
        with st.expander("🎵 Activar música romántica"):
            st.audio(URL_MUSICA, format='audio/mp3')

# ==========================================
# LÓGICA DE PANTALLAS
# ==========================================

# CONTENEDOR PRINCIPAL SIMULANDO LA TARJETA
st.markdown('<div class="card">', unsafe_allow_html=True)

mostrar_contador()
reproducir_musica()

# ---------------------------------
# PANTALLA 1: La Pregunta
# ---------------------------------
if st.session_state.page == 1:
    st.markdown(f'<img src="{URL_FOTO}" class="profile-pic">', unsafe_allow_html=True)
    st.markdown("<h1>🌸 Mi reina 🌸</h1>", unsafe_allow_html=True)
    st.markdown("<h3>¿Quieres salir conmigo este fin de semana? ❤️</h3>", unsafe_allow_html=True)
    
    st.write("") # Espacio
    
    col1, col2 = st.columns(2)
    
    # Botón SÍ (Nativo de Streamlit)
    with col1:
        if st.button("Sí ❤️", use_container_width=True):
            set_page(2)
            st.rerun()

    # Botón NO (HTML/JS Personalizado para que escape)
    with col2:
        # Usamos un componente iframe para inyectar JS puro que esquive el mouse
        components.html("""
            <style>
                #btn-no {
                    background-color: #f1f3f5;
                    color: #495057;
                    border-radius: 25px;
                    border: 1px solid #ced4da;
                    padding: 10px 24px;
                    font-size: 16px;
                    font-weight: 600;
                    font-family: 'Poppins', sans-serif;
                    cursor: pointer;
                    position: absolute;
                    transition: top 0.15s ease, left 0.15s ease;
                    width: 100%;
                    box-sizing: border-box;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                }
                body { margin: 0; padding: 0; overflow: hidden; height: 150px; position: relative;}
            </style>
            <button id="btn-no" onmouseover="escapar()">No 🙄</button>
            <script>
                function escapar() {
                    const btn = document.getElementById("btn-no");
                    // Cambia la posición aleatoriamente dentro del iframe
                    const newX = Math.random() * 60; // Hasta 60% del ancho
                    const newY = Math.random() * 80; // Hasta 80% del alto
                    btn.style.width = "auto";
                    btn.style.left = newX + "%";
                    btn.style.top = newY + "%";
                }
            </script>
        """, height=150)

# ---------------------------------
# PANTALLA 2: Aceptación
# ---------------------------------
