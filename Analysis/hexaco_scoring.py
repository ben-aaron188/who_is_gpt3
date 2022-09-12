import pandas as pd

hsv_full = pd.read_csv (r'data/hexaco/nonreinforced/hexaco_nonreinf_full_data_cleaned.csv')

# Reverse likert scale scoring
def reverseScoring(df, high, cols):
    '''Reverse scores on given columns
     df = your data frame,
     high = highest score available
     cols = the columns you want reversed in list form'''
    df[cols] = (high+1) - df[cols]
    return df

# list of columns to be reversed
to_be_reversed = list(hsv_full.columns)[1:]
for n in range(len(to_be_reversed)):
    to_be_reversed[n] = 'Q'+str(to_be_reversed[n]+1)

# new df with reversed values
hsv_reversed = [30, 12, 60, 42, 24, 48, 53, 35, 41, 59, 28, 52, 10, 46,
                  9, 15, 57, 21, 26, 32, 14, 20, 44, 56, 1, 31, 49, 19, 55]
hsv_reversed = reverseScoring(hsv_reversed, 5, to_be_reversed)

# dictionary with test scoring keys
values_dict = {'Honesty-Humility':[6, 30, 54, 12, 36, 60, 18, 42, 24, 48],
                   'Emotionality':[5, 29, 53, 11, 35, 17, 41, 23, 47, 59],
                   'Extraversion':[4, 28, 52, 10, 34, 58, 16, 40, 22, 46],
                   'Agreeableness':[3, 27, 9, 33, 51, 15, 39, 57, 21, 45],
                   'Conscientiousness':[2, 26, 8, 32, 14, 38, 50, 20, 44, 56],
                   'Openness to Experience':[1, 25, 7, 31, 13, 37, 49, 19, 43, 55]
              }
# adapt scoring keys to column names
for k in values_dict:
    for n in range(len(values_dict[k])):
        values_dict[k][n] = ('Q'+str(values_dict[k][n]))

# compute raw means according to scoring keys
for k in values_dict:
    hsv_reversed[k] = hsv_reversed[values_dict[k]].mean(axis=1)

hsv_reversed.to_csv('data/hexaco/nonreinforced/hexaco_nonreinf_full_data_scores.csv', index=False)
