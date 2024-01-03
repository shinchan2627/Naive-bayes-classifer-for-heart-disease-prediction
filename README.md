# Naive-bayes-classifer-for-heart-disease-prediction
Overview:

This repository contains a simple implementation of a Naive Bayes classifier for predicting heart disease based on a dataset. The classifier is trained using the scikit-learn library in Python.

Requirements:
pandas,
numpy,
scikit-learn.

Install the required packages using the following command:
pip install pandas numpy scikit-learn

Usage
1.Clone the repository:
git clone https://github.com/shinchan2627/heart-disease-prediction.git
cd heart-disease-prediction
2.Run the code:
python heart_disease_prediction.py

This will load the dataset, split it into training and testing sets, train the Naive Bayes classifier, make predictions on the test set, and provide an example of predicting heart disease for a given input.

Dataset:

The dataset used for this project is the Heart Disease UCI dataset from the UCI Machine Learning Repository. The dataset file (heart.csv) should be placed in the specified location ('your file location').

Code Explanation:

The dataset is loaded using pandas, and features (x) and target (y) are separated.
Data is split into training and testing sets using the train_test_split function from scikit-learn.
A Multinomial Naive Bayes classifier is instantiated and trained using the training data.
Predictions are made on the test set (x_test) to evaluate the model's performance.
An example prediction is demonstrated with a sample input ([45, 0, 1, 136, 315, 0, 1, 125, 1, 1.8, 1, 0, 1]).
Feel free to modify the code or integrate it into your own projects as needed. For any questions or issues, please open an issue.

License:

This project is licensed under the MIT License - see the LICENSE file for details.
