#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4
import concurrent.futures
import datetime, csv

def get_latest_xkcd(latest_xkcd_url):
    url = 'http://xkcd.com'  #starting url
    os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd

    # Download the page.
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    prev_link = soup.select('a[rel="prev"]')[0]
    href = prev_link.get('href')
    previous_number = href.strip('/')
    current_number = int(previous_number) + 1
    url = f'{url}/{str(current_number)}/'
    latest_xkcd_url_number = latest_xkcd_url.split('/')[3]
    #print(latest_xkcd_url_number)
    

    if url == latest_xkcd_url:
        print(f'This comic has already been downloaded: {latest_xkcd_url}')
    # Find the page number for the URL
    else:
        while current_number > latest_xkcd_url_number:
            res = requests.get(url)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, 'lxml')

            comic_elem = soup.select('#comic img')
            if comic_elem == []:
                print('could not find comic image.')
            else:
                try:
                    comic_url = 'https:' + comic_elem[0].get('src')
                    # Download the image.
                    print('Downloading image {}'.format(comic_url))
                    res = requests.get(comic_url)
                    res.raise_for_status()
                except requests.exceptions.MissingSchema:
                    # Skip this comic.
                    prev_link = soup.select('a[rel="prev"]')[0]
                    url = 'https://xkcd.com' + prev_link.get('href')
                    continue

            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd',os.path.basename(comic_url)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        # Get the Prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')

    return latest_xkcd_url

