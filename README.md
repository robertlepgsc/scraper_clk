## Solution explanation
After doing some research on some sameples web result, I decided to choose output data structure like:

>
    {
    "council_file_id": <council_file_id>,
    "primary_data": {
        "title": <title>,
        ...
        "file_activities": [
            {
                "date": <data>,
                "activity": <activity>,
                "documents": [
                    <document_title>
                    ...
                ]
            }
            ...
        ]
    },
    "online_documents": [
        {
            "title": <document_title>,
            "url": <url>,
            "doc_date": <doc_date>
        }
        ...
    ],
    "council_vote_informations": [
        {
            "general_info": {
                "meeting_date": <meeting_date>,
                ...
            },
            "votes_detail": [
                {
                    "member_name": <member_name>,
                    "cd": <cd>,
                    "vote": <vote>
                }
                ...
            ]
        }
    ]
    }

Here I use CSS selector to talk about elemen tracking.

**Primary Data**
We find `div#CFI_MainContent` as for extracting primary data block, from this block we can also extract council file ID
Primary data block will be in `.xboxcontent #viewrecord`. The data here can be presented as key value pair, key will be formatted with `get_snakecase_header` function, so I extract the value from `div.reclabel`  for key processing and `div.rectext` processing value and they are from `div.section`. And we apply special process for `Reference Numbers` section to parse the info block to key value pair

**Activities**
While process `Primary Data` we will see that `Activities` will be extracted from `File Activities` section, so that's why I put `file_activities` inside `primary_data`. Here we will extract data from table and store them in object with 3 key `date`, `activity`, `documents`, and get only document title list for each activity ( by retrieve information from a hidden `div` and `showtip_<number>` id ) if any because later we will collect document date and its URL from `Online Documents` block

**Online Documents**
We find `div#CFI_OnlineDocsContent` as for extracting online document data block, here we have a table and we can extract document title, url and doc date

**Council Votes Information**
We find `div#CFI_VotesContent` as for extracting votes data block, here we have block with two tables, and some page will come with more than 1 block
For first table, it will have two column, and I extract 2 column to key and value respectively, key will be formatted with `get_snakecase_header` function
For second table is about votes detail information, I choose to extract that table as a list of object with 3 keys `member_name`, `cd`, `vote`


### How to run
From root folder
- Create virtual environment
```
python -m venv venv
```

- After activated virtual environment, install packages:
```
pip install -r requirements.txt
```

- Run the scraper, module is structured to be run directly
```
python scraper
```
In case you want to test another url, change `url` variable in `__main__.py` file in `scraper` folder

- For testing, simply run
```
pytest
```
