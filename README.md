# Local GenAI Assistant & Evolutionary Prompt Optimization (PSO)

A complete local Generative AI ecosystem combining an offline **Customer Support AI Assistant** built with **Ollama** and **Streamlit**, alongside a **Nature-Inspired Computing (NIC)** module that uses **Particle Swarm Optimization (PSO)** to automatically optimize LLM prompts.

## 📌 Architectural Overview

This repository demonstrates two core paradigms of modern AI engineering:

1. **Local Privacy-First Execution:** Running `llama3.2:1b` locally via Ollama to guarantee air-gapped data safety without cloud dependencies.
2. **Automated Prompt Optimization (NIC ~ LLM):** Replacing manual prompt trial-and-error with Particle Swarm Optimization (PSO)—a swarm intelligence algorithm that searches prompt space to optimize model output quality.

   ┌────────────────┐        ┌──────────────────┐        ┌────────────────┐
   │  Ollama Engine │ ───►   │ Python Controller│ ───►   │ Streamlit UI   │
   │  (phi3:mini)   │        │ (Agent Pipeline) │        │(User Interface)│
   └────────────────┘        └──────────────────┘        └────────────────┘

---

## 🚀 Key Modules

### Module 1: Customer Support AI Triage (`01_support_ai_app.py`)
Utilizes a two-step **Chain-of-Thought** pipeline:
* **The Analyst:** Extracts customer intent, urgency, sentiment, product, and order details into structured JSON format.
* **The Writer:** Injects corporate business guidelines and customer analysis to synthesize a professional, empathetic email draft.

### Module 2: Particle Swarm Optimization for Prompts (`02_pso_prompt_optimization.py`)
Applies Nature-Inspired Swarm Intelligence to prompt engineering:
* **Particle:** Represents a candidate prompt variation.
* **Search Space:** All linguistic variations of the prompt instructions.
* **Fitness Function:** Evaluates generated outputs based on output length and keyword target hits (`FAQ`, `question`, `answer`, `summary`).
* **Mutation:** Introduces text transformations with a 30% probability to explore new search space trajectories and prevent getting stuck in local optima.

---

A beginner-friendly project that combines **Local Generative AI** with **Nature-Inspired Computing (NIC)**.

The project has two main parts:

1. A local **Customer Support AI Assistant** using Ollama and Streamlit.
2. A **Particle Swarm Optimization (PSO)** experiment that searches for better LLM prompts automatically.

---

## 1. What is NIC ~ LLM?

**NIC** means **Nature-Inspired Computing**.

**LLM** means **Large Language Model**.

In this project, we connect the two ideas:

> **Nature-Inspired Computing → Particle Swarm Optimization → Prompt Optimization → LLM**

Instead of manually trying many different prompts, PSO can be used to search through different prompt variations and find prompts that produce better results according to a chosen **fitness function**.

### Simple idea

Imagine a group of birds searching for food.

- Each bird represents a **particle**.
- Each particle represents a possible **prompt**.
- The quality of a prompt is its **fitness**.
- Particles learn from their own best result.
- Particles also learn from the best result found by the swarm.
- The swarm gradually searches for better solutions.

In our project:

```text
Particle
   ↓
Candidate Prompt
   ↓
LLM Response
   ↓
Fitness Score
   ↓
Better Prompt
```

---

# 2. What are we building?

The project contains two independent learning modules.

## Module 1 — Customer Support AI

The first application uses a local LLM to help process customer emails.

```text
Customer Email
      ↓
   Analyst
      ↓
Structured Information
      ↓
    Writer
      ↓
Professional Reply
```

The **Analyst** extracts useful information such as:

- Customer intent
- Urgency
- Sentiment
- Product
- Order information

The **Writer** then uses this information to create a professional response.

The application is built with:

- **Ollama** — runs the LLM locally
- **Python** — controls the application
- **Streamlit** — provides the web interface

---

# 3. Module 2 — PSO Prompt Optimization

The second module introduces **Nature-Inspired Computing**.

We use **Particle Swarm Optimization (PSO)** to experiment with different LLM prompts.

A simplified workflow is:

```text
Initial Prompts
      ↓
Create Particles
      ↓
Send Prompts to LLM
      ↓
Calculate Fitness
      ↓
Find Best Prompt
      ↓
Mutate / Improve Prompts
      ↓
Repeat
      ↓
Best Prompt
```

### Important PSO concepts

| PSO Concept | In This Project |
|---|---|
| Particle | A candidate prompt |
| Swarm | A group of candidate prompts |
| Position | Current prompt |
| Fitness | Quality score of the prompt |
| pBest | Particle's best prompt |
| gBest | Best prompt found by the swarm |
| Mutation | Small change to a prompt |
| Iteration | One optimization cycle |

The important learning point is that **PSO is normally designed for numerical search spaces**, while prompts are text.

Therefore, this project uses a simplified approach where PSO ideas are adapted to **text prompt variations**.

---

# 4. Project Structure

```text
Local-GenAI-Prompt-Optimization-PSO/
│
├── 01_support_ai_app.py
├── 02_pso_prompt_optimization.py
├── requirements.txt
├── .gitignore
├── README.md
└── Local_GenAI_Building_and_Evolutionary_Optimization.pdf
```

### Files

**`01_support_ai_app.py`**  
Customer support AI application.

**`02_pso_prompt_optimization.py`**  
PSO-based prompt optimization experiment.

**`requirements.txt`**  
Python dependencies required by the project.

**`README.md`**  
Project documentation and learning guide.

**PDF**  
Lecture notes and theoretical reference material.

---

# 5. Requirements

You need:

- Python 3.10+
- Ollama
- A local LLM such as `llama3.2:1b`
- Git
- A web browser

---

# 6. Install Ollama

Install Ollama from:

[Ollama](https://ollama.com?utm_source=chatgpt.com)

After installation, download and run the model:

```bash
ollama run llama3.2:1b
```

Keep Ollama running while using the Python applications.

---

# 7. Set Up the Project

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Local-GenAI-Prompt-Optimization-PSO.git
```

Move into the project:

```bash
cd Local-GenAI-Prompt-Optimization-PSO
```

Create a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

# 8. Run the Customer Support App

Start Streamlit:

```bash
streamlit run 01_support_ai_app.py
```

Open the address shown in the terminal, normally:

```text
http://localhost:8501
```

Enter a customer email and generate a response.

---

# 9. Run the PSO Experiment

Run:

```bash
python 02_pso_prompt_optimization.py
```

The program creates candidate prompts, evaluates them, and searches for a prompt with a better fitness score.

You should see information about:

- Particles
- Fitness scores
- pBest
- gBest
- Optimization iterations
- Best prompt

---

# 10. How the Learning Connects

The main idea of this project can be summarized as:

```text
Nature
  ↓
Swarm Intelligence
  ↓
Particle Swarm Optimization
  ↓
Search / Optimization
  ↓
Prompt Variations
  ↓
Large Language Model
  ↓
Evaluate Responses
  ↓
Improve Prompt
```

This demonstrates how an optimization technique inspired by nature can be applied to an LLM-related problem.

---

# 11. What You Should Learn

After completing this project, you should understand:

### Generative AI

- What an LLM is
- How to interact with a local LLM
- What prompt engineering means
- How structured output can be used in an AI pipeline

### Local AI

- What Ollama does
- How to run an LLM locally
- How Python can communicate with a local model

### Streamlit

- How to create a simple AI web application
- How users can interact with a Python AI program

### Nature-Inspired Computing

- What PSO is
- What particles and swarms represent
- What pBest and gBest mean
- How a fitness function guides optimization

### Prompt Optimization

- Why manually testing prompts can be inefficient
- How optimization can search for better prompt variations
- Why defining a good fitness function is important

---

# 12. A Simple Mental Model

Remember these three ideas:

**LLM**

> Generates an answer from a prompt.

**Fitness Function**

> Measures how good the result is.

**PSO**

> Searches for a better prompt.

Together:

```text
PSO
 ↓
Find better prompt
 ↓
LLM
 ↓
Generate response
 ↓
Fitness Function
 ↓
Measure response
 ↓
PSO improves search
```

---

## 13. Next Steps

Once the basic project works, try improving it.

Possible experiments:

1. Change the initial prompts.
2. Change the mutation strategy.
3. Create a better fitness function.
4. Penalize unwanted or irrelevant responses.
5. Add response-quality metrics.
6. Compare the original prompt with the optimized prompt.
7. Experiment with different local LLMs.

The goal is not just to run the code, but to understand **how optimization can be used to improve prompts for LLM applications**.
