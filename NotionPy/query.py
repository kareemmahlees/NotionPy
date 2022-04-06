from typing import Optional

import requests

from NotionPy import constants
from NotionPy.utils import parse_into_dict, parse_into_json


class Query:
    """
    class that retrieves data from page or database with option to get it
    json or dict like data
    """

    TOKEN = None

    def __init__(self) -> None:
        pass

    def page(
        self,
        page_id: str,
        in_json: Optional[bool] = False,
        json_indent: Optional[int] = None,
        print_data: Optional[bool] = False,
    ):
        res = requests.post(
            url=constants.QUERY_PAGE_URL(page_id),
            headers=constants.HEADERS(Query.TOKEN),
        )
        data = (
            parse_into_json(res.json(), json_indent)
            if in_json is True
            else parse_into_dict(parse_into_json(res.json(), json_indent))
        )
        if print_data is True:
            print(data)

    def db(
        self,
        db_id,
        in_json: Optional[bool] = False,
        json_indent: Optional[int] = None,
        print_data: Optional[bool] = False,
    ):
        res = requests.post(
            url=constants.QUERY_DB_URL(db_id), headers=constants.HEADERS(Query.TOKEN)
        )
        data = (
            parse_into_json(res.json(), json_indent)
            if in_json is True
            else parse_into_dict(parse_into_json(res.json(), json_indent))
        )
        if print_data == True:
            print(data)
