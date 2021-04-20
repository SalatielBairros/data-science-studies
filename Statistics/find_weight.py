import random
from math import sqrt

def mean(data):
    return sum(data)/len(data)

def variance(data):
    mu=mean(data)
    return sum([(x-mu)**2 for x in data])/len(data)

def stddev(data):
    return sqrt(variance(data))



weight=[80.,85,200,85,69,65,68,66,85,72,85,82,65,105,75,80,
    70,74,72,70,80,60,80,75,80,78,63,88.65,90,89,91,1.00E+22,
    75,75,90,80,75,-1.00E+22,-1.00E+22,-1.00E+22,86.54,67,70,92,70,76,81,93,
    70,85,75,76,79,89,80,73.6,80,80,120,80,70,110,65,80,
    250,80,85,81,80,85,80,90,85,85,82,83,80,160,75,75,
    80,85,90,80,89,70,90,100,70,80,77,95,120,250,60]

print (mean(weight))

def remove_obvious_outliers(data):
  return list(filter(lambda x: x > 0 and x < 250, data))
  
def calculate_quartiles(data):
  filtred_weight = remove_obvious_outliers(data)
  mean_weight = mean(filtred_weight);
  first_half = list(filter(lambda x: x < mean_weight, filtred_weight))
  last_half = list(filter(lambda x: x >= mean_weight, filtred_weight))
  mean_fh = mean(first_half)
  mean_lh = mean(last_half)
  Q2 = list(filter(lambda x: x >= mean_fh, first_half))
  Q3 = list(filter(lambda x: x < mean_lh, last_half))
  return Q2 + Q3

def calculate_weight(data, z):
    valid_weight = calculate_quartiles(data)
    mean_weight = mean(valid_weight)
    standard_deviation = stddev(valid_weight)
    standard_score = mean_weight + z * standard_deviation;
    return standard_score

print (calculate_weight(weight, -2.))