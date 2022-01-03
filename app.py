import mysql.connector, uvicorn, os, time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()


class Entries(BaseModel):
    DiaryName: str
    DiaryEntries: str


class SecondEntry(BaseModel):
    DiaryEntries: str


def start_db():
    global mydb, my_cursor
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user=os.environ.get("MYSQLDB_USER"),
        password=os.environ.get("MYSQLDB_PASS")
    )

    my_cursor = mydb.cursor()

    my_cursor.execute("CREATE DATABASE IF NOT EXISTS diaries")
    print("Database initiated! Connecting...")
    print("Connected!")

    # Once the database is created, you now connect to it
    mydb = mysql.connector.connect(
        host="localhost",
        user=os.environ.get("MYSQLDB_USER"),
        password=os.environ.get("MYSQLDB_PASS"),
        database="diaries"
    )

    my_cursor = mydb.cursor()

    # Creating the entries table and two columns for entry name and the entry itself
    my_cursor.execute(
        "CREATE TABLE IF NOT EXISTS entries (id INT AUTO_INCREMENT PRIMARY KEY, DiaryName LONGTEXT NOT NULL, "
        "DiaryEntries LONGTEXT NOT NULL, UNIQUE (id))")
    time.sleep(2)
    print("All contents fully loaded!")
    return mydb


# To create a database on startup
@app.on_event("startup")
def startup_event():
    start_db()


# To make an entry
@app.post('/publishentry/{first_entry}')
def make_entry(first_entry: str, second_entry: SecondEntry) -> str:
    sqlval = "INSERT INTO entries (DiaryName, DiaryEntries) VALUES (%s, %s)"
    myval = (first_entry, second_entry.DiaryEntries)
    my_cursor.execute(sqlval, myval)

    mydb.commit()
    return ''


# Read an entry
@app.get("/readentry/{read_diary}")
def read_entry(read_diary: str) -> Entries:
    my_cursor.execute(f"SELECT DiaryName, DiaryEntries FROM entries WHERE DiaryName='{read_diary}'")
    result = my_cursor.fetchone()

    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return Entries(DiaryName=result[0], DiaryEntries=result[1])


# Delete an entry
@app.delete('/removeentry/{remove_diary}')
def delete_entry(remove_diary: str) -> str:
    sqlvalue = "DELETE FROM entries WHERE DiaryName = %s LIMIT 1"

    my_cursor.execute(sqlvalue, (remove_diary, ))

    mydb.commit()

    if my_cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return ''


if __name__ == '__main__':
    uvicorn.run("app:app")
