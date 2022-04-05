from typing import List, Optional, Tuple, Any

import requests

from source import constants
from source.utils import parse_for_pg_creation, parse_into_json, parse_for_db_creation

Vector = List[Tuple[str, str, Optional[Any]]]


class Create:
    """
    class that creates pages or databases with provided data , icon and cover
    """

    TOKEN = None

    def __init__(self) -> None:
        pass

    def page(
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
            headers=constants.HEADERS(Create.TOKEN),
            data=data_,
        )

    def db(
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
            headers=constants.HEADERS(Create.TOKEN),
            data=data_,
        )
