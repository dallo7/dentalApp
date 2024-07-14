# This is a Plotly Dash Demo for an AI powered Dental Diagnosis and Treatment Tool
#  For Dash.Plotly Community!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-v2-orange)](https://dash.plotly.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24-orange.svg)](https://scikit-learn.org/stable/)
[![Made with ML](https://img.shields.io/badge/Made%20with-ML-red)](https://github.com/madewithml)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

This application leverages the Dash framework and AI models to provide dental diagnosis and treatment recommendations. It offers multiple input methods (audio recording, chat, questionnaire) to gather patient information and utilizes machine learning models to process the input and generate actionable insights.
                    
[![Video Thumbnail Image](https://github.com/dallo7/dentalApp/blob/16629fccf0c875b1ba9a9402b1cd3909ed0bbb97/dental.png)](https://github.com/dallo7/dentalApp/blob/caa55f60d2b74f2f6eba08006112584ec7bba8e8/dentalDecay.mp4)                      
  

FYI, the tool, is not accurate especially the text generation. I am using Large NN models and classic ML algorithms for classification(
* DT
* SVM
* RF
* whisper-large-v2
* Mixtral-8x7B-Instruct-v0.1
)

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Models & Data](#models--data)
- [Contributing](#contributing)

## Project Overview

**Purpose:** The Dash Community Dentals tool aims to streamline and enhance the initial stages of dental consultations by using AI to analyze patient symptoms and provide preliminary diagnoses and treatment plans.

**Target Users:**

- **Patients:** Can self-assess their dental concerns and gain insights before a formal appointment.
- **Dental Professionals:** Can utilize the tool as a supplemental resource to gather patient information and expedite diagnosis.

## Features

- **Multiple Input Methods:**
  - **Audio Recording:** Patients can describe their symptoms verbally.
  - **Chat:** Interact with a basic chatbot to convey concerns.
  - **Questionnaire:** Answer a series of multiple-choice questions.
- **AI-Powered Diagnosis:**  Machine learning models process patient input and generate a likely diagnosis.
- **Treatment Recommendations:** Provides initial treatment plans based on the predicted diagnosis.
- **Inference Monitoring:**  Tracks and displays the history of user inputs, diagnoses, and treatment suggestions.
- **Word Cloud Analysis:**  Visually summarizes common symptoms and diagnoses from user interactions.

## Technologies

- **Dash:** A Python framework for building web applications.
- **Dash Bootstrap Components (dbc):** Provides styling and layout elements for the UI.
- **Hugging Face Transformers:**  (Assuming this is how your models are integrated) Library for using pre-trained NLP models like "whisper-large-v2".
- **scikit-learn (sklearn):** Machine learning library for tasks like text vectorization.
- **Pandas:** Data manipulation library for handling dataframes and CSV files.
- **Other:** NumPy, SoundFile, matplotlib, etc.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>

  ```bash
  pip install -r requirements.txt                    
  
  *run app.py*
  python app.py
  ```                    
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
  

Usage
1. Access the App: Open your web browser and navigate to the app's URL.
2. Choose Input Method: Select how you'd like to provide your information (audio, chat, or questionnaire).
3. Provide Symptoms:
* Audio: Record your voice describing your symptoms.
* Chat: Type your concerns in the chatbox.
* Questionnaire: Answer the provided questions.
4. View Results: The app will display the predicted diagnosis, treatment suggestions, and relevant analysis.

File Structure
* app.py: Main application file, contains the Dash layout and callbacks.
* chatInput.py: Contains logic for the chatbot interaction.
* landingPage.py: Defines the initial landing page layout.
* modelsDisease.py: Handles the disease diagnosis model.
* modelforTreatment.py: Handles the treatment recommendation model.
* verbsNouns.py: (Presumably) Extracts relevant verbs and nouns from text input.
* Other files: Contain UI components, audio handling logic, etc.

Models & Data
1. Disease Diagnosis Model: (Specify the model name/type used)
2. Treatment Recommendation Model: (Specify the model name/type used)

Contributing
Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Make your changes and commit them with clear messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

**Key improvements:**

*   **Markdown Formatting:** Used headings (`#`, `##`, etc.), lists, and links to create a well-structured document.
*   **License Badge:** Added a badge indicating the project's license (replace with the actual license).
*   **Clear Sections:** Organized content into logical sections for easy navigation.

