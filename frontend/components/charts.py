import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def render_charts():
    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-header">
            <h3>📈 Lead Score Distribution</h3>
            <div class="card-icon">📊</div>
        </div>
        """, unsafe_allow_html=True)

        scores = pd.DataFrame({
            "Range": ["0-20", "21-40", "41-60", "61-80", "81-100"],
            "Count": [5, 12, 28, 45, 62],
        })
        fig = px.bar(
            scores, x="Range", y="Count",
            color="Count", color_continuous_scale="blues",
            text="Count",
        )
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="rgba(255,255,255,0.7)",
            margin=dict(l=10, r=10, t=10, b=10),
            height=300,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False),
        )
        fig.update_traces(
            marker_line_color="rgba(37,99,235,0.3)",
            marker_line_width=1,
            textfont_color="#fff",
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-header">
            <h3>📊 Workflow Success Rate</h3>
            <div class="card-icon">🎯</div>
        </div>
        """, unsafe_allow_html=True)

        fig = go.Figure()
        fig.add_trace(go.Pie(
            labels=["Completed", "Running", "Failed"],
            values=[78, 15, 7],
            marker_colors=["#10B981", "#3B82F6", "#EF4444"],
            textinfo="label+percent",
            textfont_color="#fff",
            hole=0.5,
        ))
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="rgba(255,255,255,0.7)",
            margin=dict(l=10, r=10, t=10, b=10),
            height=300,
            showlegend=False,
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    c3, c4 = st.columns(2)

    with c3:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-header">
            <h3>📅 Weekly Workflows</h3>
            <div class="card-icon">📆</div>
        </div>
        """, unsafe_allow_html=True)

        weekly = pd.DataFrame({
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "Workflows": [18, 24, 31, 28, 35, 12, 8],
        })
        fig = px.line(
            weekly, x="Day", y="Workflows",
            markers=True,
        )
        fig.update_traces(
            line_color="#3B82F6",
            marker_color="#3B82F6",
            marker_size=8,
            line_width=3,
        )
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="rgba(255,255,255,0.7)",
            margin=dict(l=10, r=10, t=10, b=10),
            height=250,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False),
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c4:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-header">
            <h3>🏭 Top Industries</h3>
            <div class="card-icon">🏢</div>
        </div>
        """, unsafe_allow_html=True)

        industries = pd.DataFrame({
            "Industry": ["SaaS", "Fintech", "Healthcare", "E-commerce", "AI/ML"],
            "Count": [42, 28, 19, 15, 12],
        })
        fig = px.bar(
            industries, x="Count", y="Industry",
            orientation="h",
            color="Count", color_continuous_scale="blues",
            text="Count",
        )
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="rgba(255,255,255,0.7)",
            margin=dict(l=10, r=10, t=10, b=10),
            height=250,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False),
        )
        fig.update_traces(
            marker_line_color="rgba(37,99,235,0.3)",
            marker_line_width=1,
            textfont_color="#fff",
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)