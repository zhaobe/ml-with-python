from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

# sklearn.cross_validation will be deprecated so replaced with sklearn.model_selection
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

# TODO: new classifier here

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)

from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)
