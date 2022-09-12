import pandas as pd

hsv_full = pd.read_csv (r'data/hexaco/nonreinforced/hsv_nonreinf_full_data_cleaned.csv')

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
hsv_reversed = hsv_full.copy()
hsv_reversed = reverseScoring(hsv_reversed, 6, to_be_reversed)

# dictionary with test scoring keys
values_dict = {'Conformity' : [7,16],
               'Tradition' : [9,20],
               'Benevolence' : [12,18],
               'Universalism' : [3,8,19],
               'Self-Direction' : [1,11],
               'Stimulation' : [6,15],
               'Hedonism' : [10,21],
               'Achievement' : [4,13],
               'Power' : [2,17],
               'Security' : [5,14]
}
# adapt scoring keys to column names
for k in values_dict:
    for n in range(len(values_dict[k])):
        values_dict[k][n] = ('Q'+str(values_dict[k][n]))

# compute raw means according to scoring keys
for k in values_dict:
    hsv_reversed[k] = hsv_reversed[values_dict[k]].mean(axis=1)

hsv_reversed.to_csv('data/hsv/nonreinforced/hsv_nonreinf_full_data_scores.csv', index=False)
