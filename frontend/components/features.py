import streamlit as st


FEATURES = [
    ("Research Agent", "Automatically crawl and understand company websites using Firecrawl. Extracts business model, products, and market positioning."),
    ("Analysis Agent", "Gemini-powered deep analysis of company data. Identifies customer segments, pain points, and strategic opportunities."),
    ("Contacts Agent", "Intelligent discovery of decision-makers using Tavily search. Finds LinkedIn profiles, emails, roles, and relevant information."),
    ("Qualification Agent", "AI scores every lead on intent, fit, and engagement. Prioritizes high-value opportunities automatically."),
    ("Outreach Agent", "Generates hyper-personalized cold emails using company context. Tailors messaging to each prospect's role and industry."),
    ("Review Agent", "AI quality assurance on every email. Checks tone, accuracy, personalization, and compliance before sending."),
]


def render_features():
    st.markdown('<h2 class="section-title">AI Agent Features</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Six specialized agents working together to automate your lead generation pipeline</p>', unsafe_allow_html=True)

    cols = st.columns(3)
    for i, (title, desc) in enumerate(FEATURES):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="feature-card" style="animation-delay:{i * 0.1}s">
                <div class="feature-icon">{i + 1}</div>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)