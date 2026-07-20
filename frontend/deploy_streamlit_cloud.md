# Deploy LeadPilot AI to Streamlit Community Cloud

## Prerequisites
- Push your code to a GitHub repository (already done)
- A Streamlit Cloud account (sign up at https://share.streamlit.io)

## Step 1: Update Backend URL

The app will work without a backend connection (demo data is injected automatically). If you want live data, deploy the backend separately on Render or Railway first, then update `config.py`.

## Step 2: Deploy Frontend

1. Go to **https://share.streamlit.io**
2. Click **"New app"**
3. Select your GitHub repository: `HazelSharmaCoderHZ/LeadPilot-AI`
4. Set:
   - **Branch:** `main`
   - **Main file path:** `frontend/app.py`
   - **App URL:** Choose your preferred subdomain
5. Click **Deploy**

## Step 3: Set Secrets (Optional — for backend URL)

If you deployed the backend separately:
1. In your Streamlit Cloud app dashboard, go to **Settings → Secrets**
2. Add: `BACKEND_URL = "https://your-backend-url.com"`

The app will fall back to demo data automatically if the backend isn't available.

## Note
The frontend works fully with injected demo data. To get live AI-generated results, deploy the backend on Render/Railway and update `frontend/config.py` with the backend URL.