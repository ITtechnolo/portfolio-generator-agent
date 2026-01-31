# Order Completion Agent

An AI-powered agent built with **LangGraph** and **Google Gemini** that handles product orders through a multi-turn conversation.

## 🌟 Features
- **Multi-turn Interaction**: Handles product availability checks followed by order placement.
- **Stateful Management**: Uses LangGraph to maintain conversation stages (Checking vs. Ordering).
- **Concise Replies**: Generates clear, professional confirmation messages (1-2 sentences).
- **Robust Error Handling**: Includes fallback logic for API quota limits.

## 🛠️ Tech Stack
- **Python**
- **LangGraph** (State management)
- **LangChain** (AI Orchestration)
- **Google Generative AI (Gemini 2.0 Flash)**

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.11+
- A Google Gemini API Key

### 2. Installation
Clone the repository and install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory and add your API key:
```env
GOOGLE_API_KEY=your_actual_api_key_here
```

### 4. Usage
Run the interactive agent:
```bash
python main.py
```

## 🎥 Example Flow
1. **User**: "Do you have a Wireless Mouse?"
2. **Agent**: "Yes, Wireless Mouse is available."
3. **User**: "I want to order 2."
4. **Agent**: "Order completed successfully. Thank you!"

## 📄 License
MIT
