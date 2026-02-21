# Burhani Electricals — Streamlit Website

Professional website for Burhani Electricals built with Python + Streamlit.

---

## 🚀 Deploy FREE on Streamlit Cloud (Easiest!)

### Step 1 — Upload to GitHub
1. Create a new **public** repo on GitHub (e.g. `burhani-electricals`)
2. Upload all these files (**do NOT upload** `.streamlit/secrets.toml`)

### Step 2 — Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your **GitHub account**
3. Click **"New app"**
4. Select your repo and set:
   - **Main file path**: `app.py`
5. Click **"Deploy!"**

### Step 3 — Add Gemini API Key
1. In Streamlit Cloud dashboard → your app → **"⋮" menu** → **"Settings"**
2. Click **"Secrets"** tab
3. Paste this:
   ```toml
   GEMINI_API_KEY = "your_actual_gemini_api_key"
   ```
4. Click **Save** — app restarts automatically

Get a free Gemini API key at: https://aistudio.google.com

### Step 4 — Your site is live! 🎉
```
https://YOUR_USERNAME-burhani-electricals-app-XXXX.streamlit.app
```

---

## 💻 Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Add your API key to .streamlit/secrets.toml

# Run the app
streamlit run app.py
```
Open http://localhost:8501

---

## 📁 Files
```
burhani-electricals/
├── app.py                     ← Main Streamlit app (entire website)
├── requirements.txt           ← Python dependencies
├── .gitignore
├── README.md
└── .streamlit/
    ├── config.toml            ← Theme & server config
    └── secrets.toml           ← API keys (DO NOT upload to GitHub)
```
