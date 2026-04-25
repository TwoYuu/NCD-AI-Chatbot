def calculate_score(data):
    score = 0

    # Sleep scoring
    if data.sleep_hours < 6:
        score += 2
    elif data.sleep_hours < 8:
        score += 1

    # Exercise scoring
    if data.exercise_hours < 1:
        score += 2
    elif data.exercise_hours < 3:
        score += 1


    #Risk Score
    if score <= 1:
        level = "Low"
        message = "Healthy Lifestyle"
    elif score <= 3:
        level = "Moderate"
        message = "Some improvements needed"
    else:
        level = "High"
        message = "High Health Risk"

    return score, level, message