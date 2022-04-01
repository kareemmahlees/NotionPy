from typing import List, Tuple, Optional, Any

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from source.create import Create
from source.query import Query

# Vector1 = List[Tuple[str, str, Optional[Any]]]
# Vector2 = List[Tuple[str, str]]


class NotionClient(Create, Query):
    def __init__(self, token: str) -> None:
        Create.TOKEN = token
        Query.TOKEN = token

    class create:
        def page(
            database_id: str,
            data: List[Tuple[str, str, Optional[Any]]],
            icon: Optional[str] = None,
            cover: Optional[str] = None,
        ) -> None:
            Create.page(Create, database_id, icon, cover, data)

        def db(
            page_id: str,
            title: str,
            data: List[Tuple[str, str]],
            icon: Optional[str] = None,
            cover: Optional[str] = None,
        ) -> None:
            Create.db(Create, page_id, title, icon, cover, data)

    class query:
        def page(
            page_id,
            in_json: Optional[bool] = False,
            json_indent: Optional[int] = None,
            print_data: Optional[bool] = False,
        ) -> None:
            Query.page(Query, page_id, in_json, json_indent, print_data)

        def db(
            db_id,
            in_json: Optional[bool] = False,
            json_indent: Optional[int] = None,
            print_data: Optional[bool] = False,
        ) -> None:
            Query.db(Query, db_id, in_json, json_indent, print_data)
