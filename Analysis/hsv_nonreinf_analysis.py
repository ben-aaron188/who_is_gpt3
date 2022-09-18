import pandas as pd
from scipy.stats import spearmanr
from statsmodels.formula.api import glm

hvs_full = pd.read_csv (r'data/hvs_nonreinf_full_data_cleaned.csv')
hvs_full = hvs_full.dropna()
# Reverse likert scale scoring
def reverseScoring(df, high, cols):
    '''Reverse scores on given columns
     df = your data frame,
     high = highest score available
     cols = the columns you want reversed in list form'''
    df[cols] = (high+1) - df[cols]
    return df

def calculate_pvalues(df):
    df = df.dropna()._get_numeric_data()
    dfcols = pd.DataFrame(columns=df.columns)
    pvalues = dfcols.transpose().join(dfcols, how='outer')
    for r in df.columns:
        for c in df.columns:
            pvalues[r][c] = round(spearmanr(df[r], df[c])[1], 4)
    return pvalues

# list of columns to be reversed
to_be_reversed = list(hvs_full.columns)[1:]

# new df with reversed values
hsv_reversed = hvs_full.copy()
hsv_reversed = reverseScoring(hsv_reversed, 6, to_be_reversed)

# Correlation table to be compared to gesis (https://zis.gesis.org/skala/Schwartz-Breyer-Danner-Human-Values-Scale-(ESS))
values_dict = {'Conformity': [7,16],
               'Tradition' : [9,20],
               'Benevolence': [12,18],
               'Universalism' : [3,8,19],
               'Self_Direction' : [1,11],
               'Stimulation' : [6,15],
               'Hedonism' : [10,21],
               'Achievement': [4,13],
               'Power' : [2,17],
               'Security' : [5,14]
               }
values = values_dict.keys()
# adapt scoring keys to column names
for k in values_dict:
    for n in range(len(values_dict[k])):
        values_dict[k][n] = ('Q'+str(values_dict[k][n]))

# compute raw means according to scoring keys
hvs = hsv_reversed.copy()
for k in values_dict:
    hvs[k] = hsv_reversed[values_dict[k]].mean(axis=1)
hvs.to_csv('data/hvs_nonreinf_plus_values.csv', index=False)

# correlation tab
corr_tab = hvs.iloc[:,22:].corr(method ='spearman')
corr_tab = corr_tab.round(decimals = 2)
p_values_cor_tab = calculate_pvalues(hvs.iloc[:,22:])
p_values_cor_tab = p_values_cor_tab.round(decimals = 3)
p_values_cor_tab_symb = p_values_cor_tab.copy()
for col in p_values_cor_tab_symb:
    for n in range(len(p_values_cor_tab_symb[col])):
        if p_values_cor_tab_symb[col][n] <.05 and p_values_cor_tab_symb[col][n] >= .01:
            p_values_cor_tab_symb[col][n] = '*'
            continue
        if p_values_cor_tab_symb[col][n] <.01 and p_values_cor_tab_symb[col][n] >= .001:
            p_values_cor_tab_symb[col][n] = '**'
            continue
        if p_values_cor_tab_symb[col][n] <.001:
            p_values_cor_tab_symb[col][n] = '***'
            continue

# Put symbols into corr tab
corr_tab_simb = corr_tab.copy()
for col in p_values_cor_tab_symb:
    lst = []
    for n in range(len(p_values_cor_tab_symb[col])):
        if p_values_cor_tab_symb[col][n] == '*' or p_values_cor_tab_symb[col][n] == '**' or p_values_cor_tab_symb[col][n] == '***':
            v = str(corr_tab_simb[col][n])+str(p_values_cor_tab_symb[col][n])
            lst.append(v)
            continue
        else:
            v = str(corr_tab_simb[col][n])
            lst.append(v)
            continue
    corr_tab_simb[col] = lst

corr_tab.to_csv(r'tabs/nonreinf/corr_tab.csv', index = False)
p_values_cor_tab.to_csv(r'tabs/nonreinf/cor_tab_p_values.csv', index = False)
corr_tab_simb.to_csv(r'tabs/nonreinf/corr_tab_simb.csv', index = False)

# correlation tab by temperature
hvs_by_temp = []
for t in hvs.temp.unique():
    hvs_by_temp.append(hvs.loc[hvs['temp'] == t])
hvs_corr_by_temp = []
temp = 0
for t in hvs_by_temp:
    corr_tab = t.iloc[:, 22:].corr(method='spearman')
    corr_tab = corr_tab.round(decimals=2)
    hvs_corr_by_temp.append(corr_tab)
    corr_tab.to_csv(r'tabs/nonreinf/corr_by_temp/corr_0.'+str(temp)+'.csv')
    temp+=1

# Overall Stats
mean_values = []
sd_values = []
median_values = []
for v in values:
    mean = round(hvs[v].mean(),2)
    sd = round(hvs[v].std(),2)
    median = round(hvs[v].median(),2)
    mean_values.append(mean)
    sd_values.append(sd)
    median_values.append(median)
overall_stats = pd.DataFrame({'values': values, 'Mean': mean_values, 'SD': sd_values, 'Median': median_values})
overall_stats.to_csv('tabs/nonreinf/overall_stats.csv', index=False)

# Look at overall mean and SD with centered data
center_function = lambda x: x - x.mean()
hvs_centered = center_function(hvs.iloc[:,1:22])
hvs_centered['temp'] = hvs['temp']
for k in values_dict:
    hvs_centered[k] = hvs_centered[values_dict[k]].mean(axis=1)

mean_centered_values = []
sd_centered_values = []
for v in values:
    mean = round(hvs_centered[v].mean(),2)
    sd = round(hvs_centered[v].std(),2)
    mean_centered_values.append(mean)
    sd_centered_values.append(sd)
overall_stats_centered = pd.DataFrame({'values_C': values, 'Mean_C': mean_centered_values, 'SD_C': sd_centered_values})

# Combine overall mean stats with overall centered mean
combined_overall_stats = pd.concat([overall_stats, overall_stats_centered], axis=1)
combined_overall_stats.drop(['values_C', 'Median'], axis=1)
combined_overall_stats.to_csv('tabs/nonreinf/overall_stats_centered.csv', index=False)

# Mean (SD) by temperature
hvs_mean_SD_by_temp = pd.DataFrame()
hvs_mean_SD_by_temp['temp'] = hvs['temp'].unique()
for v in values:
    value_mean = hvs.groupby('temp')[v].mean().tolist()
    value_SD = hvs.groupby('temp')[v].std().tolist()
    results = []
    for n in range(len(value_mean)):
        m = value_mean[n]
        s = value_SD[n]
        y = str(round(m,2))+' ('+ str(round(s,2)) +')'
        results.append(y)
    hvs_mean_SD_by_temp[v] = results

hsv_total_mean_SD = {'temp':'TOT'}
for v in values:
    m = hvs[v].mean()
    s = hvs[v].std()
    y = str(round(m, 2)) + ' (' + str(round(s, 2)) + ')'
    hsv_total_mean_SD[v] = y

hvs_mean_SD_by_temp = hvs_mean_SD_by_temp.append(hsv_total_mean_SD, ignore_index=True)
hvs_mean_SD_by_temp = hvs_mean_SD_by_temp.transpose()
hvs_mean_SD_by_temp.to_csv('tabs/nonreinf/mean_SD_by_temp.csv', index=False)

# Median by temperature
hvs_median_by_temp = pd.DataFrame()
hvs_median_by_temp['temp'] = hvs['temp'].unique()
for v in values:
    value_median = hvs.groupby('temp')[v].median().tolist()
    results = []
    for n in range(len(value_median)):
        md = value_median[n]
        results.append(round(md,2))
    hvs_median_by_temp[v] = results

hsv_total_median = {'temp':'TOT'}
for v in values:
    value_median = hvs[v].median()
    md = value_median
    hsv_total_median[v] = md

hvs_median_by_temp = hvs_median_by_temp.append(hsv_total_median, ignore_index=True)
hvs_median_by_temp = hvs_median_by_temp.transpose()
hvs_median_by_temp.to_csv('tabs/nonreinf/median_by_temp.csv', index=False)

# MANOVA
from statsmodels.multivariate.manova import MANOVA
formula = ''
for v in values:
    if v == 'Security':
        formula = formula + v
    else:
        formula = formula + v + ' + '

formula = formula + ' ~ temp'
hvs_MANOVA = MANOVA.from_formula(formula, data=hvs)
print(hvs_MANOVA.mv_test()) # Wilk's test and Pilai's test are significat

# Regression Value ~ Temperature
GLM_models = {}
coef = []
std_err = []
CI = []
for v in values:
    model = glm(formula = v+'~temp', data= hvs).fit()
    GLM_models[v] = model.summary()
    c = round(model.params[1], 2)       # coefficient
    se = round(model.bse[1],2)         # stsandard error
    cl = round(model.conf_int()[0][1], 2) # lower bound
    ch = round(model.conf_int()[1][1],2) # upper bound
    ci = '['+str(cl)+', '+str(ch)+']'
    coef.append(c)
    std_err.append(se)
    CI.append(ci)

GLM_tab = pd.DataFrame({'Coefficient':coef, 'Std Err':std_err, 'CI':CI},
                          index=values)
GLM_tab.to_csv('tabs/nonreinf/GLM_coefficients.csv')



