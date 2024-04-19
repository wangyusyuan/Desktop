from sklearn import datasets # type: ignore
from sklearn import svm # type: ignore

iris=datasets.load_iris()
print(iris.data.shape)
