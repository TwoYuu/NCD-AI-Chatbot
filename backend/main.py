from fastapi import FastAPI, HTTPException
import pandas as pd
import sqlite3

app = FastAPI()

# Database setup (simplified)
DATABASE = "student_data.db"

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            weight REAL,
            height REAL,
            BMI REAL,
            activity_level TEXT,
            diet_score INTEGER,
            sleep_score INTEGER
        )
    """)
    conn.commit()
    conn.close()

create_table() # Ensures the table is created if it doesn't exist



@app.get("/students/{student_id}")
async def get_student(student_id: int):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student = cursor.fetchone()
        conn.close()
        if student is None:
            raise HTTPException(status_code=500, detail="Student not found")
        return {"id": student[0], "name": student[1], "age": student[2], "weight": student[3], "height": student[4], "BMI": student[5], "activity_level": student[6], "diet_score": student[7], "sleep_score": student[8]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")



@app.post("/students/")
async def create_student(student_id: int):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Simulate data - replace with actual data processing
        student_data = {"id": student_id, "name": "Alice", "age": 25, "weight": 60, "height": 175, "BMI": 24.5, "activity_level": "Moderate", "diet_score": 7, "sleep_score": 8}
        cursor.execute("INSERT INTO students (id, name, age, weight, height, BMI, activity_level, diet_score, sleep_score) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", student_data)
        conn.commit()
        conn.close()
        return {"message": "Student data created successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

