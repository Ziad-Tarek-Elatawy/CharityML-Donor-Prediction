import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def clean_and_preprocess(df):
    

    # 1. Log-transformation 
    skewed = ['capital-gain', 'capital-loss']
    df_transformed = df.copy()
    df_transformed[skewed] = df[skewed].apply(lambda x: np.log(x + 1))
    
    # 2. Normalization (MinMaxScaler)
    scaler = MinMaxScaler()
    numerical = ['age', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
    df_transformed[numerical] = scaler.fit_transform(df_transformed[numerical])
    
    # 3. One-hot encoding 
    if 'income' in df_transformed.columns:
        income_raw = df_transformed['income']
        income = income_raw.map({'>50K': 1, '<=50K': 0})
        features_raw = df_transformed.drop('income', axis=1)
    else:
        features_raw = df_transformed
        income = None
        
    features_final = pd.get_dummies(features_raw)
    
    return features_final, income

def save_processed_data(features, income, filepath):
    
    final_df = features.copy()
    if income is not None:
        final_df['income'] = income
    
    final_df.to_csv(filepath, index=False)
    print(f"✅ Successfully saved processed data to: {filepath}")