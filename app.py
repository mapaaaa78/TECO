
import streamlit as st
from datetime import date

st.set_page_config(page_title="TECO", page_icon="♻️", layout="centered")

GREEN = "#16833B"
LIGHT = "#EAF6E8"
DARK = "#102018"

st.markdown("""
<style>
.stApp {background:#eef1ed;}

/* Mobile canvas: style the page itself so all Streamlit widgets remain visible. */
.block-container {
    max-width:430px !important;
    background:white;
    border:8px solid #111;
    border-radius:36px;
    padding:28px 20px 92px 20px !important;
    box-shadow:0 8px 28px #0002;
    min-height:760px;
    margin-top:18px;
    margin-bottom:18px;
}
header[data-testid="stHeader"] {background:transparent;}
[data-testid="stAppViewContainer"] {background:#eef1ed;}
.phone-start {display:none;}
h1,h2,h3 {color:#102018;}
.stButton>button {
    width:100%; border-radius:12px; min-height:44px; font-weight:650;
}
.stButton>button[kind="primary"] {background:#16833B; border-color:#16833B;}
.card {background:#F3F8F1;border:1px solid #e1eadf;padding:14px;border-radius:16px;margin:8px 0;}
.hero {text-align:center;padding:35px 4px 22px;}
.logo {font-size:74px;line-height:1}
.brand {font-size:42px;font-weight:800;color:#16833B}
.muted {color:#5f6f65;font-size:.92rem}
.tag {display:inline-block;background:#e7f4e5;color:#176c35;border-radius:999px;padding:5px 10px;margin:3px;font-size:.8rem}
.step {display:flex;gap:10px;align-items:flex-start;margin:12px 0}
.num {background:#16833B;color:white;border-radius:50%;min-width:28px;height:28px;text-align:center;padding-top:3px;font-weight:700}
.bottom {position:fixed;left:50%;transform:translateX(-50%);bottom:8px;background:white;border:1px solid #ddd;
        width:min(410px,94vw);padding:7px;border-radius:18px;z-index:999;box-shadow:0 4px 18px #0002}
</style>
""", unsafe_allow_html=True)

if "screen" not in st.session_state: st.session_state.screen = 1
if "device" not in st.session_state: st.session_state.device = "Computador portátil"
if "logged" not in st.session_state: st.session_state.logged = False
if "request_code" not in st.session_state: st.session_state.request_code = "TECO-2026-001"

def go(n):
    st.session_state.screen = n
    st.rerun()

def phone():
    st.markdown('<div class="phone-start"></div>', unsafe_allow_html=True)

def title(t, sub=None):
    st.markdown(f"## {t}")
    if sub: st.markdown(f'<div class="muted">{sub}</div>', unsafe_allow_html=True)

def card(html):
    st.markdown(f'<div class="card">{html}</div>', unsafe_allow_html=True)

def back(n):
    if st.button("← Atrás"):
        go(n)

def nav():
    st.markdown('<div class="bottom">', unsafe_allow_html=True)
    cols=st.columns(5)
    items=[("🏠","Inicio",9),("📱","Dispositivos",33),("📍","Mapa",31),("💬","Asistente",32),("👤","Perfil",36)]
    for c,(ic,lab,n) in zip(cols,items):
        with c:
            if st.button(f"{ic}\n{lab}", key=f"nav{n}"): go(n)
    st.markdown('</div>', unsafe_allow_html=True)

s=st.session_state.screen
phone()

# 1–10
if s==1:
    st.markdown('<div class="hero"><div class="logo">♻️</div><div class="brand">TECO</div><h3>Dale un mejor destino<br>a tus electrónicos</h3><p>Identifica · Reutiliza · Repara · Recicla</p></div>', unsafe_allow_html=True)
    if st.button("Entrar a TECO", type="primary"): go(2)

elif s==2:
    title("¿Tienes un dispositivo que ya no usas?","Te ayudamos a descubrir qué puedes hacer con él y dónde llevarlo.")
    st.markdown("<div class='hero'><div class='logo'>💻📱🎧</div></div>",unsafe_allow_html=True)
    if st.button("Comenzar",type="primary"): go(3)
    if st.button("Ya tengo una cuenta"): go(8)

elif s==3:
    title("Identifica tu dispositivo","Toma una fotografía o busca el dispositivo manualmente y TECO te ayudará a identificarlo.")
    st.markdown("<div class='hero'><div class='logo'>📷</div><h2>📱 → ♻️</h2></div>",unsafe_allow_html=True)
    if st.button("Siguiente",type="primary"): go(4)
    if st.button("Omitir"): go(6)

elif s==4:
    title("Descubre qué hacer con él","Conoce si puede repararse, reutilizarse, reciclarse o si requiere una disposición especial.")
    c1,c2=st.columns(2)
    for c,x in [(c1,"🔧 Reparar"),(c2,"🔄 Reutilizar"),(c1,"♻️ Reciclar"),(c2,"🗑️ Disposición adecuada")]:
        with c: card(f"<b>{x}</b>")
    c1,c2=st.columns(2)
    with c1:
        if st.button("Atrás"): go(3)
    with c2:
        if st.button("Siguiente",type="primary"): go(5)

elif s==5:
    title("Encuentra la mejor alternativa cerca de ti","Consulta puntos de recolección, recicladores autorizados, puntos móviles o solicita una recolección.")
    st.markdown("<div class='hero'><div class='logo'>🗺️</div><p>📍 Puntos de recolección<br>♻️ Recicladores autorizados<br>🚚 Puntos móviles<br>🏠 Recolección a domicilio</p></div>",unsafe_allow_html=True)
    if st.button("Empezar",type="primary"): go(6)

elif s==6:
    title("¿Nos permites conocer tu ubicación?","La utilizaremos para mostrarte opciones de reciclaje cercanas.")
    st.markdown("<div class='hero'><div class='logo'>📍</div></div>",unsafe_allow_html=True)
    if st.button("Permitir ubicación",type="primary"): go(7)
    if st.button("Ahora no"): go(7)
    st.text_input("O escribe tu ciudad, barrio o dirección de referencia")

elif s==7:
    title("TECO puede ayudarte a identificar tu dispositivo mediante una fotografía.")
    st.markdown("<div class='hero'><div class='logo'>📷</div></div>",unsafe_allow_html=True)
    if st.button("Permitir cámara",type="primary"): go(8)
    if st.button("Lo haré después"): go(8)
    st.caption("Tus fotos se usan solo para identificar el dispositivo dentro de este prototipo.")

elif s==8:
    title("Guarda tus dispositivos y solicitudes")
    st.markdown("<div class='hero'><div class='logo'>👤♻️</div></div>",unsafe_allow_html=True)
    if st.button("Crear cuenta",type="primary"):
        st.session_state.logged=True; go(9)
    if st.button("Iniciar sesión"):
        st.session_state.logged=True; go(9)
    if st.button("Continuar como invitado"): go(9)

elif s==9:
    st.markdown("<h2 style='color:#16833B'>TECO</h2>",unsafe_allow_html=True)
    title("Hola 👋","¿Qué dispositivo quieres gestionar hoy?")
    st.text_input("Buscar",placeholder="Busca celular, computador, audífonos...")
    if st.button("📷 Identificar con una foto",type="primary"): go(10)
    c1,c2=st.columns(2)
    with c1:
        if st.button("🔎 Buscar dispositivo"): go(30)
        if st.button("🚚 Solicitar recolección"): go(21)
    with c2:
        if st.button("📍 Puntos cercanos"): go(31)
        if st.button("💬 Preguntar al asistente"): go(32)
    card("<b>💡 ¿Sabías que...?</b><br>Muchos materiales de tus electrónicos pueden recuperarse.")
    if st.button("Aprende sobre residuos electrónicos"): go(35)
    nav()

elif s==10:
    title("Identificar dispositivo","Ubica el dispositivo dentro del recuadro.")
    pic=st.camera_input("Toma una foto")
    if pic is not None:
        st.session_state.photo=True
        if st.button("Usar esta foto",type="primary"): go(11)
    if st.button("Buscar manualmente"): go(30)
    if st.button("Cancelar"): go(9)

# 11–20
elif s==11:
    title("Confirma la foto","¿La imagen se ve correctamente?")
    st.markdown("<div class='hero'><div class='logo'>💻</div></div>",unsafe_allow_html=True)
    if st.button("Usar esta foto",type="primary"): go(12)
    if st.button("Tomar otra foto"): go(10)

elif s==12:
    title("Estamos identificando tu dispositivo…")
    st.progress(82)
    for x in ["✓ Analizando imagen","✓ Identificando tipo de dispositivo","✓ Consultando base de datos","◌ Buscando recomendaciones"]:
        st.write(x)
    if st.button("Continuar",type="primary"): go(13)

elif s==13:
    title("Dispositivo identificado")
    st.markdown("<div class='hero'><div class='logo'>💻</div></div>",unsafe_allow_html=True)
    card("Creemos que es:<br><b>Computador portátil</b><br>Marca: Dell · Categoría: Computadores")
    st.write("### ¿Es correcto?")
    if st.button("Sí, continuar",type="primary"):
        st.session_state.device="Computador portátil"; go(15)
    if st.button("No, cambiar dispositivo"): go(14)

elif s==14:
    title("Selecciona tu dispositivo")
    q=st.text_input("Buscar",placeholder="Escribe el nombre del dispositivo...")
    cats=["📱 Celulares","💻 Computadores","▣ Tablets","🎧 Audio","🔌 Cables y cargadores","🖨️ Electrónicos pequeños","🖱️ Periféricos","••• Otro"]
    cols=st.columns(2)
    for i,x in enumerate(cats):
        with cols[i%2]:
            if st.button(x,key=x):
                st.session_state.device=x.split(" ",1)[-1]; go(15)

elif s==15:
    title("Cuéntanos sobre tu dispositivo",st.session_state.device)
    st.radio("1. ¿El dispositivo todavía funciona?",["Sí, funciona","Funciona parcialmente","No funciona","No estoy seguro"])
    st.selectbox("2. ¿Por qué dejaste de utilizarlo?",["Compré uno nuevo","Se dañó","Está muy viejo","Ya no lo necesito","Otro"])
    st.selectbox("3. ¿Presenta algún daño visible?",["No","Pantalla/carcasa","Batería","Cable o conexión","Otro","No sé"])
    if st.button("Ver recomendación",type="primary"): go(16)

elif s==16:
    title("Tu recomendación",st.session_state.device)
    card("<div style='text-align:center;font-size:38px'>🔄</div><h2 style='text-align:center;color:#16833B'>Reutilizar</h2><p>Tu dispositivo todavía puede tener una segunda vida.</p>")
    st.write("**¿Por qué esta recomendación?**")
    st.write("Según la información registrada, el equipo aún puede ser útil para otra persona o para otros usos.")
    if st.button("Ver paso a paso",type="primary"): go(17)
    if st.button("Encontrar dónde llevarlo"): go(18)
    if st.button("Tengo una pregunta"): go(32)

elif s==17:
    title("Paso a paso: prepara tu dispositivo")
    steps=["Realiza un respaldo de tu información.","Elimina tus datos personales.","Retira accesorios cuando corresponda.","Si tiene daños, evita manipular componentes internos.","Selecciona una alternativa de entrega."]
    for i,x in enumerate(steps,1):
        st.markdown(f"<div class='step'><span class='num'>{i}</span><span>{x}</span></div>",unsafe_allow_html=True)
    if st.button("Ya preparé mi dispositivo",type="primary"): go(18)

elif s==18:
    title("¿Cómo prefieres entregarlo?",st.session_state.device)
    c1,c2=st.columns(2)
    with c1:
        if st.button("📍 Llevarlo a un punto cercano"): go(19)
        if st.button("♻️ Buscar reciclador autorizado"): go(27)
    with c2:
        if st.button("🚚 Solicitar recolección a domicilio"): go(21)
        if st.button("🚐 Consultar punto móvil"): go(29)

elif s==19:
    title("Puntos de recolección cerca de ti")
    st.text_input("Buscar zona o dirección")
    st.markdown("<div class='hero'><div class='logo'>🗺️</div><h3>📍  📍  🔵  📍</h3></div>",unsafe_allow_html=True)
    card("<b>Punto Verde UniSabana</b><br>0,8 km · Abierto<br>Recibe: computadores, celulares, tablets")
    if st.button("Ver Punto Verde UniSabana",type="primary"): go(20)
    card("<b>EcoPunto Colina</b><br>2,1 km · Abierto<br>Recibe: electrónicos pequeños, cables")

elif s==20:
    title("Punto Verde UniSabana","0,8 km · Abierto")
    card("📍 Campus Universidad de La Sabana, Chía<br>🕒 Lun–Vie: 7:00 a.m.–6:00 p.m.<br><br><b>Tipos que recibe:</b><br>✓ Computadores<br>✓ Celulares<br>✓ Tablets<br>✓ Accesorios<br>✓ Electrónicos pequeños")
    st.success(f"Sí reciben tu dispositivo: {st.session_state.device}")
    if st.button("Cómo llegar",type="primary"): st.info("En el prototipo, este botón abriría la aplicación de mapas.")
    if st.button("Solicitar recolección"): go(21)
    back(19)

# 21–30
elif s==21:
    title("Solicitar recolección a domicilio")
    card(f"<b>{st.session_state.device}</b><br>1 unidad")
    if st.button("+ Agregar otro dispositivo"): go(30)
    card("🚚 Recogemos tus dispositivos y los entregamos a gestores autorizados.")
    if st.button("Continuar",type="primary"): go(22)

elif s==22:
    title("Dirección de recolección")
    st.text_input("Dirección *",value="Calle 123 # 45 - 67")
    st.text_input("Apartamento / Oficina",value="Apto 401")
    st.text_input("Barrio *",value="La Colina")
    st.text_input("Ciudad *",value="Bogotá")
    st.text_input("Referencia (opcional)",value="Torre 2, recepción")
    if st.button("Continuar",type="primary"): go(23)

elif s==23:
    title("Selecciona la fecha de recolección")
    st.date_input("Fecha",value=date(2026,9,30))
    st.radio("Horarios disponibles",["8:00 a.m. – 10:00 a.m.","10:00 a.m. – 12:00 m.","2:00 p.m. – 4:00 p.m.","4:00 p.m. – 6:00 p.m."])
    if st.button("Continuar",type="primary"): go(24)

elif s==24:
    title("Confirma tu solicitud")
    card(f"<b>Dispositivo</b><br>{st.session_state.device} · 1 unidad")
    card("<b>Dirección</b><br>Calle 123 #45-67 · Bogotá")
    card("<b>Fecha y horario</b><br>30 de septiembre de 2026 · 8:00–10:00 a.m.")
    card("<b>Operador asignado</b><br>Gestor autorizado TECO")
    if st.button("Confirmar recolección",type="primary"): go(25)
    if st.button("Editar datos"): go(22)

elif s==25:
    st.markdown("<div class='hero'><div class='logo'>✅</div><h1>¡Solicitud registrada!</h1><p>Tu recolección ha sido programada exitosamente.</p></div>",unsafe_allow_html=True)
    card(f"<b>Código:</b> {st.session_state.request_code}<br>📅 30 sep. 2026 · 8:00–10:00 a.m.<br>📍 Bogotá<br>💻 1 dispositivo")
    if st.button("Ver seguimiento",type="primary"): go(26)
    if st.button("Volver al inicio"): go(9)

elif s==26:
    title("Seguimiento de tu recolección",f"Código: {st.session_state.request_code}")
    for x in ["✅ Solicitud recibida","✅ Recolección asignada","🚚 En camino","◯ Dispositivo recogido","◯ Entregado al gestor"]:
        card(x)
    if st.button("Volver al inicio",type="primary"): go(9)

elif s==27:
    title("Recicladores autorizados cerca de ti")
    st.text_input("Buscar recicladores")
    recyclers=[("Gestor Verde","0,8 km · Chía"),("Reciclaje Andino","2,1 km · Usaquén"),("Cierra el Ciclo","3,4 km · Suba")]
    for i,(a,b) in enumerate(recyclers):
        card(f"♻️ <b>{a}</b><br>{b}<br>Recibe: computadores, celulares, cables")
        if st.button(f"Ver {a}",key=f"r{i}"): go(28)

elif s==28:
    title("Gestor Verde","Reciclador autorizado · 0,8 km")
    card("📍 Zona norte<br>🕒 Lun–Vie: 8:00 a.m.–5:00 p.m.<br><br><b>Dispositivos que reciben</b><br>✓ Computadores<br>✓ Celulares<br>✓ Tablets<br>✓ Cables y cargadores<br>✓ Periféricos")
    if st.button("Llevar dispositivo",type="primary"): go(19)
    if st.button("Solicitar recolección"): go(21)
    if st.button("Contactar"): st.info("En una versión real aquí se abriría el canal de contacto.")

elif s==29:
    title("Puntos móviles próximos")
    for a,b in [("Parque La Colina","Mié. 30 sep. · 9:00 a.m.–1:00 p.m."),("Centro Comercial","Sáb. 3 oct. · 10:00 a.m.–4:00 p.m."),("Universidad","Mar. 6 oct. · 8:00 a.m.–2:00 p.m.")]:
        card(f"🚐 <b>{a}</b><br>📅 {b}")
    if st.button("Ver en el mapa",type="primary"): go(19)

elif s==30:
    title("Busca tu dispositivo")
    q=st.text_input("Buscar",value="audífonos")
    for x in ["🎧 Audífonos inalámbricos","🎧 Audífonos con cable","🎧 Audífonos gaming","🎧 Audífonos de diadema","🎧 Audífonos deportivos"]:
        if st.button(x,key=x):
            st.session_state.device=x.split(" ",1)[-1]; go(15)
    if st.button("Explorar todas las categorías"): go(14)

# 31–40
elif s==31:
    title("¿Qué quieres reciclar?","Selecciona un dispositivo para ver los puntos que lo reciben o explora todos.")
    cats=["Todos","Celulares","Computadores","Tablets","Audio","Cables y cargadores","Electrónicos pequeños","Periféricos","Otro"]
    cols=st.columns(3)
    for i,x in enumerate(cats):
        with cols[i%3]:
            if st.button(x,key=f"m{x}"): st.session_state.device=x
    if st.button("Ver puntos en el mapa",type="primary"): go(19)
    nav()

elif s==32:
    title("🤖 Asistente TECO","En línea · 24/7")
    card("¡Hola! 👋<br>Soy tu asistente de TECO. Puedo ayudarte con dudas sobre dispositivos electrónicos, reciclaje, reutilización y dónde llevar tus equipos.")
    for q in ["¿Qué hago con un celular que no prende?","¿Dónde puedo reciclar un computador?","¿Puedo reciclar audífonos?","¿Qué hago con una batería dañada?"]:
        if st.button(q,key=q):
            st.session_state.question=q; go(34)
    st.chat_input("Escribe tu pregunta...")
    nav()

elif s==33:
    title("Conversación con asistente")
    st.chat_message("user").write("Tengo un computador viejo pero todavía funciona, ¿qué puedo hacer?")
    st.chat_message("assistant").write("Si todavía funciona, una alternativa es reutilizarlo: donarlo, venderlo o entregarlo a un programa de reacondicionamiento.")
    if st.button("Ver opciones de reutilización",type="primary"): go(16)
    if st.button("Buscar puntos cercanos"): go(19)
    if st.button("Solicitar recolección"): go(21)
    nav()

elif s==34:
    title("Respuesta del asistente")
    q=st.session_state.get("question","¿Dónde puedo reciclar mi celular?")
    st.chat_message("user").write(q)
    st.chat_message("assistant").write("Puedo ayudarte. TECO puede mostrarte puntos compatibles cercanos y alternativas de entrega según el dispositivo.")
    if st.button("Ver puntos cercanos",type="primary"): go(19)
    if st.button("Evaluar mi dispositivo"): go(15)
    nav()

elif s==35:
    title("Aprende con TECO","Información clara para tomar mejores decisiones.")
    topics=["🌿 ¿Qué son los residuos electrónicos?","📱 ¿Qué aparatos pueden reciclarse?","♻️ ¿Qué materiales se pueden recuperar?","⚠️ ¿Por qué no deben ir a la basura común?","🔧 Reparar antes de reemplazar","🔄 Reutilizar: una segunda vida"]
    for x in topics: card(f"<b>{x}</b>")
    nav()

elif s==36:
    title("Perfil")
    card("👤 <b>Usuario TECO</b><br>usuario@teco.app")
    opts=[("Mis datos",36),("Mis dispositivos",33),("Mis solicitudes",37),("Ubicación",38),("Permisos",36),("Notificaciones",39),("Ayuda",32),("Acerca de TECO",35)]
    for x,n in opts:
        if st.button(x,key=f"p{x}"): go(n)
    if st.button("Cerrar sesión"): go(2)
    nav()

elif s==37:
    title("Mis solicitudes")
    card(f"📅 <b>{st.session_state.request_code}</b><br>Recolección a domicilio<br>30 sep. 2026 · 8:00–10:00 a.m. · Programada")
    card("📅 <b>TECO-2026-000</b><br>Punto Verde · Finalizada")
    if st.button("Ver seguimiento",type="primary"): go(26)
    nav()

elif s==38:
    title("Mi ubicación")
    st.radio("Cómo quieres definirla",["Usar mi ubicación actual","Ingresar manualmente"])
    st.selectbox("Ciudad",["Bogotá","Chía","Cajicá","Otra"])
    st.text_input("Barrio",value="La Colina")
    st.text_input("Dirección de referencia",value="Calle 123 #45-67")
    if st.button("Guardar cambios",type="primary"): st.success("Ubicación guardada.")
    nav()

elif s==39:
    title("Notificaciones")
    card("🚚 <b>Tu recolección está en camino</b><br>Llegaremos aproximadamente en 20 minutos.")
    card("📍 <b>Nuevo punto de recolección cerca de ti</b><br>Hay una nueva alternativa disponible.")
    card("💡 <b>Consejo de la semana</b><br>Antes de entregar un dispositivo, elimina tu información personal.")
    card("✅ <b>Tu solicitud ha sido confirmada</b>")
    nav()

elif s==40:
    st.markdown("<div class='hero'><div class='logo'>🌎</div><h1>¡Gracias por ser parte del cambio!</h1><p>Cada dispositivo que gestionas contribuye a una disposición más responsable.</p></div>",unsafe_allow_html=True)
    c1,c2,c3=st.columns(3)
    c1.metric("Dispositivos","3")
    c2.metric("Material","12 kg*")
    c3.metric("CO₂","25 kg*")
    st.caption("*Valores ilustrativos para el prototipo; no son métricas ambientales validadas.")
    if st.button("Gestionar otro dispositivo",type="primary"): go(9)
    if st.button("Volver al inicio"): go(9)
    nav()

else:
    go(1)
