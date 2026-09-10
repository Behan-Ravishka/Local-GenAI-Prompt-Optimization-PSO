import streamlit as st
import numpy as np
import random
import requests
from typing import List, Tuple

class Particle:
    def __init__(self, prompt_template: str, dim: int = 1):
        self.position = np.array([prompt_template], dtype=object)
        self.velocity = np.zeros(dim, dtype=float)
        self.best_position = self.position.copy()
        self.best_score = -np.inf

# Fix: Switched from subprocess CLI to Ollama REST API for Streamlit compatibility
def call_ollama(prompt: str, context_text: str, timeout: int = 300) -> str:
    full_prompt = f"{prompt}\n\nContext:\n{context_text}"
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.2:1b",
        "prompt": full_prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=timeout)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.exceptions.Timeout:
        return "[ERROR: Ollama call timed out]"
    except requests.exceptions.ConnectionError:
        return "[ERROR: Could not connect to Ollama. Is 'ollama serve' running?]"
    except Exception as e:
        return f"[ERROR: {str(e)}]"


def fitness_function(prompt: str, context_text: str) -> Tuple[float, str]:
    output = call_ollama(prompt, context_text)
    if output.startswith("[ERROR:"):
        return 0.0, output

    length_score = len(output.split())
    keyword_hits = sum([kw in output.lower() for kw in ["faq", "question", "answer", "summary"]])
    score = length_score * 0.1 + keyword_hits * 5
    return score, output

def pso_optimize(prompts: List[str], context_text: str, num_iterations: int, status_container):
    particles = [Particle(prompt) for prompt in prompts]
    global_best_score = -np.inf
    global_best_prompt = None
    global_best_output = ""

    for it in range(num_iterations):
        status_container.write(f"**=== Iteration {it+1}/{num_iterations} ===**")
        for idx, p in enumerate(particles):
            score, output = fitness_function(p.position[0], context_text)

            # Print live scores to the UI so it doesn't look frozen
            status_container.write(f"Particle {idx+1}: Score={score:.2f}")

            if score > p.best_score:
                p.best_score = score
                p.best_position = p.position.copy()

            if score > global_best_score:
                global_best_score = score
                global_best_prompt = p.position[0]
                global_best_output = output

            if random.random() < 0.3:
                mutated = (
                    p.position[0]
                    .replace("Summarize", "Please summarize")
                    .replace("FAQ", "Frequently Asked Questions")
                    .replace("Q&A", "question and answer pairs")
                )
                p.position[0] = mutated

    return global_best_prompt, global_best_output, global_best_score


# UI Setup
st.set_page_config(page_title="PSO Prompt Optimization", page_icon="🧠", layout="wide")
st.title("🧠 PSO Prompt Optimization")
st.divider()

st.sidebar.header("⚙️ Optimization Settings")
num_iterations = st.sidebar.number_input("Number of PSO iterations", min_value=1, max_value=20, value=2, step=1)

st.subheader("📄 Context Text")
default_context = """Large Language Models (LLMs) are revolutionizing natural language processing.\nThey can summarize documents, answer questions, and generate creative content.\nHowever, results vary drastically depending on how prompts are phrased.\nFinding the best formulation is known as prompt engineering."""

context_text = st.text_area("Enter the document/context that Ollama should process:", value=default_context, height=150)

st.subheader("📝 Initial Prompts")
default_prompts = [
    "Summarize the following document into an FAQ style with answers:",
    "Create a Frequently Asked Questions section from this text:",
    "Turn this document into 5 question-and-answer pairs, concise and clear:"
]

prompt1 = st.text_area("Prompt 1", value=default_prompts[0], height=70)
prompt2 = st.text_area("Prompt 2", value=default_prompts[1], height=70)
prompt3 = st.text_area("Prompt 3", value=default_prompts[2], height=70)

st.divider()

if st.button("🚀 Run PSO Optimization", type="primary", use_container_width=True):
    valid_prompts = [p.strip() for p in [prompt1, prompt2, prompt3] if p.strip()]

    st.subheader("⏳ Optimization Progress (Live)")
    # Create an empty container to hold the live Jupyter-style text output
    status_container = st.container()

    with st.spinner("Evaluating prompts with Ollama (API)..."):
        best_prompt, best_output, best_score = pso_optimize(
            valid_prompts,
            context_text,
            num_iterations=int(num_iterations),
            status_container=status_container
        )

    st.divider()
    st.header("🏆 Optimization Results")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Best Fitness Score", f"{best_score:.2f}")
    with col2:
        st.metric("Number of Iterations", num_iterations)

    st.subheader("🥇 Best Prompt Found")
    st.code(best_prompt, language="text")

    st.subheader("📘 Best Generated Output")
    st.text_area("Ollama Output", value=best_output, height=300)
