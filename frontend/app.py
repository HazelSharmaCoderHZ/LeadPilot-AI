import streamlit as st
from pathlib import Path
from components.stats import render_stats
from components.features import render_features
from components.workflow import render_workflow
from components.tech_stack import render_tech
from components.hero import render_hero
from components.footer import render_footer
from pages.dashboard import dashboard
from pages.searched import searched
from pages.run_workflow import run_workflow_page

st.set_page_config(
    page_title="LeadPilot AI",
    page_icon="LP",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "page" not in st.session_state:
    st.session_state.page = "landing"

if "selected_company" not in st.session_state:
    st.session_state.selected_company = None

BASE = Path(__file__).parent

def load_css():
    css_path = BASE / "styles" / "custom.css"
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

load_css()

# ---- NAVBAR ----
pages_opts = {
    "landing": "Home",
    "dashboard": "Dashboard",
    "searched": "Users Also Searched For",
}
current = st.session_state.page

with st.container():
    c1, c2, c3 = st.columns([1.5, 4, 1.5])
    with c1:
        st.markdown("""
        <div class="navbar-brand">
            <div class="brand-icon">LP</div>
            <div class="brand-text">Lead<span>Pilot</span></div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        cols = st.columns(len(pages_opts))
        for i, (key, label) in enumerate(pages_opts.items()):
            with cols[i]:
                if st.button(label, key=f"nav_{key}", use_container_width=True):
                    st.session_state.page = key
                    st.rerun()

    with c3:
        if current != "run":
            if st.button("New Workflow", key="nav_cta", use_container_width=True):
                st.session_state.page = "run"
                st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# ---- PAGE ROUTING ----
page = st.session_state.page

if page == "landing":
    render_hero()
    st.markdown("<br>", unsafe_allow_html=True)
    render_stats()
    st.markdown("<br><br>", unsafe_allow_html=True)
    render_features()
    st.markdown("<br><br>", unsafe_allow_html=True)
    render_workflow()
    st.markdown("<br><br>", unsafe_allow_html=True)
    render_tech()

elif page == "dashboard":
    dashboard()

elif page == "searched":
    searched()

elif page == "run":
    run_workflow_page()

elif page == "workflow_detail":
    from pages.workflow_detail import workflow_detail
    workflow_detail()

st.markdown("<br><br>", unsafe_allow_html=True)
render_footer()