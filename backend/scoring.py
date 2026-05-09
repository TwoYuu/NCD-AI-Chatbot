def calculate_score(data):
    score = 0

    # -------------------
    # Sleep scoring
    # -------------------
    if data.sleep_hours < 6:
        score += 2
    elif data.sleep_hours < 8:
        score += 1

    # -------------------
    # Exercise scoring
    # -------------------
    if data.exercise_hours < 1:
        score += 2
    elif data.exercise_hours < 3:
        score += 1

    # -------------------
    # BMI scoring
    # height is in cm
    # -------------------
    height_m = data.height / 100

    bmi = data.weight / (height_m ** 2)

    if bmi < 18.5:
        score += 1
    elif bmi >= 25 and bmi < 30:
        score += 1
    elif bmi >= 30:
        score += 2

    # -------------------
    # Age scoring
    # -------------------
    if data.age >= 60:
        score += 2
    elif data.age >= 40:
        score += 1

    # -------------------
    # Risk Level Classification
    # -------------------
    if score <= 2:
        level = "Low"
        message = "Healthy Lifestyle"

    elif score <= 5:
        level = "Moderate"
        message = "Some improvements needed"

    else:
        level = "High"
        message = "High Health Risk"

    return score, level, message