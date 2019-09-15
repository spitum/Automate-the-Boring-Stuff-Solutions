from downloadXkcd import get_latest_xkcd
from downloadCSC import get_latest_CSC
import csv, datetime, sys




def downloadcomics(sources):
    ''' pass a list of comics to download. Works for xkcd and CompletelySeriousComics. 
    Check if latest comic has been downloaded, else downloads it.'''
    date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    for source in sources:
        if source == 'xkcd':
            try:
                with open('./xkcd/latest_url.csv', 'r') as f:
                    csvReader = csv.DictReader(f)
                    for line in csvReader:
                        latest_xkcd_url = line['URL']
                        xkcd_url = get_latest_xkcd(latest_xkcd_url)            
                        latest_url = {'Date':date, 'URL': xkcd_url, 'source': 'xkcd'}

            except FileNotFoundError:
                with open('./xkcd/latest_url.csv', 'w', newline = '') as f:
                    fieldnames = ['Date','URL','source']
                    csvWriter = csv.DictWriter(f,fieldnames = fieldnames, delimiter = ',')
                    csvWriter.writeheader()
                    csvWriter.writerow(latest_url) 

        if source == 'CSC':
            try:
                with open('./completelyseriouscomics/latest_url.csv', 'r') as f:
                    csvReader = csv.DictReader(f)
                    for line in csvReader:
                        latest_CSC_url = line['URL']
                        CSC_URL = get_latest_CSC(latest_CSC_url)        
                        latest_url = {'Date':date, 'URL': CSC_URL, 'source': 'CSC'}

            except FileNotFoundError:
                with open('./completelyseriouscomics/latest_url.csv', 'w', newline = '') as f:
                    fieldnames = ['Date','URL','source']
                    latest_CSC_url = 'http://completelyseriouscomics.com/'
                    CSC_URL = get_latest_CSC(latest_CSC_url)        
                    latest_url = {'Date':date, 'URL': CSC_URL, 'source': 'CSC'}
                    csvWriter = csv.DictWriter(f,fieldnames = fieldnames, delimiter = ',')
                    csvWriter.writeheader()
                    csvWriter.writerow(latest_url)

    
#Call the main functions 
if __name__ == '__main__':
    sources = ['xkcd','CSC']
    downloadcomics(sources)
