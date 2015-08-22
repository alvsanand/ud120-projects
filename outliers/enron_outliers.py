#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
import numpy

meanPoint = numpy.array([0,0])
for i in range(0,len(data)-1):
     meanPoint +=  data[i]

meanPoint = meanPoint / len(data)


maxDistance = 0
maxI = 0
outlier = None
for i in range(0,len(data)-1):
    dist = numpy.linalg.norm(data[i]-meanPoint)
    
    if dist>maxDistance:
         maxDistance = dist
         maxI = i
         outlier = data[i]



name = None
for key in data_dict.keys():
    if outlier[0] == data_dict[key]["salary"] and outlier[1] == data_dict[key]["bonus"]:
        name = key

print "The max distance is %d" % maxDistance
print "The outlier is %s" %str(name)

for point in data:
    if outlier[0] == point[0] and outlier[1] == point[1]:
        continue
    
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

outliers = []
for point in data:
    if point[0] > 800000 or point[1] > 6000000:
        outliers.append(point)

names = []  
for key in data_dict.keys():
    if outlier[0] == point[0] and outlier[1] == point[1]:
        continue
    
    for point in outliers:
        if point[0] == data_dict[key]["salary"] and point[1] == data_dict[key]["bonus"]:
            names.append("%s -> %s"%(key, data_dict[key]))
        
print "The outliers are %s" %str(names)
