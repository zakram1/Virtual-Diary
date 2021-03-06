# Virtual Diary

Virtual Diary saves your diary entries in a database, so you can manage the stories of your life.

---

### About
This project utilizes FastAPI as the web framework to aid in the transferring of  user data and MySQL as the database to store your diary entries.

---

## Usage

#### Installation
Use [pip](https://pip.pypa.io/en/stable/) to install the required dependencies.

```bash
pip3 install requests, mysql-connector-python, fastapi[all], python-dotenv
```

#### Setup
First, open the `.env` file and edit the `MYSQLDB_USER` and `MYSQLDB_PASS` values to match your MySQL username and password.

Then, run `app.py` to boot up the uvicorn server and initialize the database.

Finally, run `diary.py` to start the program.
