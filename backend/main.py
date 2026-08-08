from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import uvicorn
#TODO: Start up backend, cd frontend + python -m http.server 5500 in terminal, localhost:5500 in google
import models, schemas, scoring
from database import engine, SessionLocal


#Creates database; database.py sets up essential variables

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/analyze", response_model=schemas.UserHealthResponse)
def analyze(data: schemas.UserHealthCreate, db: Session = Depends(get_db)):
    
    # CALCULATE FIRST
    score, level, message, bmi, bmi_percentile = scoring.calculate_score(data)

    # Save to database - data_dict is where data is stored
    data_dict = data.dict()   # <- add ()

    data_dict.update({
        "risk_score": score,
        "risk_level": level
    })
    print(data_dict)
    db_data = models.UserHealth(**data_dict)
    print(db_data)

    
    db.add(db_data)
    print("About to save:")
    print(data_dict)
    db.commit()
    print("Database commit successful")
    db.refresh(db_data)

    return {
        "risk_score": score,
        "risk_level": level,
        "message": message,
        "bmi": bmi,
        "bmi_percentile": bmi_percentile
        
    }


# RUN APP
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


