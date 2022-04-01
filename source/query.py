from optparse import Option
from typing import Optional

import requests

from source import constants
from source.utils import parse_into_dict, parse_into_json


class Query:
    TOKEN = None

    def __init__(self) -> None:
        pass

    def page(
        self,
        page_id,
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
