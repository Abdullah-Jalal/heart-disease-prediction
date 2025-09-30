# Heart Disease Prediction

[![Python Version](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project applies Machine Learning models to predict the presence of heart disease using patient data. The goal is to compare different algorithms, visualize results, and evaluate model performance with multiple metrics.

## Dataset

The dataset provides information on various medical parameters associated with heart disease risk factors. Key features include:

- **Age**: Patient's age (numeric)
- **Sex**: Gender of patient (Male/Female)
- **CP**: Type of chest pain (1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic)
- **Trestbps**: Resting blood pressure (numeric)
- **Chol**: Serum cholesterol in mg/dl (numeric)
- **Fbs**: Fasting blood sugar > 120 mg/dl (1: true, 0: false)
- **Restecg**: Resting electrocardiographic results (0: normal, 1: ST-T wave abnormality, 2: left ventricular hypertrophy)
- **Thalach**: Maximum heart rate achieved (numeric)
- **Exang**: Exercise induced angina (1: yes, 0: no)
- **Oldpeak**: ST depression induced by exercise relative to rest (numeric)
- **Slope**: Slope of the peak exercise ST segment (1: upsloping, 2: flat, 3: downsloping)
- **Ca**: Number of major vessels colored by fluoroscopy (0-3)
- **Thal**: Thalassemia (3: normal, 6: fixed defect, 7: reversible defect)

**Target Variable**: Presence (1) or Absence (0) of heart disease

## Models Implemented

### Logistic Regression
- Baseline model for binary classification
- Evaluated using Accuracy, Precision, Recall, F1-score, and ROC-AUC

### K-Nearest Neighbors (KNN)
- Tested multiple values of k
- Plotted Accuracy vs k and AUC vs k

### Random Forest Classifier
- Ensemble learning model
- Evaluated using Accuracy, Precision, Recall, F1-score, and ROC-AUC

### Decision Tree Classifier
- Single tree model
- Evaluated using Accuracy, Precision, Recall, F1-score, and ROC-AUC

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
Usage

1.Clone the repository:
git clone https://github.com/Abdullah-Jalal/heart-disease-prediction.git
cd heart-disease-prediction

2.Install dependencies:
pip install -r requirements.txt

3.jupyter notebook ML_Heart.ipynb:
jupyter notebook ML_Heart.ipynb

Follow the instructions in the notebook to load the dataset, train models, and evaluate performance.

Contributing

Feel free to fork this repository, submit issues, or create pull requests. Contributions are welcome!

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

Heart Disease dataset from UCI Machine Learning Repository
