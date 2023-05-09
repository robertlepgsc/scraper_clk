import sys
sys.path.append('.')

from scrape import scrape_data

def main():
    url = "https://cityclerk.lacity.org/lacityclerkconnect/index.cfm?fa=ccfi.viewrecord&cfnumber=11-0180"
    data = scrape_data(url)
    print(f"Finish data scraping for CFI: {data['council_file_id']}")

if __name__ == "__main__":
    main()