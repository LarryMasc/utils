#!/usr/local/bin/python3
"""Script to watch Adobe Security page

This script looks at https://helpx.adobe.com/security.html and parses the
html file for all the products. It then determines if the page was updated
from the last check.

Design Spec
 - Create 2 tables with the following schemas
 Table 1
    - Product Name
    - Product URL
    - Published Date
 Table 2
    - Product Name
    - Link
    - Title
    - Posted
    - Updated
    - collection_date
"""

import urllib.request
from urllib.parse import urljoin
import bs4 as bs

url = "https://helpx.adobe.com/security.html"

def main():
    """Fabled main, where it all begins."""
    print (url)
    sauce = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(sauce, "html.parser")

    for meta in soup.find_all('meta', attrs = {'name': 'publishDate'}, content=True):
        # print (type(meta))
        print ("Published Date : {}".format(meta.get('content')))
    bulletin_items = soup.find(class_="noHeader")
    b_href = bulletin_items.find_all("a")

    # Loop through the Table records
    for t_row in bulletin_items.find_all("tr")[1::]:
        t_data = t_row.find_all("td")
        #link = t_row.find_all("a")
        link = t_row.find_all("a")
        link = link[0].get("href")
        href = urljoin(url,link)
        print ("Link    : {}\n"
               "Title   : {}\n"
               "Posted  : {}\n"
               "Updated : {}\n".format(href, t_data[0].text, t_data[1].text, t_data[2].text))
        f_href = urllib.request.urlopen(href).read()
        print(f_href)
        exit(0)


if __name__ == "__main__":
    main()