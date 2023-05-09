import requests
import json
import re

from bs4 import BeautifulSoup
from scraper.ultils import get_snakecase_header
from collections import OrderedDict


def is_recorded_council_file(primary_data_box: BeautifulSoup):
    if primary_data_box.find("div", {"id": "viewrecord"}) is None:
        return False
    return True



def get_counil_file_id(primary_data_box: BeautifulSoup):
    council_file_header_box = primary_data_box.find("h1", {"id": "CouncilFileHeader"})
    council_file_header_id_box = council_file_header_box.find("font", {"class": "cfheader"})
    if council_file_header_id_box is None:
        return None
    search_result = re.search(r"\d+-\d+", council_file_header_id_box.text.strip())
    council_file_id = None if  search_result is None else search_result.group()

    return council_file_id


def get_activities(activies_box: BeautifulSoup, primary_data_box: BeautifulSoup):
    activities_data = []
    activities_table_box = activies_box.find("table", {"id": "inscrolltbl"})
    if activities_table_box is None:
        return activities_data
    
    activity_boxes = activities_table_box.find_all("tr")
    for activity_box in activity_boxes:
        columns = activity_box.find_all("td")
        if columns:
            date_box, activity_box, document_urls_box = columns

            documents_list = []
            documents_icon_box = document_urls_box.find("img")
            if documents_icon_box is not None:
                documents_box_id = re.findall(r"showtip\w+", documents_icon_box["onclick"])[0]
                url_boxes = primary_data_box.find("div", {"id": documents_box_id}).find_all("a")
                documents_list = [url_box.text.strip().replace("\u00a0", " ") for url_box in url_boxes]

            activities_data.append({
                "date": date_box.text.strip(),
                "activity": activity_box.text.strip().replace("\u00a0", " "),
                "documents": documents_list
            })
    

    return activities_data


def get_references_number(references_number_box: BeautifulSoup):
    key_value_strings = references_number_box.get_text(separator="<br>").split("<br>")
    key_value_strings = [e for e in key_value_strings if e]
    references_number_data = {}
    for kv_string in key_value_strings:
        key, value = kv_string.split(":")
        references_number_data[get_snakecase_header(key)] = value.strip()
    return references_number_data


def extract_key_value_section(key_value_box: BeautifulSoup, primary_data: dict, primary_data_box: BeautifulSoup):
    key_box = key_value_box.find("div", {"class": "reclabel"})
    if key_box is None:
        return
    key = key_box.text.strip()
    if not key or key == "File History":
        return
    
    value_box = key_value_box.find("div", {"class": "rectext"})
    if key == "File Activities":
        value = get_activities(value_box, primary_data_box)
    elif key == "Reference Numbers":
        value = get_references_number(value_box)
    else:
        value = None if value_box is None else value_box.text.strip().replace("\u00a0", " ")
        
    primary_data[get_snakecase_header(key)] = value


def get_primary_data(primary_data_box: BeautifulSoup):
    primary_data_section_boxes = primary_data_box.find("div", {"id": "viewrecord"}).find_all("div", {"class": "section"})
    primary_data = OrderedDict()
    
    for section in primary_data_section_boxes:
        #Find primary key value
        if section.find("div", {"class": "left"}) is None:
            extract_key_value_section(section, primary_data, primary_data_box)

        #Find secondary key value
        else:
            left_section =  section.find("div", {"class": "left"})
            if left_section is not None:
                extract_key_value_section(left_section, primary_data, primary_data_box)

            right_section =  section.find("div", {"class": "right"})
            if right_section is not None:
                extract_key_value_section(right_section, primary_data, primary_data_box)

    return primary_data


def get_online_documents(online_documents_box: BeautifulSoup):
    online_documents = []
    online_documents_table_boxes = online_documents_box.find_all("table")
    if len(online_documents_table_boxes) < 2:
        return online_documents
    
    #Take the second one
    online_documents_table_boxes = online_documents_table_boxes[1]
    online_document_boxes = online_documents_table_boxes.find_all("tr")
    for online_document_box in online_document_boxes:
        title_box, doc_date_box = online_document_box.find_all("td")
        url_title_box = title_box.find("a")

        url = url_title_box["href"]
        title = url_title_box.text.strip().replace("\u00a0", " ")
        doc_date = doc_date_box.text.strip()

        online_documents.append({
            "title": title,
            "url": url,
            "doc_date": doc_date
        })

    return online_documents


def get_votes_single_box(votes_single_box: BeautifulSoup):
    general_info_box, votes_detail_box = votes_single_box.find_all("table")

    general_info = OrderedDict()
    info_row_boxes = general_info_box.find_all("tr")
    for row_box in info_row_boxes:
        key_box, value_box = row_box.find_all("td")
        general_info[get_snakecase_header(key_box.text.strip())] = value_box.text.strip()
        
    votes_detail = []
    vote_detail_boxes = votes_detail_box.find_all("tr")
    for row_box in vote_detail_boxes:
        row_data_boxes = row_box.find_all("td")
        if row_data_boxes:
            member_name, cd, vote = row_data_boxes
            votes_detail.append({
                "member_name": member_name.text.strip().replace("\u00a0", " "),
                "cd": cd.text.strip(),
                "vote": vote.text.strip()
            })
    
    return {
        "general_info": general_info,
        "votes_detail": votes_detail
    }
    


def get_votes(votes_box: BeautifulSoup):
    table_boxes = votes_box.find_all("table")
    if not table_boxes:
        return []
    
    votes_single_boxes = votes_box.find_all("div")
    if votes_single_boxes:
        return [get_votes_single_box(child_box) for child_box in votes_single_boxes]
    
    return get_votes_single_box(votes_box)
        


def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract primary data points
    primary_data = {}
    cfi_main_content_box = soup.find("div", {"id": "CFI_MainContent"}).find("div", {"class": "xboxcontent"})
    primary_data_box = cfi_main_content_box.find("div", {"id": "xboxholder"})

    if not is_recorded_council_file(primary_data_box):
        print("No record found")
        return {}

    council_file_id = get_counil_file_id(cfi_main_content_box)
    primary_data = get_primary_data(primary_data_box)
    
    cfi_online_docs_content_box = soup.find("div", {"id": "CFI_OnlineDocsContent"}).find("div", {"class": "xboxcontent"})
    online_documents_box = cfi_online_docs_content_box.find("div", {"id": "xboxholder"})
    online_documents = get_online_documents(online_documents_box)
    
    cfi_votes_content_box = soup.find("div", {"id": "CFI_VotesContent"}).find("div", {"class": "xboxcontent"})
    votes_box = cfi_votes_content_box.find("div", {"id": "xboxholder"})
    votes = get_votes(votes_box)

    # Create JSON object
    data = {
        "council_file_id": council_file_id,
        "primary_data": primary_data,
        "online_documents": online_documents,
        "council_vote_informations": votes
    }

    # Save JSON to file
    with open(f"{council_file_id}.json", "w") as outfile:
        json.dump(data, outfile, indent=2)

    return data

