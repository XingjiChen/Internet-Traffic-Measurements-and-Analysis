# Import libraries needed
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

## Skeleton code for Task 7.3.

def preprocessing_for_ML(file_name, n_samples):

    # Read CSV file
    df = pd.read_csv(file_name)
    print(df.head())

    # Step 1. Delete the instances that have empty values
    df = "???"
    
    # Step 2. Stratifies sampling (n samples)
    df_less2000ms = df [ df['duration'] < 2000 ]
    df_more2000ms = df [ df['duration'] >= 2000 ]
    sampling_less2000ms = df_less2000ms.sample( "???" )
    sampling_more2000ms = df_more2000ms.sample( "???" )

    df = pd.concat( "???" )
    
    # Step 3. Encode the non-numerical values (srcip and dstip)
    encoder = LabelEncoder()
    df['srcip'] = "???"
    df['dstip'] = "???"
    
    # Step 4. Standardize the values (this is automatically converts dataframe to array)
    scaler_standard = StandardScaler()
    df = "???"
    
    # Step 5. Normalization (values between 0 and 1)
    scaler_normal = MinMaxScaler(feature_range=(0, 1))
    df = "???"
    
    # Return the new pre-processed data set (data frame)
    df = pd.DataFrame(df, columns=['srcip', 'srcport', 'dstip', 'dstport', 'proto', 'duration'])
    df = df.sample(frac=1)
    print(df.head())
    print(df.shape)
    
    return(df)

# Call the function passing the information about "file name" and "number of samples" as arguments
df_stratified = preprocessing_for_ML("simple_flow_data.csv",200)