# How you would call it in your main app logic:
# data = db.query(UserHealth).filter(...).first()
# score, level, message = calculate_score(data)
# data.risk_score = score
# data.risk_level = level
# db.commit()

def calculate_score(data):
    # =========================================================================
    # CONFIGURATION: Curve shapes & scaling factors
    # =========================================================================
    SCALES = {
        "stress_slope": 1.0,         
        "fruit_slope": -1.0,         
        "energy_slope": -1.5,        
        "sugary_drinks_curve": 0.35,  
        "caffeinated_drinks_curve": 0.35, # Synced from your database column
        "processed_food_curve": 0.30, 
        "drug_usage_curve": 0.31,     
    }
    
    BINARY_WEIGHTS = {
        "late_night_scrolling": 2, "late_night_studying": 2,
        "caffeine_at_night": 2, "sugar_at_night": 2,
        "mostly_sitting": 1, "vape_cigarette": 2, 
        "alcohol": 2, "cannabis": 2
    }

    score = 0.0 

    # =========================================================================
    # 1. LINEAR PATTERNS
    # =========================================================================
    score += (data.stress_level - 1) * SCALES["stress_slope"]
    score += 3 + (data.fruits_vegetables_frequency - 1) * SCALES["fruit_slope"]
    score += 2 + (data.energy_level - 1) * SCALES["energy_slope"]
    score += 4 + (data.social_connection - 1) * -1.25

    # =========================================================================
    # 2. CURVED / EXPONENTIAL PATTERNS
    # =========================================================================
    score += -2 + ((data.sugary_drinks_frequency - 1) ** 2) * SCALES["sugary_drinks_curve"]
    score += -1 + ((data.caffeinated_drinks_frequency - 1) ** 2) * SCALES["caffeinated_drinks_curve"]
    score += -2 + ((data.processed_food_frequency - 1) ** 2) * SCALES["processed_food_curve"]
    score += 0 + ((data.overwhelmed_level - 1) ** 2) * 0.31
    score += 0 + ((data.excessive_drug_usage - 1) ** 2) * SCALES["drug_usage_curve"]

    # =========================================================================
    # 3. BINARY & STEP CONDITIONS
    # =========================================================================
    if data.sleep_hours < 6: score += 2
    elif data.sleep_hours < 8: score += 1
    
    if data.sleep_consistency == 3: score -= 1
    elif data.sleep_consistency <= 2: score += 1 
    
    if data.exercise_hours < 1: score += 2
    elif data.exercise_hours < 3: score += 1

    habits = [
        ("late_night_scrolling", data.late_night_scrolling),
        ("late_night_studying", data.late_night_studying),
        ("caffeine_at_night", data.caffeine_at_night),
        ("sugar_at_night", data.sugar_at_night),
        ("mostly_sitting", data.mostly_sitting),
        ("vape_cigarette", data.vape_cigarette),
        ("alcohol", data.alcohol),
        ("cannabis", data.cannabis)
    ]
    score += sum(BINARY_WEIGHTS[key] for key, active in habits if active)

    # BMI & Age
    bmi = data.weight / ((data.height / 100) ** 2)
    if bmi < 18.5 or (25 <= bmi < 30): score += 1
    elif bmi >= 30: score += 2

    if data.age >= 60: score += 2
    elif data.age >= 40: score += 1

    final_score = round(score, 2) # Saved as Float in database, keeping decimals intact for better tracking

    # Risk Level Classification 
    if final_score <= 10: level, message = "Low", "Healthy Lifestyle"
    elif final_score <= 25: level, message = "Moderate", "Some improvements needed"
    else: level, message = "High", "High Health Risk; Please consult a doctor"

    return final_score, level, message

#For Future Reference:
#For the AI, it can be kinda concerning if the user says that they are a 1 year old that
#weighs 50 kg and is 180 cm. For now, we do not need to worry about these outliers


# 7 - Family History/Genetic Pattern (Yes or no of diabetes, heart attack...)
# Instead of just adding points when bad behavior, decrease/reward when good behavior
# RECOMMENDATION SYSTEM (eg. Reduce sugar, increase exercise)
#TODO: RESEARCH the EVIDENCE that validates every factor (ex: Bad sleep -->cardiac arrest)
#TODO: WEIGHT the factors based off reputable data and research
#TODO: Interaction Effects: If bad_sleep > 1 & stress > 2: score += 1
#TODO: VALIDATE the model by testing it (gather data from ppl around you)
# State that the model is just a prediction and should not be used over proffessional advice
#TODO: Extend index