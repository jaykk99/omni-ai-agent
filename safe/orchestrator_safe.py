import os
import json
from typing import TypedDict, List, Dict
from datetime import datetime
from dotenv import load_dotenv
from litellm import completion
from langgraph.graph import StateGraph, END

load_dotenv()

SAFE_MODELS = {
    "default": "groq/llama3-70b-8192"
}

class AgentState(TypedDict):
    messages: List[Dict]
    next: str
    mission_id: str
    context: Dict
    lessons_learned: List[Dict]

class CloudMemory:
    def __init__(self):
        self.sessions = {}

    def save_context(self, mission_id: str, data: Dict):
        self.sessions[mission_id] = data

memory = CloudMemory()

def call_safe_llm(prompt: str, model: str = "default", temperature: float = 0.7):
    model_name = SAFE_MODELS.get(model, SAFE_MODELS["default"])
    response = completion(model=model_name, messages=[{"role": "user", "content": prompt}], temperature=temperature, max_tokens=2048)
    return response.choices[0].message.content

def observe(state: AgentState) -> AgentState:
    print(f"[Safe] Mission {state['mission_id']}")
    return state

def think(state: AgentState) -> AgentState:
    last_message = state["messages"][-1]["content"]
    prompt = f"""
You are Monico Safe.
User request: {last_message}
Respond in JSON with reasoning and safe plan.
"""
    response_text = call_safe_llm(prompt, temperature=0.6)
    try:
        decision = json.loads(response_text)
        state["messages"].append({"role": "assistant", "content": str(decision)})
        state["context"]["last_decision"] = decision
    except:
        state["messages"].append({"role": "assistant", "content": response_text})
    return state

def act(state: AgentState) -> AgentState:
    state["messages"].append({"role": "system", "content": "Safe sandbox action executed"})
    return state

def evaluate(state: AgentState) -> AgentState:
    reflection = call_safe_llm("Evaluate last actions.")
    state["lessons_learned"].append({"timestamp": datetime.now().isoformat(), "reflection": reflection})
    state["next"] = END if "success" in reflection.lower() or len(state["messages"]) > 10 else "think"
    return state

def build_safe_graph():
    workflow = StateGraph(AgentState)
    workflow.add_node("observe", observe)
    workflow.add_node("think", think)
    workflow.add_node("act", act)
    workflow.add_node("evaluate", evaluate)
    workflow.set_entry_point("observe")
    workflow.add_edge("observe", "think")
    workflow.add_edge("think", "act")
    workflow.add_edge("act", "evaluate")
    workflow.add_conditional_edges("evaluate", lambda s: s.get("next", END))
    return workflow.compile()

async def run_monico_safe(user_input: str, mission_id: str = None):
    if not mission_id:
        mission_id = f"safe_mission_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    state = AgentState(messages=[{"role": "user", "content": user_input}], next="think", mission_id=mission_id, context={}, lessons_learned=[])
    graph = build_safe_graph()
    result = await graph.ainvoke(state)
    memory.save_context(mission_id, {"final_state": result})
    return result

if __name__ == "__main__":
    print("✅ Monico Safe (Sandbox) Ready")