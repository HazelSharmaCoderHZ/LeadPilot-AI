import streamlit as st


def render_recent(runs=None):
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-header">
        <h3>Recent Workflow Runs</h3>
        <div class="card-icon">List</div>
    </div>
    """, unsafe_allow_html=True)

    if runs is None:
        runs = [
            {"company_name": "OpenAI", "status": "completed", "qualification_score": 92, "id": 1},
            {"company_name": "Stripe", "status": "completed", "qualification_score": 88, "id": 2},
            {"company_name": "Notion", "status": "completed", "qualification_score": 95, "id": 3},
        ]

    for i, run in enumerate(runs):
        name = run.get("company_name", f"Run #{run.get('id', i)}")
        status = run.get("status", "unknown")
        score = run.get("qualification_score")
        score_str = f"{score}/100" if score is not None else "Pending"

        st.markdown(f"""
        <div class="history-row" style="cursor:default;grid-template-columns:2fr 1fr 1fr 1fr;animation-delay:{i * 0.06}s;">
            <div class="row-item"><strong>{name}</strong></div>
            <div class="row-item">
                <span class="status-badge {status}">{status.title()}</span>
            </div>
            <div class="row-item">{score_str}</div>
            <div class="row-item" style="color:rgba(255,255,255,0.3);font-size:0.75rem;">#{run.get('id', i)}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)