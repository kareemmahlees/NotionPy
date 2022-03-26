from typing import Any, Callable, Dict, List, Tuple
import json

import _constants

Vector = List[Tuple[str, str, Any]]


def parse_data_for_creating(data: Vector) -> Dict:
    """
    function for collecting the inputed params into a notion acceptable dict for further conversion into json
    Args:
        list of tuples each containing (property name , property type , value of property )
    """
    parsed_dict = {}
    for name, type_, content in data:
        if type_.upper() not in {
            i for i in _constants.__dict__.keys()
        }:  # check if property type exists
            raise ValueError(f"Property {type_} Doesn't exist")

        else:
            type_attr = getattr(_constants, type_.upper())
            parsed_dict.update(type_attr(name, content))

    return parsed_dict


def parse_into_json(parsed_data: Callable[[Vector], Dict]):
    return json.dumps(parsed_data)
