import requests
import re
from bs4 import BeautifulSoup

def get_HTML_doc(url):
    try:
        request = requests.get(url)
    except:
        print("Issue opening {}").format(url)

    return request.text


def parse_HTML(html):
    return BeautifulSoup(html, "html.parser")


def get_confluence_table_from_HTML_object(html_object):
    return html_object.find("table", attrs={"class": "confluenceTable"})


def get_release_date_from_confluenceTable_object(table_object):
    datasets = []
    for row in table_object.find_all("tr")[1:]:
        for dataset in row.find_all("td"):
            datasets.append(dataset)

    match = re.search(r'[a-zA-Z]{3} \d{2}, \d{4}', str(datasets[0]))
    return match.group()
