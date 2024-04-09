import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.simplefilter("ignore")

def evaluate_model(model, X_train, X_test, Y_train, Y_test):
    start = time.time()

    model.fit(X_train, Y_train)
    Y_predicted = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_predicted)

    end = time.time()
    running_time = end - start

    return accuracy, running_time

def main():
    np.random.seed(1)

    df = pd.read_csv("datasets/combined_mix_nofs.csv")
    X = df.iloc[:, :-1]  # features (all except last column)
    Y = df.iloc[:, -1]  # targets (the last column)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

    selector = SelectKBest(f_classif, k=5)
    X_train_selected = selector.fit_transform(X_train, Y_train)
    X_test_selected = selector.transform(X_test)

    knn = KNeighborsClassifier()
    accuracy, runtime = evaluate_model(knn, X_train_selected, X_test_selected, Y_train, Y_test)
    print("KNN with 5 features - Accuracy:", accuracy, "| Running time:", runtime)

    accuracy, runtime = evaluate_model(knn, X_train, X_test, Y_train, Y_test)
    print("KNN with all features - Accuracy:", accuracy, "| Running time:", runtime)

    decision_tree = DecisionTreeClassifier()
    accuracy, runtime = evaluate_model(decision_tree, X_train_selected, X_test_selected, Y_train, Y_test)
    print("Decision Tree with 5 features - Accuracy:", accuracy, "| Running time:", runtime)

    accuracy, runtime = evaluate_model(decision_tree, X_train, X_test, Y_train, Y_test)
    print("Decision Tree with all features - Accuracy:", accuracy, "| Running time:", runtime)

if __name__ == "__main__":
    main()