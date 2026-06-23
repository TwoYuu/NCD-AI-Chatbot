console.log("script.js loaded");
const form = document.getElementById("healthForm");

document.getElementById("analyzeBtn").addEventListener("click", async (e) => {
    e.preventDefault();
    console.log("Submit intercepted");
    // Collect values matching your schemas.py fields
    const data = {
        // Demographics & Physical Metrics
        age: parseInt(document.getElementById("age").value),
        weight: parseFloat(document.getElementById("weight").value),
        height: parseFloat(document.getElementById("height").value),

        // Sleep & Night Habits
        sleep_hours: parseFloat(document.getElementById("sleep_hours").value),
        sleep_consistency: parseInt(document.getElementById("sleep_consistency").value),
        late_night_scrolling: document.getElementById("late_night_scrolling").checked,
        late_night_studying: document.getElementById("late_night_studying").checked,
        caffeine_at_night: document.getElementById("caffeine_at_night").checked,
        sugar_at_night: document.getElementById("sugar_at_night").checked,

        // Physical Activity
        exercise_hours: parseFloat(document.getElementById("exercise_hours").value),
        mostly_sitting: document.getElementById("mostly_sitting").checked,

        // Diet & Energy
        fruits_vegetables_frequency: parseInt(document.getElementById("fruits_vegetables_frequency").value),
        sugary_drinks_frequency: parseInt(document.getElementById("sugary_drinks_frequency").value),
        caffeinated_drinks_frequency: parseInt(document.getElementById("caffeinated_drinks_frequency").value),
        processed_food_frequency: parseInt(document.getElementById("processed_food_frequency").value),
        energy_level: parseInt(document.getElementById("energy_level").value),

        // Mental Health
        stress_level: parseInt(document.getElementById("stress_level").value),
        overwhelmed_level: parseInt(document.getElementById("overwhelmed_level").value),
        social_connection: parseInt(document.getElementById("social_connection").value),

        // Substance Use
        vape_cigarette: document.getElementById("vape_cigarette").checked,
        alcohol: document.getElementById("alcohol").checked,
        cannabis: document.getElementById("cannabis").checked,
        excessive_drug_usage: parseInt(document.getElementById("excessive_drug_usage").value)
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const result = await response.json();
        console.log("Received result:", result);

        // Display results
        document.getElementById("riskScore").textContent = result.risk_score;
        console.log("Updated score");
        document.getElementById("riskLevel").textContent = result.risk_level;
        console.log("Updated level");
        document.getElementById("message").textContent = result.message;
        console.log("Updated message");
        
        document.getElementById("result").style.backgroundColor = "yellow";
    } catch (error) {
        console.error(error);
        alert("Error connecting to backend or invalid inputs submitted.");
    }
});