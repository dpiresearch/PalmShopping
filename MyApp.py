from googleapiclient.discovery import build
import streamlit as st
import requests
from openai import OpenAI
import os

client = OpenAI()
client.key = os.getenv("OPENAI_API_KEY")
GOOGLE_API_DEV_KEY = os.getenv("GOOGLE_API_DEV_KEY")


def search_amazon(query: str, num: int = 10) -> str:
    service = build(
        "customsearch", "v1", developerKey=GOOGLE_API_DEV_KEY
    )

    res = (
        service.cse()
        .list(
            q=query,
            cx="103114c8487ce4aa1",
            num=num,
        )
        .execute()
    )

    links = ""

    if res['items'] is None or res['items'] == []:
        return "No items found"
    for item in res['items']:
        links += f"- [{item['title']}]({item['link']})\n"

    return links

def remove_quotes(input_string):
    return input_string.replace('"', '')

import re

def append_tag_to_amazon_url(input_string):
    pattern = r'(https?://www\.amazon\.com[^)]*)'

    def append_tag(match):
        url = match.group(0)
        if '?' in url:
            return url + '&tag=dpang-20'
        else:
            return url + '?tag=dpang-20'

    return re.sub(pattern, append_tag, input_string)

# Streamlit interface
st.title('Vision SHop')
url = st.text_input('Enter the url link to the image', 'Image URL')
if st.button('Shop'):
    # Make a POST request
    try:
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text",
                            "text": "Summarize the image as a search string for Amazon.com"},
#                         "text": "Identify all the items available to be purchased and for each item list the search terms you would to find them on Amazon.com.  Put a number before the search terms"},

                        {
                            "type": "image_url",
                            "image_url": {
                                "url": url,
                            },
                        },
                    ],
                }
            ],
            max_tokens=300,
        )
        search_str = response.choices[0].message.content
        print(search_str)
        st.write(search_str)

        search_str = remove_quotes(search_str)
        
        amazon_output = search_amazon(search_str)

        processed_lines = [append_tag_to_amazon_url(line) for line in amazon_output.split('\n')]
        output_str = '\n'.join(processed_lines)

        print(output_str)
        st.write(output_str)

    except Exception as e:
        st.error(f'An error occurred: {e}')



