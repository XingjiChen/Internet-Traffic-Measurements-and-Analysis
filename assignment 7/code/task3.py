import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler

def prepare_dataset(file_path):
    # Step 1: Load the data and remove instances with missing values
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)

    # Step 2: Perform stratified random sampling
    less_than_2000 = df[df['duration'] < 2000].sample(n=100, random_state=1)
    more_than_2000 = df[df['duration'] >= 2000].sample(n=100, random_state=1)
    df = pd.concat([less_than_2000, more_than_2000])

    # Step 3: Encode non-numeric data
    label_encoder = LabelEncoder()
    df['srcip'] = label_encoder.fit_transform(df['srcip'])
    df['dstip'] = label_encoder.fit_transform(df['dstip'])

    # Step 4: Standardize values
    standard_scaler = StandardScaler()
    df[['srcport', 'dstport', 'proto', 'duration']] = standard_scaler.fit_transform(
        df[['srcport', 'dstport', 'proto', 'duration']])

    # Step 5: Normalize values between 0 and 1
    minmax_scaler = MinMaxScaler()
    df[['srcip', 'srcport', 'dstip', 'dstport', 'proto', 'duration']] = minmax_scaler.fit_transform(
        df[['srcip', 'srcport', 'dstip', 'dstport', 'proto', 'duration']])

    # Return the preprocessed dataset
    return df.reset_index(drop=True)

# Assuming the CSV file is in the 'file' directory as specified:
file_path = 'file/simple_flow_data.csv'
preprocessed_dataset = prepare_dataset(file_path)
print(preprocessed_dataset)