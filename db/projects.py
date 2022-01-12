from typing import List
from pymongo import MongoClient


mongo_client = MongoClient('mongo')
db = mongo_client['mos']
project_collection = db['projects']


def get_project(title: str):
    return project_collection.find_one({'title': title})


def get_all_projects():
    return project_collection.find()


def create_project(start_date, title: str, description: str, contributors: List[str]):
    if not get_project(title):
        project = {
            'start_date': start_date,
            'title': title,
            'description': description,
            'contributors': contributors
        }
        return project_collection.insert_one(project)

    raise ValueError('title already taken!')

