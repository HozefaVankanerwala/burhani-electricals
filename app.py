import streamlit as st
import requests
import os
from datetime import datetime

# ── PAGE CONFIG ─────────────────────────────────────────
st.set_page_config(
    page_title="Burhani Electricals - Expert Repair Services",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── GLOBAL STYLE SYSTEM ─────────────────────────────────
st.markdown("""
<style>

/* ===== DESIGN SYSTEM ===== */
:root {
  --primary:#0284c7;
  --primary-dark:#0369a1;
  --primary-light:#e0f2fe;

  --accent:#22c55e;
  --accent-dark:#16a34a;

  --text-dark:#0f172a;
  --text:#334155;
  --muted:#64748b;

  --border:#e2e8f0;
  --bg:#f8fafc;
  --white:#ffffff;
}

/* RESET */
*{box-sizing:border-box;font-family:Verdana,Geneva,Tahoma,sans-serif;}
html,body{margin:0;background:var(--bg);scroll-behavior:smooth;}

#MainMenu,footer,header{visibility:hidden;}
.block-container{padding:0!important;max-width:100%!important;}
section[data-testid="stSidebar"]{display:none;}

/* NAVBAR */
.navbar{
 position:sticky;top:0;z-index:999;background:#fff;
 box-shadow:0 2px 12px rgba(0,0,0,.08);
 padding:0 2rem;height:64px;display:flex;justify-content:space-between;align-items:center;
}
.nav-links a{margin-left:1.8rem;text-decoration:none;color:#475569;font-weight:600;}
.nav-links a:hover{color:var(--primary);}

.nav-cta{
 background:var(--primary);color:#fff!important;padding:8px 20px;border-radius:10px;
}
.nav-cta:hover{background:var(--primary-dark);}

/* HERO */
.hero{
 background:linear-gradient(135deg,#e0f2fe,#f0f9ff);
 padding:90px 2rem 120px;text-align:center;
}
.hero h1{font-size:3rem;margin-bottom:.6rem;color:var(--text-dark);}
.hero p{color:var(--text);max-width:650px;margin:auto;margin-bottom:2rem;}
.btn-primary{
 background:var(--primary);color:#fff!important;padding:14px 34px;border-radius:12px;font-weight:700;text-decoration:none;
}
.btn-primary:hover{background:var(--primary-dark);}
.btn-secondary{
 border:2px solid var(--primary-light);padding:14px 34px;border-radius:12px;font-weight:700;text-decoration:none;color:var(--primary-dark);background:#fff;
}
.btn-secondary:hover{background:var(--primary-light);}

/* SERVICE CARD */
.service-card{
 background:#fff;border:1px solid var(--border);border-radius:16px;
 transition:.25s;display:flex;flex-direction:column;
}
.service-card:hover{
 transform:translateY(-6px);
 box-shadow:0 20px 40px rgba(2,132,199,.15);
 border-color:var(--primary);
}
.card-icon{
 width:54px;height:54px;background:var(--primary-light);color:var(--primary);
 display:flex;align-items:center;justify-content:center;border-radius:12px;font-size:1.6rem;margin-bottom:1rem;
}
.service-card:hover .card-icon{background:var(--primary);color:#fff;}
.card-body{padding:2rem}
.card-footer{padding:14px 2rem;background:#f1f5f9;border-top:1px solid var(--border);color:var(--primary);font-weight:700}

/* CHAT */
.chat-container{
 max-width:700px;margin:auto;background:#fff;border:1px solid var(--border);
 border-radius:20px;overflow:hidden;box-shadow:0 10px 40px rgba(0,0,0,.08);
}
.chat-messages{
 padding:1.5rem;background:#f1f5f9;max-height:380px;overflow-y:auto;display:flex;flex-direction:column;gap:12px;
}
.msg-bubble-user{background:#4f46e5;color:#fff;padding:12px 16px;border-radius:18px 18px 4px 18px;max-width:85%;}
.msg-bubble-bot{background:#fff;border:1px solid var(--border);padding:12px 16px;border-radius:18px 18px 18px 4px;max-width:85%;}

/* WHATSAPP BUTTON */
.wa-btn{
 display:inline-block;background:var(--accent);color:#fff;padding:16px 36px;border-radius:14px;font-weight:800;text-decoration:none;
}
.wa-btn:hover{background:var(--accent-dark);}

/* FLOAT CALL */
.fab-call{
 position:fixed;bottom:24px;right:24px;background:var(--primary);color:#fff;padding:14px 22px;border-radius:999px;text-decoration:none;font-weight:700;
}
.fab-call:hover{background:var(--primary-dark);}

</style>
""", unsafe_allow_html=True)

# ── CHAT STATE ─────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages=[{"role":"bot","text":"Hello! 👋 Ask me about fan, mixer or geyser repair."}]

# ── GEMINI ─────────────────────────────────────────────
def ask_gemini(user_msg):
    api_key=os.environ.get("GEMINI_API_KEY","")
    if not api_key:
        return "Please contact Husain at +91 8780514062."

    try:
        r=requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}",
            json={"contents":[{"parts":[{"text":user_msg}]}]},
            timeout=10
        )
        return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "Please call +91 8780514062."

# ── HERO ───────────────────────────────────────────────
st.markdown("""
<div class="hero">
<h1>⚡ Burhani Electricals</h1>
<p>Expert repairing & rewinding of all types of fans, mixers, irons & geysers in Surat.</p>
<a href="tel:+918780514062" class="btn-primary">Call Now</a>
<a href="#chat" class="btn-secondary">Ask Assistant</a>
</div>
""",unsafe_allow_html=True)

# ── SERVICES ───────────────────────────────────────────
st.markdown("<h2 style='text-align:center'>Our Services</h2>",unsafe_allow_html=True)

cols=st.columns(3)
services=["Ceiling Fan Repair","Table & Wall Fan","Exhaust & Industrial Fans","Mixer Repair","Iron Repair","Geyser Repair"]

for i,s in enumerate(services):
    with cols[i%3]:
        st.markdown(f"""
        <div class="service-card">
            <div class="card-body">
                <div class="card-icon">🔧</div>
                <h3>{s}</h3>
                <p>Professional repairing service with quality work and affordable cost.</p>
            </div>
            <div class="card-footer">Expert Service</div>
        </div>
        """,unsafe_allow_html=True)

# ── CHAT ───────────────────────────────────────────────
st.markdown("<h2 id='chat' style='text-align:center'>Chat Assistant</h2>",unsafe_allow_html=True)

st.markdown('<div class="chat-container"><div class="chat-messages">',unsafe_allow_html=True)
for m in st.session_state.messages:
    cls="msg-bubble-bot" if m["role"]=="bot" else "msg-bubble-user"
    st.markdown(f'<div class="{cls}">{m["text"]}</div>',unsafe_allow_html=True)
st.markdown('</div></div>',unsafe_allow_html=True)

msg=st.text_input("Ask something")
if st.button("Send") and msg:
    st.session_state.messages.append({"role":"user","text":msg})
    reply=ask_gemini(msg)
    st.session_state.messages.append({"role":"bot","text":reply})
    st.rerun()

# ── FOOTER ─────────────────────────────────────────────
year=datetime.now().year
st.markdown(f"""
<div style="text-align:center;padding:40px;color:#64748b">
© {year} Burhani Electricals
</div>

<a href="tel:+918780514062" class="fab-call">📞 Call</a>
""",unsafe_allow_html=True)
