import streamlit as st

STATS = [
    ("6", "AI Agents", "+100%"),
    ("127", "Workflows Run", "+18%"),
    ("91%", "Qualified Leads", "+6%"),
    ("842", "Emails Generated", "+34%"),
]

def render_stats():
    st.markdown('<div class="stats-section">', unsafe_allow_html=True)
    cols = st.columns(4)
    for i, (value, label, trend) in enumerate(STATS):
        with cols[i]:
            st.markdown(f"""
            <div class="stat-card" style="animation-delay:{i * 0.1}s">
                <div class="stat-value">{value}</div>
                <div class="stat-label">{label}</div>
                <div class="stat-trend">{trend}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)