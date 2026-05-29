import os
import json
from typing import TypedDict, List, Dict
from datetime import datetime
from dotenv import load_dotenv
from litellm import completion
from langgraph.graph import StateGraph, END

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

UNCENSORED_MODELS = {
    "default": "HuggingFaceH4/zephyr-7b-beta",
    "creative": "Qwen/Qwen2.5-72B-Instruct",
    "uncensored": "gryphe/mythalion-13b",
    "powerful": "meta-llama/Llama-3.1-70B-Instruct",
    "dark": "TheBloke/DarkIdol-Llama-3.1-70B-Instruct"
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

    def get_context(self, mission_id: str) -> Dict:
        return self.sessions.get(mission_id, {})

memory = CloudMemory()

def call_uncensored_llm(prompt: str, model: str = "default", temperature: float = 0.85):
    model_name = UNCENSORED_MODELS.get(model, UNCENSORED_MODELS["default"])
    response = completion(
        model=f"huggingface/{model_name}",
        messages=[{"role": "user", "content": prompt}],
        api_key=HF_TOKEN,
        temperature=temperature,
        max_tokens=4096,
        top_p=0.95,
    )
    return response.choices[0].message.content

def observe(state: AgentState) -> AgentState:
    print(f"[Observe] Processing mission {state['mission_id']}")
    return state

def think(state: AgentState) -> AgentState:
    last_message = state["messages"][-1]["content"]
    prompt = f"""
You are Monico Uncensored (Paid Tier).
Mission: {state.get('mission_id')}

User request: {last_message}

Think step-by-step and respond in valid JSON.
"""
    response_text = call_uncensored_llm(prompt, model="uncensored", temperature=0.9)
    try:
        decision = json.loads(response_text)
        state["messages"].append({"role": "assistant", "content": str(decision)})
        state["context"]["last_decision"] = decision
    except:
        state["messages"].append({"role": "assistant", "content": response_text})
    return state

def act(state: AgentState) -> AgentState:
    decision = state["context"].get("last_decision", {})
    state["messages"].append({"role": "system", "content": f"Action completed for {decision.get('tool')}" })
    return state

def evaluate(state: AgentState) -> AgentState:
    reflection = call_uncensored_llm("Evaluate success.")
    state["lessons_learned"].append({"timestamp": datetime.now().isoformat(), "reflection": reflection})
    state["next"] = END if "success" in reflection.lower() or len(state["messages"]) > 12 else "think"
    return state

def build_uncensored_graph():
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

async def run_monico_uncensored(user_input: str, mission_id: str = None):
    if not mission_id:
        mission_id = f"mission_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    state = AgentState(messages=[{"role": "user", "content": user_input}], next="think", mission_id=mission_id, context={}, lessons_learned=[])
    graph = build_uncensored_graph()
    result = await graph.ainvoke(state)
    memory.save_context(mission_id, {"final_state": result})
    return result

if __name__ == "__main__":
    print("🚀 Monico Uncensored (Paid) Ready - No local deps")