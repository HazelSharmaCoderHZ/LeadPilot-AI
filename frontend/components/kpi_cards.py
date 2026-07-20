import streamlit as st


def render_kpis(data=None):
    if data is None:
        data = {"total_workflows": 126, "avg_score": 91, "companies": 74, "emails": 531}

    items = [
        ("📊", str(data.get("total_workflows", 0)), "Total Workflows", "#10B981"),
        ("⭐", str(data.get("avg_score", 0)), "Avg Lead Score", "#3B82F6"),
        ("🏢", str(data.get("companies", 0)), "Companies", "#F59E0B"),
        ("✉️", str(data.get("emails", 0)), "Emails Generated", "#8B5CF6"),
    ]

    cols = st.columns(4)
    for i, (icon, value, label, color) in enumerate(items):
        with cols[i]:
            st.markdown(f"""
            <div class="dashboard-card" style="animation-delay:{i * 0.08}s;text-align:center;">
                <div style="font-size:1.8rem;margin-bottom:0.3rem;">{icon}</div>
                <div style="font-size:2rem;font-weight:800;color:#fff;">{value}</div>
                <div style="font-size:0.8rem;color:rgba(255,255,255,0.45);text-transform:uppercase;letter-spacing:0.5px;">{label}</div>
            </div>
            """, unsafe_allow_html=True)