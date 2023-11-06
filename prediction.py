import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv("https://raw.githubusercontent.com/wongwara/fare-prediction/main/data/sample_itineraries.csv")

#transform date column: searchDate
df['searchDate'] = pd.to_datetime(df['searchDate'])
df['searchDate_day'] = df['searchDate'].dt.day
df['searchDate_month'] = df['searchDate'].dt.month
df['searchDate_year'] = df['searchDate'].dt.year

#transform date column: flightDate
df['flightDate'] = pd.to_datetime(df['flightDate'])
df['flightDate_day'] = df['flightDate'].dt.day
df['flightDate_month'] = df['flightDate'].dt.month
df['flightDate_year'] = df['flightDate'].dt.year

#drop date cols
df = df.drop(columns=['searchDate', 'flightDate'])

df['DepartTime'] = df['segmentsDepartureTimeEpochSeconds'].apply(lambda x: x[1:-1].split(',')[0] if isinstance(x, str) else x)
df['DepartTime'] = pd.to_datetime(df['DepartTime'], unit='s')

# Extract and create new columns for hours, minutes, and seconds
df['DepartTime_hour'] = df['DepartTime'].dt.hour
df['DepartTime_minute'] = df['DepartTime'].dt.minute
df['DepartTime_second'] = df['DepartTime'].dt.second

df = df[['totalTravelDistance', 'isNonStop', 'isBasicEconomy', 'startingAirport', 'destinationAirport', 'segmentsCabinCode','flightDate_day', 'flightDate_month', 'flightDate_year',
                         'DepartTime_hour', 'DepartTime_minute', 'DepartTime_second','totalFare']]

cols = df_cleaned.columns.to_list()
num_cols = df_cleaned.select_dtypes(np.number).columns.to_list()
cat_cols = list(set(cols) - set(num_cols))
df['totalTravelDistance']= df['totalTravelDistance'].fillna(df['totalTravelDistance'].mean())

## Lable Encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df[cat_cols] = df[cat_cols].apply(le.fit_transform)
#scale numeric column
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

df[num_cols] = scaler.fit_transform(df[num_cols])

def pop_target(df, target_col):
    df_copy = df.copy()
    target = df_copy.pop(target_col)

    return df_copy, target

features, target = pop_target(df, 'totalFare')

def split_sets_random(features, target, test_ratio=0.2):
    from sklearn.model_selection import train_test_split
    val_ratio = test_ratio / (1 - test_ratio)
    X_data, X_test, y_data, y_test = train_test_split(features, target, test_size=test_ratio, random_state=8)
    X_train, X_val, y_train, y_val = train_test_split(X_data, y_data, test_size=val_ratio, random_state=8)
    return X_train, y_train, X_val, y_val, X_test, y_test
  
X_train, y_train, X_val, y_val, X_test, y_test = split_sets_random(features, target, test_ratio=0.2)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

# Model evaluation for training set
y_train_preds_lr = lr.predict(X_train)
y_test_preds_lr = lr.predict(X_test)

import pickle
data = {"model": linear}
with open('saved_steps.pkl', 'wb') as file:
    pickle.dump(data, file)
  
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

regressor_loaded = data["model"]

