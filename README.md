# Crop Recommendation System

This repository contains a machine learning-powered web application for recommending the best crop to plant based on environmental and soil features. The application uses Flask for deployment and a Random Forest model for predictions.

---

## Features
- **Input Parameters**: Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall.
- **Prediction**: Recommends the most suitable crop based on input features.
- **Responsive Web Interface**: User-friendly front end for seamless interaction.

---

## Getting Started

Follow the steps below to set up and run the application locally.

### Prerequisites
- Python (Recommended: Installed via [Anaconda](https://www.anaconda.com/products/distribution))
- Git

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/fatsasabila/crop-recommendation-ksd.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd crop-recommendation-ksd
   ```

3. **Install Dependencies**:
   ```bash
   pip install Flask scikit-learn
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Application**:
   - Open a web browser and navigate to:
     ```
     http://127.0.0.1:5000/
     ```

---

## File Structure

- `app.py`: The Flask application script.
- `model/random_forest_model.pkl`: Pre-trained Random Forest model used for crop prediction.
- `templates/index2.html`: HTML template for the web interface.
- `static/`: Directory for static files such as CSS and JavaScript.

---

## Usage
1. Enter the required environmental and soil parameters into the form on the web interface.
2. Submit the form to get a recommendation for the best crop to plant.

---

## Acknowledgments
- The machine learning model was trained using data from open-source datasets.
- Thanks to Flask and Scikit-learn for providing robust libraries for development.

---

For any issues or questions, please open an issue in this repository.

---
Komputasi Sains Data Project

Fatsa Vidyaningtyas Sabila (2306319445)

Shafa Khadijah Rahmat (2306319496)

Arif Rezky Aprilianto (2406372584)

