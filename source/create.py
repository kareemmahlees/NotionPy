from typing import List, Optional, Tuple, Any

import requests

import constants
from utils import parse_for_pg_creation, parse_into_json, parse_for_db_creation

Vector = List[Tuple[str, str, Optional[Any]]]


class Create:
    def __init__(
        self,
        token: str,
    ) -> None:
        self.token = token

    def create_page(
        self,
        db_id: str,
        icon: Optional[str] = None,
        cover_url: Optional[str] = None,
        data: Optional[Vector] = None,
    ) -> None:
        data_ = parse_for_pg_creation(
            db_id=db_id, data=data, icon=icon, cover_url=cover_url
        )
        data_ = parse_into_json(data_)
        requests.post(
            url=constants.CREATE_PAGE_URL,
            headers=constants.HEADERS(self.token),
            data=data_,
        )

    def create_db(
        self,
        page_id: str,
        title: str,
        icon: Optional[str] = None,
        cover_url: Optional[str] = None,
        data: Vector = None,
    ) -> None:
        data_ = parse_for_db_creation(
            pg_id=page_id, title=title, data=data, icon=icon, cover_url=cover_url
        )
        data_ = parse_into_json(data_)
        requests.post(
            url=constants.CREATE_DB_URL,
            headers=constants.HEADERS(self.token),
            data=data_,
        )


# inst = Create("secret_LYxhmvMw0RoQncukgmKNjLkPHduLBLgELz5HE9id5MW")
# inst.create_db("cc39932a53da46be8472fdfc4c55966e", "Grocery", data=[("Name", "title")])

# secret_LYxhmvMw0RoQncukgmKNjLkPHduLBLgELz5HE9id5MW
# https://www.notion.so/Test-cc39932a53da46be8472fdfc4c55966e
