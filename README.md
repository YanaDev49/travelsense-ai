# 𝖳ravelSense 𝖠𝖨 𝖥𝖾𝖺𝗍𝗎𝗋𝖾 𝖡𝗒 𝖠𝖺𝗅𝗂𝗒𝖺𝗇𝖺 𝖠𝖽𝗈𝗅𝖾𝗒 𝖬𝗂𝗇𝗀𝗅𝖾 ![Build Passing](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)
![Flask](https://img.shields.io/pypi/v/Flask?label=Flask&style=flat-square&logo=flask&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-InMemory%20Database-red?style=flat-square)
![Model](https://img.shields.io/badge/Model-v1.0-0078D4?style=flat-square&logo=codeforces&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![HTML](https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=css3&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-2496ED?style=flat-square&logo=docker&logoColor=white)

## Welcome to 𝖳ravelSense AI 🤖
![Screenshot 2025-05-24 170214](https://github.com/user-attachments/assets/1d9715bd-3012-4f31-9c6c-ae412e0f9583)


## Feature Inspiration 💡

### Travel Sense AI was born out of my deep passion for travel and a genuine curiosity for tackling everyday challenges.
#### If you're anything like me and absolutely love exploring new places, then you’ll know just how much of a headache planning can be. Hotels, activities, restaurants; the list goes on. It can easily become overwhelming and chaotic, especially if you haven’t sorted it all months in advance. But imagine having an AI model that takes care of all of that for you, tailored entirely around your preferences, from dietary requirements to specific interests and personal needs. If that’s not the ultimate travel solution, then honestly, what is?

![Screenshot 2025-05-24 181334](https://github.com/user-attachments/assets/a8d4f36b-3325-42e3-937e-41d6629ca65e)


Software development often involves a degree of **uncertainty**. Developers strive to solve problems and build features that meet user needs, but it’s all too easy to fall into the trap of building for **assumptions** rather than facts, which is why I actively researched the impact of having a person centred approach for this AI model and why it solves a universal problem. 🔍

 A study titled *"Validation of User Preferences and Effects of Personalized Gamification"* found that **software features reflecting user preferences significantly improve engagement and task performance**. Participants using **personalised settings** reported a more enjoyable experience and showed higher interaction rates. 📊

For Travel sense AI, having a **questionnaire** to gather data about users' **travel preferences** and syncing itineraries with their **past travel history** and additional present data can improve **engagement**. This approach enhances the **relevance** of travel recommendations and creates a more **seamless**, **personalised travel experience**. ✈️

![Screenshot 2025-05-24 181437](https://github.com/user-attachments/assets/0a9e6f6c-b884-4d7c-ae08-43f592fdda84)


**[Link to study](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2020.00029/full)** 📎

This research helped me foresee how **Travel Sense AI** could positively impact Travellers for the better. By going the extra mile to ensure that each **itinerary recommendation** was **thoughtfully tailored** to individual preferences, the model wouldn’t just meet **user needs** but would create **moments of delight**. It became clear to me that a person centred approach wasn’t just a method to improve **accuracy**, it was a way to embed **empathy** into development. ✨


### Now, Lets dive into the technical Components of Travel Sense AI and how the technologies I used assemble together to create this solution!
#

# 📝 Technologies I used for Travel-Sense 📋

![Screenshot 2025-05-24 181503](https://github.com/user-attachments/assets/c9312ad8-9f86-48cd-8a29-1298204b638e)


### These are the core technologies used to build and run the application itself:

| **Technologies**            | **Description**                          |
|-----------------------------|------------------------------------------|
| 🐍 **Python Flask**          | I used Flask to build the backend of my app, handling the user questionnaire and generating personalised itineraries based on the data collected. |
| 📦 **Redis**                 | Redis is used to store the answers from my questionnaire and manage session data, ensuring quick access to user responses and improving the app’s performance. |
| 📜 **JavaScript**            | I used JavaScript to make the frontend interactive and responsive, allowing users to smoothly complete the questionnaire and view their personalised itineraries. |
| 🧠 **Model**                 | I developed a model that processes user responses from the questionnaire to generate personalised itineraries tailored to Trainline user preferences. |
| 🌐 **HTML**                  | HTML structures the content of my app’s user interface, making it straightforward for users to navigate through the questionnaire and results. |
| 🎨 **CSS**                   | CSS styles the user interface, ensuring the app looks clean, modern, and visually appealing. |
| 🐳 **Docker Compose**        | I used Docker Compose to manage both the app and its dependencies, such as Redis, making it simple to deploy my application consistently across different environments. |
| 🛠️ **Docker**                | Docker allowed me to containerise my app, ensuring it runs smoothly and reliably on any system without compatibility issues. |

# 



# What I learned from developing Tailored-line (Errors, Concepts, Engineering and more!)💡

![Screenshot 2025-05-24 181620](https://github.com/user-attachments/assets/e6f5b0bc-6561-4e94-a953-0d5a8f66fd3a)


### concepts:

Developing **Travel Sense AI** challenged me to think critically about making certain **decisions** such as what **database** to use to store **user inputs** and how to handle **user data** to make **predictions** for the **itinerary**.

I thought about the **functionality** of my application and knew I would need a **database** that could quickly retrieve **data** in a **cached state**.

In regards to the **Python module (model)** that I used to handle the **data**, I initially settled on researching different types of **machine learning models** to fit within this feature. However, I realised that understanding the **principles of machine learning** and how to **train a machine learning model** to understand and process **data** would require extensive **time and research**.

The **Python module (model)** handles the **data** using **recommendation logic** to create the perfect **travel options** with **key-value pairs**. It **cross joins** data from **preloaded CSV files** along with **JSON data** stored in **Redis** with the **user inputs** from the **travel questionnaire**.

#

### Errors:

 In my application, one of the purposes of my **JavaScript** code was to store **user inputs** as a **JSON string** so that it could communicate a **POST request** to the **backend** to send the **user input data** to generate the **itinerary**.

However, there was an **error** in my **JavaScript** code where it was sending **multiple POST requests** to the **backend Python code**. This caused my **Python code** to have trouble processing all these **requests** and to understand which **request** was in **JSON form**.

To solve this problem, I had to add a **HTTP header** within my **Python code** to ensure that the **POST requests** were in **JSON form** before processing it for the **itinerary**. (The HTTP header is what makes sure the data is in JSON form so that the backend can process the request.)

#
# Improvements I could have made with Travel Sense  ✅📈

### Implementing realtime machine learning model:

 One of the key **improvements** I could implement with **Tailored-line** is using an actual **machine learning model** to present a **realtime experience** for the application.

While the **Python module (model)** simulates an **AI experience**, having a real **trained model** to perform the **function** of the application improves overall **user experience** and **organisation** of the **code**.


### Improving adaptability of code:

 When thinking about my **application** in a **production** sense, I think I could have improved my **code** by developing it to **receive** all different types of **user inputs**.

For example, the current **code** in my **application** is specifically developed to represent our **Trainliner 'Ruby'**, with **pre-configured travel data** and **inputs** from her **questionnaire**. However, this **application** will need to be open to **receiving** all different types of **user inputs** from different **user destinations**, **dietary requirements**, to **travel preferences**.

This is what will make **Tailored-line** **inclusive** to all **users**, by adapting the **code** to be **receptive** to all **user inputs**.

### Thinking about scalability:

 Although I thought carefully about each and every **technology** I used in my **application**, thinking about **optimisation** and **scalability** would have improved the overall **system design** and **architecture**.

For example, understanding whether I would need to **vertically** or **horizontally scale** my **application**. **Tailored-line** is a feature intended to be used by **billions of Trainline users** simultaneously, meaning that **horizontal scaling** would be something I would need to think about (adding more **servers** to my **machine** to handle **user traffic**).

Critically thinking about how much **data traffic** would be coming in and out of the **application** is crucial as well, and therefore applying concepts such as **database replication** would need to be considered additionally.



#
# Local App Set up 🖥️

### Build and run the containers 🐳
```
 docker-compose --build
```
This command builds the images for application as defined in the docker-compose.yml file. It reads the Dockerfile for each service, such as my Flask app and Redis, and creates the necessary images to run the application.
```                        
docker-compose up
```
This command builds the images and starts the containers in one step. In this app, if I’ve made changes to the Dockerfile or any dependencies, this command ensures the images are rebuilt before the app starts running.

#
## How to Access The Application 🚀
### Open your browser and navigate to this web link after running the docker containers: http://127.0.0.1:5000/

#### You will be greeted with a beautiful and sleek Welcome page Ready for you to experience Tailored-line 😊

**Note:** I have specifically developed the code for the Travel Questionnaire to only accept specified inputs as a test run.

> ## Here are the answers for each question
>
> ### 1. Where is your travel destination = 'milan'
>
> ### 2. Do you have dietry requirements = 'vegan' (select button)
>
> ### 3. Where is the area of your stay location (hotel)? = 'isola'
>
> ### 4. What do you prefer? = A. Sight seeing, Tourist attractions, museums (select button)

### Navigate to http://127.0.0.1:5000/itinerary after finishing the Travel Questionnaire to view the web page with the travel itinerary displayed!
#
# Thank you! 🎊
