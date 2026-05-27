# 🤖 Project 1 — Rule-Based AI Chatbot


## 📌 Project Overview

This project implements a **Rule-Based AI Chatbot** — the foundational milestone of the DecodeLabs AI Engineering track. Unlike machine learning models, this chatbot operates entirely on **hand-crafted logical rules**, `if/elif/else` conditions, and **pattern matching** to simulate intelligent conversation.

> *"Before machines can learn, they must first follow rules."*

---

## 🎯 Goal

Build a functional AI chatbot that:
- Understands user intent through keyword matching
- Responds intelligently using predefined rule sets
- Handles unknown inputs gracefully with fallback responses
- Demonstrates the foundation of conversational AI design

---

## 📂 Repository Structure

```
DecodeLabs-Project1-RuleBasedAI-Chatbot/
│
├── chatbot.py               ← Main chatbot script
├── rules.py                 ← Rule definitions and response logic
├── requirements.txt         ← Required Python packages
├── README.md                ← Project documentation (this file)
└── sample_output.png        ← Screenshot of chatbot in action
```

---

## ⚙️ Key Concepts Covered

| Concept              | Description                                      |
|----------------------|--------------------------------------------------|
| Rule-Based Logic     | IF/ELIF/ELSE decision trees                      |
| Pattern Matching     | Keyword detection in user input                  |
| Fallback Handling    | Default responses for unrecognized inputs        |
| Conversation Flow    | Multi-turn dialogue management                   |
| String Processing    | `.lower()`, `.strip()`, `in` keyword matching    |

---

## 🆚 Rule-Based vs Machine Learning

```
Rule-Based AI (This Project)       Machine Learning AI (Project 2+)
─────────────────────────────      ───────────────────────────────
✅ Fully transparent logic         ✅ Learns from data automatically
✅ No training data needed         ✅ Handles unseen inputs better
✅ Fast and predictable            ✅ Scales with complexity
❌ Cannot learn or improve         ❌ Needs large datasets
❌ Breaks on unexpected input      ❌ Black-box decisions
```

---

## 🚀 How to Run

### Prerequisites
```bash
Python 3.10 or higher
```

### Installation
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/DecodeLabs-Project1-RuleBasedAI-Chatbot.git

# Navigate into the folder
cd DecodeLabs-Project1-RuleBasedAI-Chatbot

# Install dependencies
pip install -r requirements.txt
```

### Run the Chatbot
```bash
python chatbot.py
```

---

## 💬 Sample Interaction

```
============================================================
   DecodeLabs | Project 1 | Rule-Based AI Chatbot
============================================================

Bot: Hello! I am DecodeLabs AI Assistant. How can I help you?

You: What is artificial intelligence?
Bot: Artificial Intelligence is the simulation of human 
     intelligence by machines to perform tasks like learning, 
     reasoning, and problem-solving.

You: Tell me a joke
Bot: Why do programmers prefer dark mode? Because light 
     attracts bugs! 😄

You: bye
Bot: Goodbye! Have a great day. 👋
============================================================
```

---

## 📋 Requirements

```
# requirements.txt
# No external libraries required for basic version
# Standard Python built-ins only: re, string, random
```

---

## 📊 Project Evaluation Criteria

| Criteria               | Status  |
|------------------------|---------|
| Chatbot runs without errors | ✅ |
| Handles greetings / farewells | ✅ |
| Responds to AI-related questions | ✅ |
| Fallback for unknown inputs | ✅ |
| Clean, commented code | ✅ |
| README documentation | ✅ |

---

## 👤 Author

| Field        | Detail                          |
|--------------|---------------------------------|
| Name         | *[Your Full Name]*              |
| Batch        | DecodeLabs 2026                 |
| Track        | Artificial Intelligence         |
| Project      | 1 — Rule-Based AI Chatbot       |
| Submitted    | *[Submission Date]*             |

---


