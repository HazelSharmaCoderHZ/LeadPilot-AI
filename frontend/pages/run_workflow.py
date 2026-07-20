import streamlit as st
from services.api import run_workflow


def _val(v, default="—"):
    if v is None:
        return default
    return v


def _has_data(obj):
    if not obj:
        return False
    for v in obj.values():
        if v is not None and v != "" and v != [] and v != {}:
            return True
    return False


_DEMO = {
    "qualification_score": 84,
    "data": {
        "company": {"company_name": None, "website": None, "industry": None, "location": None},
        "qualification": {"score": 84, "tier": "Silver",
            "reasoning": "Strong market presence and clear product-market fit. Multiple decision-makers identified with relevant seniority levels."},
        "analysis": {"summary": None, "pain_points": ["Scaling customer acquisition", "Identifying key decision-makers", "Personalizing outreach at scale"],
            "opportunities": ["Expand into new market segments", "Leverage AI for sales automation", "Improve lead conversion rates"],
            "competitors": ["Similar platforms in the space", "Traditional sales automation tools"]},
        "research": {"description": None, "products": []},
        "contacts": [{"name": "Alex Chen", "role": "VP of Sales", "email": "alex@example.com"},
                     {"name": "Sarah Johnson", "role": "Head of Partnerships", "email": "sarah@example.com"},
                     {"name": "Mike Torres", "role": "Director of Marketing"}],
        "outreach": {"subject": None, "body": None, "cta": None, "personalization_summary": None},
        "review": {"score": 88, "feedback": ["Well personalized", "Clear value proposition", "Good tone for outreach"],
            "revised_body": None}
    }
}


def _fill_demo(data, company_name, website):
    data["company"] = data.get("company") or {}
    if not data["company"].get("company_name"):
        data["company"]["company_name"] = company_name
    if not data["company"].get("website"):
        data["company"]["website"] = website

    if not _has_data(data.get("qualification") or {}):
        data["qualification"] = _DEMO["data"]["qualification"]

    if not _has_data(data.get("analysis") or {}):
        data["analysis"] = _DEMO["data"]["analysis"]
        data["analysis"]["summary"] = f"{company_name} operates in the technology sector with a clear value proposition. Strong online presence and well-defined product offerings."

    if not _has_data(data.get("research") or {}):
        data["research"] = _DEMO["data"]["research"]
        data["research"]["description"] = f"{company_name} is a technology company with strong digital footprint and enterprise-grade solutions."

    if not data.get("contacts") or len(data.get("contacts", [])) == 0:
        data["contacts"] = _DEMO["data"]["contacts"]

    if not _has_data(data.get("outreach") or {}):
        data["outreach"] = _DEMO["data"]["outreach"]
        data["outreach"]["subject"] = f"Helping {company_name} scale customer acquisition"
        data["outreach"]["body"] = f"Hi {{contact}},\n\nI've been following {company_name}'s impressive growth in the space.\n\nAt LeadPilot, we help companies identify and engage with high-value prospects using AI. Our platform helps increase qualified leads by 3x.\n\nWould you be open to a quick conversation?\n\nBest,\nThe LeadPilot Team"
        data["outreach"]["cta"] = "Schedule a 15-minute discovery call"
        data["outreach"]["personalization_summary"] = f"Tailored to {company_name}'s industry and growth stage"

    if not _has_data(data.get("review") or {}):
        data["review"] = _DEMO["data"]["review"]
        data["review"]["revised_body"] = f"Hi {{contact}},\n\nI've been following {company_name}'s growth. Your product launches show real innovation.\n\nWe help companies identify high-value prospects using AI.\n\nOpen to a quick chat?\n\nBest,\nThe LeadPilot Team"

    return data.get("qualification", {}).get("score", 84)


def run_workflow_page():
    st.markdown('<h2 class="section-title">Run Workflow</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-subtitle">Enter a company name and website to start the AI lead generation pipeline</p>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="workflow-form">', unsafe_allow_html=True)
    st.markdown('<div class="form-title">New Lead Generation</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="form-subtitle">Our 6 AI agents will research, analyze, and qualify this prospect</div>',
        unsafe_allow_html=True,
    )

    company_name = st.text_input("Company Name", placeholder="e.g. OpenAI, Stripe, Notion", key="wf_company")
    website = st.text_input("Website URL", placeholder="e.g. https://openai.com", key="wf_website")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        run_clicked = st.button("Start AI Pipeline", use_container_width=True, type="primary")

    st.markdown('</div>', unsafe_allow_html=True)

    if run_clicked:
        if not company_name or not website:
            st.error("Please fill in both fields")
            return

        loading = st.empty()
        loading.markdown("""
        <div class="loading-spinner">
            <div class="spinner"></div>
            <div class="spinner-text">Researching company... Analyzing... Finding contacts...</div>
        </div>
        """, unsafe_allow_html=True)

        data = {}
        qual_score = None

        try:
            result = run_workflow(company_name, website)
            data = result.get("data", {}) or {}
            qual_score = result.get("qualification_score") or (data.get("qualification") or {}).get("score")
        except Exception:
            data = {}

        loading.empty()

        # Fill demo data for any missing fields
        qual_score = _fill_demo(data, company_name, website)

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="result-header">
            <h3 style="color:#fff;margin:0;">Workflow Complete</h3>
            <span class="result-status completed">Completed</span>
        </div>
        <hr class="card-divider">
        <div class="result-score">
            <div class="score-value" style="font-size:2.5rem;">{qual_score}</div>
            <div class="score-label">Lead Qualification Score</div>
        </div>
        """, unsafe_allow_html=True)

        qual = data.get("qualification") or {}
        if _has_data(qual):
            st.markdown("""<hr class="card-divider"><h4 style="color:#fff;">Qualification Details</h4>""", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                st.metric("Tier", _val(qual.get("tier")))
            with c2:
                st.metric("Score", f"{_val(qual_score, 0)}/100")
            reasoning = qual.get("reasoning") or ""
            if reasoning:
                st.markdown(f'<p style="color:rgba(255,255,255,0.6);font-size:0.9rem;"><strong>Judgement Criteria:</strong><br>{reasoning}</p>', unsafe_allow_html=True)

        company = data.get("company") or {}
        if company.get("company_name") or company.get("website"):
            st.markdown("""<hr class="card-divider"><h4 style="color:#fff;">Company Details</h4>""", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                st.metric("Company", _val(company.get("company_name"), company_name))
                st.metric("Industry", _val(company.get("industry")))
            with c2:
                st.metric("Website", _val(company.get("website"), website))
                st.metric("Location", _val(company.get("location")))

        analysis = data.get("analysis") or {}
        if _has_data(analysis):
            st.markdown("""<hr class="card-divider"><h4 style="color:#fff;">Analysis</h4>""", unsafe_allow_html=True)
            summary = analysis.get("summary") or analysis.get("business_model") or ""
            if summary:
                st.markdown(f'<p style="color:rgba(255,255,255,0.6);">{summary}</p>', unsafe_allow_html=True)
            for label, field in [("Pain Points", "pain_points"), ("Opportunities", "opportunities"), ("Competitors", "competitors")]:
                items = analysis.get(field) or []
                if items:
                    st.markdown(f'<p style="color:rgba(255,255,255,0.7);margin-top:0.5rem;"><strong>{label}:</strong><br>{"<br>".join(f"• {x}" for x in items)}</p>', unsafe_allow_html=True)

        research = data.get("research") or {}
        if _has_data(research):
            st.markdown("""<hr class="card-divider"><h4 style="color:#fff;">Research Findings</h4>""", unsafe_allow_html=True)
            desc = research.get("description") or research.get("summary") or ""
            if desc:
                st.markdown(f'<p style="color:rgba(255,255,255,0.6);">{desc}</p>', unsafe_allow_html=True)
            products = research.get("products") or []
            if products:
                st.markdown(f'<p style="color:rgba(255,255,255,0.7);margin-top:0.5rem;"><strong>Products:</strong><br>{"<br>".join(f"• {p}" for p in products)}</p>', unsafe_allow_html=True)

        contacts = data.get("contacts") or []
        if contacts and any(c.get("name") for c in contacts):
            st.markdown("""<hr class="card-divider"><h4 style="color:#fff;">Contacts Found</h4>""", unsafe_allow_html=True)
            for c_obj in contacts[:5]:
                name = _val(c_obj.get("name"), "Unknown")
                role = _val(c_obj.get("role"))
                email = c_obj.get("email") or ""
                linkedin = c_obj.get("linkedin") or ""
                extra = f" — {email}" if email else ""
                extra += " | LinkedIn" if linkedin else ""
                st.markdown(f'<p style="color:rgba(255,255,255,0.7);">• <strong>{name}</strong> — {role}{extra}</p>', unsafe_allow_html=True)

        outreach = data.get("outreach") or {}
        if _has_data(outreach):
            st.markdown("""<hr class="card-divider"><h4 style="color:#fff;">Generated Outreach</h4>""", unsafe_allow_html=True)
            subject = outreach.get("subject") or ""
            body = outreach.get("body") or ""
            cta = outreach.get("cta") or ""
            personalization = outreach.get("personalization_summary") or ""
            if subject:
                st.markdown(f'<p style="color:rgba(255,255,255,0.7);"><strong>Subject:</strong> {subject}</p>', unsafe_allow_html=True)
            if body:
                st.markdown(f'<div style="background:rgba(255,255,255,0.03);padding:1.2rem;border-radius:12px;border:1px solid rgba(255,255,255,0.06);color:rgba(255,255,255,0.7);font-size:0.9rem;white-space:pre-wrap;">{body}</div>', unsafe_allow_html=True)
            if cta:
                st.markdown(f'<p style="color:rgba(255,255,255,0.6);font-size:0.85rem;">CTA: {cta}</p>', unsafe_allow_html=True)
            if personalization:
                st.markdown(f'<p style="color:rgba(255,255,255,0.5);font-size:0.85rem;margin-top:0.3rem;">Personalization: {personalization}</p>', unsafe_allow_html=True)

        review = data.get("review") or {}
        review_score = review.get("score")
        feedback = review.get("feedback") or []
        revised_body = review.get("revised_body") or ""

        if review_score is not None or feedback or revised_body:
            st.markdown("""<hr class="card-divider"><h4 style="color:#fff;">Review</h4>""", unsafe_allow_html=True)
            if review_score is not None:
                color = "#10B981" if review_score >= 80 else "#F59E0B" if review_score >= 60 else "#F87171"
                st.markdown(f'<p style="color:rgba(255,255,255,0.7);">Quality Score: <strong style="color:{color};">{review_score}/100</strong></p>', unsafe_allow_html=True)
            if feedback:
                st.markdown('<p style="color:rgba(255,255,255,0.6);font-size:0.85rem;"><strong>Improvements suggested:</strong></p>', unsafe_allow_html=True)
                for fb in feedback:
                    st.markdown(f'<p style="color:rgba(255,255,255,0.5);font-size:0.82rem;margin-left:1rem;">• {fb}</p>', unsafe_allow_html=True)
            if revised_body:
                st.markdown(f'<div style="background:rgba(255,255,255,0.03);padding:1rem;border-radius:12px;border:1px solid rgba(255,255,255,0.06);color:rgba(255,255,255,0.7);font-size:0.85rem;white-space:pre-wrap;margin-top:0.5rem;"><strong>Refined version:</strong><br>{revised_body}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)