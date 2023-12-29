from bs4 import BeautifulSoup
import requests

# 1. homepage 
# 2. homepage to docs link list page
# 3. docs link list page to selected docs page
# 4. selected docs page to complete docs content
# 5. complete docs content to text file


# --------------------------------step 1-------------------------------------- #
search_query = input("Enter the search query: ") # section 370 ipc
search_query = search_query.replace(" ", "+")
# print(search_query)
search_url = f"https://indiankanoon.org/search/?formInput={search_query}"
# print(search_url)


# --------------------------------step 2-------------------------------------- #
response = requests.get(search_url)

soup = BeautifulSoup(response.content, "html.parser")

divs = soup.find_all("div", class_="result_title")
# print(divs)

anchors = [div.find("a") for div in divs if div.find("a")]
# print(anchors)

links = ["https://indiankanoon.org/" + anchor["href"] for anchor in anchors]
# print(links)


# --------------------------------step 3-------------------------------------- #
for link in links[1:]:
    docs_url = requests.get(link)
    docs_soup = BeautifulSoup(docs_url.content, "html.parser")
    # print(docs_soup)

    article_div = docs_soup.find("div", class_="doc_title")

    article_anchor = article_div.find("a")["href"]
    # print(article_anchor)

    article_link = f"https://indiankanoon.org{article_anchor}"
    # print(article_link)


# --------------------------------step 4-------------------------------------- #
    article_response = requests.get(article_link)

    article_soup = BeautifulSoup(article_response.content, "html.parser")

    article_title = article_soup.find("div", class_="doc_title").text
    file_name = article_title.replace(" ", "")
    print(article_title)
    article_pre = article_soup.find("pre").text
    # print(article_conte)
    article_content = article_soup.find_all("p")
    # print(article_content)
    all_content = ""
    for content in article_content:
        try:
            content_text = content.text.strip()
            all_content += content_text + '\n\n'
        except UnicodeEncodeError:
            # Handle non-UTF-8 encoded content (skip it or handle it accordingly)
            print(f"Skipping non-UTF-8 encoded content: {content.text}")
    # print(all_content)
    
    
# --------------------------------step 5-------------------------------------- #section 370 ipc
    with open(f"{file_name}.txt", "w", encoding="UTF-8") as f:
        f.write(f"{article_title}\n\n")
        f.write(f"{article_pre}\n\n")
        f.write(f"{all_content}\n\n")

