document.addEventListener("DOMContentLoaded", () => {
    const greetingSection = document.getElementById("greeting-section");
    const questionnaireSection = document.getElementById("questionnaire-section");
    const startButton = document.getElementById("start-questionnaire");

    // We'll store responses in a simple JSON string that grows as questions are answered.
    let jsonString = "{}";

    // Starts the questionnaire when the start button is clicked.
    startButton?.addEventListener("click", () => {
        console.log("Starting questionnaire...");
        greetingSection?.classList.add("hidden");
        questionnaireSection?.classList.remove("hidden");
        loadQuestions();
    });

    // Manages loading and displaying each question from the list.
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

        // Updates the JSON string with the latest response.
        function updateJsonString(key, value) {
            const json = JSON.parse(jsonString);
            json[key] = value;
            jsonString = JSON.stringify(json);
        }

        // Displays a single question and handles its input logic.
        function showQuestion(index) {
            form.innerHTML = ""; // Clear out the previous question
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

        // Decides whether to show the next question or send the data.
        function handleNextQuestion() {
            if (currentQuestion < questions.length) {
                showQuestion(currentQuestion);
            } else {
                submitToQuestionnaire(); // When it's all done it triggers this function.
            }
        }

        // sends JSON string to the server when the questionnaire's done.
        function submitToQuestionnaire() {
            console.log("Submitting JSON string to /recommend:", jsonString);

            const submitButton = document.querySelector("#submit-button");
            if (submitButton) submitButton.disabled = true; // Disable the button to prevent spamming.

            fetch("/recommend", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json", // Set the content type to JSON.
                },
                body: jsonString,
            })
                .then((response) => {
                    if (response.ok) {
                        console.log("Data submitted successfully! Flask will handle redirection.");
                        // Let Flask deal with redirection
                    } else {
                        console.error("Failed to submit data. Status:", response.status);
                    }
                })
                .catch((error) => {
                    console.error("Error during fetch:", error.message);
                    alert(`Error: ${error.message}`);
                })
                .finally(() => {
                    if (submitButton) submitButton.disabled = false; // Re-enable button once done.
                });
        }

        showQuestion(currentQuestion); // Start the process with the first question.
    }

    // Adds background images to sections if a data-bg attribute is set.
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
