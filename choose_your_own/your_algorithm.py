#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from matplotlib.pyplot import clf

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
#################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn import neighbors
from sklearn.metrics import accuracy_score
 
best_score = 0
best_clf = None
best_weights = None
best_n_neighbors = None
 
scores = []
for weights in ['uniform', 'distance']:
    for n_neighbors in [2,5,10,20,50,100]:
        clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, weights=weights)
        clf.fit(features_train, labels_train)
         
        pred = clf.predict(features_test)
 
        score = accuracy_score(labels_test, pred)
         
        scores.append(score)
 
        if(score>best_score):
            best_score = score
            best_clf = clf
            best_weights = weights
            best_n_neighbors = n_neighbors
 
print "Scores: %s"%(str(scores))
print "The best NearestNeighbors[weights=%s, n_neighbors=%d]: %f"%(best_weights, best_n_neighbors, best_score)


# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
#  
# best_score = 0
# best_clf = None
# best_n_estimators = None
#  
# scores = []
#  
# for n_estimators in [2,5,10,20,50,100]:
#     clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=None, min_samples_split=1, random_state=0)
#     clf.fit(features_train, labels_train)
#      
#     pred = clf.predict(features_test)
#  
#     score = accuracy_score(labels_test, pred)
#      
#     scores.append(score)
#  
#     if(score>best_score):
#         best_score = score
#         best_clf = clf
#         best_n_estimators = n_estimators
#  
# print "Scores: %s"%(str(scores))
# print "The best RandomForestClassifier[n_estimators=%d]: %f"%(best_n_estimators, best_score)


# from sklearn.ensemble import AdaBoostClassifier
# from sklearn.metrics import accuracy_score
# 
# best_score = 0
# best_clf = None
# best_n_estimators = None
# 
# scores = []
# 
# for n_estimators in [10,25,50,100,150,250]:
#     clf = AdaBoostClassifier(n_estimators=n_estimators)
#     clf.fit(features_train, labels_train)
#     
#     pred = clf.predict(features_test)
# 
#     score = accuracy_score(labels_test, pred)
#     
#     scores.append(score)
# 
#     if(score>best_score):
#         best_score = score
#         best_clf = clf
#         best_n_estimators = n_estimators
# 
# print "Scores: %s"%(str(scores))
# print "The best AdaBoostClassifier[n_estimators=%d]: %f"%(best_n_estimators, best_score)


clf = best_clf

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
