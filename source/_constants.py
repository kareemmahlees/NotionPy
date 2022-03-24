CREATE_DB_URL = "https://api.notion.com/v1/databases"

CREATE_PAGE_URL = "https://api.notion.com/v1/pages"

QUERY_DB_URL = lambda dbid: f"https://api.notion.com/v1/databases/{dbid}/query"

QUERY_PAGE_URL = lambda pgid: f"https://api.notion.com/v1/pages/{pgid}"

NAME_PROP = lambda prop_name, content: {
    prop_name: {"title": [{"type": "text", "text": {"content": content}}]}
}

RICH_TXT_PROP = lambda prop_name, content: {
    prop_name: {"rich_text": [{"type": "text", "text": {"content": content}}]}
}

SELECT_PROP = lambda prop_name, option_name: {
    prop_name: {"select": {"name": option_name}}
}

MULTI_SELECT_PROP = lambda prop_name, select_options: {
    prop_name: {"multi_select": [{"name": option} for option in select_options]}
}

RELATION_PROP = lambda prop_name, releated_pg_id: {
    prop_name: {"relation": [{"id": releated_pg_id}]}
}

PEOPLE_PROP = lambda prop_name, person_id: {
    prop_name: {"people": [{"object": "user", "id": p_id} for p_id in person_id]}
}

CHECKBOX_PROP = lambda prop_name, status: {prop_name: {"checkbox": status}}

URL_PROP = lambda prop_name, content: {prop_name: {"url": content}}

FILES_PROP = lambda prop_name, url: {
    prop_name: {"files": [{"type": "external", "name": "content", "external": url}]}
}

EMAIL_PROP = lambda prop_name, email: {prop_name: {"email": email}}

PHONE_PROP = lambda prop_name, phone: {prop_name: {"phone_number": phone}}
