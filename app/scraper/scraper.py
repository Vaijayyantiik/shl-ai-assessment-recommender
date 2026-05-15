import requests

from bs4 import BeautifulSoup

import json

import time


URL = "https://www.shl.com/solutions/products/product-catalog/"


headers = {

    "User-Agent": "Mozilla/5.0"
}


response = requests.get(

    URL,

    headers=headers
)


print("Status Code:")

print(response.status_code)


soup = BeautifulSoup(

    response.text,

    "html.parser"
)


links = soup.find_all("a")


catalog = []

seen = set()


for link in links:

    href = link.get("href")

    if (

        href

        and "product-catalog/view" in href

        and "/view/" in href

        and len(link.text.strip()) > 3

    ):

        name = link.text.strip()

        full_url = "https://www.shl.com" + href


        if full_url not in seen:

            seen.add(full_url)

            print(f"Scraping: {name}")


            description = ""


            try:

                product_response = requests.get(

                    full_url,

                    headers=headers
                )

                product_soup = BeautifulSoup(

                    product_response.text,

                    "html.parser"
                )

                paragraphs = product_soup.find_all("p")

                paragraph_texts = []

                for p in paragraphs[:5]:

                    text = p.get_text(

                        strip=True
                    )

                    if text:

                        paragraph_texts.append(text)

                description = " ".join(

                    paragraph_texts
                )

                time.sleep(1)

            except Exception as e:

                print("Error:", e)


            catalog.append({

                "name": name,

                "url": full_url,

                "description": description
            })


print("\nTotal Assessments Found:")

print(len(catalog))


with open(

    "data/shl_catalog.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        catalog,

        f,

        indent=4
    )


print("\nCatalog Saved Successfully")