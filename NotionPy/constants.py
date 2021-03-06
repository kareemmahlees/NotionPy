HEADERS = lambda token: {
    "Authorization": "Bearer " + token,
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json",
}

CREATE_DB_URL = "https://api.notion.com/v1/databases"

CREATE_PAGE_URL = "https://api.notion.com/v1/pages"

QUERY_DB_URL = lambda dbid: f"https://api.notion.com/v1/databases/{dbid}/query"

QUERY_PAGE_URL = lambda pgid: f"https://api.notion.com/v1/pages/{pgid}"

UPDATE_PAGE_URL = lambda pgid: f"https://api.notion.com/v1/pages/{pgid}"

ICON = lambda icon: {"icon": {"type": "emoji", "emoji": icon}}

COVER = lambda cover_url: {
    "cover": {"type": "external", "external": {"url": cover_url}}
}

ARCHIVE = lambda state: {"archived": state}

SORT = lambda sorting_info: {
    "sorts": [
        {"property": prop_name, "direction": direction}
        for prop_name, direction in sorting_info
    ]
}

FILTER = lambda filtering_info: {
    "filter": {"property": prop_name, prop_type: {condition: value}}
    for prop_name, prop_type, condition, value in filtering_info
}

AND_FILTER = lambda filtering_info: {
    "filter": {
        "and": [
            {"property": prop_name, prop_type: {condition: value}}
            for prop_name, prop_type, condition, value in filtering_info
        ]
    }
}

OR_FILTER = lambda filtering_info: {
    "filter": {
        "or": [
            {"property": prop_name, prop_type: {condition: value}}
            for prop_name, prop_type, condition, value in filtering_info
        ]
    }
}

DB_TITLE = lambda title: {
    "title": [{"type": "text", "text": {"content": title, "link": None}}]
}

CREATING_PAGE_TEMPLATE = lambda dbid, data=None: {
    "parent": {
        "database_id": dbid,
    },
    "properties": data,
}

CREATING_DATABASE_TEMPLATE = (
    lambda page_id, title=None, data=None: {
        "parent": {"type": "page_id", "page_id": page_id},
        "title": [{"type": "text", "text": {"content": title, "link": None}}],
        "properties": data,
    }
    if title is not None
    else {
        "parent": {"type": "page_id", "page_id": page_id},
        "properties": data,
    }
)

# not currently in use but for future updates
UPDATE_DB_TEMPLATE = (
    lambda db_id, data=None: {
        "parent": {
            "database_id": db_id,
        },
        "properties": data,
    }
    if data is not None
    else {
        "parent": {
            "database_id": db_id,
        },
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
    prop_name: {
        "files": [{"type": "external", "name": "content", "external": {"url": url}}]
    }
}

EMAIL = lambda prop_name, email: {prop_name: {"email": email}}

PHONE = lambda prop_name, phone: {prop_name: {"phone_number": phone}}

NUMBER = lambda prop_name, number: {prop_name: {"number": number}}
