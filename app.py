# app.py

import streamlit as st
import os
import re
from reddit_scraper import get_user_data
from persona_generator import generate_persona

# === Streamlit Config ===
st.set_page_config(page_title="Reddit Persona Generator", layout="centered")
st.markdown("<h1>🛠️ Reddit Persona Generator</h1>", unsafe_allow_html=True)
st.markdown("Generate an AI-powered user persona from a Reddit profile using Groq LLM.", unsafe_allow_html=True)
st.markdown("---")

# === Info Box: What You’ll Get ===
with st.expander("📄 What will the Persona include?", expanded=False):
    st.markdown("""
    - 🧠 **Personality Traits** (with direct quotes)  
    - 🎯 **Goals and Motivations**  
    - ⚠️ **Frustrations**  
    - 🔁 **Behavior Patterns**  
    - 👤 **Inferred Interests / Profession**  
    - 📊 **Personality Bars**  
    - 💬 **Quote Highlight**  
    - 🧵 **Persona Summary**  
    """)

# === Input Reddit Profile URL ===
reddit_url = st.text_input("🔗 Reddit Profile URL:", placeholder="https://www.reddit.com/user/kojied/")
st.caption("💡 Example: [https://www.reddit.com/user/kojied/](https://www.reddit.com/user/kojied/)")
st.warning("⚠️ The Reddit profile must be public and have visible comments or posts.")



def extract_username(url):
    match = re.search(r"reddit\.com/user/([a-zA-Z0-9_-]+)", url)
    return match.group(1) if match else None

if reddit_url:
    username = extract_username(reddit_url)

    if not username:
        st.error("❌ Invalid Reddit profile URL.")
    else:
        with st.spinner("🔍 Scraping Reddit data..."):
            user_data = get_user_data(reddit_url)

        comments = user_data.get("comments", [])
        posts = user_data.get("posts", [])

        if not comments and not posts:
            st.warning("⚠️ No comments or posts found. User may be inactive or private.")
        else:
            

            with st.spinner("🤖 Generating persona..."):
                user_data = {
                    "username": username,
                    "comments": comments,
                    "posts": posts
                }
                persona_txt = generate_persona(user_data)

                # Save to file
                os.makedirs("outputs", exist_ok=True)
                file_path = os.path.join("outputs", f"{username}.txt")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(persona_txt)

                st.success("✅ Persona generated successfully!")

                # Show download button
                with open(file_path, "rb") as f:
                    st.download_button(
                        label="📥 Download Persona (.txt)",
                        data=f,
                        file_name=f"{username}_persona.txt",
                        mime="text/plain"
                    )
