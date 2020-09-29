# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:21:39 2020

@author: HP
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Q7_data=pd.read_csv('C:/Users/HP/Desktop/assignments submission/basic stats level 1/Q7.csv')

#############Measures of central tendency################
#Mean
Q7_data.mean()
#Median
Q7_data.median()
#or
Q7_data['Points'].median()
Q7_data['Score'].median()
Q7_data['Weigh'].median()
#Mode
Q7_data['Points'].mode()
Q7_data['Score'].mode()
Q7_data['Weigh'].mode()

################Measures of Variance/Dispersion##################
#Variance of data
Q7_data.var()#sample variance
np.var(Q7_data)#population variance
#standard deviation
Q7_data.std()#sample std
np.std(Q7_data)#population std
#range
Range=max(Q7_data.Points)-min(Q7_data.Points)
Range

##################skewness#####################
Q9_data=pd.read_csv("C:/Users/HP/Desktop/assignments submission/basic stats level 1/Q9_a.csv")
#skewness
Q9_data.skew()
#kurtosis
Q9_data.kurt()

##############probability##############
cars_data=pd.read_csv('C:/Users/HP/Desktop/assignments submission/basic stats level 1/Cars.csv')
cars_data.MPG.mean()
cars_data.MPG.std()
import scipy.stats as stats
#	P(MPG>38)
1-stats.norm.cdf(38,34.42208,9.131445)
# P(MPG<40)
stats.norm.cdf(40,34.42208,9.131445)
#	P (20<MPG<50)
stats.norm.cdf(50,34.42208,9.131445)-stats.norm.cdf(20,34.42208,9.131445)


####################To check Normal Distribution###################
plt.hist(cars_data.MPG)
plt.boxplot(cars_data.MPG)
import pylab
stats.probplot(cars_data.MPG,dist='norm',plot=pylab)

#Z scores of  90% confidence interval,94% confidence interval, 60% confidence interval 
stats.norm.ppf(0.95)
stats.norm.ppf(0.97)
stats.norm.ppf(0.8)

#t scores of 95% confidence interval, 96% confidence interval, 99% confidence interval for sample size of 25
stats.t.ppf(0.975,24)
stats.t.ppf(0.98,24)
stats.t.ppf(0.995,24)

################Confidence Interval#####################
confidence_level=0.95
degrees_freedom=cars_data['MPG'].size-1
sample_mean=cars_data.MPG.mean()
sample_standard_error=stats.sem(cars_data['MPG'])
confidence_interval = stats.t.interval(confidence_level, degrees_freedom, sample_mean, sample_standard_error)
confidence_interval
