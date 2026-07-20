import streamlit as st


def render_footer():
    st.markdown("""
    <div class="footer">
        <p>Built with <strong>LeadPilot AI</strong> — AI-Powered Lead Generation · © 2026</p>
        <p style="margin-top:0.2rem;">FastAPI · LangGraph · Gemini · Firecrawl · Supabase · Tavily · Streamlit · Plotly</p>
    </div>
    """, unsafe_allow_html=True)