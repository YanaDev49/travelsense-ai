document.addEventListener("DOMContentLoaded", () => {
    const greetingSection = document.getElementById("greeting-section");
    const questionnaireSection = document.getElementById("questionnaire-section");
    const startButton = document.getElementById("start-questionnaire");

    // questionnaire input data from user will be stored as JSON string.
    let jsonString = "{}";

    
    startButton?.addEventListener("click", () => {
        console.log("Starting questionnaire...");
        greetingSection?.classList.add("hidden");
        questionnaireSection?.classList.remove("hidden");
        loadQuestions();
    });

    
    function loadQuestions() {
        const form = document.getElementById("questionnaire-form");

        const questions = [
            { question: "Where is your travel destination?", inputType: "text", expected: "milan", key: "destination" },
            {
                question: "Do you have dietary requirements?",
                inputType: "button",
                options: ["Vegan", "Pescatarian", "Halal", "Vegetarian", "Celiac", "Gluten Free"],
                expected: "Vegan",
                key: "dietary",
            },
            { question: "Where is the area of your stay location (hotel)?", inputType: "text", expected: "isola", key: "hotel_area" },
            {
                question: "What do you prefer?",
                inputType: "button",
                options: ["A. Sightseeing, Tourist attractions, museums", "B. Road trips, historical sites"],
                expected: "A. Sightseeing, Tourist attractions, museums",
                key: "preference",
            },
        ];

        let currentQuestion = 0;

        
        function updateJsonString(key, value) {
            const json = JSON.parse(jsonString);
            json[key] = value;
            jsonString = JSON.stringify(json);
        }

        
        function showQuestion(index) {
            form.innerHTML = ""; 
            const question = questions[index];
            const questionText = document.createElement("h3");
            questionText.textContent = question.question;
            form.appendChild(questionText);

            if (question.inputType === "text") {
                const input = document.createElement("input");
                input.type = "text";
                form.appendChild(input);

                const nextButton = document.createElement("button");
                nextButton.textContent = "Next";
                nextButton.classList.add("question-button");
                nextButton.addEventListener("click", () => {
                    if (input.value.trim().toLowerCase() !== question.expected.toLowerCase()) {
                        alert("Incorrect input. Try again.");
                        return;
                    }
                    updateJsonString(question.key, input.value.trim());
                    currentQuestion++;
                    handleNextQuestion();
                });
                form.appendChild(nextButton);
            } else if (question.inputType === "button") {
                question.options.forEach((option) => {
                    const button = document.createElement("button");
                    button.textContent = option;
                    button.classList.add("question-button");
                    button.addEventListener("click", () => {
                        if (button.textContent === question.expected) {
                            updateJsonString(question.key, button.textContent);
                            currentQuestion++;
                            handleNextQuestion();
                        } else {
                            alert("Incorrect choice. Try again.");
                        }
                    });
                    form.appendChild(button);
                });
            }
        }

        
        function handleNextQuestion() {
            if (currentQuestion < questions.length) {
                showQuestion(currentQuestion);
            } else {
                submitToQuestionnaire(); 
            }
        }

        
        function submitToQuestionnaire() {
            console.log("Submitting JSON string to /recommend:", jsonString);

            const submitButton = document.querySelector("#submit-button");
            if (submitButton) submitButton.disabled = true; 

            fetch("/recommend", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json", 
                },
                body: jsonString,
            })
                .then((response) => {
                    if (response.ok) {
                        console.log("Data submitted successfully! Flask will handle redirection.");
                        
                    } else {
                        console.error("Failed to submit data. Status:", response.status);
                    }
                })
                .catch((error) => {
                    console.error("Error during fetch:", error.message);
                    alert(`Error: ${error.message}`);
                })
                .finally(() => {
                    if (submitButton) submitButton.disabled = false; 
                });
        }

        showQuestion(currentQuestion); // Start the process with the first question.
    }

    
    const bgSections = document.querySelectorAll("[data-bg]");
    bgSections.forEach((section) => {
        const bgImage = section.getAttribute("data-bg");
        if (bgImage) {
            section.style.backgroundImage = `url('${bgImage}')`;
        } else {
            console.warn("No data-bg found for section:", section);
        }
    });
});
