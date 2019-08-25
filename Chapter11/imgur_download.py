import time
import sys
import bs4
import os
import webbrowser
import requests
import lxml


def imgur_downloader():
    '''Search imgur for command line argument passed. Create directory if doesn't exist.Download images, and store in directory'''

    imgur_url = 'https://imgur.com/search?q='

    ## make subfolders for the search term:
    os.makedirs('imgur' + '/' + sys.argv[1], exist_ok=True)   # store images in ./imgur/[search term]


    print("Searching...")
    res = requests.get(imgur_url + ' '.join(sys.argv[1:]))
    res.raise_for_status()

    '''Function to return the top search result links'''
    soup = bs4.BeautifulSoup(res.text, "lxml")
    image_elem = soup.select('.post > .image-list-link img')

    if image_elem == []:
         print('Could not find image. with search term: %s' % (sys.argv[1:]))

    else:
        for i, img in enumerate(image_elem):
            img_url = 'https:' + str(img['src'])
            print('Downloading image %s' % (img_url))
            try:
                res = requests.get(img_url)
                res.raise_for_status()
            except requests.exceptions.MissingSchema:
                print('Missing URL'+ str(res.raise_for_status()))
                continue
            # Save the image to ./imgur.
            imageFile = open(os.path.join('imgur',sys.argv[1], os.path.basename(img_url)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

    return  'Number of images downloaded: ' + str(len(image_elem))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(imgur_downloader())
    else:
        print('Please call the script with a search term.')
