# auto-py-notion

for creating,updating and querying databases and pages ,
auto-py-notion is a python module to help you integrete notion with your software/workflow

# installation

in your terminal :

```
pip install auto-py-notion
```

# Requirments

before we get started there are a couple of things we need to do :

1. create an integration and grab a token from [here](https://www.notion.com/my-integrations)
1. share the integration with you database or page
1. get the id of the database or page :
   `https://www.notion.so/myworkspace/a8aec43384f447ed84390e8e42c2e089?v=...`

   the database id is before the question mark and after the backslash

more details from [official notion docs](https://developers.notion.com/docs)

# Getting Started

let's create a sample page inside a database :

```python
from NotionPy.notionpy import NotionClient

inst = NotionClient("Your integration token")

inst.create.page(
    database_id="the id of database of choice",
    data=[      # List of tuples # provided properties must be created first in the db
        ("Name", "title", "kareem"),
            ("price", "number", 254),
            ("to-do", "checkbox", False),
    ],
    #Optional
    icon="🔥",
    #Optional
    cover="https://images.unsplash.com/photo-1523867574998-1a336b6ded04?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y292ZXJ8ZW58MHx8MHx8&w=1000&q=80",
)
```

-> Note that the data inserted must be [(prop_name,type,value)]

- currently there is no support for creating empty pages or empty values but look forward for feature updates

retreiving data from a database :

```python
inst.query.db("id of the database",
                in_json=True, #Optional
                json_indent=2, #Optional
                print_data=True #Optional
            )
```

## Supported properties type

        -title          -rich_text
        -select         -multi_select
        -relation       -people
        -checkbox       -url
        -files          -email
        -phone          -number

# Upcoming Updates

- Add filters and sorts to querying databases for
- Add children objects in page creating
- Add number formating
- Add support for saving the query data in a json file

## Notes

- there are other modules that interact with notion's API so what makes this module different ? it is the fact that , as far as my research went , it is the most userfriendly and practical one
- This module is still fairly simple and has a lot to offer in the future , so all of your suggestions , issues , contributions are very welcomed
