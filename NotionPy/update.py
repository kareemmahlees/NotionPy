from typing import List, Tuple, Optional, Any

import requests

from NotionPy import constants
from NotionPy.utils import parse_for_pg_creation, parse_into_json, parse_for_updating_db

Vector = List[Tuple[str, str, Optional[Any]]]


class Update:
    """
    class that updates the contents of (currently) pages
    """

    TOKEN = None

    def __init__(self) -> None:
        pass

    def page(
        self,
        pg_id: str,
        icon: Optional[str] = None,
        cover_url: Optional[str] = None,
        data: Optional[Vector] = None,
        archived: Optional[bool] = False,  # Delete
    ) -> None:
        data_ = parse_for_pg_creation(
            db_id=pg_id, data=data, icon=icon, cover_url=cover_url
        )  # the pg_id and db_id params are little bit confusing to understand but it works just fine
        data_.update(constants.ARCHIVE(archived))
        data_ = parse_into_json(data_)
        requests.patch(
            url=constants.UPDATE_PAGE_URL(pg_id),
            headers=constants.HEADERS(Update.TOKEN),
            data=data_,
        )

    # not currently in use for some bugs but left for feature updates
    def db(
        self,
        db_id: str,
        title: str,
        icon: Optional[str] = None,
        cover_url: Optional[str] = None,
        data: Vector = None,
        archived: Optional[bool] = False,  # Delete
    ) -> None:
        data_ = parse_for_updating_db(
            db_id=db_id, data=data, title=title, icon=icon, cover_url=cover_url
        )  # the pg_id and db_id params are little bit confusing to understand but it works just fine
        data_.update(constants.ARCHIVE(archived))
        data_ = parse_into_json(data_)
        res = requests.patch(
            url=constants.UPDATE_PAGE_URL(db_id),
            headers=constants.HEADERS(Update.TOKEN),
            data=data_,
        )
