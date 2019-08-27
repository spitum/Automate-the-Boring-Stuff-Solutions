import time
import sys
import bs4
import os
import webbrowser
import requests
import lxml


# Get a web page link
# Download every linked page
#If link not working, print out broken links


def link_verification(URL):

    response = requests.get(URL)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'lxml')

    links = soup.find_all('a')


    for link in links:
        try:
            if link.has_attr('href'):
                print(link['href'])
                res = requests.get(link['href'])
                res.raise_for_status()
        except (requests.exceptions.HTTPError,requests.exceptions.MissingSchema,requests.exceptions.InvalidSchema):
                print('Link not avaiable: %s' % (link['href']))