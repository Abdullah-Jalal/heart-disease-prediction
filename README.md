🫀 Heart Disease Prediction

This project applies Machine Learning models to predict the presence of heart disease using patient data. The goal is to compare different algorithms, visualize results, and evaluate model performance with multiple metrics.

📊 Dataset

Heart disease dataset (features: age, sex, chest pain type, blood pressure, cholesterol, etc.)

Target: Presence (1) or Absence (0) of heart disease

⚙️ Models Implemented
🔹 Logistic Regression

First baseline model

Evaluated with Accuracy, Precision, Recall, F1-score, and ROC-AUC

🔹 K-Nearest Neighbors (KNN)

Tested multiple values of k

Plotted Accuracy vs k

Plotted AUC vs k

Compared best k=7 against Logistic Regression

🔹 Decision Tree Classifier

Trained and visualized decision tree splits using sklearn.tree.plot_tree

Evaluated with confusion matrix and classification report

📈 Model Comparison
Model	Accuracy	Precision	Recall	F1	ROC-AUC
Logistic Regression	✅	✅	✅	✅	✅
KNN (k=7)	✅	✅	✅	✅	✅
Decision Tree	✅	✅	✅	✅	✅

📊 Visualizations

Confusion Matrix heatmaps

Accuracy vs k (KNN)

ROC-AUC vs k (KNN)

Decision Tree visualization

🚀 How to Run
