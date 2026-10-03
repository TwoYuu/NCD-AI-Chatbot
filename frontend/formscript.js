const pages = document.querySelectorAll(".form-page");

const backBtn = document.getElementById("backBtn");
const nextBtn = document.getElementById("nextBtn");
const analyzeBtn = document.getElementById("analyzeBtn");

const result = document.getElementById("result");

let currentPage = 0;


// Start with the first page
function showPage(pageIndex) {

    pages.forEach((page, index) => {
        page.style.display = index === pageIndex ? "block" : "none";
    });

    // Back button
    backBtn.style.display =
        pageIndex === 0 ? "none" : "block";

    // Next button
    nextBtn.style.display =
        pageIndex === pages.length - 1 ? "none" : "block";

    // Analyze button
    analyzeBtn.style.display =
        pageIndex === pages.length - 1 ? "block" : "none";
}


// Check whether the current page is valid
function validateCurrentPage() {

    const currentPageElement = pages[currentPage];

    const inputs =
        currentPageElement.querySelectorAll(
            "input, select"
        );

    for (const input of inputs) {

        if (!input.checkValidity()) {

            input.reportValidity();

            return false;
        }
    }

    return true;
}


// Next button
nextBtn.addEventListener("click", () => {

    if (!validateCurrentPage()) {
        return;
    }

    if (currentPage < pages.length - 1) {

        currentPage++;

        showPage(currentPage);

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    }
});


// Back button
backBtn.addEventListener("click", () => {

    if (currentPage > 0) {

        currentPage--;

        showPage(currentPage);

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    }
});


// Hide results when the page first loads
result.style.display = "none";


// Analyze Health
document.getElementById("healthForm").addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();

        if (!validateCurrentPage()) {
            return;
        }

        const data = {

            age: parseInt(
                document.getElementById("age").value
            ),

            weight: parseFloat(
                document.getElementById("weight").value
            ),

            height: parseFloat(
                document.getElementById("height").value
            ),

            gender: document.getElementById("gender").value,

            sleep_hours: parseFloat(
                document.getElementById("sleep_hours").value
            ),

            sleep_consistency: parseInt(
                document.getElementById("sleep_consistency").value
            ),

            late_night_scrolling:
                document.getElementById(
                    "late_night_scrolling"
                ).checked,

            late_night_studying:
                document.getElementById(
                    "late_night_studying"
                ).checked,

            caffeine_at_night:
                document.getElementById(
                    "caffeine_at_night"
                ).checked,

            sugar_at_night:
                document.getElementById(
                    "sugar_at_night"
                ).checked,

            exercise_hours: parseFloat(
                document.getElementById(
                    "exercise_hours"
                ).value
            ),

            mostly_sitting:
                document.getElementById(
                    "mostly_sitting"
                ).checked,

            fruits_vegetables_frequency: parseInt(
                document.getElementById(
                    "fruits_vegetables_frequency"
                ).value
            ),

            sugary_drinks_frequency: parseInt(
                document.getElementById(
                    "sugary_drinks_frequency"
                ).value
            ),

            caffeinated_drinks_frequency: parseInt(
                document.getElementById(
                    "caffeinated_drinks_frequency"
                ).value
            ),

            processed_food_frequency: parseInt(
                document.getElementById(
                    "processed_food_frequency"
                ).value
            ),

            energy_level: parseInt(
                document.getElementById(
                    "energy_level"
                ).value
            ),

            stress_level: parseInt(
                document.getElementById(
                    "stress_level"
                ).value
            ),

            overwhelmed_level: parseInt(
                document.getElementById(
                    "overwhelmed_level"
                ).value
            ),

            social_connection: parseInt(
                document.getElementById(
                    "social_connection"
                ).value
            ),

            vape_cigarette:
                document.getElementById(
                    "vape_cigarette"
                ).checked,

            alcohol:
                document.getElementById(
                    "alcohol"
                ).checked,

            cannabis:
                document.getElementById(
                    "cannabis"
                ).checked,

            excessive_drug_usage: parseInt(
                document.getElementById(
                    "excessive_drug_usage"
                ).value
            )
        };


        try {
//Gotta make the fetch/port adaptable
//const API_URL = "http://192.168.1.42:8000";
//
//const response = await fetch(
    //`${API_URL}/analyze`,
    //{
        //method: "POST",
        //headers: {
            //"Content-Type": "application/json"
        //},
        //body: JSON.stringify(data)
    //}
//);
            const response = await fetch(
                `${CONFIG.API_BASE_URL}/analyze`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify(data)
                }
            );


            if (!response.ok) {

                throw new Error(
                    "Server returned an error."
                );
            }


            const resultData =
                await response.json();


            // Display results
            document.getElementById(
                "riskScore"
            ).textContent =
                resultData.risk_score;

            document.getElementById(
                "riskLevel"
            ).textContent =
                resultData.risk_level;

            document.getElementById(
                "message"
            ).textContent =
                resultData.message;


            // Hide the form
            document.getElementById(
                "healthForm"
            ).style.display = "none";


            // Show results
            result.style.display = "block";


            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });

        } catch (error) {

            console.error(error);

            alert(
                "There was a problem analyzing your health data. Please try again."
            );
        }
    }
);


// Initialize
showPage(currentPage);