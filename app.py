import streamlit as st
import requests
import os
from datetime import datetime

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Burhani Electricals",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
/* Hide Streamlit chrome */
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { visibility: hidden; }
.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    max-width: 100% !important;
}
section[data-testid="stSidebar"] { display: none; }

/* Global font */
html, body, [class*="css"] {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}

/* ── Navbar ── */
.navbar {
    background: #ffffff;
    border-bottom: 1px solid #e2e8f0;
    padding: 0 40px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 999;
    box-shadow: 0 1px 8px rgba(0,0,0,0.06);
}
.navbar-brand {
    font-size: 1.3rem;
    font-weight: 900;
    color: #0f172a;
    text-decoration: none;
}
.navbar-brand span { color: #0284c7; }
.navbar-links {
    display: flex;
    gap: 28px;
    align-items: center;
}
.navbar-links a {
    text-decoration: none;
    color: #475569;
    font-weight: 600;
    font-size: 0.88rem;
    transition: color 0.2s;
}
.navbar-links a:hover { color: #0284c7; }
.nav-call {
    background: #0284c7;
    color: #ffffff !important;
    padding: 8px 20px;
    border-radius: 8px;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
}

/* ── Hero ── */
.hero-wrap {
    background: linear-gradient(135deg, #dbeafe 0%, #f0f9ff 60%, #e0f2fe 100%);
    text-align: center;
    padding: 72px 20px 90px;
    position: relative;
}
.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.9);
    border: 1px solid #bae6fd;
    color: #0369a1;
    font-weight: 700;
    font-size: 0.82rem;
    padding: 6px 18px;
    border-radius: 999px;
    margin-bottom: 20px;
    letter-spacing: 0.03em;
}
.hero-title {
    font-size: clamp(2.2rem, 5vw, 3.8rem);
    font-weight: 900;
    color: #0c1a2e;
    margin: 0 0 16px;
    line-height: 1.1;
}
.hero-title span { color: #0284c7; }
.hero-sub {
    font-size: 1.1rem;
    color: #334155;
    max-width: 580px;
    margin: 0 auto 36px;
    line-height: 1.75;
    font-weight: 500;
}
.hero-btns {
    display: flex;
    gap: 14px;
    justify-content: center;
    flex-wrap: wrap;
}
.btn-primary {
    background: #0284c7;
    color: #fff;
    padding: 14px 34px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 1rem;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    box-shadow: 0 4px 14px rgba(2,132,199,0.35);
    transition: background 0.2s, transform 0.15s;
}
.btn-primary:hover {
    background: #0369a1;
    color: #fff;
    transform: translateY(-2px);
}
.btn-outline {
    background: #fff;
    color: #0369a1;
    padding: 14px 34px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 1rem;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    border: 2px solid #93c5fd;
    transition: background 0.2s, transform 0.15s;
}
.btn-outline:hover {
    background: #eff6ff;
    color: #0369a1;
    transform: translateY(-2px);
}

/* ── Section wrappers ── */
.sec-light  { background: #f8fafc; padding: 64px 40px; }
.sec-white  { background: #ffffff; padding: 64px 40px; }
.sec-blue   { background: linear-gradient(135deg, #0284c7, #0369a1); padding: 60px 40px; }

/* ── Section heading ── */
.sec-label {
    display: block;
    color: #0284c7;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 6px;
    text-align: center;
}
.sec-title {
    font-size: clamp(1.6rem, 3vw, 2.3rem);
    font-weight: 900;
    color: #0f172a;
    margin: 0 0 10px;
    text-align: center;
}
.sec-desc {
    color: #64748b;
    font-size: 0.97rem;
    max-width: 540px;
    margin: 0 auto 36px;
    text-align: center;
    line-height: 1.7;
}

/* ── Service Cards ── */
.svc-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 28px 24px;
    height: 100%;
    transition: transform 0.25s, box-shadow 0.25s;
}
.svc-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 18px 40px rgba(0,0,0,0.10);
}
.svc-icon {
    font-size: 2.2rem;
    margin-bottom: 14px;
    display: block;
}
.svc-card h3 {
    font-size: 1.05rem;
    font-weight: 800;
    color: #0f172a;
    margin: 0 0 10px;
}
.svc-card p {
    font-size: 0.87rem;
    color: #64748b;
    line-height: 1.7;
    margin: 0 0 18px;
}
.svc-tag {
    font-size: 0.78rem;
    font-weight: 700;
    color: #0284c7;
    background: #e0f2fe;
    padding: 4px 12px;
    border-radius: 999px;
    display: inline-block;
}

/* ── Stat cards ── */
.stat-card {
    background: rgba(255,255,255,0.13);
    border-radius: 14px;
    padding: 28px 20px;
    text-align: center;
    color: #fff;
    height: 100%;
}
.stat-num {
    font-size: 2.6rem;
    font-weight: 900;
    line-height: 1;
    margin-bottom: 6px;
}
.stat-label {
    font-size: 0.85rem;
    font-weight: 600;
    color: #bae6fd;
}

/* ── Contact cards ── */
.con-card {
    background: #f0f9ff;
    border: 1px solid #bae6fd;
    border-radius: 14px;
    padding: 32px 20px;
    text-align: center;
    height: 100%;
    transition: box-shadow 0.25s, transform 0.25s;
}
.con-card:hover {
    box-shadow: 0 12px 30px rgba(2,132,199,0.12);
    transform: translateY(-3px);
}
.con-icon { font-size: 2.4rem; margin-bottom: 14px; display: block; }
.con-card h3 {
    font-size: 1rem;
    font-weight: 800;
    color: #0f172a;
    margin: 0 0 8px;
}
.con-card a {
    color: #0284c7;
    font-weight: 700;
    font-size: 1.05rem;
    text-decoration: none;
}
.con-card p { color: #475569; font-weight: 600; margin: 0; }

/* ── WhatsApp button ── */
.wa-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: #22c55e;
    color: #fff;
    padding: 16px 38px;
    border-radius: 12px;
    font-weight: 800;
    font-size: 1.05rem;
    text-decoration: none;
    box-shadow: 0 4px 18px rgba(34,197,94,0.38);
    transition: background 0.2s, transform 0.15s;
}
.wa-btn:hover { background: #16a34a; color: #fff; transform: translateY(-2px); }

/* ── Chat ── */
.chat-wrap {
    max-width: 660px;
    margin: 0 auto;
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(0,0,0,0.08);
}
.chat-head {
    background: linear-gradient(135deg, #4f46e5, #6d28d9);
    padding: 18px 22px;
    display: flex;
    align-items: center;
    gap: 14px;
    color: #fff;
}
.chat-head-text h4 { margin: 0; font-size: 1rem; font-weight: 700; }
.chat-head-text p  { margin: 0; font-size: 0.76rem; opacity: 0.82; }
.chat-body {
    padding: 16px;
    background: #f8fafc;
    min-height: 280px;
    max-height: 340px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.bubble-bot {
    align-self: flex-start;
    background: #fff;
    border: 1px solid #e2e8f0;
    color: #1e293b;
    padding: 10px 14px;
    border-radius: 14px 14px 14px 4px;
    max-width: 80%;
    font-size: 0.87rem;
    line-height: 1.6;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}
.bubble-user {
    align-self: flex-end;
    background: #4f46e5;
    color: #fff;
    padding: 10px 14px;
    border-radius: 14px 14px 4px 14px;
    max-width: 80%;
    font-size: 0.87rem;
    line-height: 1.6;
}
.chat-note {
    padding: 8px 16px;
    text-align: center;
    font-size: 0.72rem;
    color: #94a3b8;
    background: #fff;
    border-top: 1px solid #f1f5f9;
}

/* ── Streamlit form inputs ── */
div[data-testid="stTextInput"] > div > div > input {
    border-radius: 999px !important;
    border: 2px solid #e2e8f0 !important;
    padding: 10px 20px !important;
    font-size: 0.9rem !important;
}
div[data-testid="stTextInput"] > div > div > input:focus {
    border-color: #4f46e5 !important;
    box-shadow: 0 0 0 3px rgba(79,70,229,0.1) !important;
}
div[data-testid="stFormSubmitButton"] > button {
    background: #4f46e5 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 999px !important;
    font-weight: 700 !important;
    padding: 10px 26px !important;
    width: 100% !important;
    transition: background 0.2s !important;
}
div[data-testid="stFormSubmitButton"] > button:hover {
    background: #4338ca !important;
    color: #fff !important;
}

/* ── Footer ── */
.footer {
    background: #0f172a;
    color: #94a3b8;
    padding: 50px 40px 28px;
}
.footer-brand {
    font-size: 1.15rem;
    font-weight: 900;
    color: #fff;
    margin-bottom: 10px;
}
.footer-brand span { color: #38bdf8; }
.footer-desc { font-size: 0.83rem; line-height: 1.75; }
.footer h4 { color: #fff; font-weight: 700; margin: 0 0 14px; font-size: 0.95rem; }
.footer ul { list-style: none; padding: 0; margin: 0; }
.footer li { margin-bottom: 9px; }
.footer li a { color: #94a3b8; text-decoration: none; font-size: 0.83rem; }
.footer li a:hover { color: #38bdf8; }
.footer-bottom {
    border-top: 1px solid #1e293b;
    margin-top: 32px;
    padding-top: 20px;
    text-align: center;
    font-size: 0.78rem;
    color: #475569;
}

/* ── Floating call button ── */
.fab {
    position: fixed;
    bottom: 26px;
    right: 26px;
    z-index: 9999;
    background: #0284c7;
    color: #fff;
    padding: 12px 22px;
    border-radius: 999px;
    font-weight: 700;
    font-size: 0.88rem;
    text-decoration: none;
    box-shadow: 0 4px 18px rgba(2,132,199,0.45);
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: background 0.2s, transform 0.15s;
}
.fab:hover { background: #0369a1; color: #fff; transform: scale(1.04); }

/* Remove extra Streamlit padding between markdown blocks */
div[data-testid="stMarkdownContainer"] > div { margin: 0; padding: 0; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "bot", "text": "Hello! 👋 I'm the Burhani Electricals Assistant. Ask me about fan issues, mixer problems, or how we can help you!"}
    ]

# ─────────────────────────────────────────────
# GEMINI API
# ─────────────────────────────────────────────
def ask_gemini(user_msg: str) -> str:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = os.environ.get("GEMINI_API_KEY", "")

    if not api_key:
        return "Please contact Mr. Husain directly at ☎️ +91 8780514062 for assistance!"

    system = (
        'You are the friendly assistant for "Burhani Electricals" owned by '
        "Mr. Husain M Vankanerwala in Surat, India. "
        "Services: all fan types (Ceiling, Wall, Table, Pedestal, Stand, Tower, "
        "Exhaust, Mini Exhaust, Talvar, Farata, Lift), Mixer/Blender, Iron, Geyser repair. "
        "Always end by suggesting to call +91 8780514062. "
        "Keep answers short, friendly and helpful."
    )
    try:
        url = (
            "https://generativelanguage.googleapis.com/v1beta/"
            f"models/gemini-1.5-flash:generateContent?key={api_key}"
        )
        res = requests.post(
            url,
            json={
                "system_instruction": {"parts": [{"text": system}]},
                "contents": [{"parts": [{"text": user_msg}]}],
                "generationConfig": {"temperature": 0.7, "maxOutputTokens": 300},
            },
            timeout=12,
        )
        return res.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return "I'm having trouble right now. Please call Mr. Husain at +91 8780514062 directly!"

# ═══════════════════════════════════════════════════════════════
# NAVBAR
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="navbar">
    <span class="navbar-brand">⚡ Burhani <span>Electricals</span></span>
    <div class="navbar-links">
        <a href="#services">Services</a>
        <a href="#contact">Contact</a>
        <a href="#chat">AI Chat</a>
        <a href="tel:+918780514062" class="nav-call">📞 Call Now</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-wrap">
    <div class="hero-badge">⚡ Trusted Repair Service Since 2018</div>
    <h1 class="hero-title">Burhani <span>Electricals</span></h1>
    <p class="hero-sub">
        Expert rewinding &amp; repairing for all types of fans, mixers, irons
        &amp; geysers. Fast, reliable and affordable service in Surat.
    </p>
    <div class="hero-btns">
        <a href="tel:+918780514062" class="btn-primary">📞 Call Now</a>
        <a href="#services" class="btn-outline">🔧 Our Services</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SERVICES  (6 cards, 3 columns × 2 rows, equal height)
# ═══════════════════════════════════════════════════════════════
st.markdown('<a name="services"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-light">', unsafe_allow_html=True)

st.markdown("""
<span class="sec-label">What We Do</span>
<h2 class="sec-title">Our Premium Services</h2>
<p class="sec-desc">We specialize in extending the life of your appliances
with quality parts and expert workmanship.</p>
""", unsafe_allow_html=True)

SERVICES = [
    ("🌀", "Ceiling Fan Repair & Rewinding",
     "Expert repair and rewinding of all ceiling fans. We fix noise, speed problems, motor burnouts and restore full performance.", "Fan"),
    ("💨", "Table, Wall & Pedestal Fans",
     "Complete repair for table fans, wall fans, pedestal fans, stand fans, cabin fans and tower fans. All brands accepted.", "Fan"),
    ("🔄", "Exhaust & Industrial Fans",
     "Repair of exhaust fans, mini exhaust, talvar, farata, lift fans and all industrial ventilation fans.", "Fan"),
    ("⚙️", "Mixer & Blender Repair",
     "Professional repair for all mixer and blender brands. Motor failures, blade issues, speed control and electrical faults.", "Appliance"),
    ("🔥", "Iron Repair",
     "Fast repair for steam irons, dry irons and automatic irons. Heating elements, thermostats and cord issues fixed.", "Appliance"),
    ("🚿", "Geyser Repair",
     "Expert geyser and water heater repair. Thermostat, heating element replacement, leaks and all electrical problems.", "Appliance"),
]

for row_start in range(0, len(SERVICES), 3):
    cols = st.columns(3, gap="medium")
    for col, (icon, title, desc, tag) in zip(cols, SERVICES[row_start:row_start+3]):
        with col:
            st.markdown(f"""
<div class="svc-card">
    <span class="svc-icon">{icon}</span>
    <h3>{title}</h3>
    <p>{desc}</p>
    <span class="svc-tag">✦ {tag} Repair</span>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # end sec-light

# ═══════════════════════════════════════════════════════════════
# STATS  (4 equal columns)
# ═══════════════════════════════════════════════════════════════
st.markdown('<div class="sec-blue">', unsafe_allow_html=True)

st.markdown("""
<h2 style="color:#fff;font-size:1.9rem;font-weight:900;text-align:center;margin:0 0 6px;">
    Why Choose Burhani Electricals?
</h2>
<p style="color:#bae6fd;text-align:center;margin:0 0 32px;font-size:1rem;">
    Trusted by hundreds of customers across Surat
</p>
""", unsafe_allow_html=True)

STATS = [("7+", "Years Experience"), ("500+", "Repairs Done"),
         ("6", "Service Types"),   ("100%", "Satisfaction")]

cols = st.columns(4, gap="medium")
for col, (num, label) in zip(cols, STATS):
    with col:
        st.markdown(f"""
<div class="stat-card">
    <div class="stat-num">{num}</div>
    <div class="stat-label">{label}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # end sec-blue

# ═══════════════════════════════════════════════════════════════
# CONTACT  (3 equal columns)
# ═══════════════════════════════════════════════════════════════
st.markdown('<a name="contact"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-white">', unsafe_allow_html=True)

st.markdown("""
<span class="sec-label">Get In Touch</span>
<h2 class="sec-title">Contact Us</h2>
<p class="sec-desc">Reach out to Mr. Husain M Vankanerwala for fast, affordable repairs.</p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")
with col1:
    st.markdown("""
<div class="con-card">
    <span class="con-icon">📞</span>
    <h3>Call / WhatsApp</h3>
    <a href="tel:+918780514062">+91 87805 14062</a>
</div>
""", unsafe_allow_html=True)
with col2:
    st.markdown("""
<div class="con-card">
    <span class="con-icon">📍</span>
    <h3>Location</h3>
    <p>Surat, Gujarat, India</p>
</div>
""", unsafe_allow_html=True)
with col3:
    st.markdown("""
<div class="con-card">
    <span class="con-icon">🕐</span>
    <h3>Working Hours</h3>
    <p>Mon – Sat: 9AM – 8PM</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<br>', unsafe_allow_html=True)
_, mid, _ = st.columns([1, 2, 1])
with mid:
    st.markdown("""
<div style="text-align:center;">
    <a href="https://wa.me/918780514062" target="_blank" class="wa-btn">
        💬 Chat on WhatsApp
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # end sec-white

# ═══════════════════════════════════════════════════════════════
# AI CHAT
# ═══════════════════════════════════════════════════════════════
st.markdown('<a name="chat"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-light">', unsafe_allow_html=True)

st.markdown("""
<span class="sec-label">AI Powered</span>
<h2 class="sec-title">Chat with Our Assistant</h2>
<p class="sec-desc">Ask about repair issues, troubleshooting tips, or service availability.</p>
""", unsafe_allow_html=True)

_, chat_col, _ = st.columns([1, 3, 1])
with chat_col:
    # Chat window header
    st.markdown("""
<div class="chat-wrap">
    <div class="chat-head">
        <span style="font-size:2rem">🤖</span>
        <div class="chat-head-text">
            <h4>Burhani Electricals Assistant</h4>
            <p>Online · Powered by Gemini AI</p>
        </div>
    </div>
    <div class="chat-body">
""", unsafe_allow_html=True)

    for msg in st.session_state.chat_history:
        css_class = "bubble-bot" if msg["role"] == "bot" else "bubble-user"
        st.markdown(
            f'<div class="{css_class}">{msg["text"]}</div>',
            unsafe_allow_html=True,
        )

    st.markdown("""
    </div>
    <div class="chat-note">
        AI may make mistakes. Contact Husain for official quotes.
    </div>
</div>
""", unsafe_allow_html=True)

    # Input form (clear_on_submit avoids ghost text)
    with st.form("chat_form", clear_on_submit=True):
        c1, c2 = st.columns([5, 1])
        with c1:
            user_msg = st.text_input(
                "msg", label_visibility="collapsed",
                placeholder="Ask about fan repair, mixer issues…"
            )
        with c2:
            send = st.form_submit_button("Send ➤")

    if send and user_msg.strip():
        st.session_state.chat_history.append({"role": "user",  "text": user_msg.strip()})
        with st.spinner("Thinking…"):
            reply = ask_gemini(user_msg.strip())
        st.session_state.chat_history.append({"role": "bot", "text": reply})
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)  # end sec-light

# ═══════════════════════════════════════════════════════════════
# FOOTER  (3 equal columns)
# ═══════════════════════════════════════════════════════════════
year = datetime.now().year
st.markdown('<div class="footer">', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3, gap="large")
with f1:
    st.markdown(f"""
<div class="footer-brand">⚡ Burhani <span>Electricals</span></div>
<p class="footer-desc">
    Professional repair and rewinding for all fans and home appliances.<br>
    Owned by <strong style="color:#e2e8f0;">Mr. Husain M Vankanerwala</strong>, Surat.
</p>
""", unsafe_allow_html=True)

with f2:
    st.markdown("""
<h4>Quick Links</h4>
<ul>
    <li><a href="#services">Services</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#chat">AI Chat</a></li>
</ul>
""", unsafe_allow_html=True)

with f3:
    st.markdown("""
<h4>Contact</h4>
<ul>
    <li><a href="tel:+918780514062">📞 +91 87805 14062</a></li>
    <li><a href="https://wa.me/918780514062" target="_blank">💬 WhatsApp Us</a></li>
    <li>📍 Surat, Gujarat, India</li>
</ul>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="footer-bottom">
    © {year} Burhani Electricals. All rights reserved.
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # end footer

# Floating call button (always visible)
st.markdown("""
<a href="tel:+918780514062" class="fab">📞 Call Now</a>
""", unsafe_allow_html=True)
