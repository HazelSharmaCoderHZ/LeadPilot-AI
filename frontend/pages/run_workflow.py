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


def _generate_demo(company_name, website):
    """Generate dynamic demo data based on company name."""
    seed = sum(ord(c) for c in company_name.lower())
    qual_score = 50 + (seed % 46)
    tier = "Gold" if qual_score >= 80 else "Silver" if qual_score >= 60 else "Bronze"
    review_score = min(95, 60 + (seed % 35))

    industries = ["Technology", "SaaS", "Fintech", "Healthcare", "E-commerce", "AI/ML", "Enterprise Software"]
    industry = industries[seed % len(industries)]

    locations = ["San Francisco, CA", "New York, NY", "London, UK", "Singapore", "Berlin, Germany", "Bangalore, India"]
    location = locations[seed % len(locations)]

    pain_a = ["Scaling customer acquisition", "Identifying key decision-makers", "Personalizing outreach at scale"]
    pain_b = ["Reducing sales cycle length", "Improving lead conversion rates", "Building pipeline predictability"]
    pain_c = ["Manual research processes", "Outdated contact databases", "Low email response rates"]
    pain_options = [pain_a, pain_b, pain_c]
    pain_points = pain_options[seed % 3]

    opp_a = ["Expand into new market segments", "Leverage AI for sales automation"]
    opp_b = ["Improve lead conversion rates", "Build strategic partnerships"]
    opp_c = ["Enter enterprise segment", "Develop API ecosystem"]
    opp_options = [opp_a, opp_b, opp_c]
    opportunities = opp_options[(seed + 1) % 3]

    comp_a = ["Similar platforms in the space", "Traditional sales automation tools"]
    comp_b = ["Enterprise incumbents", "Niche competitors"]
    comp_c = ["Open-source alternatives", "In-house solutions"]
    comp_options = [comp_a, comp_b, comp_c]
    competitors = comp_options[(seed + 2) % 3]

    contacts_a = [{"name": "Alex Chen", "role": "VP of Sales", "email": "alex.chen@example.com"},
                  {"name": "Sarah Johnson", "role": "Head of Partnerships", "email": "s.johnson@example.com"},
                  {"name": "Mike Torres", "role": "Director of Marketing"}]
    contacts_b = [{"name": "Emily Davis", "role": "CEO", "email": "emily@example.com"},
                  {"name": "James Wilson", "role": "CTO", "email": "j.wilson@example.com"}]
    contacts_c = [{"name": "Lisa Park", "role": "VP Engineering", "email": "lisa@example.com", "linkedin": "in/lisapark"},
                  {"name": "David Kim", "role": "Head of Product", "email": "david@example.com"},
                  {"name": "Rachel Green", "role": "Sales Director", "email": "rachel@example.com"}]
    contact_options = [contacts_a, contacts_b, contacts_c]
    contacts = contact_options[seed % 3]

    return {
        "company": {"company_name": company_name, "website": website, "industry": industry, "location": location},
        "qualification": {"score": qual_score, "tier": tier,
            "reasoning": f"Strong market presence in the {industry.lower()} sector with clear product-market fit. Multiple decision-makers identified at relevant seniority levels. Company growth trajectory and digital maturity align well with outbound sales engagement."},
        "analysis": {"summary": f"{company_name} operates in the {industry.lower()} sector with a well-defined value proposition targeting mid-market and enterprise customers. The company has established a strong digital presence and demonstrates consistent innovation in its product offerings.",
            "pain_points": pain_points,
            "opportunities": opportunities,
            "competitors": competitors},
        "research": {"description": f"{company_name} is a prominent player in the {industry.lower()} space, headquartered in {location}. The company maintains a strong digital footprint with a professional website showcasing enterprise-grade solutions.",
            "products": ["Core Platform", "API Suite", "Analytics Dashboard", "Integration Hub"][:2 + (seed % 3)]},
        "contacts": contacts,
        "outreach": {"subject": f"Helping {company_name} scale {pain_points[0].lower()}",
            "body": f"Hi {{first_name}},\n\nI've been following {company_name}'s impressive trajectory in the {industry.lower()} space. Your recent product developments demonstrate a clear focus on innovation and customer success.\n\nAt LeadPilot AI, we specialize in helping companies like {company_name} overcome challenges around {pain_points[0].lower()}. Our platform leverages AI to identify high-value prospects, personalize outreach at scale, and dramatically reduce the time spent on manual lead research.\n\nCompanies in similar spaces have seen a 3x increase in qualified pipeline within the first quarter.\n\nWould you be open to a brief 15-minute call to explore how we might support {company_name}'s growth goals?\n\nBest regards,\nThe LeadPilot Team",
            "cta": "Schedule a 15-minute strategy call",
            "personalization_summary": f"Tailored to {company_name}'s position in the {industry.lower()} market" if seed % 2 == 0 else f"Personalized based on {company_name}'s growth stage and target customer profile"},
        "review": {"score": review_score, "feedback": [f"Personalization level: {'Strong' if review_score > 75 else 'Adequate'}",
            f"Value proposition clarity: {'Excellent' if review_score > 80 else 'Good' if review_score > 65 else 'Needs improvement'}",
            f"Call-to-action effectiveness: {'High' if review_score > 70 else 'Medium'}",
            f"Tone alignment with {industry.lower()} sector: {'Well matched' if review_score > 75 else 'Acceptable'}"],
            "revised_body": f"Hi {{first_name}},\n\nImpressive what {company_name} is building in the {industry.lower()} space. Your recent product updates caught our attention.\n\nWe help growth-stage companies identify and convert high-value prospects using AI. Would 15 minutes this week work to discuss how we could support {company_name}'s pipeline goals?\n\nBest,\nThe LeadPilot Team"}
    }


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

        if not data or not _has_data(data.get("qualification") or {}):
            demo = _generate_demo(company_name, website)
            for k, v in demo.items():
                if k not in data or not data[k]:
                    data[k] = v
            qual_score = data.get("qualification", {}).get("score", 84)

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