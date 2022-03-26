from datetime import datetime

# from notionpy import NotionClient

# HEADERS = NotionClient().headers


CREATE_DB_URL = "https://api.notion.com/v1/databases"

CREATE_PAGE_URL = "https://api.notion.com/v1/pages"

QUERY_DB_URL = lambda dbid: f"https://api.notion.com/v1/databases/{dbid}/query"

QUERY_PAGE_URL = lambda pgid: f"https://api.notion.com/v1/pages/{pgid}"

CREATING_PAGE_TEMPLATE = lambda dbid, icon=None, cover_url=None, data=None: {
    "parent": {
        "database_id": dbid,
    },
    "icon": {"type": "emoji", "emoji": icon},
    "cover": {"type": "external", "external": {"url": cover_url}},
    "properties": data,
}

CREATING_DATABASE_TEMPLATE = (
    lambda page_id, title, icon=None, cover_url=None, data=None: {
        "parent": {"type": "page_id", "page_id": page_id},
        "icon": {"type": "emoji", "emoji": icon},
        "cover": {"type": "external", "external": {"url": cover_url}},
        "title": [{"type": "text", "text": {"content": title, "link": None}}],
        "properties": data,
    }
)


TITLE = lambda prop_name, content: {
    prop_name: {"title": [{"type": "text", "text": {"content": content}}]}
}

RICH_TEXT = lambda prop_name, content: {
    prop_name: {"rich_text": [{"type": "text", "text": {"content": content}}]}
}

SELECT = lambda prop_name, option_name: {prop_name: {"select": {"name": option_name}}}

MULTI_SELECT = lambda prop_name, select_options: {
    prop_name: {"multi_select": [{"name": option} for option in select_options]}
}

RELATION = lambda prop_name, releated_pg_id: {
    prop_name: {"relation": [{"id": releated_pg_id}]}
}

PEOPLE = lambda prop_name, person_id: {
    prop_name: {"people": [{"object": "user", "id": p_id} for p_id in person_id]}
}

CHECKBOX = lambda prop_name, status: {prop_name: {"checkbox": status}}

URL = lambda prop_name, content: {prop_name: {"url": content}}

FILES = lambda prop_name, url: {
    prop_name: {"files": [{"type": "external", "name": "content", "external": url}]}
}

EMAIL = lambda prop_name, email: {prop_name: {"email": email}}

PHONE = lambda prop_name, phone: {prop_name: {"phone_number": phone}}

DATE = lambda prop_name, start=None, end=None: {
    prop_name: {
        "date": {
            "start": datetime(start).astimezone().isoformat(),
            "end": datetime(end).astimezone().isoformat(),
        }
    }
}

NUMBER = lambda prop_name, number: {prop_name: {"number": number}}
