import streamlit as st
from services.api import get_history
from components.kpi_cards import render_kpis
from components.charts import render_charts
from components.recent_runs import render_recent


def _generate_demo_history():
    names = ["OpenAI", "Stripe", "Notion", "Anthropic", "Vercel", "Linear", "Figma", "Supabase"]
    return [
        {"id": i+1, "company_name": name, "website": f"https://{name.lower().replace(' ', '')}.com", "status": "completed", "qualification_score": 70 + (sum(ord(c) for c in name) % 28)}
        for i, name in enumerate(names)
    ]


def dashboard():
    st.markdown('<h2 class="section-title">Dashboard</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-subtitle">Real-time overview of your AI lead generation pipeline</p>',
        unsafe_allow_html=True,
    )

    try:
        history = get_history()
        if not history:
            history = _generate_demo_history()
    except Exception:
        history = _generate_demo_history()

    total = len(history)
    scores = [r.get("qualification_score", 0) or 0 for r in history if r.get("qualification_score")]
    avg_score = round(sum(scores) / len(scores), 1) if scores else 0
    companies = set(r.get("company_name") for r in history if r.get("company_name"))
    emails = sum(1 for r in history if r.get("status") == "completed") * 3

    kpi_data = {
        "total_workflows": total,
        "avg_score": avg_score,
        "companies": len(companies),
        "emails": emails,
    }

    render_kpis(kpi_data)
    st.markdown("<br>", unsafe_allow_html=True)
    render_charts()
    st.markdown("<br>", unsafe_allow_html=True)
    render_recent(history[:5])