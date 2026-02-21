import streamlit as st
import requests
import os
from datetime import datetime

# ── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Burhani Electricals - Expert Repair Services",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Verdana&display=swap');

  /* Hide Streamlit defaults */
  #MainMenu, footer, header { visibility: hidden; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  section[data-testid="stSidebar"] { display: none; }

  * { font-family: Verdana, Geneva, Tahoma, sans-serif; box-sizing: border-box; }
  html, body { scroll-behavior: smooth; margin: 0; padding: 0; background: #f8fafc; }

  /* ── NAVBAR ── */
  .navbar {
    position: sticky; top: 0; z-index: 999;
    background: #ffffff; box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    padding: 0 2rem; display: flex; justify-content: space-between;
    align-items: center; height: 64px;
  }
  .nav-logo { display: flex; align-items: center; gap: 10px; text-decoration: none; }
  .nav-logo-icon {
    background: #0284c7; padding: 6px; border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
  }
  .nav-brand { font-size: 1.2rem; font-weight: 900; color: #0f172a; }
  .nav-brand span { color: #0284c7; }
  .nav-links { display: flex; gap: 2rem; align-items: center; }
  .nav-links a {
    text-decoration: none; color: #475569; font-weight: 600;
    font-size: 0.9rem; transition: color 0.2s;
  }
  .nav-links a:hover { color: #0284c7; }
  .nav-cta {
    background: #0284c7; color: #fff !important; padding: 8px 20px;
    border-radius: 8px; font-weight: 700 !important;
    animation: pulse-ring 2s infinite;
  }
  @keyframes pulse-ring {
    0%,100%{box-shadow:0 0 0 0 rgba(2,132,199,.4)}
    50%{box-shadow:0 0 0 10px rgba(2,132,199,0)}
  }

  /* ── HERO ── */
  .hero {
    position: relative; background: linear-gradient(135deg, #e0f2fe 0%, #f0f9ff 100%);
    padding: 80px 2rem 120px; text-align: center; overflow: hidden;
  }
  .hero-badge {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(255,255,255,0.8); border: 1px solid #bae6fd;
    padding: 6px 16px; border-radius: 999px; font-size: 0.85rem;
    font-weight: 700; color: #075985; margin-bottom: 1.5rem;
  }
  .hero h1 {
    font-size: clamp(2rem, 5vw, 3.5rem); font-weight: 900;
    color: #0f172a; margin: 0 0 1rem; line-height: 1.1;
  }
  .hero p {
    font-size: 1.1rem; color: #334155; max-width: 600px;
    margin: 0 auto 2rem; font-weight: 500; line-height: 1.7;
  }
  .hero-btns { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
  .btn-primary {
    background: #0284c7; color: #fff; padding: 14px 32px;
    border-radius: 10px; font-weight: 700; font-size: 1rem;
    text-decoration: none; display: inline-flex; align-items: center; gap: 8px;
    transition: background 0.2s, transform 0.2s; box-shadow: 0 4px 15px rgba(2,132,199,0.4);
  }
  .btn-primary:hover { background: #0369a1; transform: translateY(-2px); color: #fff; }
  .btn-secondary {
    background: #fff; color: #0369a1; padding: 14px 32px;
    border-radius: 10px; font-weight: 700; font-size: 1rem;
    text-decoration: none; display: inline-flex; align-items: center; gap: 8px;
    border: 2px solid #bae6fd; transition: background 0.2s, transform 0.2s;
  }
  .btn-secondary:hover { background: #f0f9ff; transform: translateY(-2px); color: #0369a1; }
  .wave-divider {
    position: absolute; bottom: 0; left: 0; width: 100%; overflow: hidden; line-height: 0;
  }

  /* ── SECTIONS ── */
  .section { padding: 80px 2rem; }
  .section-light { background: #f8fafc; }
  .section-white { background: #ffffff; }
  .section-title { text-align: center; margin-bottom: 3rem; }
  .section-label {
    color: #0284c7; font-weight: 700; font-size: 0.75rem;
    letter-spacing: 0.15em; text-transform: uppercase; display: block; margin-bottom: 8px;
  }
  .section-title h2 {
    font-size: clamp(1.6rem, 3vw, 2.5rem); font-weight: 900;
    color: #0f172a; margin: 0 0 12px;
  }
  .section-title p { color: #64748b; font-size: 1rem; max-width: 580px; margin: 0 auto; }

  /* ── GRID ── */
  .grid-3 {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem; max-width: 1100px; margin: 0 auto;
  }
  .grid-3-sm {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 1.5rem; max-width: 900px; margin: 0 auto;
  }

  /* ── SERVICE CARD ── */
  .service-card {
    background: #fff; border: 1px solid #e2e8f0; border-radius: 16px;
    overflow: hidden; transition: transform 0.3s, box-shadow 0.3s;
    display: flex; flex-direction: column;
  }
  .service-card:hover { transform: translateY(-5px); box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
  .card-body { padding: 2rem; flex: 1; }
  .card-icon {
    width: 54px; height: 54px; background: #e0f2fe; border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.6rem; margin-bottom: 1.2rem; transition: background 0.3s;
  }
  .service-card:hover .card-icon { background: #0284c7; }
  .card-body h3 { font-size: 1.1rem; font-weight: 800; color: #0f172a; margin: 0 0 10px; }
  .card-body p { color: #64748b; font-size: 0.9rem; line-height: 1.7; margin: 0; }
  .card-footer {
    padding: 14px 2rem; background: #f8fafc;
    border-top: 1px solid #e2e8f0; font-size: 0.85rem;
    font-weight: 700; color: #0284c7;
  }

  /* ── STATS ── */
  .stats-section {
    background: linear-gradient(135deg, #0284c7, #0369a1);
    padding: 60px 2rem; text-align: center;
  }
  .stats-section h2 { color: #fff; font-size: 1.8rem; font-weight: 900; margin: 0 0 8px; }
  .stats-section p { color: #bae6fd; font-size: 1rem; margin: 0 0 2.5rem; }
  .stats-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 1rem; max-width: 700px; margin: 0 auto;
  }
  .stat-card {
    background: rgba(255,255,255,0.12); border-radius: 14px;
    padding: 1.5rem 1rem; color: #fff;
  }
  .stat-num { font-size: 2.2rem; font-weight: 900; margin-bottom: 4px; }
  .stat-label { font-size: 0.85rem; color: #bae6fd; font-weight: 600; }

  /* ── CONTACT CARDS ── */
  .contact-card {
    background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 16px;
    padding: 2rem; text-align: center; transition: transform 0.3s, box-shadow 0.3s;
  }
  .contact-card:hover { transform: translateY(-4px); box-shadow: 0 15px 30px rgba(0,0,0,0.08); }
  .contact-icon {
    width: 56px; height: 56px; background: #0284c7; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.5rem; margin: 0 auto 1rem;
  }
  .contact-card h3 { font-size: 1rem; font-weight: 800; color: #0f172a; margin: 0 0 6px; }
  .contact-card a { color: #0284c7; font-weight: 700; font-size: 1.1rem; text-decoration: none; }
  .contact-card p { color: #475569; font-weight: 600; margin: 0; }
  .wa-btn {
    display: inline-flex; align-items: center; gap: 10px;
    background: #22c55e; color: #fff; padding: 16px 36px;
    border-radius: 14px; font-weight: 800; font-size: 1.1rem;
    text-decoration: none; margin-top: 2.5rem;
    transition: background 0.2s, transform 0.2s;
    box-shadow: 0 4px 20px rgba(34,197,94,0.4);
  }
  .wa-btn:hover { background: #16a34a; transform: translateY(-2px); color: #fff; }

  /* ── AI CHAT ── */
  .chat-container {
    max-width: 700px; margin: 0 auto;
    background: #fff; border: 1px solid #e2e8f0;
    border-radius: 20px; overflow: hidden;
    box-shadow: 0 10px 40px rgba(0,0,0,0.08);
  }
  .chat-header {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    padding: 1.2rem 1.5rem; color: #fff;
    display: flex; align-items: center; gap: 10px;
  }
  .chat-header h3 { margin: 0; font-size: 1rem; font-weight: 700; }
  .chat-header p { margin: 0; font-size: 0.8rem; opacity: 0.8; }
  .chat-messages {
    padding: 1.5rem; background: #f8fafc;
    min-height: 320px; max-height: 380px; overflow-y: auto;
    display: flex; flex-direction: column; gap: 1rem;
  }
  .msg-bot { display: flex; justify-content: flex-start; }
  .msg-user { display: flex; justify-content: flex-end; }
  .msg-bubble-bot {
    background: #fff; border: 1px solid #e2e8f0; color: #1e293b;
    padding: 12px 16px; border-radius: 18px 18px 18px 4px;
    max-width: 80%; font-size: 0.9rem; line-height: 1.6;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
  }
  .msg-bubble-user {
    background: #4f46e5; color: #fff;
    padding: 12px 16px; border-radius: 18px 18px 4px 18px;
    max-width: 80%; font-size: 0.9rem; line-height: 1.6;
  }

  /* ── FOOTER ── */
  .footer { background: #0f172a; color: #94a3b8; padding: 60px 2rem 30px; }
  .footer-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 2rem; max-width: 1100px; margin: 0 auto 2rem;
  }
  .footer-logo { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
  .footer-logo span { font-size: 1.2rem; font-weight: 900; color: #fff; }
  .footer-logo span b { color: #38bdf8; }
  .footer p { font-size: 0.85rem; line-height: 1.7; }
  .footer h4 { color: #fff; font-weight: 700; margin: 0 0 12px; }
  .footer ul { list-style: none; padding: 0; margin: 0; }
  .footer ul li { margin-bottom: 8px; }
  .footer ul li a { color: #94a3b8; text-decoration: none; font-size: 0.85rem; }
  .footer ul li a:hover { color: #38bdf8; }
  .footer-bottom {
    border-top: 1px solid #1e293b; padding-top: 1.5rem;
    text-align: center; font-size: 0.8rem; color: #64748b;
    max-width: 1100px; margin: 0 auto;
  }

  /* ── FLOATING BUTTONS ── */
  .fab-call {
    position: fixed; bottom: 24px; right: 24px; z-index: 999;
    background: #0284c7; color: #fff; padding: 14px 22px;
    border-radius: 999px; font-weight: 700; text-decoration: none;
    font-size: 0.9rem; box-shadow: 0 4px 20px rgba(2,132,199,0.5);
    display: flex; align-items: center; gap: 8px;
    transition: transform 0.2s, background 0.2s;
  }
  .fab-call:hover { background: #0369a1; transform: scale(1.05); color: #fff; }

  /* Streamlit widget cleanup */
  div[data-testid="stTextInput"] input {
    border-radius: 999px !important;
    border: 2px solid #e2e8f0 !important;
    padding: 10px 20px !important;
  }
  div[data-testid="stTextInput"] input:focus {
    border-color: #4f46e5 !important;
    box-shadow: 0 0 0 3px rgba(79,70,229,0.1) !important;
  }
  div[data-testid="stButton"] button {
    background: #4f46e5 !important; color: #fff !important;
    border-radius: 999px !important; font-weight: 700 !important;
    padding: 10px 28px !important; border: none !important;
    transition: background 0.2s !important;
  }
  div[data-testid="stButton"] button:hover { background: #4338ca !important; }
</style>
""", unsafe_allow_html=True)

# ── Session state for chat ───────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "text": "Hello! I'm the Burhani Electricals Assistant 😊 Ask me about fan issues, mixer problems, or how we can help you!"}
    ]

# ── Gemini API Call ──────────────────────────────────────────────────────────
def ask_gemini(user_msg: str) -> str:
    api_key = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY", ""))
    if not api_key:
        return "Please contact Mr. Husain directly at ☎️ +91 8780514062 for assistance!"

    system = """You are the friendly AI assistant for "Burhani Electricals" owned by Mr. Husain M Vankanerwala in Surat, India.
Services: Repairing and rewinding of all types of fans (Ceiling, Wall, Table, Cabin, Pedestal, Stand, Tower, Exhaust, Mini Exhaust, Talvar, Farata, Lift fans), Mixer/Blender, Iron, and Geyser repairing.
Always conclude by suggesting the user contact Mr. Husain at +91 8780514062.
Keep answers concise and polite. For price queries say: prices vary, please call for a quote."""

    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        payload = {
            "system_instruction": {"parts": [{"text": system}]},
            "contents": [{"parts": [{"text": user_msg}]}],
            "generationConfig": {"temperature": 0.7, "maxOutputTokens": 300}
        }
        r = requests.post(url, json=payload, timeout=10)
        return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return "I'm having trouble right now. Please call Mr. Husain at +91 8780514062!"

# ════════════════════════════════════════════════════════════════════════════
#  NAVBAR
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="navbar">
  <a class="nav-logo" href="#home">
    <div class="nav-logo-icon">
      <svg width="20" height="20" fill="white" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
    </div>
    <span class="nav-brand">Burhani <span>Electricals</span></span>
  </a>
  <div class="nav-links">
    <a href="#services">Services</a>
    <a href="#contact">Contact</a>
    <a href="#ai-assistant">AI Chat</a>
    <a href="tel:+918780514062" class="nav-cta">📞 Call Now</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
#  HERO
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero" id="home">
  <div class="hero-badge">
    ⚡ Trusted Repair Service Since 2018
  </div>
  <h1>Burhani Electricals</h1>
  <p>Expert rewinding and repairing for all types of fans, mixers, irons &amp; geysers.
     Fast, reliable and affordable service in Surat.</p>
  <div class="hero-btns">
    <a href="tel:+918780514062" class="btn-primary">📞 Call Now</a>
    <a href="#services" class="btn-secondary">🔧 Our Services</a>
  </div>
  <div class="wave-divider">
    <svg viewBox="0 0 1200 80" preserveAspectRatio="none" style="width:100%;height:60px;fill:#f8fafc">
      <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z"/>
    </svg>
  </div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
#  SERVICES
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section section-light" id="services">
  <div class="section-title">
    <span class="section-label">What We Do</span>
    <h2>Our Premium Services</h2>
    <p>We specialize in extending the life of your electrical appliances with quality parts and expert workmanship.</p>
  </div>
  <div class="grid-3">

    <div class="service-card">
      <div class="card-body">
        <div class="card-icon">🌀</div>
        <h3>Ceiling Fan Repair & Rewinding</h3>
        <p>Expert repair and rewinding of all ceiling fans. We fix noise, speed problems, motor burnouts and restore full performance.</p>
      </div>
      <div class="card-footer">✦ Expert Repair</div>
    </div>

    <div class="service-card">
      <div class="card-body">
        <div class="card-icon">💨</div>
        <h3>Table, Wall & Pedestal Fans</h3>
        <p>Complete repair for table fans, wall fans, pedestal fans, stand fans, cabin fans, and tower fans. All brands accepted.</p>
      </div>
      <div class="card-footer">✦ Expert Repair</div>
    </div>

    <div class="service-card">
      <div class="card-body">
        <div class="card-icon">🔄</div>
        <h3>Exhaust & Industrial Fans</h3>
        <p>Repair and rewinding of exhaust fans, mini exhaust, talvar fans, farata fans, lift fans, and all industrial ventilation fans.</p>
      </div>
      <div class="card-footer">✦ Expert Repair</div>
    </div>

    <div class="service-card">
      <div class="card-body">
        <div class="card-icon">⚙️</div>
        <h3>Mixer & Blender Repair</h3>
        <p>Professional repair for all mixer and blender brands. We fix motor failures, blade issues, speed control, and electrical faults.</p>
      </div>
      <div class="card-footer">✦ Expert Repair</div>
    </div>

    <div class="service-card">
      <div class="card-body">
        <div class="card-icon">🔥</div>
        <h3>Iron Repair</h3>
        <p>Fast repair for steam irons, dry irons, and automatic irons. Fixing heating elements, thermostats, and cord issues.</p>
      </div>
      <div class="card-footer">✦ Expert Repair</div>
    </div>

    <div class="service-card">
      <div class="card-body">
        <div class="card-icon">🚿</div>
        <h3>Geyser Repair</h3>
        <p>Expert geyser and water heater repair. Thermostat issues, heating element replacement, leaks, and all electrical problems.</p>
      </div>
      <div class="card-footer">✦ Expert Repair</div>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
#  STATS
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="stats-section">
  <h2>Why Choose Burhani Electricals?</h2>
  <p>Trusted by hundreds of customers in Surat</p>
  <div class="stats-grid">
    <div class="stat-card"><div class="stat-num">7+</div><div class="stat-label">Years Experience</div></div>
    <div class="stat-card"><div class="stat-num">500+</div><div class="stat-label">Repairs Done</div></div>
    <div class="stat-card"><div class="stat-num">6</div><div class="stat-label">Service Types</div></div>
    <div class="stat-card"><div class="stat-num">100%</div><div class="stat-label">Satisfaction</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
#  CONTACT
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section section-white" id="contact">
  <div class="section-title">
    <span class="section-label">Get In Touch</span>
    <h2>Contact Us</h2>
    <p>Reach out to Mr. Husain M Vankanerwala for fast, affordable repairs.</p>
  </div>
  <div class="grid-3-sm">
    <div class="contact-card">
      <div class="contact-icon">📞</div>
      <h3>Call / WhatsApp</h3>
      <a href="tel:+918780514062">+91 87805 14062</a>
    </div>
    <div class="contact-card">
      <div class="contact-icon">📍</div>
      <h3>Location</h3>
      <p>Surat, Gujarat, India</p>
    </div>
    <div class="contact-card">
      <div class="contact-icon">🕐</div>
      <h3>Working Hours</h3>
      <p>Mon – Sat: 9AM – 8PM</p>
    </div>
  </div>
  <div style="text-align:center">
    <a href="https://wa.me/918780514062" target="_blank" class="wa-btn">
      <svg width="24" height="24" fill="white" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
      Chat on WhatsApp
    </a>
  </div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
#  AI CHAT ASSISTANT
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section section-light" id="ai-assistant">
  <div class="section-title">
    <span class="section-label">AI Powered</span>
    <h2>Chat with Our Assistant</h2>
    <p>Ask about repair issues, troubleshooting tips, or service availability.</p>
  </div>
  <div class="chat-container">
    <div class="chat-header">
      <span style="font-size:1.5rem">🤖</span>
      <div>
        <h3>Burhani Electricals Assistant</h3>
        <p>Online • Powered by Gemini AI</p>
      </div>
    </div>
    <div class="chat-messages" id="chat-box">
""", unsafe_allow_html=True)

# Render chat messages
for msg in st.session_state.messages:
    if msg["role"] == "bot":
        st.markdown(f'<div class="msg-bot"><div class="msg-bubble-bot">{msg["text"]}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="msg-user"><div class="msg-bubble-user">{msg["text"]}</div></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close chat-messages

# Chat input row
col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input("", placeholder="Ask about fan repair, mixer issues...", label_visibility="collapsed", key="chat_input")
with col2:
    send = st.button("Send ➤")

st.markdown("""
    <p style="text-align:center;font-size:0.75rem;color:#94a3b8;margin-top:8px;padding-bottom:1rem">
      AI may make mistakes. Contact Husain for official quotes.
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

# Handle send
if send and user_input.strip():
    st.session_state.messages.append({"role": "user", "text": user_input.strip()})
    with st.spinner("Thinking..."):
        reply = ask_gemini(user_input.strip())
    st.session_state.messages.append({"role": "bot", "text": reply})
    st.rerun()

# ════════════════════════════════════════════════════════════════════════════
#  FOOTER
# ════════════════════════════════════════════════════════════════════════════
year = datetime.now().year
st.markdown(f"""
<div class="footer">
  <div class="footer-grid">
    <div>
      <div class="footer-logo">
        <span>⚡</span>
        <span>Burhani <b>Electricals</b></span>
      </div>
      <p>Professional repair and rewinding services for all types of fans and home appliances.
         Owned by Mr. Husain M Vankanerwala, Surat.</p>
    </div>
    <div>
      <h4>Quick Links</h4>
      <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#contact">Contact</a></li>
        <li><a href="#ai-assistant">AI Assistant</a></li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul>
        <li><a href="tel:+918780514062">📞 +91 87805 14062</a></li>
        <li><a href="https://wa.me/918780514062" target="_blank">💬 WhatsApp Us</a></li>
        <li><a href="#contact">📍 Surat, Gujarat</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    © {year} Burhani Electricals. All rights reserved.
  </div>
</div>

<!-- Floating Call Button -->
<a href="tel:+918780514062" class="fab-call">📞 <span>Call Now</span></a>
""", unsafe_allow_html=True)
