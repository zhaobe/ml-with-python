import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

# load iris data
iris = load_iris()
test_idx = [0, 50, 100]

# training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

# these two outputs should match
print test_target
print clf.predict(test_data)

# viz code to generate graphviz
from sklearn.externals.six import StringIO
import pydotplus
dot_data = StringIO()
tree.export_graphviz(clf, 
						out_file=dot_data,
						feature_names=iris.feature_names,
						class_names=iris.target_names,
						filled=True, rounded=True,
						impurity=False)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("2_iris.pdf")

# 1 - the second testing example,
# 2 - reference of features, names
print "test:\t", test_data[1], test_target[1]
print "feat:\t", iris.feature_names
print "names:\t", iris.target_names