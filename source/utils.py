from typing import Any, Callable, Dict, List, Optional, Tuple
import json

import constants

Vector = List[Tuple[str, str, Optional[Any]]]


def parse_for_pg_creating(db_id, data: Vector, icon=None, cover_url=None) -> Dict:
    """
    function for collecting the inputed params into a notion acceptable dict for further conversion into json
    :param data:
        list of tuples each containing (property name , property type , value of property )
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
    else:
        return


def parse_into_json(parsed_data: Callable[[Vector], Dict]):
    return json.dumps(parsed_data)
