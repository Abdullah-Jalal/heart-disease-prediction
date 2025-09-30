# Heart Disease Prediction

This project applies Machine Learning models to predict the presence of heart disease using patient data. The goal is to compare different algorithms, visualize results, and evaluate model performance with multiple metrics.

## Dataset

The dataset used provides information on various medical parameters associated with heart disease risk factors. Key features include:

- **Age**: Patient's age (numeric)
- **Sex**: Gender of patient (Male/Female)
- **CP**: Type of chest pain experienced by patient (1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic)
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
- First baseline model
- Evaluated with Accuracy, Precision, Recall, F1-score, and ROC-AUC

### K-Nearest Neighbors (KNN)
- Tested multiple values of k
- Plotted Accuracy vs k
- Plotted AUC vs k

### Random Forest Classifier
- Evaluated with Accuracy, Precision, Recall, F1-score, and ROC-AUC

### Decision Tree Classifier
- Evaluated with Accuracy, Precision, Recall, F1-score, and ROC-AUC

## Requirements

To run this project, you'll need to install the following Python packages:

```bash
pip install -r requirements.txt

1.Usage

Clone the repository
git clone https://github.com/Abdullah-Jalal/heart-disease-prediction.git
cd heart-disease-prediction

2.Install dependencies:
pip install -r requirements.txt

3.Run the Jupyter notebook:
jupyter notebook ML_Heart.ipynb

llow the instructions within the notebook to load the dataset, train models, and evaluate performance.

Contributing

Feel free to fork this repository, submit issues, or create pull requests. Contributions are welcome!

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

Heart Disease dataset from UCI Machine Learning Repository


---

### 🔧 How to Update Your GitHub README

1. **Edit the README**: Navigate to your repository on GitHub and click on the `README.md` file.
2. **Update Content**: Click the pencil icon to edit the file.
3. **Paste the New README**: Replace the existing content with the updated README provided above.
4. **Commit Changes**: Scroll down to the commit section, add a commit message (e.g., "Update README with project details"), and click "Commit changes".

This will update your GitHub repository's README, providing visitors with a clear overview of your project, its dataset, models implemented, and how to use it.

Let me know if you'd like any further modifications or additions!
::contentReference[oaicite:16]{index=16}
 
