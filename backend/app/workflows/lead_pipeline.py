from langgraph.graph import StateGraph, START, END

from app.schemas.state import LeadPilotState
from app.agents.dummy import DummyAgent


dummy_agent = DummyAgent()


def dummy_node(state: LeadPilotState):
    return dummy_agent.execute(state)


builder = StateGraph(LeadPilotState)

builder.add_node("dummy", dummy_node)

builder.add_edge(START, "dummy")
builder.add_edge("dummy", END)

lead_pipeline = builder.compile()