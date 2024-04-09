# IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold


def main():
    # Step 1. Load CSV file
    df = pd.read_csv("datasets/combined_mix.csv")

    # Step 2. Split the data set into training set (80%) and test set (20%)
    split_ratio = 0.8  # The split ratio should be a float
    split_index = int(split_ratio * len(df))
    train = df.iloc[:split_index]  # Training set
    test = df.iloc[split_index:]  # Test set

    # Step 3. Define the features and targets for both sets (training and test)
    X_train = train.iloc[:, :-1]  # features (all except last column)
    Y_train = train.iloc[:, -1]  # targets (the last column)
    X_test = test.iloc[:, :-1]  # features (all except last column)
    Y_test = test.iloc[:, -1]  # targets (the last column)

    # Step 4. Train some ML models through different algorithms
    model1 = svm.LinearSVC(max_iter=100000, dual=False)  # 1. LinearSVC model
    model1.fit(X_train, Y_train)

    model2 = GaussianNB()  # 2. Naive Bayes model
    model2.fit(X_train, Y_train)

    model3 = KNeighborsClassifier(n_neighbors=5)  # 3. KNN model
    model3.fit(X_train, Y_train)

    model4 = DecisionTreeClassifier()  # 4. Decision Tree Classifier model
    model4.fit(X_train, Y_train)

    # Step 5. Perform classification (prediction) on an array of test vectors X (features) for each model
    Y_predicted_model1 = model1.predict(X_test)
    Y_predicted_model2 = model2.predict(X_test)
    Y_predicted_model3 = model3.predict(X_test)
    Y_predicted_model4 = model4.predict(X_test)

    # Step 6. Plot the distribution of the targets between the prediction set and test set (real data).
    plt.figure(figsize=(12, 8))
    sns.countplot(x=Y_test, color='blue', label='Actual')
    sns.countplot(x=Y_predicted_model1, color='red', label='Predicted - LinearSVC')
    sns.countplot(x=Y_predicted_model2, color='green', label='Predicted - GaussianNB')
    sns.countplot(x=Y_predicted_model3, color='purple', label='Predicted - KNN')
    sns.countplot(x=Y_predicted_model4, color='orange', label='Predicted - Decision Tree')
    plt.legend()
    plt.title('Distribution of the targets between the prediction set and test set')
    plt.show()

    # Step 5. Evaluate the performance of each by calculating their accuracy score
    print("-- Accuracy score: --")
    print("   1. LinearSVC model:                ", accuracy_score(Y_test, Y_predicted_model1))
    print("   2. Naive Bayes model:              ", accuracy_score(Y_test, Y_predicted_model2))
    print("   3. KNN model:                      ", accuracy_score(Y_test, Y_predicted_model3))
    print("   4. Decision Tree Classifier model: ", accuracy_score(Y_test, Y_predicted_model4))

    # Step 6. Setup K-fold CV and reset models. Using whole dataset for K-fold CV.
    kf = KFold(n_splits=10)

    # Re-instantiate the models with the updated LinearSVC
    model1 = svm.LinearSVC(max_iter=100000, dual=False)
    model2 = GaussianNB()
    model3 = KNeighborsClassifier(n_neighbors=5)
    model4 = DecisionTreeClassifier()

    X = df.iloc[:, :-1]  # features (all except last column)
    Y = df.iloc[:, -1]  # targets (the last column)

    # Calculate the CV scores
    cv_scores_model1 = np.mean(cross_val_score(model1, X, Y, cv=kf))
    cv_scores_model2 = np.mean(cross_val_score(model2, X, Y, cv=kf))
    cv_scores_model3 = np.mean(cross_val_score(model3, X, Y, cv=kf))
    cv_scores_model4 = np.mean(cross_val_score(model4, X, Y, cv=kf))

    # Print the CV scores
    print("\n-- K-fold CV score: --")
    print("   1. LinearSVC model:                ", cv_scores_model1)
    print("   2. Naive Bayes model:              ", cv_scores_model2)
    print("   3. KNN model:                      ", cv_scores_model3)
    print("   4. Decision Tree Classifier model: ", cv_scores_model4)

    # Step 7. Save the most suitable model
    # Assuming the model with the highest cross-validation score as the most suitable
    best_model = max([(model1, cv_scores_model1), (model2, cv_scores_model2),
                      (model3, cv_scores_model3), (model4, cv_scores_model4)],
                     key=lambda item: item[1])[0]

    with open('model_saved_ml_1.pkl', 'wb') as f:
        pickle.dump(best_model, f)


if __name__ == "__main__":
    main()
