#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score

# clf = svm.SVC(kernel="linear")
# 
# t0 = time()
# clf.fit(features_train, labels_train)
# print "full dataset Linear SVM training time:", round(time()-t0, 3), "s"
# 
# t0 = time()
# pred = clf.predict(features_test)
# print "full dataset Linear SVM predicting time:", round(time()-t0, 3), "s"
# 
# print "full dataset Linear SVM accuracy score: %f" % accuracy_score(labels_test, pred)
# 
clf = svm.SVC(C=10000, kernel="rbf")
 
t0 = time()
clf.fit(features_train, labels_train)
print "full dataset RBF[C=10000] SVM training time:", round(time()-t0, 3), "s"
 
t0 = time()
pred = clf.predict(features_test)
print "full dataset RBF[C=10000] SVM predicting time:", round(time()-t0, 3), "s"
 
print "full dataset RBF[C=10000] SVM accuracy score: %f" % accuracy_score(labels_test, pred)

print "full dataset RBF[C=10000] SVM predict of class 1: %f" % sum(pred)
#
#  
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 
#  
# t0 = time()
# clf.fit(features_train, labels_train)
# print "partial dataset Linear SVM training time:", round(time()-t0, 3), "s"
# 
# t0 = time()
# pred = clf.predict(features_test)
# print "partial dataset Linear SVM predicting time:", round(time()-t0, 3), "s"
# 
# print "partial dataset Linear SVM accuracy score: %f" % accuracy_score(labels_test, pred)
# 
# clf = svm.SVC(kernel="rbf")
# 
# t0 = time()
# clf.fit(features_train, labels_train)
# print "partial dataset RBF SVM training time:", round(time()-t0, 3), "s"
# 
# t0 = time()
# pred = clf.predict(features_test)
# print "partial dataset RBF SVM predicting time:", round(time()-t0, 3), "s"
# 
# print "partial dataset RBF SVM accuracy score: %f" % accuracy_score(labels_test, pred)
# 
# for c in [10,100,1000,10000]:
#     clf = svm.SVC(C=c, kernel="rbf")
#     
#     t0 = time()
#     clf.fit(features_train, labels_train)
#     print "partial dataset RBF[C=%d] SVM training time: %fs" % (c, round(time()-t0, 3))
#     
#     t0 = time()
#     pred = clf.predict(features_test)
#     print "partial dataset RBF[C=%d] SVM predicting time: %fs" % (c, round(time()-t0, 3))
#     
#     print "partial dataset RBF[C=%d] SVM accuracy score: %f" % (c, accuracy_score(labels_test, pred))
# 
# c=10000
# 
# clf = svm.SVC(C=c, kernel="rbf")
#  
# t0 = time()
# clf.fit(features_train, labels_train)
# print "partial dataset RBF[C=%d] SVM training time: %fs" % (c, round(time()-t0, 3))
#  
# t0 = time()
# pred = clf.predict(features_test)
# print "partial dataset RBF[C=%d] SVM predicting time: %fs" % (c, round(time()-t0, 3))
#  
# print "partial dataset RBF[C=%d] SVM accuracy score: %f" % (c, accuracy_score(labels_test, pred))
# 
# labels = [features_test[10],features_test[26],features_test[50]]
# 
# print "Prediction for %s with full dataset RBF[C=10000] SVM: %s" % (str([10, 26, 50]), str(clf.predict(labels)))
#########################################################


