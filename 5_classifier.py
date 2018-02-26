import random

class newKNN():
	# fit method - takes in features and labels for training set
	def fit(self, X_train, y_train):
		# memorize train data
		self.X_train = X_train
		self.y_train = y_train

	# predict method - takes in features for our testing data, returns predictions for the labels
	def predict(self, X_test):
		# X_test is a 2D array, each row contains features of one testing example
		predictions = []
		# randomly pick a label from the training data and append to predictions
		for row in X_test:
			label = random.choice(self.y_train)
			predictions.append(label)
		return predictions

from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

# sklearn.cross_validation will be deprecated so replaced with sklearn.model_selection
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

# TODO: new classifier here
my_classifier = newKNN()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)

from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)
