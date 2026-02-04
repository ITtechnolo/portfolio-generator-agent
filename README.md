# Portfolio Project Idea Generator Agent 🚀

An AI-powered agent built with **LangChain** and **Google Gemini** that generates curated, innovative, and practical portfolio project ideas based on your area of interest.

## ✨ Features

- **Personalized Recommendations:** Generates ideas tailored to your specific field (e.g., Data Science, NLP, Web Dev, AI).
- **Innovative Concepts:** Focuses on beginner-to-intermediate friendly yet unique projects.
- **Actionable Prompts:** Provides a starting prompt for each idea to help you begin building immediately.
- **Structured Output:** Each suggestion includes a Title, a Statement of purpose, and a Building Prompt.

## 🛠️ Tech Stack

- **Language:** Python
- **AI Framework:** [LangChain](https://www.langchain.com/)
- **LLM:** [Google Gemini (Generative AI)](https://ai.google.dev/)
- **Environment Management:** `python-dotenv`

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- A Google AI Studio API Key. Get one for free [here](https://aistudio.google.com/app/apikey).

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ITtechnolo/portfolio-generator-agent.git
   cd portfolio-generator-agent
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**
   - Create a `.env` file in the root directory:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and add your API key:
     ```env
     GOOGLE_API_KEY=your_actual_api_key_here
     ```

### Usage

Run the agent and follow the interactive prompt:

```bash
python main.py
```

Example Input: `Natural Language Processing`

## 📝 Example Output

1. **Project Title:** AI Interview Prep Agent  
   **Statement:** A smart AI agent that generates interview questions and answers based on job roles.  
   **Prompt:** "Build an AI agent using LangChain that takes a job role as input and dynamically generates tailored interview questions with suggested answers."

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
