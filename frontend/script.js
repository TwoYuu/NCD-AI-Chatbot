const form = document.getElementById("healthForm");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    // Collect values
    const data = {
        age: parseInt(document.getElementById("age").value),
        weight: parseFloat(document.getElementById("weight").value),
        height: parseFloat(document.getElementById("height").value),
        sleep_hours: parseFloat(document.getElementById("sleep_hours").value),
        exercise_hours: parseFloat(document.getElementById("exercise_hours").value)
    };

    try {

        const response = await fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        // Display results
        document.getElementById("riskScore").textContent =
            result.risk_score;

        document.getElementById("riskLevel").textContent =
            result.risk_level;

        document.getElementById("message").textContent =
            result.message;

    } catch (error) {
        console.error(error);
        alert("Error connecting to backend");
    }
});