#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 12:51:10 2022

@author: nicolarossberg
"""
import pandas as pd
import statistics
from statistics import mean

dat = pd.read_csv('/Users/nicolarossberg/Desktop/hexaco_nonreinf_full_data_cleaned copy.csv')

#Reverse coding R-items
#List of items that need to be reverse coded
reverse_list = [30, 12, 60, 42, 24, 48, 53, 35, 41, 59, 28, 52, 10, 46, 9, 15, 57, 21,
                26, 32, 14, 20, 44, 56, 1, 31, 49, 19, 55]

new_list = []
for item in reverse_list:
    new_list.append('Q'+str(item))

reverse_dict = {}
for name, values in dat[['Q30','Q12','Q60', 'Q42','Q24','Q48',
 'Q53','Q35','Q41','Q59','Q28','Q52','Q10','Q46','Q9','Q15',
 'Q57', 'Q21', 'Q26', 'Q32', 'Q14', 'Q20', 'Q44', 'Q56','Q1',
 'Q31','Q49','Q19','Q55']].iteritems():
    l = values.tolist()
    reverse_dict['R'+name] = l

reversed_dict = {}
for key, value in reverse_dict.items():
    coded_list = []
    for number in value:
        if number == 1.0:
            coded_list.append(5.0)
        elif number == 2.0:
            coded_list.append(4.0)
        elif number == 2.0:
            coded_list.append(4.0)
        elif number == 5.0:
            coded_list.append(1.0)
        else:
            coded_list.append(number)
    reversed_dict[key] = coded_list

for key, value in reversed_dict.items():
    dat[key] = value
#Create list for each facet
sincerity = []
fairness = []
greed_avoidance = []
modesty = []
honesty_humility = []
fearfulness = []
anxiety = []
dependence = []
sentimentality = []
emotionality = []
social_self_esteem = []
social_boldness = []
sociability = []
liveliness = []
extraversion = []
forgiveness = []
gentleness = []
flexibility = []
patience = []
agreeableness = []
organization = []
diligence = []
perfectionism = []
prudence = []
conscientiousness = []
aesthetic_appreciation = []
inquisitiveness = []
creativity = []
unconventionality = []
openness_to_experience = []


for index, row in dat.iterrows():
    try:
        sincerity.append((row['Q6'] +row['RQ30'] + row['Q54']) / 3)
    except: 
        sincerity.append('nan')
    try:
        fairness.append((row['RQ12'] + row['Q36'] + row['RQ60']) / 3)
    except:
        fairness.append('nan')
    try:
        greed_avoidance.append((row['Q18'] + row['RQ42']) / 2)
    except:
        greed_avoidance.append('nan')
    try:
        modesty.append((row['RQ24'] + row['RQ48']) / 2)
    except:
        modesty.append('nan')
    try:
        honesty_humility.append((row['Q6'] + row['RQ30'] + row['Q54'] + row['RQ12']
                           + row['Q36'] + row['RQ60'] +row['Q18'] + row['RQ42']
                           + row['RQ24'] + row['RQ48']) / 10)
    except:
        honesty_humility.append('nan')
    try:
        fearfulness.append((row['Q5'] + row['RQ53'] + row['Q29']) / 3)
    except:
        fearfulness.append('nan')
    try:
        anxiety.append((row['Q11'] + row['RQ35']) / 2)
    except:
        anxiety.append('nan')
    try:
        dependence.append((row['Q17'] + row['RQ41']) / 2)
    except:
        dependence.append('nan')
    try:
        sentimentality.append((row['Q23'] + row['RQ59'] + row['Q47']) / 3)
    except:
        sentimentality.append('nan')
    try:
        emotionality.append((row['Q5'] + row['RQ53'] + row['Q29'] +
                       row['Q11'] + row['RQ35'] + 
                       row['Q17'] + row['RQ41'] +
                       row['Q23'] + row['RQ59'] + row['Q47']) / 10)
    except:
        emotionality.append('nan')
    try:
        social_self_esteem.append((row['Q4'] + row['RQ28'] + row['RQ52']) / 3)
    except:
        social_self_esteem.append('nan')
    try:
        social_boldness.append((row['Q58'] + row['RQ10'] + row['Q34']) / 3)
    except:
        social_boldness.append('nan')
    try:
        sociability.append((row['Q16'] + row['Q40']) / 2)
    except:
        sociability.append('nan')
    try:
        liveliness.append((row['Q22'] + row['RQ46']) / 2)
    except:
        liveliness.append('nan')
    try:
        extraversion.append((row['Q4'] + row['RQ28'] + row['RQ52']+
                       row['Q58'] + row['RQ10'] + row['Q34'] +
                           row['Q16'] + row['Q40'] + 
                           row['Q22'] + row['RQ46']) / 10)
    except:
        extraversion.append('nan')
    try:
        forgiveness.append((row['Q3'] + row['Q27']) / 2)
    except:
        forgiveness.append('nan')
    try:
        gentleness.append((row['RQ9'] + row['Q33'] + row['Q51']) / 3)
    except:
        gentleness.append('nan')
    try:
        flexibility.append((row['RQ15'] + row['Q39'] + row['RQ57']) / 3)
    except:
        flexibility.append('nan')
    try:
        patience.append((row['RQ21'] + row['Q45']) / 2)
    except:
        patience.append('nan')
    try:
        agreeableness.append((row['Q3'] + row['Q27']+
                        row['RQ9'] + row['Q33'] + row['Q51'] +
                        row['RQ15'] + row['Q39'] + row['RQ57'] +
                        row['RQ21'] + row['Q45']) / 10)
    except:
        agreeableness.append('nan')
    try:
        organization.append((row['Q2'] + row['RQ26']) / 2)
    except:
        organization.append('nan')
    try:
        diligence.append((row['Q8'] + row['RQ32']) / 2)
    except:
        diligence.append('nan')
    try:
        perfectionism.append((row['RQ14'] + row['Q38'] + row['Q50']) / 3)
    except:
        perfectionism.append('nan')
    try:
        prudence.append((row['RQ20'] + row['RQ44'] + row['RQ56']) / 3)
    except:
        prudence.append('nan')
    try:
        conscientiousness.append((row['Q2'] + row['RQ26'] +
                            row['Q8'] + row['RQ32'] +
                            row['RQ14'] + row['Q38'] + row['Q50'] +
                            row['RQ20'] + row['RQ44'] + row['RQ56']) / 10)
    except:
        conscientiousness.append('nan')
    try:
        aesthetic_appreciation.append((row['Q25'] + row['RQ1']) / 2)
    except:
        aesthetic_appreciation.append('nan')
    try:
        inquisitiveness.append((row['Q7'] + row['RQ31']) / 2)
    except:
        inquisitiveness.append('nan')
    try:
        creativity.append((row['RQ49'] + row['Q13'] + row['Q37']) / 3)
    except:
        creativity.append('nan')
    try:
        unconventionality.append((row['RQ19'] + row['Q43'] + row['RQ55']) / 3)
    except:
        unconventionality.append('nan')
    try:
        openness_to_experience.append((row['Q25'] + row['RQ1']+
                                 row['Q7'] + row['RQ31']+
                                 row['RQ49'] + row['Q13'] + row['Q37']+
                                 row['RQ19'] + row['Q43'] + row['RQ55']) / 10)
    except:
        openness_to_experience.append('nan')
#Add each list to data set 
df = pd.DataFrame()
dat['sincerity'] = sincerity
dat['fairness'] = fairness
dat['greed_avoidance'] = greed_avoidance
dat['modesty'] = modesty
dat['honesty_humility'] = honesty_humility
dat['fearfulness'] = fearfulness
dat['anxiety'] = anxiety
dat['dependence'] = dependence
dat['sentimentality'] = sentimentality
dat['emotionality'] = emotionality
dat['social_self_esteem'] = social_self_esteem
dat['social_boldness'] = social_boldness
dat['sociability'] = sociability
dat['liveliness']= liveliness
dat['extraversion'] = extraversion
dat['forgiveness'] = forgiveness
dat['gentleness'] = gentleness
dat['flexibility'] = flexibility
dat['patience'] = patience
dat['agreeableness'] = agreeableness
dat['organization'] = organization
dat['diligence'] = diligence
dat['perfectionism'] = perfectionism
dat['prudence'] = prudence
dat['conscientiousness'] = conscientiousness
dat['aesthetic_appreciation'] = aesthetic_appreciation
dat['inquisitiveness'] = inquisitiveness
dat['creativity'] = creativity
dat['unconventionality'] = unconventionality
dat['openness_to_experience'] = openness_to_experience            

df.to_csv('facets_by_person.csv')
dat.to_csv('hexaco_plus_facets.csv')
    
#Calculating mean values by temperature
overall_dict = {}
temp_list = ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
factor_list = ['sincerity','fairness','greed_avoidance','modesty','honesty_humility','fearfulness',
               'anxiety','dependence','sentimentality','emotionality','social_self_esteem','social_boldness',
               'sociability','liveliness','extraversion','forgiveness','gentleness','flexibility','patience',
               'agreeableness','organization','diligence','perfectionism','prudence','conscientiousness',
               'aesthetic_appreciation','inquisitiveness','creativity','unconventionality','openness_to_experience']
for item in temp_list:
    overall_dict[item] = {}
for key, value in overall_dict.items():
    for i in factor_list:
        value[i] = []

for index, row in dat.iterrows():
    temperature = (row['temp'])
    for item in factor_list:
        j = row[item]
        overall_dict[str(temperature)][str(item)].append(j)

for item in temp_list:
    y = pd.DataFrame()
    x = overall_dict[item]
    for key, value in x.items():
        y[key] = value
    name = str(item) + '.csv'
    y.to_csv(name)



#Get mean for each option
for temp in temp_list:
    mean_dict = {}
    f = pd.read_csv(str(temp) + '.csv')
    q = f.fillna(0)
    for x in factor_list:
        y = q[str(x)].tolist()
        t = [i for i in y if i != 0]
        mean_dict[x] = mean(t)
    df = pd.DataFrame([mean_dict]) 
    df.to_csv(str(temp) + '_mean.csv')
    
#Get standdev for each option
for temp in temp_list:
    mean_dict = {}
    f = pd.read_csv(str(temp) + '.csv')
    q = f.fillna(0)
    for x in factor_list:
        y = q[str(x)].tolist()
        t = [i for i in y if i != 0]
        mean_dict[x] = statistics.pstdev(t)
    df = pd.DataFrame([mean_dict]) 
    df.to_csv(str(temp) + '_SD.csv')    

#Get median for each option
for temp in temp_list:
    med_dict = {}
    f = pd.read_csv(str(temp) + '.csv')
    q = f.fillna(0)
    for x in factor_list:
        y = q[str(x)].tolist()
        t = [i for i in y if i != 0]
        med_dict[x] = statistics.median(t)
    df = pd.DataFrame([med_dict]) 
    df.to_csv(str(temp) + '_median.csv')

#Merging individual temperature documents into general overview
mdf = pd.read_csv('0.0_mean.csv', header = 0)
mdf = mdf.iloc[: , 1:]
sdf = pd.read_csv('0.0_SD.csv', header = 0)
sdf = sdf.iloc[: , 1:]
meddf = pd.read_csv('0.0_median.csv', header = 0)
meddf = meddf.iloc[: , 1:]

temp2_list = temp_list = ['0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']

for temp in temp2_list:
    m = pd.read_csv(str(temp) + '_mean.csv')
    s = pd.read_csv(str(temp) + '_SD.csv')
    p = pd.read_csv(str(temp) + '_median.csv')
    t=[]
    y=[]
    u = []
    for index, row in m.iterrows():
        for value in factor_list:
            t.append(row[value])
    mdf.loc[len(mdf)] = t
    for index, row in s.iterrows():
        for value in factor_list:
            y.append(row[value])
    sdf.loc[len(sdf)] = y
    for index, row in p.iterrows():
        for value in factor_list:
            u.append(row[value])
    meddf.loc[len(meddf)] = t
    
mdf['temp'] = temp_list
sdf['temp'] = temp_list
meddf['temp'] = temp_list
#Writing overview per temperature to outfile
mdf.to_csv('full_temp_mean.csv')
sdf.to_csv('full_temp_sd.csv')
meddf.to_csv('full_temp_median.csv')

#Compute mean, median and SD whole data set
mean_whole_set = {}
df = pd.read_csv('facets_by_person.csv')
dfn = df.fillna(0)
for item in factor_list:
    x = dfn[str(item)].tolist()
    t = [u for u in x if u != 0]
    y = statistics.pstdev(x)
    mean_whole_set[str(item)] = y

wf = pd.DataFrame([mean_whole_set])

wf.to_csv('SD_whole_dataset.csv')
    

#Calculate correlations
df = pd.read_csv('hexaco_plus_facets.csv')
df2 = df[['temp', 'openness_to_experience', 'honesty_humility', 'extraversion', 'emotionality', 'agreeableness', 'conscientiousness']]
df3 = df[['openness_to_experience', 'honesty_humility', 'extraversion', 'emotionality', 'agreeableness', 'conscientiousness']]

t = df3.corr()
for value in temp_list:
    temp_dict = {}
    temp_dict['openness_to_experience'] = []
    temp_dict['honesty_humility'] = []
    temp_dict['extraversion'] = []
    temp_dict['emotionality'] = []
    temp_dict['agreeableness'] = []
    temp_dict['conscientiousness'] = []
    for index, row in df2.iterrows():
        temp = row['temp']
        if str(temp) == str(value):
            temp_dict['openness_to_experience'].append(row['openness_to_experience'])
            temp_dict['honesty_humility'].append(row['honesty_humility'])
            temp_dict['extraversion'].append(row['extraversion'])
            temp_dict['emotionality'].append(row['emotionality'])
            temp_dict['agreeableness'].append(row['agreeableness'])
            temp_dict['conscientiousness'].append(row['conscientiousness'])
        else:
            continue
    f = pd.DataFrame().from_dict(temp_dict)
    f.to_csv('dataset_split_by_temp' + str(value) +'.csv')
         
for value in temp_list:
    t = pd.read_csv('dataset_split_by_temp' + str(value) +'.csv')
    p = t.corr()
    p.to_csv('correlation_' + str(value) + '.csv')
         
main_facets = ['openness_to_experience', 'honesty_humility', 'extraversion', 'emotionality', 'agreeableness', 'conscientiousness']
for value in temp_list:
    t = pd.read_csv('dataset_split_by_temp' + str(value) +'.csv')
    t = t.drop('Unnamed: 0', axis=1)
    for x in main_facets:
        
