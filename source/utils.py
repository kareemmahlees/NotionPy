from typing import Any, Callable, Dict, List, Optional, Tuple
import json

from source import constants

Vector1 = List[Tuple[str, str, Optional[Any]]]
Vector2 = List[Tuple[str, str]]


def parse_for_pg_creation(
    db_id: str,
    data: Vector1,
    icon: Optional[str] = None,
    cover_url: Optional[str] = None,
) -> Dict:
    """
    function for collecting the inputed params into a notion acceptable dict for further conversion into json
    :param db_id:
        the database id in which the page will be created
    :param data:
        list of tuples each containing (property name , property type , value of property )
    :param icon:
        icon of page
    :param cover_url:
        url of the page's cover
    """
    data_dict = {}
    temp_dict = {}
    if icon is not None:
        temp_dict.update(constants.ICON(icon))
    if cover_url is not None:
        temp_dict.update(constants.COVER(cover_url))
    if data is not None:
        for name, type_, content in data:
            if type_.upper() not in {
                i for i in constants.__dict__.keys()
            }:  # check if property type exists
                raise ValueError(f"Property {type_} Doesn't exist")

            else:
                type_attr = getattr(constants, type_.upper())
                data_dict.update(type_attr(name, content))
        parsed_dict = constants.CREATING_PAGE_TEMPLATE(db_id, data_dict)
        parsed_dict.update(temp_dict)
        return parsed_dict


def parse_into_json(
    parsed_data: Callable[[Optional[Vector1]], Dict], indent: Optional[int] = None
):
    return json.dumps(parsed_data, indent)


def parse_into_dict(json_data):
    return json.loads(json_data)


def parse_for_db_creation(
    pg_id: str,
    title: str,
    data: Vector2,
    icon: Optional[str] = None,
    cover_url: Optional[str] = None,
) -> Dict:
    """
    function for collecting the inputed params into a notion acceptable dict for further conversion into json
    :param pg_id:
        the page id in which the database will be created as a subpage
    :param data:
        list of tuples each containing ( property name , property type )
    :param icon:
        icon of database
    :param cover_url:
        url of the database's cover
    """
    data_dict = {}
    temp_dict = {}
    if icon is not None:
        temp_dict.update(constants.ICON(icon))
    if cover_url is not None:
        temp_dict.update(constants.COVER(cover_url))
    if data is not None:
        for name, type_ in data:
            if type_.upper() not in {
                i for i in constants.__dict__.keys()
            }:  # check if property type exists
                raise ValueError(f"Property {type_} Doesn't exist")

            else:
                type_attr = getattr(constants, type_.upper())
                type_attr_ = type_attr(name, None)
                type_attr_[name] = {type_: {}}

                data_dict.update(type_attr_)
        parsed_dict = constants.CREATING_DATABASE_TEMPLATE(pg_id, title, data_dict)
        parsed_dict.update(temp_dict)
        return parsed_dict


# parse_for_db_creation(
#     "lksjdkjf", "kareem mahlees", [("Name", "title"), ("price", "number")]
# )
