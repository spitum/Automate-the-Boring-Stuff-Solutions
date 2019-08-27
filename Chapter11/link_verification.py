import time
import sys
import bs4
import os
import webbrowser
import requests
import lxml
import re


# Get a web page link
# Download every linked page
#If link not working, print out broken links


def link_verification(URL):

    response = requests.get(URL)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'lxml')

    links = soup.find_all('a')


    for link in links[:5]:
        if link.has_attr('href'):
            link_download = link['href']
            print(link_download)
            if link_download.startswith('http:'):
                link_download = link_download
            elif link_download.startswith(('/','#')):
                link_download = URL + link_download[1:]
        try:
            res = requests.get(link_download)
            res.raise_for_status()

        except (requests.exceptions.HTTPError,requests.exceptions.MissingSchema,requests.exceptions.InvalidSchema):
            print('Link not avaiable: %s' % (link_download))

## Call the function
link_verification('https://automatetheboringstuff.com/chapter11/')
