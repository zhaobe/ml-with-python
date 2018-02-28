from scipy.spatial import distance

# a is a point from training data, b is a point from testing data
def euc(a, b):
	return distance.euclidean(a,b)

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
			label = self.closest(row) # method closest finds nearest training point to the test point
			predictions.append(label)
		return predictions

	# loop over all training points and keep track of closest one so far
	# calculate distance from test point to the first training point
	def closest(self, row):
		best_dist = euc(row, self.X_train[0]) # keep track of the shortest distance we found so far
		best_index = 0 # keep track of the index of the training point that is closest

		# iterate over all other training points
		for i in range(1, len(self.X_train)):
			dist = euc(row, self.X_train[i])
			# everytime we find a closer one, we update our variables
			if dist < best_dist:
				best_dist = dist
				best_index = i
		return self.y_train[best_index] # use index to return the label for the closest training example


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
