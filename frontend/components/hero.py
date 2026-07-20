import streamlit as st


def render_hero():
    left, right = st.columns([1.3, 1])

    with left:
        st.markdown("""
        <div class="hero-section">
            <div class="hero-badge">
                <span class="badge-dot"></span>
                AI Powered Sales Intelligence
            </div>
            <h1 class="hero-title">
                Transform Cold Prospects Into<br>
                <span class="gradient-text">Qualified Opportunities</span>
            </h1>
            <p class="hero-subtitle">
                LeadPilot AI orchestrates 6 specialized AI agents to research
                companies, discover decision-makers, qualify leads,
                generate personalized outreach and review every email.
            </p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            if st.button("Start Workflow", key="hero_start", use_container_width=True):
                st.session_state.page = "run"
                st.rerun()
        with c2:
            if st.button("View Dashboard", key="hero_demo", use_container_width=True):
                st.session_state.page = "dashboard"
                st.rerun()

    with right:
        st.markdown("""
        <div class="glass-card">
            <div class="card-title">Agent Pipeline</div>
            <hr class="card-divider">
            <div class="agent-item">
                <span class="agent-dot"></span>
                ResearchAgent
                <span class="agent-label">Firecrawl</span>
            </div>
            <div class="agent-item">
                <span class="agent-dot"></span>
                AnalysisAgent
                <span class="agent-label">Gemini AI</span>
            </div>
            <div class="agent-item">
                <span class="agent-dot"></span>
                ContactsAgent
                <span class="agent-label">Tavily Search</span>
            </div>
            <div class="agent-item">
                <span class="agent-dot"></span>
                QualificationAgent
                <span class="agent-label">Score: 0-100</span>
            </div>
            <div class="agent-item">
                <span class="agent-dot"></span>
                OutreachAgent
                <span class="agent-label">Personalization</span>
            </div>
            <div class="agent-item">
                <span class="agent-dot"></span>
                ReviewerAgent
                <span class="agent-label">Quality Check</span>
            </div>
        </div>
        """, unsafe_allow_html=True)