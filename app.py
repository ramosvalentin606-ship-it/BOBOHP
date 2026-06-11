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

    /* Fondo general */
    .stApp {
        background: linear-gradient(135deg, #ffe6ea 0%, #fdfbfb 100%);
        font-family: 'Poppins', sans-serif;
    }

    /* Tarjetas blancas con sombra */
    .card {
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(255, 182, 193, 0.3);
        backdrop-filter: blur(10px);
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.5);
    }

    /* Estilo de los textos */
    h1, h2, h3, p {
        color: #6a4c70; /* Morado suave/oscuro */
        text-align: center;
    }

    /* Imagen circular */
    .profile-pic {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
        border: 4px solid #ffb6c1;
        box-shadow: 0 4px 15px rgba(255, 182, 193, 0.5);
        display: block;
        margin: 0 auto;
    }

    /* Estilo general para los botones nativos de Streamlit */
    div.stButton > button:first-child {
        background-color: #ff9a9e;
        color: white;
        border-radius: 25px;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(255, 154, 158, 0.4);
        width: 100%;
    }

    div.stButton > button:first-child:hover {
        background-color: #ff758c;
        transform: translateY(-2px);
        color: white;
        box-shadow: 0 6px 15px rgba(255, 117, 140, 0.5);
        border: none;
    }

    /* Contador de tiempo */
    .counter {
        font-size: 14px;
        color: #ff758c;
        text-align: center;
        margin-bottom: 20px;
        font-weight: 600;
    }

    /* Animación de corazones flotantes */
    .heart-bg {
        position: fixed;
        font-size: 20px;
        color: #ff758c;
        opacity: 0.4;
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
                    color: #6c757d;
                    border-radius: 25px;
                    border: 1px solid #dee2e6;
                    padding: 10px 24px;
                    font-size: 16px;
                    font-weight: 600;
                    font-family: 'Poppins', sans-serif;
                    cursor: pointer;
                    position: absolute;
                    transition: top 0.15s ease, left 0.15s ease;
                    width: 100%;
                    box-sizing: border-box;
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
elif st.session_state.page == 2:
    st.balloons() # Animación de confeti/globos
    st.markdown("<h1>🥹 ¿De verdad dijiste que sí?</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Sabía que tenía una oportunidad contigo ❤️</h3>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc29lYWZ5NmZ5M2x3ZGExMzhzYnQwbmt6N3ZqZWx3YmR6aW9wN2I4biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Vz58J8shFW6BvqnYTm/giphy.gif", use_container_width=True) # GIF lindo opcional
    
    st.write("")
    if st.button("Continuar ✨", use_container_width=True):
        set_page(3)
        st.rerun()

# ---------------------------------
# PANTALLA 3: Fecha y Hora
# ---------------------------------
elif st.session_state.page == 3:
    st.markdown("<h1>📅 Ahora elige el día</h1>", unsafe_allow_html=True)
    st.write("Dime cuándo estás libre para mí:")
    
    col_fecha, col_hora = st.columns(2)
    with col_fecha:
        fecha = st.date_input("Día de la cita")
    with col_hora:
        hora = st.time_input("Hora de la cita")
        
    st.write("")
    if st.button("Reservar cita ❤️", use_container_width=True):
        if fecha and hora:
            st.session_state.selected_date = fecha
            st.session_state.selected_time = hora
            set_page(4)
            st.rerun()
        else:
            st.error("Por favor, completa la fecha y la hora mi amor.")

# ---------------------------------
# PANTALLA 4: Elección del Plan
# ---------------------------------
elif st.session_state.page == 4:
    st.markdown("<h1>🍽️ ¿Qué te provoca?</h1>", unsafe_allow_html=True)
    
    planes = [
        "🍔 Hamburguesa", "🍕 Pizza", "🍣 Sushi", 
        "🌮 Tacos", "🍦 Helado", "☕ Café", 
        "🎬 Cine", "🌳 Picnic", "🎁 Sorpresa"
    ]
    
    # Grid de botones (3x3)
    cols = st.columns(3)
    for i, plan in enumerate(planes):
        with cols[i % 3]:
            # Resaltar si ya está seleccionado
            is_selected = st.session_state.selected_plan == plan
            button_type = "primary" if is_selected else "secondary"
            
            if st.button(plan, use_container_width=True, type=button_type, key=f"plan_{i}"):
                st.session_state.selected_plan = plan
                st.rerun()
                
    if st.session_state.selected_plan:
        st.success(f"¡Excelente elección! Vamos por: **{st.session_state.selected_plan}**")
        
    st.write("")
    if st.button("Continuar ✨", use_container_width=True):
        if st.session_state.selected_plan:
            set_page(5)
            st.rerun()
        else:
            st.warning("Elige un plan primero 🥺")

# ---------------------------------
# PANTALLA 5: Razones
# ---------------------------------
elif st.session_state.page == 5:
    st.markdown("<h1>❤️ Antes de terminar...</h1>", unsafe_allow_html=True)
    
    razones = [
        "Porque me haces sonreír todos los días.",
        "Porque siempre me apoyas en todo.",
        "Porque eres la mujer más hermosa.",
        "Porque haces mejores mis días grises.",
        "Porque contigo todo es más divertido y espontáneo.",
        "Porque eres una persona increíble y admiro cómo eres.",
        "Porque me encanta escucharte hablar por horas.",
        "Porque me haces sentir el hombre más afortunado del mundo."
    ]
    
    if st.button("Razón aleatoria por la que me gustas 🥰", use_container_width=True):
        st.session_state.reason = random.choice(razones)
        
    if st.session_state.reason:
        st.info(f"✨ **{st.session_state.reason}**")
        
    st.write("")
    if st.button("Ver sorpresa final 🎁", use_container_width=True):
        set_page(6)
        st.rerun()

# ---------------------------------
# PANTALLA 6: Final (Resumen)
# ---------------------------------
elif st.session_state.page == 6:
    st.balloons()
    st.markdown("<h1>Perfecto mi reina ❤️</h1>", unsafe_allow_html=True)
    
    st.markdown("### 💌 Resumen de nuestra cita:")
    st.success(f"**📅 Fecha:** {st.session_state.selected_date.strftime('%d de %B, %Y')}")
    st.success(f"**⏰ Hora:** {st.session_state.selected_time.strftime('%I:%M %p')}")
    st.success(f"**💖 Plan:** {st.session_state.selected_plan}")
    
    st.markdown("""
    <div style='background-color: #fff0f3; padding: 20px; border-radius: 15px; border-left: 5px solid #ff758c; margin-top: 20px; margin-bottom: 20px;'>
        <p style='font-size: 16px; font-weight: 400; text-align: left;'>
        Gracias por aguantar a este hombre que a veces parece más frío de lo que realmente es.<br><br>
        Puede que no siempre encuentre las palabras más tiernas, pero quiero que sepas que te quiero muchísimo y que me haces muy feliz.<br><br>
        <b>Ahora prepárate porque tenemos una cita pendiente ❤️</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Reiniciar experiencia 🔄", use_container_width=True):
        # Limpiar el estado y volver al inicio
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # Cierra el div class="card"
