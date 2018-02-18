from sklearn.datasets import load_iris

#load iris data
iris = load_iris()

# column headers
print iris.feature_names
print iris.target_names

# first row of data
print iris.data[0]
print iris.target[0]

# load dataset in nice fashion
for i in range(len(iris.target)):
	print "Example %d: \tlabel %s, \tfeatures %s" % (i , iris.target[i], iris.data[i])
