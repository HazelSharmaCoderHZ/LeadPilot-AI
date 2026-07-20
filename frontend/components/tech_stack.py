import streamlit as st


BACKEND_TECH = [
    ("FastAPI", "High-performance Python API framework"),
    ("LangGraph", "Orchestrate multi-agent workflows"),
    ("Gemini", "Google's LLM for analysis and generation"),
    ("Firecrawl", "Intelligent web crawling and scraping"),
    ("Supabase", "PostgreSQL database with real-time"),
    ("SQLAlchemy", "ORM for database interactions"),
    ("Tavily", "AI-powered search for contacts"),
    ("Plotly", "Interactive data visualizations"),
    ("Streamlit", "Python-based UI framework"),
]


def render_tech():
    st.markdown('<h2 class="section-title">Technology Stack</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-subtitle">Built with modern AI and web technologies</p>',
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    for i, (name, desc) in enumerate(BACKEND_TECH):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="backend-tech-card" style="animation-delay:{i * 0.08}s">
                <h4>{name}</h4>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)