import streamlit as st
from services.api import get_history


def searched():
    st.markdown('<h2 class="section-title">Users Also Searched For</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-subtitle">Companies analyzed by other users with LeadPilot</p>',
        unsafe_allow_html=True,
    )

    search_query = st.text_input("Search companies", placeholder="Search company name...", key="search_input", label_visibility="collapsed").strip().lower()

    try:
        data = get_history()
    except Exception:
        data = [
            {"id": 1, "company_name": "OpenAI", "website": "https://openai.com", "qualification_score": 92},
            {"id": 2, "company_name": "Stripe", "website": "https://stripe.com", "qualification_score": 88},
            {"id": 3, "company_name": "Notion", "website": "https://notion.so", "qualification_score": 95},
        ]

    if search_query:
        data = [r for r in data if search_query in r.get("company_name", "").lower()]

    if not data:
        st.markdown(
            '<p style="color:rgba(255,255,255,0.4);text-align:center;padding:2rem;">No companies found matching your search.</p>',
            unsafe_allow_html=True,
        )
        return

    for i, run in enumerate(data):
        name = run.get("company_name", f"Run #{run.get('id', i)}")
        website = run.get("website", "")
        score = run.get("qualification_score")
        score_str = f"{score}/100" if score is not None else "—"

        st.markdown(f"""
        <div class="history-row" style="cursor:default;grid-template-columns:2fr 2fr 1fr;animation-delay:{i * 0.05}s;">
            <div class="row-item"><strong>{name}</strong></div>
            <div class="row-item" style="color:rgba(255,255,255,0.35);font-size:0.78rem;">{website}</div>
            <div class="row-item">{score_str}</div>
        </div>
        """, unsafe_allow_html=True)