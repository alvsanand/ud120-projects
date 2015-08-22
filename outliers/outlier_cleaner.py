#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### your code goes here
    residualError = abs(predictions - net_worths)
    numToRemove = int(len(predictions) * 0.10)
    
    residualErrorSorted = sorted(residualError, reverse=True)[0:numToRemove]
    
    i = 0
    for i in range(0,len(predictions)-1):
        if residualError[i] not in residualErrorSorted:
            cleaned_data.append((ages[i][0],net_worths[i], residualError[i]))
    
    return cleaned_data

