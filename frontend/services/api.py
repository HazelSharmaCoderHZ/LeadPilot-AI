import requests
from config import BACKEND_URL

import streamlit as st

def run_workflow(company_name: str, website: str):
    st.write("Calling backend:", BACKEND_URL)

    resp = requests.post(
        f"{BACKEND_URL}/workflow/run",
        json={
            "company_name": company_name,
            "website": website,
        },
        timeout=300,
    )

    st.write(resp.status_code)

    resp.raise_for_status()
    return resp.json()

def get_history():
    resp = requests.get(f"{BACKEND_URL}/workflow/history", timeout=30)
    resp.raise_for_status()
    return resp.json()


def get_workflow(workflow_id: int):
    resp = requests.get(f"{BACKEND_URL}/workflow/{workflow_id}", timeout=30)
    resp.raise_for_status()
    return resp.json()