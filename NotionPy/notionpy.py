from typing import List, Tuple, Optional, Any


from NotionPy.create import Create
from NotionPy.query import Query
from NotionPy.update import Update


class NotionClient(Create, Query, Update):
    """
    A class that acts like an entry point for other classes methods
    """

    def __init__(self, token: str) -> None:
        Create.TOKEN = token
        Query.TOKEN = token
        Update.TOKEN = token

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

    class update:
        def page(
            page_id,
            data: List[Tuple[str, str, Optional[Any]]],
            icon: Optional[str] = None,
            cover: Optional[str] = None,
            archived: Optional[bool] = False,
        ):
            Update.page(Update, page_id, icon, cover, data, archived)

        # not currently in use but for future updates
        def db(
            page_id,
            title: Optional[str] = None,
            data: Optional[List[Tuple[str, str, Optional[Any]]]] = None,
            icon: Optional[str] = None,
            cover: Optional[str] = None,
            archived: Optional[bool] = False,
        ):
            Update.db(Update, page_id, title, icon, cover, data, archived)
