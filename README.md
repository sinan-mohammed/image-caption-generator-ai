# AI SaaS Idea Validator – Multi-Agent System

A Multi-Agent AI system that validates startup ideas by performing:

* Market Research
* Competitor Analysis
* Monetization Planning
* Risk Estimation

The system generates a structured validation report to help founders assess feasibility before building.

---

# System Architecture

## High-Level Architecture Diagram

```
                          ┌─────────────────────┐
                          │     Streamlit UI    │
                          │  (User Input Layer) │
                          └──────────┬──────────┘
                                     │
                                     ▼
                          ┌─────────────────────┐
                          │    Orchestrator     │
                          │ (Agent Controller)  │
                          └──────────┬──────────┘
                                     │
         ┌─────────────────┬─────────────────┬──────────────────┐
         ▼                 ▼                 ▼                  ▼
┌─────────────────┐ ┌──────────────┐ ┌───────────────┐ ┌────────────────┐
│ Market Research │ │ Competitor   │ │  Monetization │ │ Risk Estimator │
│     Agent       │ │    Agent     │ │     Agent     │ │     Agent      │
└────────┬────────┘ └──────┬───────┘ └───────┬───────┘ └────────┬───────┘
         │                 │                 │                  │
         ▼                 ▼                 ▼                  ▼
   Google Search        Google Search        LLM              LLM
     (Serper API)       (Serper API)      (Groq API)      (Groq API)
         │                 │                 │                  │
         └─────────────────┴─────────┬───────┴──────────────────┘
                                     ▼
                            ┌──────────────────┐
                            │ Report Generator │
                            └────────┬─────────┘
                                     ▼
                           Final Validation Report
```

---

# Multi-Agent Workflow

1. User enters startup idea in Streamlit UI.
2. Orchestrator receives idea.
3. Orchestrator triggers all specialized agents.
4. Each agent:

   * Fetches relevant data (via Serper API if needed)
   * Sends structured prompt to Groq LLM
   * Returns formatted analysis
5. Report Generator aggregates all responses.
6. Final report is displayed in Streamlit UI.
7. Logs are stored for debugging and traceability.

---

# Agents Overview

## 1️.Market Research Agent

Responsible for:

* TAM / SAM / SOM estimation
* Market growth rate
* Target audience segmentation
* Industry trends

Uses:

* Serper API (Google search)
* Groq LLM

---

## 2️.Competitor Finder Agent

Responsible for:

* Identifying top competitors
* Extracting pricing models
* Comparing features
* Building competitor table

Uses:

* Serper API
* Groq LLM

---

## 3️.Monetization Analyst Agent

Responsible for:

* Revenue model selection
* Pricing tier recommendations
* Upsell strategies
* Revenue projections

Uses:

* Groq LLM

---

## 4️.Risk Estimator Agent

Responsible for:

* Technical risk analysis
* Market risk analysis
* Regulatory risk identification
* Overall risk score
* Go / No-Go recommendation

Uses:

* Groq LLM

---

# Project Structure

```
ai-saas-validator/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── config/
│   └── settings.py
│
├── agents/
│   ├── market_agent.py
│   ├── competitor_agent.py
│   ├── monetization_agent.py
│   └── risk_agent.py
│
├── core/
│   ├── orchestrator.py
│   ├── report_generator.py
│   └── search_tool.py
│
└── utils/
    ├── logger.py
    └── helpers.py
```

---

# Tech Stack (Free Tier)

| Component  | Tool                  |
| ---------- | --------------------- |
| LLM        | Groq API (LLaMA 3)    |
| Web Search | Serper API            |
| UI         | Streamlit             |
| Language   | Python                |
| Logging    | Python Logging Module |

---

# Installation Guide

## 1️.Clone Repository

```bash
git clone https://github.com/yourusername/ai-saas-validator.git
cd ai-saas-validator
```

---

## 2️.Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

## 3️.Install Dependencies

```bash
pip install -r requirements.txt
```

Minimal recommended requirements:

```
streamlit
groq
requests
python-dotenv
```

---

## 4️.Setup API Keys

Create `.env` file in root directory:

```
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

---

## 5️.Run Application

```bash
streamlit run app.py
```

---

# Output Format

The system generates:

* Executive Summary
* Market Analysis (TAM/SAM/SOM)
* Competitor Landscape
* Monetization Strategy
* Risk Assessment
* Go / No-Go Recommendation

---

# Logging & Error Handling

The system includes:

* Centralized logging (`utils/logger.py`)
* Rotating log files
* Error tracking for:

  * LLM failures
  * Search API failures
  * Agent execution issues

Logs stored in:

```
logs/app.log
```

---

# Evaluation Criteria Coverage

* Agent Collaboration Logic
* Prompt Engineering
* Market Research Accuracy
* Clean Code Structure
* Logging & Error Handling
* Structured Report Generation
* Streamlit UI

---

# Future Improvements

* Parallel agent execution (async)
* Vector database memory (ChromaDB)
* PDF report export
* Competition heatmap visualization
* User authentication
* SaaS deployment (Render / Railway)
* LangGraph or CrewAI integration
* Multi-LLM fallback system

---

# License

MIT License

---

# Author Note

This project demonstrates how multi-agent AI systems can simulate real-world startup validation workflows using modular architecture and free-tier APIs.
