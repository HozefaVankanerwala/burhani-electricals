# Burhani Electrical's Website

Professional repair and rewinding services website for Burhani Electrical's.

---

## 🚀 How to Deploy to GitHub Pages (Step-by-Step)

### Step 1 — Create a GitHub Account
If you don't have one, go to [github.com](https://github.com) and sign up for free.

---

### Step 2 — Create a New Repository
1. Click the **"+"** button (top-right) → **"New repository"**
2. Repository name: `burhani-electrical` *(must match the `base` in vite.config.ts)*
3. Set to **Public**
4. Do **NOT** check "Initialize this repository"
5. Click **"Create repository"**

---

### Step 3 — Install Git & Node.js on Your Computer
- **Git**: Download from [git-scm.com](https://git-scm.com/downloads)
- **Node.js**: Download from [nodejs.org](https://nodejs.org) (choose LTS version)

---

### Step 4 — Upload the Code to GitHub
Open your terminal / command prompt and run these commands one by one:

```bash
# 1. Navigate to the project folder (change the path to where you extracted the zip)
cd path/to/burhani-electrical

# 2. Initialize git
git init

# 3. Add all files
git add .

# 4. Create first commit
git commit -m "Initial commit"

# 5. Set the branch name to main
git branch -M main

# 6. Connect to your GitHub repo (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/burhani-electrical.git

# 7. Push to GitHub
git push -u origin main
```

---

### Step 5 — Add Your Gemini API Key (for the AI Chat feature)
1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"**
4. Name: `VITE_GEMINI_API_KEY`
5. Value: Your Gemini API key (get one free at [aistudio.google.com](https://aistudio.google.com))
6. Click **"Add secret"**

> ⚠️ If you don't add the API key, the AI chat feature won't work, but the rest of the site will work fine.

---

### Step 6 — Enable GitHub Pages
1. Go to your repository → **Settings** → **Pages**
2. Under **"Build and deployment"**, set Source to: **"GitHub Actions"**
3. Click **Save**

---

### Step 7 — Trigger Deployment
GitHub Actions will automatically build and deploy your site every time you push to `main`.

To manually trigger it:
1. Go to your repository → **Actions** tab
2. Click **"Deploy to GitHub Pages"** → **"Run workflow"** → **"Run workflow"**

---

### Step 8 — View Your Live Website 🎉
After ~2 minutes, your site will be live at:
```
https://YOUR_USERNAME.github.io/burhani-electrical/
```

---

## 💻 Local Development

```bash
# Install dependencies
npm install

# Create .env.local with your API key
cp .env.example .env.local
# Edit .env.local and add your VITE_GEMINI_API_KEY

# Start development server
npm run dev
```

---

## 📁 Project Structure
```
burhani-electrical/
├── src/
│   ├── components/       # React components
│   │   ├── Navbar.tsx
│   │   ├── Hero.tsx
│   │   ├── Services.tsx
│   │   ├── ServicesPage.tsx
│   │   ├── Contact.tsx
│   │   ├── Footer.tsx
│   │   ├── FloatingCTA.tsx
│   │   └── AIChat.tsx
│   ├── services/
│   │   └── geminiService.ts  # AI chat service
│   ├── App.tsx
│   ├── index.tsx
│   ├── index.css
│   └── types.ts
├── .github/workflows/
│   └── deploy.yml        # Auto-deployment workflow
├── index.html
├── package.json
├── tailwind.config.js
├── vite.config.ts
└── tsconfig.json
```
