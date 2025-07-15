
##Generates a user persona using Reddit content and Groq LLM via LangChain.
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from reddit_scraper import get_user_data


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def build_prompt(comments, posts, username):
    """
    Builds the prompt text from Reddit comments and posts.

    Args:
        comments (list): List of user comments.
        posts (list): List of user posts.
        username (str): Reddit username.

    Returns:
        str: Prompt string for LLM.
    """
    combined_text = "\n\n".join(
        [f"[Comment] {c['body']}" for c in comments[:10]] +
        [f"[Post] {p['title']} - {p['selftext']}" for p in posts[:5]]
    )
         

    prompt = f"""
You are a persona profiler bot. Based on the Reddit activity below, generate a full user persona for the Reddit user '{username}'.

The persona must include:
- Name (can be same as username)
- Personality traits (short tags)
- Goals and motivations
- Frustrations
- Behavior patterns
- Inferred interests or profession
- Personality bars (e.g., Introvert ██████)
- 1–2 direct quotes with the Reddit comment/post 
- A brief summary of the user's online presence
- Add a single line summary of the user for personality profiling

Reddit Activity:
{combined_text}

Cite specific comments or posts wherever possible.
Return the output in well-formatted text.
"""

    return prompt


def generate_persona(user_data):
    """
    Generates a persona from Reddit user data using Groq's LLM.

    Args:
        user_data (dict): Dictionary containing 'username', 'comments', and 'posts'.

    Returns:
        str: Generated user persona.
    """
    # Initialize Groq LLM 
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="mistral-saba-24b" 
    )

    prompt_text = build_prompt(
        user_data["comments"],
        user_data["posts"],
        user_data["username"]
    )


    prompt_template = PromptTemplate.from_template("{text}")
    chain = prompt_template | llm  
    result = chain.invoke({"text": prompt_text})


    return result.content


if __name__ == "__main__":
    data = get_user_data("https://www.reddit.com/user/kojied/")
    persona = generate_persona(data)
    print(persona)
