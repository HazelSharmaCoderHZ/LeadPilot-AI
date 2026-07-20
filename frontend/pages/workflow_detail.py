import streamlit as st
from services.api import get_workflow


def workflow_detail():
    run = st.session_state.get("selected_company", {})
    if not run:
        st.markdown('<p style="color:rgba(255,255,255,0.4);">No company selected.</p>', unsafe_allow_html=True)
        if st.button("Back to search"):
            st.session_state.page = "searched"
            st.rerun()
        return

    name = run.get("company_name", "Unknown")
    status = run.get("status", "unknown")
    score = run.get("qualification_score")
    wid = run.get("id")

    st.markdown(f'<h2 class="section-title">{name}</h2>', unsafe_allow_html=True)

    # Try to fetch full details from backend
    if wid:
        try:
            details = get_workflow(wid)
            if details and isinstance(details, dict):
                run = details
        except Exception:
            pass

    status_dot = "completed" if status == "completed" else ("running" if status == "running" else "failed")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Status", status.title())
    with c2:
        st.metric("Score", f"{score}/100" if score else "Pending")
    with c3:
        st.metric("Workflow ID", f"#{wid}")

    website = run.get("website", "N/A")
    company_data = run.get("company", {})
    if company_data and isinstance(company_data, dict):
        website = company_data.get("website", website)

    st.markdown(f"""
    <div class="dashboard-card" style="margin-top:1rem;">
        <div class="card-header">
            <h3>Company Info</h3>
            <div class="card-icon">Info</div>
        </div>
        <p style="color:rgba(255,255,255,0.6);font-size:0.88rem;">Website: {website}</p>
    </div>
    """, unsafe_allow_html=True)

    workflow_data = run.get("workflow_data", {}) or run.get("data", {}) or {}
    if isinstance(workflow_data, str):
        import json
        try:
            workflow_data = json.loads(workflow_data)
        except Exception:
            workflow_data = {}

    analysis = workflow_data.get("analysis", {})
    qual = workflow_data.get("qualification", {})
    contacts = workflow_data.get("contacts", [])
    outreach = workflow_data.get("outreach", {})
    review = workflow_data.get("review", {})
    research = workflow_data.get("research", {})

    if analysis:
        st.markdown("""
        <div class="dashboard-card" style="margin-top:0.8rem;">
            <div class="card-header">
                <h3>Analysis</h3>
                <div class="card-icon">AI</div>
            </div>
        """, unsafe_allow_html=True)
        summary = analysis.get("summary") or analysis.get("business_model") or ""
        if summary:
            st.markdown(f'<p style="color:rgba(255,255,255,0.6);font-size:0.88rem;">{summary}</p>', unsafe_allow_html=True)
        pain = analysis.get("pain_points") or []
        if pain:
            st.markdown(f'<p style="color:rgba(255,255,255,0.6);font-size:0.82rem;"><strong>Pain Points:</strong> {", ".join(pain)}</p>', unsafe_allow_html=True)
        opps = analysis.get("opportunities") or []
        if opps:
            st.markdown(f'<p style="color:rgba(255,255,255,0.6);font-size:0.82rem;"><strong>Opportunities:</strong> {", ".join(opps)}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if qual:
        st.markdown(f"""
        <div class="dashboard-card" style="margin-top:0.8rem;">
            <div class="card-header">
                <h3>Qualification</h3>
                <div class="card-icon">Score</div>
            </div>
            <p style="color:rgba(255,255,255,0.6);font-size:0.88rem;">
                Tier: {qual.get("tier", "N/A")} | Score: {qual.get("score", "N/A")}/100
            </p>
            <p style="color:rgba(255,255,255,0.5);font-size:0.82rem;">{qual.get("reasoning", "")}</p>
        </div>
        """, unsafe_allow_html=True)

    if contacts:
        st.markdown("""
        <div class="dashboard-card" style="margin-top:0.8rem;">
            <div class="card-header">
                <h3>Contacts</h3>
                <div class="card-icon">People</div>
            </div>
        """, unsafe_allow_html=True)
        for c in contacts[:5]:
            name = c.get("name", "Unknown")
            role = c.get("role", "")
            st.markdown(f'<p style="color:rgba(255,255,255,0.6);font-size:0.85rem;">{name} — {role}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if outreach:
        st.markdown(f"""
        <div class="dashboard-card" style="margin-top:0.8rem;">
            <div class="card-header">
                <h3>Outreach</h3>
                <div class="card-icon">Email</div>
            </div>
            <p style="color:rgba(255,255,255,0.6);font-size:0.88rem;"><strong>Subject:</strong> {outreach.get("subject", "")}</p>
            <p style="color:rgba(255,255,255,0.5);font-size:0.85rem;">{outreach.get("body", "")}</p>
        </div>
        """, unsafe_allow_html=True)

    if st.button("Back to search"):
        st.session_state.page = "searched"
        st.rerun()