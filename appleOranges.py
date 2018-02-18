from sklearn import tree
# features array - [weight, 0 = bumpy, 1 = smooth]
# labels [0 = apple, 1 = orange]
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print clf.predict([[150, 0]])