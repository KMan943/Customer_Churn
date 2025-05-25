# Customer Churn Predictor
## Overview

This project is a customer churn prediction system that uses a machine learning model (XGBoost classifier) to predict whether a customer is likely to churn based on their details. The web application is built with Flask and provides a simple, user-friendly interface for inputting customer data and receiving instant predictions. All code is written in Python and organized in a modular structure for maintainability and scalability.

---

## Project Motivation

Customer churn prediction is essential for businesses aiming to retain their customers and reduce revenue loss. By identifying customers at risk of leaving, companies can take targeted actions to improve satisfaction and loyalty. This project delivers a reliable and accessible tool for churn prediction, making advanced analytics available to non-technical users via a web interface.

---

## Key Features

- **XGBoost Classifier:** The model was selected after testing several common classifiers and was chosen for its superior accuracy and performance on the dataset.
- **Modular Codebase:** The Python code is organized into modules for data handling, prediction pipeline, and application logic, making it easy to extend or modify.
- **Flask Web Interface:** Users can enter customer details through a web form and receive real-time churn predictions.
- **Simple Deployment:** The application can be run locally with minimal setup.

---

## Workflow

1. **Model Selection:** Multiple classification algorithms were evaluated, with XGBoost chosen for deployment based on its results.
2. **Model Training:** The model was trained offline using preprocessed data and saved for inference.
3. **Web Application:** The Flask app loads the trained model and exposes a web form for user input.
4. **Prediction:** When a user submits the form, the app processes the input and displays the churn prediction.

---

## Technology Stack

- **Programming Language:** Python 3
- **Machine Learning:** XGBoost, scikit-learn
- **Web Framework:** Flask
- **Data Handling:** pandas, numpy
- **Frontend:** HTML, CSS

---

## Usage

1. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask app:**  
   ```bash
   python app.py
   ```

3. **Access the app:**  
   Open your browser and go to `http://localhost:5000/`.

4. **Input Data:**  
   Enter customer details via the web form and submit to receive a churn prediction.

---

## Project Structure

```
├── app.py
├── src/
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   ├── train_pipeline.py
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── exception.py
│   ├── utils.py
│   └── logger.py
├── templates/
│   ├── index.html
│   └── home.html
├── requirements.txt
├── setup.py
└── README.md
```

---

## Why XGBoost?

- **Performance:** Outperformed other tested classifiers on this dataset.
- **Interpretability:** Provides feature importance metrics.
- **Efficiency:** Fast training and inference.

---


