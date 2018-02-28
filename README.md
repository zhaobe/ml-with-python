# ml-with-python

This project requires pip to be installed.

# Setup
- if you don't have the most recent pip, run `pip install --upgrade pip`
- run `pip install --user numpy scipy` to install numpy and scipy
- run `pip install -U scikit-learn` to install the scikit
- run `pip install pydotplus graphviz` to install pydot and graphviz library 
	- note: had to `brew install graphviz` due to error with graphviz
- run `python -mpip install -U matplotlib` to install matplotlib

# Reference
- a visual way to test around data: http://playground.tensorflow.org/

# File notes
- 5_classifier.py
	- pros: 
		- relatively simple using kNN algorithm
	- cons: 
		- computationally expensive 
		- hard to represent relationships between features compared to 3_dog_id, which has more informative features
