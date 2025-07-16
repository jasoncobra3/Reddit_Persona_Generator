# 🤖 Reddit User Persona Generator

This project is a Generative AI-powered Reddit User Persona Generator that analyzes a user's public Reddit activity - comments and posts to generate a rich, human-like persona. It leverages Large Language Models (LLMs) via **Groq** and is orchestrated using **LangChain**, providing deep behavioral insights, motivations, and personality traits based on natural language patterns.

---

## 📌 Features

- 🔗 Accepts any public Reddit user profile URL
- 🧹 Scrapes all available comments and posts using Reddit's PRAW API
- 🧠 Generates an in-depth user persona using Groq's LLM (e.g., Mixtral)
- 📄 Outputs the persona to a clean `.txt` file in the `outputs/` folder
- 📌 Cites specific posts/comments for each personality trait

---

### 📸 Screenshots

#### 🧠 AI Persona Generator UI
![UI](<img width="1275" height="627" alt="image" src="https://github.com/user-attachments/assets/1c97159c-757f-4256-836e-378fb9768e1f" />)

#### 📄 Example Persona Output
![Output](<img width="1273" height="617" alt="image" src="https://github.com/user-attachments/assets/8591a3ad-eec5-4a24-913b-01b1f5c8b175" />
)

---

## 🛠️ Tech Stack

| Purpose         | Technology Used         |
|-----------------|--------------------------|
| Web scraping    | Python + PRAW            |
| LLM pipeline    | LangChain + Groq (Mixtral) |
| Secrets mgmt    | python-dotenv            |
| Output          | `.txt` user persona files |
| Future (optional) | `python-pptx` for visual persona |

---

## 📂 Project Structure

```
Reddit_Persona_Generator/
├── reddit_scraper.py         # Fetches user comments/posts
├── persona_generator.py      # Generates persona using LLM
├── main.py                   # Main entry point
├── .env                      # API credentials (ignored in .gitignore)
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── .gitignore                # Hides secrets, venv, and outputs
└── outputs/
    ├── kojied.txt
    └── Hungry-Move-6603.txt
```






---
## 🔐 .env Setup
Create a `.env` file in the root folder with:

  ```env
  REDDIT_CLIENT_ID=your_reddit_client_id
  REDDIT_CLIENT_SECRET=your_reddit_client_secret
  REDDIT_USERNAME=your_reddit_username
  REDDIT_PASSWORD=your_reddit_password
  USER_AGENT=YourScriptName by u/yourusername
  GROQ_API_KEY=your_groq_api_key
 ```
---
## 🚀 How to Run

1. **Clone the Repo**
   ```bash
   git clone https://github.com/your-username/beyondchats_ai_intern.git
   cd beyondchats_ai_intern

2. **Create Virtual Environment**
   ```bash
   python -m venv reddit_persona
    # Windows:
    reddit_persona\Scripts\activate
    # macOS/Linux:
    source reddit_persona/bin/activate

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run the Script**
   ```bash
   python main.py
   
- 👉 Enter a Reddit profile URL when prompted.
- 📝 Output will be saved in `outputs/<username>.txt`

---

## 📄 Sample Output

### User Persona: kojied

#### Personality Traits
- Strategic Thinker
- Analytical
- Socially Aware

#### Goals
- Strategic resource management
- Creative consistency

#### Direct Quotes
1. "You have to kill the bandit units..." — [Reddit Comment]

---

## ⚠️ Notes
- Only public Reddit profiles with visible comment/post history can be analyzed.
- Quotes are extracted to reflect traits where applicable.
- Personality bars and inferred professions are approximations based on LLM predictions.

--- 

## 🌟 Future Improvements
- Generate persona slides or images using `python-pptx`
- Add Streamlit web UI for user input
- Visualize traits with charts or graphs

---
## 🤝 Contributing
**Feel free to fork, star, or submit a pull request to contribute improvements!**
