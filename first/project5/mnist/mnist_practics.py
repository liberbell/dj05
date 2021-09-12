from inspect import classify_class_attrs
import pickle
import numpy as np
from PIL import Image
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

def read():
    with open("mnist.pickle", "rb") as file:
        clf = pickle.load(file)
    return clf

def create_and_save():
    mnist = datasets.fetch_mldata("MNIST original", data_home="image/")
    X = mnist.data / 255
    y = mnist.target

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=50000, test_size=300
    )

    clf = svm.SVC()
    clf.fit(X_train, y_train)

    with("mnist", "wb") as file:
        pickle.dump(clf, file)
    return clf

try:
    clf = read()
except FileNotFoundError:
    clf = create_and_save()

def predict(img_array):
    result = clf.predict(img_array)
    return str(int(result[0]))

# # サンプル画像データのロード
# mnist = datasets.fetch_openml('mnist_784', data_home='image/')
# X = mnist.data / 255
# y = mnist.target

# # 訓練用データとテスト用データに分ける
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, train_size=1000, test_size=300
# )

# # 訓練用データで学習
# clf = svm.SVC()
# clf.fit(X_train, y_train)

# # テスト用データで実際に試す
# score = clf.score(X_test, y_test)
# print(score)
