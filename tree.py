from sklearn import tree
from sklearn.linear_model import SGDClassifier

x = [[1,2],[2,4],[6,8],[5,10]]
y = ["a","b","b","a"]

model = tree.DecisionTreeClassifier()
model = model.fit(x,y)
predict = model.predict([[2,3]])
print(predict)
clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
clf =  clf.fit(x, y)
print(clf.predict([[2,3]]))