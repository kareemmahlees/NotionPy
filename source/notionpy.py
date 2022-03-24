import json
import requests


class NotionClient(requests):
    def __init__(self, token: str, db_id: str = None, page_id: str = None):
        self.db_id = db_id
        self.token = token
        self.headers = {
            "Authorization": "Bearer " + self.token,
            "Notion-Version": "2022-02-22",
            "Content-Type": "application/json",
        }

    def create(self):
        def page(self):
            pass

        def db(self):
            pass

    def retreive(self):
        def page(self):
            pass

        def db(self):
            pass
