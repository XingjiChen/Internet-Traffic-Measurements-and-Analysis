import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
from sklearn import svm
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report


def main():
    # Step 1. Load CSV file as test set
    test = pd.read_csv("datasets/test_dataset.csv")

    # Step 2. Load ML models
    with open('LinearSVC_model_for_ml_2.pkl', 'rb') as f:
        model_loaded_1 = pickle.load(f)
    with open('GaussianNB_model_for_ml_2.pkl', 'rb') as f:
        model_loaded_2 = pickle.load(f)
    with open('KNeighborsClassifier_model_for_ml_2.pkl', 'rb') as f:
        model_loaded_3 = pickle.load(f)
    with open('DecisionTreeClassifier_for_ml_2.pkl', 'rb') as f:
        model_loaded_4 = pickle.load(f)

    # Step 3 Define the features and targets using whole set
    X_test = test.iloc[:, :-1]  # features (all except last column)
    Y_test = test.iloc[:, -1]  # targets (the last column)

    # Step 4. Perform classification (prediction) of the whole set
    Y_predicted_model1 = model_loaded_1.predict(X_test)
    Y_predicted_model2 = model_loaded_2.predict(X_test)
    Y_predicted_model3 = model_loaded_3.predict(X_test)
    Y_predicted_model4 = model_loaded_4.predict(X_test)

    # Step 5. Evaluate the models with confusion matrix
    print("-- Confusion matrix: --")
    print("   1. LinearSVC model:                  \n", confusion_matrix(Y_test, Y_predicted_model1))
    print("\n   2. Naive Bayes model:              \n", confusion_matrix(Y_test, Y_predicted_model2))
    print("\n   3. KNN model:                      \n", confusion_matrix(Y_test, Y_predicted_model3))
    print("\n   4. Decision Tree Classifier model: \n", confusion_matrix(Y_test, Y_predicted_model4))

    # Step 6. Evaluate the models with accuracy score
    print("\n-- Accuracy score: --")
    print("   1. LinearSVC model:                ", accuracy_score(Y_test, Y_predicted_model1))
    print("   2. Naive Bayes model:              ", accuracy_score(Y_test, Y_predicted_model2))
    print("   3. KNN model:                      ", accuracy_score(Y_test, Y_predicted_model3))
    print("   4. Decision Tree Classifier model: ", accuracy_score(Y_test, Y_predicted_model4))

    # Step 7. Evaluate the models with precision and recall score
    # Note: If the target variable Y is multiclass, use `average='macro'` or another averaging method suitable for multiclass
    print("\n-- Precision score: --")
    print("   1. LinearSVC model:                ", precision_score(Y_test, Y_predicted_model1, average='macro'))
    print("   2. Naive Bayes model:              ", precision_score(Y_test, Y_predicted_model2, average='macro'))
    print("   3. KNN model:                      ", precision_score(Y_test, Y_predicted_model3, average='macro'))
    print("   4. Decision Tree Classifier model: ", precision_score(Y_test, Y_predicted_model4, average='macro'))

    print("\n-- Recall score: --")
    print("   1. LinearSVC model:                ", recall_score(Y_test, Y_predicted_model1, average='macro'))
    print("   2. Naive Bayes model:              ", recall_score(Y_test, Y_predicted_model2, average='macro'))
    print("   3. KNN model:                      ", recall_score(Y_test, Y_predicted_model3, average='macro'))
    print("   4. Decision Tree Classifier model: ", recall_score(Y_test, Y_predicted_model4, average='macro'))

    # Step 8. Evaluate the models with F1 score
    print("\n-- F1 score: --")
    print("   1. LinearSVC model:                ", f1_score(Y_test, Y_predicted_model1, average='macro'))
    print("   2. Naive Bayes model:              ", f1_score(Y_test, Y_predicted_model2, average='macro'))
    print("   3. KNN model:                      ", f1_score(Y_test, Y_predicted_model3, average='macro'))
    print("   4. Decision Tree Classifier model: ", f1_score(Y_test, Y_predicted_model4, average='macro'))

    # Step 9. Plot the distribution of the targets comparing between the test set (real data) and prediction set (each model)
    plt.figure(figsize=(12, 8))
    sns.histplot(Y_test, color='blue', label='Actual', kde=True)
    sns.histplot(Y_predicted_model1, color='red', label='Predicted - LinearSVC', kde=True, alpha=0.6)
    sns.histplot(Y_predicted_model2, color='green', label='Predicted - GaussianNB', kde=True, alpha=0.6)
    sns.histplot(Y_predicted_model3, color='purple', label='Predicted - KNN', kde=True, alpha=0.6)
    sns.histplot(Y_predicted_model4, color='orange', label='Predicted - Decision Tree', kde=True, alpha=0.6)
    plt.legend()
    plt.title('Distribution of Actual vs Predicted Targets')
    plt.show()


if __name__ == "__main__":
    main()
