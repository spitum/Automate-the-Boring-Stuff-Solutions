import requests, os, bs4
import concurrent.futures
import datetime, csv
import re, time


def get_latest_CSC(latest_CSC_url):
    ''' downloads the latest CSC comic from below URL if it hasn't been downloaded already'''
    url = 'http://completelyseriouscomics.com/'  #starting url
    os.makedirs('completelyseriouscomics', exist_ok=True)   # store comics in ./completelyseriouscomics
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    
    for a in soup.find_all('a',class_="navi navi-prev",href=True):
        href = a['href']
    prev_number = int(href.split('=')[1])
    current_number = prev_number + 2
    url = f'http://completelyseriouscomics.com/?p={str(current_number)}'
    latest_CSC_url_number = int(latest_CSC_url.split('=')[1])

    if url == latest_CSC_url:
        print(f'This comic has already been downloaded: {latest_CSC_url}')
    # Find the page number for the URL
    else:
        while current_number > latest_CSC_url_number:
            res = requests.get(url)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'lxml')

            comicElem = soup.select('#comic-1 img')
            if comicElem == []:
                print('Could not find comic image.')
            else:
                try:
                    comicUrl = comicElem[0].get('src')
                    # Download the image.
                    print('Downloading image %s...' % (comicUrl))
                    res = requests.get(comicUrl)
                    res.raise_for_status()
                except Exception:
                    for a in soup.find_all('a',class_="navi navi-prev",href=True):
                        href = a['href']
                    prev_number = int(href.split('=')[1])
                    print(prev_number)
                    url = f'http://completelyseriouscomics.com/?p={str(prev_number)}'
                    continue
            # Save the image to ./xkcd.
            imageFile = open(os.path.join('completelyseriouscomics',os.path.basename(comicUrl)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

            for a in soup.find_all('a',class_="navi navi-prev",href=True):
                href = a['href']
            prev_number = int(href.split('=')[1])
            url = f'http://completelyseriouscomics.com/?p={str(prev_number)}'
    
    return latest_CSC_url

    


