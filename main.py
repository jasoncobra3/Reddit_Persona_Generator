# main.py

"""
Main execution script for Reddit Persona Generator.
"""

import os
from reddit_scraper import get_user_data
from persona_generator import generate_persona


def save_persona_to_file(username: str, persona_text: str):
    """
    Saves the generated persona to a .txt file.

    Args:
        username (str): Reddit username.
        persona_text (str): Generated persona content.
    """
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{username}.txt")

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(persona_text)

    print(f"[INFO] Persona saved to: {output_path}")


def main():
    """
    Main function to run the pipeline.
    """
    profile_url = input("Enter Reddit profile URL: ").strip()

    print("[DEBUG] Scraping user data...")
    user_data = get_user_data(profile_url)

    if not user_data["comments"] and not user_data["posts"]:
        print(f"[WARNING] No data found for user '{user_data['username']}'.")
        return

    print("[DEBUG] Generating persona...")
    persona = generate_persona(user_data)

    save_persona_to_file(user_data["username"], persona)


if __name__ == "__main__":
    main()
