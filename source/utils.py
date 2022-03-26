from typing import Any, Dict, List, Tuple

import _constants


def parse_data_for_creating(data: List[Tuple[str, str, Any]]) -> Dict:
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
