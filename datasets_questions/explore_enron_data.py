#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
print len(enron_data["SKILLING JEFFREY K"])
print len(filter(lambda (k,v): v["poi"], enron_data.items()))

print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]['from_this_person_to_poi']
print enron_data["SKILLING JEFFREY K"]['exercised_stock_options']

total_payments = []
for k in enron_data.keys():
    if 'total_payments' in enron_data[k] and enron_data[k]['total_payments']!='NaN' and k!= 'TOTAL':
        total_payments.append((enron_data[k]['total_payments'], k))
        
total_payments = sorted(total_payments)    

print "%s: %s" %(total_payments[len(total_payments)-1][1], total_payments[len(total_payments)-1][0])

print "salary: %d" %(len(filter(lambda x: 'salary' in x[1] and x[1]['salary']!='NaN', enron_data.items())))
print "email_address: %d" %(len(filter(lambda x: 'email_address' in x[1] and x[1]['email_address']!='NaN', enron_data.items())))
print "%%total_payments: %f" %(len(filter(lambda x: 'total_payments' in x[1] and x[1]['total_payments']=='NaN', enron_data.items()))/float(len(enron_data)))
print "%%poi total_payments: %f" %(len(filter(lambda x: 'total_payments' in x[1] and x[1]['total_payments']=='NaN' and x[1]['poi'], enron_data.items()))/float(len(filter(lambda (k,v): v["poi"], enron_data.items()))))
print "#number + 10: %d" %(10+len(enron_data))
print "#number NaN +10: %d" %(10+len(filter(lambda x: 'total_payments' in x[1] and x[1]['total_payments']=='NaN', enron_data.items())))
print "#number POIs +10: %d" %(10+ len(filter(lambda (k,v): v["poi"], enron_data.items())))

print "%%!poi stock_value: %f" %(len(filter(lambda x: 'stock_value' in x[1] and x[1]['stock_value']=='NaN' and not x[1]['poi'], enron_data.items()))/float(len(filter(lambda (k,v): not v["poi"], enron_data.items()))))
print "%%poi stock_value: %f" %(len(filter(lambda x: 'stock_value' in x[1] and x[1]['stock_value']=='NaN' and x[1]['poi'], enron_data.items()))/float(len(filter(lambda (k,v): v["poi"], enron_data.items()))))