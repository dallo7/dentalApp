Dash Community Dentals - AI-Powered Diagnosis & Treatment Tool
This application leverages the Dash framework and AI models to provide dental diagnosis and treatment recommendations. It offers multiple input methods (audio recording, chat, questionnaire) to gather patient information and utilizes machine learning models to process the input and generate actionable insights.

Table of Contents
Project Overview
Features
Technologies
Installation
Usage
File Structure
Models & Data
Contributing
1. Project Overview
Purpose: The Dash Community Dentals tool aims to streamline and enhance the initial stages of dental consultations by using AI to analyze patient symptoms and provide preliminary diagnoses and treatment plans.

Target Users:

Patients: Can self-assess their dental concerns and gain insights before a formal appointment.
Dental Professionals: Can utilize the tool as a supplemental resource to gather patient information and expedite diagnosis.
2. Features
Multiple Input Methods:
Audio Recording: Patients can describe their symptoms verbally.
Chat: Interact with a basic chatbot to convey concerns.
Questionnaire: Answer a series of multiple-choice questions.
AI-Powered Diagnosis: Machine learning models process patient input and generate a likely diagnosis.
Treatment Recommendations: Provides initial treatment plans based on the predicted diagnosis.
Inference Monitoring: Tracks and displays the history of user inputs, diagnoses, and treatment suggestions.
Word Cloud Analysis: Visually summarizes common symptoms and diagnoses from user interactions.
3. Technologies
Dash: A Python framework for building web applications.
Dash Bootstrap Components (dbc): Provides styling and layout elements for the UI.
Hugging Face Transformers: (Assuming this is how your models are integrated) Library for using pre-trained NLP models like "whisper-large-v2".
scikit-learn (sklearn): Machine learning library for tasks like text vectorization.
Pandas: Data manipulation library for handling dataframes and CSV files.
Other: NumPy, SoundFile, matplotlib, etc.
4. Installation
Clone the Repository:
Bash
git clone <repository-url>
cd <repository-name>
Use code with caution.

Install Dependencies:
Bash
pip install -r requirements.txt
Use code with caution.

Make sure you have the necessary model files and weights in the correct directories.
Run the App:
Bash
python app.py
Use code with caution.

The app should be accessible at http://127.0.0.1:8987/
5. Usage
Access the App: Open your web browser and navigate to the app's URL (usually http://127.0.0.1:8987/).
Choose Input Method: Select how you'd like to provide your information (audio, chat, or questionnaire).
Provide Symptoms:
Audio: Record your voice describing your symptoms.
Chat: Type your concerns in the chatbox.
Questionnaire: Answer the provided questions.
View Results: The app will display the predicted diagnosis, treatment suggestions, and relevant analysis.
6. File Structure
app.py: Main application file, contains the Dash layout and callbacks.
chatInput.py: Contains logic for the chatbot interaction.
landingPage.py: Defines the initial landing page layout.
modelsDisease.py: Handles the disease diagnosis model.
modelforTreatment.py: Handles the treatment recommendation model.
verbsNouns.py: (Presumably) Extracts relevant verbs and nouns from text input.
Other files: Contain UI components, audio handling logic, etc
