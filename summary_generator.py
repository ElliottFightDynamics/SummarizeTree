import os
import requests

def generate_summary(text_chunk):
    """
    Calls the OpenAI API to generate a summary for a given text chunk.
    
    :param text_chunk: A string containing the text to summarize.
    :return: A string containing the summary.
    """
    try:
        response = requests.post(
            "https://api.openai.com/v1/engines/davinci-codex/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
            },
            json={
                "prompt": text_chunk,
                "temperature": 0.5,
                "max_tokens": 150
            }
        )
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        summary = response.json().get('choices', [{}])[0].get('text', '').strip()
        return summary
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while requesting the OpenAI API: {e}")
        return ""