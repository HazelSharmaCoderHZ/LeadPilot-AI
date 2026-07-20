import streamlit as st


STEPS = [
    ("🔍", "Research", "Enter company name and website URL to begin crawling"),
    ("🧠", "Analysis", "Gemini AI extracts business model and pain points"),
    ("👥", "Contacts", "Tavily search finds key decision-makers and roles"),
    ("⭐", "Qualification", "Lead scored on intent, fit, and engagement"),
    ("📤", "Outreach", "Personalized cold email generated for each prospect"),
    ("✅", "Review", "AI quality check verifies tone and accuracy"),
]


def render_workflow():
    st.markdown('<h2 class="section-title">AI Workflow Pipeline</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-subtitle">From cold prospect to qualified opportunity in 6 automated steps</p>',
        unsafe_allow_html=True,
    )

    # --- structural/motion CSS only — no new colors introduced ---
    st.markdown("""
    <style>
    .workflow-timeline {
        position: relative;
        margin-top: 2.5rem;
        padding-left: 0;
    }

    .workflow-step {
        position: relative;
        display: flex;
        align-items: flex-start;
        gap: 1.25rem;
        padding-bottom: 2.25rem;
        opacity: 0;
        transform: translateY(16px);
        animation: stepReveal 0.6s ease forwards;
    }

    .workflow-step:last-child { padding-bottom: 0; }

    @keyframes stepReveal {
        to { opacity: 1; transform: translateY(0); }
    }

    /* numbered node */
    .step-number {
        position: relative;
        z-index: 2;
        flex-shrink: 0;
        width: 44px;
        height: 44px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 1.05rem;
        line-height: 1;
    }

    .step-icon {
        position: absolute;
        top: -10px;
        right: -8px;
        font-size: 1rem;
        filter: drop-shadow(0 1px 2px rgba(0,0,0,0.4));
    }

    /* connecting spine — neutral, theme-agnostic */
    .workflow-step:not(:last-child) .step-number::after {
        content: "";
        position: absolute;
        top: 44px;
        left: 50%;
        transform: translateX(-50%);
        width: 2px;
        height: calc(100% + 2.25rem - 44px);
        background: linear-gradient(
            to bottom,
            currentColor 0%,
            transparent 100%
        );
        opacity: 0.25;
        z-index: 1;
    }

    /* downward chevron riding the spine, midway between nodes */
    .step-arrow {
        position: absolute;
        left: 22px;
        top: calc(44px + 1rem);
        transform: translateX(-50%);
        font-size: 0.85rem;
        opacity: 0.35;
        animation: arrowPulse 2s ease-in-out infinite;
        z-index: 1;
    }

    @keyframes arrowPulse {
        0%, 100% { opacity: 0.2; transform: translate(-50%, 0); }
        50% { opacity: 0.55; transform: translate(-50%, 4px); }
    }

    .step-content {
        flex: 1;
        padding-top: 0.35rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid rgba(128,128,128,0.12);
        transition: transform 0.25s ease, opacity 0.25s ease;
    }

    .workflow-step:last-child .step-content { border-bottom: none; }

    .step-content:hover {
        transform: translateX(4px);
    }

    .step-title {
        font-weight: 700;
        font-size: 1.05rem;
        margin-bottom: 0.2rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .step-eyebrow {
        font-size: 0.72rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        opacity: 0.5;
        font-weight: 600;
    }

    .step-desc {
        font-size: 0.92rem;
        opacity: 0.75;
        line-height: 1.45;
    }

    @media (max-width: 600px) {
        .workflow-step { gap: 0.85rem; }
        .step-number { width: 36px; height: 36px; font-size: 0.9rem; }
    }

    @media (prefers-reduced-motion: reduce) {
        .workflow-step, .step-arrow {
            animation: none !important;
            opacity: 1 !important;
            transform: none !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="workflow-timeline">', unsafe_allow_html=True)
    for i, (icon, title, desc) in enumerate(STEPS):
        is_last = i == len(STEPS) - 1
        st.markdown(f"""
        <div class="workflow-step" style="animation-delay:{i * 0.12}s">
            <div class="step-number completed">
                {i + 1}
                <span class="step-icon">{icon}</span>
            </div>
            <div class="step-content">
                <div class="step-eyebrow">Step {i + 1} of {len(STEPS)}</div>
                <div class="step-title">{title}</div>
                <div class="step-desc">{desc}</div>
            </div>
            {'' if is_last else '<div class="step-arrow">⌄</div>'}
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)