import requests
from bs4 import BeautifulSoup
import os

# URL to scrape
# url = "https://en.wikipedia.org/w/index.php?title=Category:Medicinal_plants&pageuntil=Lycopus+americanus#mw-pages"
# url = "https://en.wikipedia.org/w/index.php?title=Category:Medicinal_plants&pagefrom=Lycopus+americanus#mw-pages"     #next page
# url = "https://en.wikipedia.org/w/index.php?title=Category:Medicinal_plants&pagefrom=Reynoutria+multiflora#mw-pages"  #next page
url = "https://en.wikipedia.org/w/index.php?title=Category:Medicinal_plants&pagefrom=Viola+%28plant%29#mw-pages"        #last page

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

main_div = soup.find(id="mw-pages")
# print (main_div)

# Find the section containing the article content (assuming it is enclosed in a <div> with a specific class)
article_divs = main_div.find_all("div", class_="mw-category-group")
# print (article_divs)

all_anchors = []
for article_div in article_divs:
    one_div_anchors = article_div.find_all("a")
    onediv_article_links = ["https://en.wikipedia.org/" + anchor.get("href") for anchor in one_div_anchors]
    # print (article_links)
    all_anchors.append(onediv_article_links)

# print(all_anchors)

all_links = []
for anchor in all_anchors:
    for link in anchor:
        all_links.append(link)
print(all_links)


for oneLink in all_links[0:]:
    docs_url = requests.get(oneLink)
    docs_soup = BeautifulSoup(docs_url.content, "html.parser")
    # print(docs_soup)

    doc_title = docs_soup.find("i").text
    file_name = doc_title.replace(" ", "")
    file_name = file_name.replace("\"","")
    # print(doc_title)

    content = docs_soup.find_all("p")
    all_content = ""
    for doc in content:
        content_text = doc.text.strip()
        all_content += content_text + '\n\n'

    # print(all_content)
    file_path = os.path.join(r"D:\Sem-5\adv. python\Vipuls py\lab\webScraping\IndianKanoon\txtFiles", f"{file_name}.txt")

    with open(file_path, "w", encoding="UTF-8") as f:
        f.write(f"{doc_title}\n\n")
        f.write(f"{all_content}\n\n")
