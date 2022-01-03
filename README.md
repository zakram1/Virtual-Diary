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
pip install -r requirements.txt  # For Windows users

pip3 install -r requirements.txt # For Mac and Linux users
```

#### Setup
First, open the `.env` file and edit the `MYSQLDB_USER` and `MYSQLDB_PASS` values to match your MySQL username and password.

Then, run `app.py` to boot up the uvicorn server and initialize the database.

Finally, run `diary.py` to start the program.

##### *As of 01/03/2022 this program runs best on `Python 3.9.5`
