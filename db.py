import json
import os
import shutil

# Path inside the bundle
DB_EXEC_PATH = os.path.join(os.path.dirname(__file__), "db.json")

# Writable path in user's home directory
DB_WRITABLE_PATH = os.path.join(os.path.expanduser("~/.myapp"), "db.json")
os.makedirs(os.path.dirname(DB_WRITABLE_PATH), exist_ok=True)

# On first run, copy db.json if it doesn't exist
if not os.path.exists(DB_WRITABLE_PATH):
    shutil.copy(DB_EXEC_PATH, DB_WRITABLE_PATH)


class Database:
    def add_data(self, name, email, passwd):
        with open(DB_WRITABLE_PATH, "r") as rf:
            database = json.load(rf)

        if email in database:
            return 0
        else:
            database[email] = [name, passwd]
            with open(DB_WRITABLE_PATH, "w") as wf:
                json.dump(database, wf)
            return 1

    def search(self, email, passwd):
        with open(DB_WRITABLE_PATH, "r") as rf:
            database = json.load(rf)

        if email in database and database[email][1] == passwd:
            return 1
        else:
            return 0
