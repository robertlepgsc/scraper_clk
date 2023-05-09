import sys
sys.path.append('.')

from scrape import scrape_data
from requests.exceptions import ConnectionError

def main():
    url = "https://cityclerk.lacity.org/lacityclerkconnect/index.cfm?fa=ccfi.viewrecord&cfnumber=11-0180"
    try:
        data = scrape_data(url)
        print(f"Finish data scraping for CFI: {data['council_file_id']}")
        
    except ConnectionError as e:
        print("Unexpected error occur while making request to CFI page:", e, ". Please check your internet connection and try again.")

if __name__ == "__main__":
    main()