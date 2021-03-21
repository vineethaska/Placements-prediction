
import numpy.random as numrandom
from Graphs import view
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn import metrics

import warnings

def performancealg():

    datainput = pd.read_csv("trainingset.csv")
    # Set the outcome and dedlete it
    y = datainput['Placed']
    del datainput['Placed']
    # Split data into Test & Training set where test data is 30% & training data is 70%
    x_train, x_test, y_train, y_test = train_test_split(datainput, y, test_size=0.3)

    # MLPClassifier() Classifier
    classify3 = MLPClassifier()
    # Train the model
    classify3.fit(x_train, y_train)
    # Use the model on the test data
    predicted3 = classify3.predict(x_test)
    lr = metrics.accuracy_score(y_test, predicted3) * 100
    print("The accuracy score using the ANN Classifier is ->")
    print(metrics.accuracy_score(y_test, predicted3))
    print('---------------------------------------------- ')

    # DecisionTreeClassifier() Classifier
    classify4 = DecisionTreeClassifier()
    # Train the model
    classify4.fit(x_train, y_train)
    # Use the model on the test data
    predicted4 = classify4.predict(x_test)
    dt = metrics.accuracy_score(y_test, predicted4) * 100
    print("The accuracy score using DecisionTreeClassifier() is ->")
    print(metrics.accuracy_score(y_test, predicted4))
    print('---------------------------------------------- ')
    # SVM()
    classify5 =  SVC(gamma='auto')
    # Train the model
    classify5.fit(x_train, y_train)
    # Use the model on the test data
    predicted5 = classify5.predict(x_test)
    rf = metrics.accuracy_score(y_test, predicted5) * 100
    print("The accuracy score using the SVM() is ->")
    print(metrics.accuracy_score(y_test, predicted5))
    print('---------------------------------------------- ')
    list = []
    list.clear()
    list.append(lr)
    list.append(dt)
    list.append(rf)
    view(list)



