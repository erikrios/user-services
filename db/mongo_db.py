import os

from pymongo import MongoClient


def get_database():
    client = MongoClient(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        authSource="admin"
    )

    return client['userservicesdb']


if __name__ == "__main__":
    db = get_database()
