import os

from os.path import join, dirname
from dotenv import load_dotenv
from invoke import task

from pymongo import MongoClient

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

mongo_root_username = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
mongo_root_password = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")

root_password = mongo_root_username + ":" + mongo_root_password
client = MongoClient("mongodb://" + root_password + "@localhost:27017")


@task
def sh(c, command):
    """Execute a shell command."""
    print("client", client)
    c.run(command)


@task
def mongo_show_company_list(c):
    """ show company list in mongodb. """

    db = client["company_search_engine"]
    collection = db["company_company"]

    for obj in collection.find():
        print(
            obj["id"],
            obj["name"],
            obj["name_kana"],
            # obj["corporate_name"]
        )

    # print(collection.find_one())
    client.close()


@task
def mongo_insert_company_list(c):
    """ insert company list. """

    db = client["company_search_engine"]
    collection = db["company_company"]

    # output_company_list.csv
    output_csv = "output_company_list.csv"

    file_path = join(
        dirname(__file__),
        "../company_search_crawler/" + output_csv
    )
    with open(file_path) as f:
        name, name_kana, description = f.readline().split(',')

        last_id = len([None for c in collection.find()])

        company_list = []
        for s_line in f:
            name, name_kana, description = s_line.split(',')

            last_id += 1

            company_list.append({
                'id': last_id,
                'name': name,
                'name_kana': name_kana,
                'description': description,
                'is_removed': False
            })

    collection.insert_many(company_list)
