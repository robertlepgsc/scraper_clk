import pytest
import re

from bs4 import BeautifulSoup
from collections import OrderedDict
from scraper.scrape import (
    is_recorded_council_file,
    get_counil_file_id,
    get_activities,
    get_references_number,
    get_primary_data,
)


def test_is_recorded_council_file():
    soup = BeautifulSoup("<div><p>Paragraph</p></div>", "html.parser")
    assert not is_recorded_council_file(soup)

    soup = BeautifulSoup("<div><div id='viewrecord'></div></div>", "html.parser")
    assert is_recorded_council_file(soup)


def test_get_counil_file_id():
    soup = BeautifulSoup(
        "<h1 id='CouncilFileHeader'><font class='cfheader'>Council File: 99-9999</font></h1>",
        "html.parser",
    )
    assert get_counil_file_id(soup) == "99-9999"

    soup = BeautifulSoup("<h1 id='CouncilFileHeader'></h1>", "html.parser")
    assert get_counil_file_id(soup) is None


def test_get_activities():
    activies_box = BeautifulSoup("<div></div>", "html.parser")
    primary_data_box = BeautifulSoup("<div></div>", "html.parser")
    assert get_activities(activies_box, primary_data_box) == []

    activies_box = BeautifulSoup(
        """
        <div>
            <table id='inscrolltbl'>
                <tr>
                    <th>Date</th>
                    <th>Activity</th>
                    <th>Document URLs</th>
                </tr>
            </table>
        </div>
        """,
        "html.parser",
    )
    primary_data_box = BeautifulSoup("<div></div>", "html.parser")
    assert get_activities(activies_box, primary_data_box) == []

    activies_box = BeautifulSoup(
        """
        <div>
            <table id='inscrolltbl'>
                <tr>
                    <th>Date</th>
                    <th>Activity</th>
                    <th>Document URLs</th>
                </tr>
                <tr>
                    <td>2023-05-09</td>
                    <td>Activity</td>
                    <td><img onclick='showtip_1' /></td>
                </tr>
            </table>
        </div>
        """,
        "html.parser",
    )
    primary_data_box = BeautifulSoup(
        """
        <div>
            <div id='showtip_1'><a>Document 1</a><a>Document 2</a></div>
        </div>
        """,
        "html.parser",
    )
    assert get_activities(activies_box, primary_data_box) == [
        {"date": "2023-05-09", "activity": "Activity", "documents": ["Document 1", "Document 2"]}
    ]


def test_get_references_number():
    references_number_box = BeautifulSoup("<div></div>", "html.parser")
    assert get_references_number(references_number_box) == {}

    references_number_box = BeautifulSoup(
        "<div>Number: 1234<br>Type: Test</div>",
        "html.parser",
    )
    assert get_references_number(references_number_box) == {"number": "1234", "type": "Test"}

def test_get_primary_data(primary_data_box_content):
    primary_data_box = BeautifulSoup(primary_data_box_content, "html.parser")
    expected_data = {
        "title": "4800 Block of Oak Park Avenue / Plan Amendment and Zone Change",
        "date_received_introduced": "01/29/2010",
        "last_changed_date": "07/09/2012",
        "expiration_date": "02/01/2012",
        "council_district": "5",
        "mover": "PAUL KORETZ",
        "second": "DENNIS ZINE",
        "file_activities": [
        {
            "date": "07/09/2012",
            "activity": "File expired per Council policy, Council file No. 05-0553.",
            "documents": [
            "Council Action"
            ]
        },
        {
            "date": "01/29/2010",
            "activity": "Motion referred to Planning and Land Use Management Committee.",
            "documents": [
            "Motion"
            ]
        }
        ]
    }

    assert dict(get_primary_data(primary_data_box)) == expected_data