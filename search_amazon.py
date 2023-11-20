from googleapiclient.discovery import build
import os

GOOGLE_API_DEV_KEY= os.getenv("GOOGLE_API_DEV_KEY")

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

    for item in res['items']:
        links += f"- [{item['title']}]({item['link']})\n"

    return links

search_str = input("Enter your amazon search string: ")
print("You entered:", search_str)
print(search_amazon(search_str))
