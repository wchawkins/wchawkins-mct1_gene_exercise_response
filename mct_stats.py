from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency
import pandas as pd
import numpy as np
import csv
student_id = []
height = []
weight = []
age = []
peak_power = []
mean_power = []
min_power = []
fatigue_index = []
genotype = []
pre = []
post = []
ten = []
twenty = []
thirty = []
forty = []

with open ('mct1_data0.csv', 'r') as csv_file: # r = read
    csv_reader = csv.DictReader(csv_file) # DictReader includes key in output reader does not
    for column in csv_reader: #print(column['Subject ID'], column['Fatigue Index']) to print Fatigue Index Data
        student_id.append(float(column['subject_id']))
        height.append(float(column['height']))
        weight.append(float(column['weight']))
        age.append(float(column['age']))
        peak_power.append(float(column['peak_power']))
        mean_power.append(float(column['mean_power']))
        min_power.append(float(column['min_power']))
        fatigue_index.append(float(column['fatigue_index']))
        genotype.append(float(column['genotype']))
        pre.append(float(column['pre']))
        post.append(float(column['post']))
        ten.append(float(column['ten']))
        twenty.append(float(column['twenty']))
        thirty.append(float(column['thirty']))
        forty.append(float(column['forty']))

        #print(column)
#mean_height = np.mean(height)
#std_height = np.std(height)
#print(mean_height)
#print(std_height)

# 2 samples t test
#tstat, pval = ttest_ind(peak_power, min_power)
#print pval

# One Way ANOVA
fstat, lactate_anova = f_oneway(pre, post, ten, twenty, thirty, forty)
print format(lactate_anova, '0.10f') #format converts from scientific notation rounding at 10th decimal
if lactate_anova < 0.05:
    print "Lactic Acid is significantly different at one or more time points. You should perform follow up test(s)"
else:
    print "Results aren't statistically different"

#Tukey Test
values = np.concatenate([pre, post, ten, twenty, thirty, forty])
labels = ['pre'] * len(pre) + ['post'] * len(post) + ['ten'] * len(ten) + ['twenty'] * len(twenty) + ['thirty'] * len(thirty) + ['forty'] * len(forty)
tukey_results = pairwise_tukeyhsd(values, labels, 0.05)
print pairwise_tukeyhsd(values, labels, .05)
