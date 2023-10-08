
################################################################
# PROGRAM NAME : income_prediction_analysis_enhanced.py
# DESCRIPTION : This script encompasses data exploration, preprocessing, and logistic regression 
#               modeling on the 'adult' dataset, aiming to predict if an individual earns above 50K a year.
#
# AUTHOR : ChatGPT
# CREATION DATE : 2023-10-09
# LAST CHANGE DATE : 2023-10-09
# REVIEWER : [Your Name]
# REVIEW DATE : YYYY-MM-DD
# 
# INPUT : The 'adult' dataset, comprising various demographic and employment-related variables.
#	
# SUMMARY : The script involves the following steps: data loading, basic descriptive statistics generation, 
#           handling missing values, data preprocessing (including one-hot encoding), and logistic regression 
#           modeling, followed by model evaluation.
# 
# REVIEW SUMMARY : [Reviewer's Notes]
# 
################################################################
# CHANGE TRACKER
# DATE			AUTHOR				DESCRIPTION
# 2023-10-09	ChatGPT				Initial version
#
################################################################

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, confusion_matrix

def load_data(filepath: str) -> pd.DataFrame:
    """
    Load the dataset into a pandas DataFrame.

    Args:
    - filepath (str): The path to the dataset.
    
    Returns:
    - DataFrame: The loaded data.
    """
    return pd.read_csv(filepath)

def basic_descriptive_stats(data: pd.DataFrame) -> pd.DataFrame:
    """
    Generate basic descriptive statistics of the data.

    Args:
    - data (DataFrame): The input data.
    
    Returns:
    - DataFrame: Descriptive statistics of the data.
    """
    return data.describe()

def handle_missing_values(data: pd.DataFrame, strategy: str='drop', columns: list=None) -> pd.DataFrame:
    """
    Handle missing values in the data.

    Args:
    - data (DataFrame): The input data.
    - strategy (str): The strategy to handle missing values ('drop' or 'placeholder'). Default is 'drop'.
    - columns (list of str): The columns to handle missing values. If None, use all columns. Default is None.
    
    Returns:
    - DataFrame: Data after handling missing values.
    """
    if columns is None:
        columns = data.columns
    
    if strategy == 'drop':
        data_clean = data.dropna(subset=columns)
    elif strategy == 'placeholder':
        data_clean = data.copy()
        for col in columns:
            if data[col].dtype == 'object':
                data_clean[col].fillna('Missing', inplace=True)
            else:
                data_clean[col].fillna(0, inplace=True)
    
    return data_clean

def preprocess_data(data: pd.DataFrame, target_var: str) -> tuple:
    """
    Preprocess the data by converting categorical variables into dummy variables.
    
    Args:
    - data (DataFrame): The input data.
    - target_var (str): The target variable.
    
    Returns:
    - tuple: The preprocessed data (X, y) where X contains the input features and y contains the target variable.
    """
    X = pd.get_dummies(data.drop(target_var, axis=1))
    y = data[target_var].apply(lambda x: 1 if x == '>50K' else 0)
    
    return X, y

def train_logistic_regression(X: pd.DataFrame, y: pd.Series) -> LogisticRegression:
    """
    Train a logistic regression model.

    Args:
    - X (DataFrame): The input features.
    - y (Series): The target variable.
    
    Returns:
    - LogisticRegression: The trained model.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("AUC:", roc_auc_score(y_test, y_prob))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    
    return model

# Example usage:
# Load data
data_path = 'path_to_your_data/adult.csv'  # Specify your data path
data = load_data(data_path)

# Perform basic descriptive statistics
desc_stats = basic_descriptive_stats(data)

# Handle missing values
data_clean = handle_missing_values(data, strategy='placeholder', columns=['workclass', 'occupation', 'native_country'])

# Preprocess data
X, y = preprocess_data(data_clean, target_var='income')

# Train logistic regression model
model = train_logistic_regression(X, y)

