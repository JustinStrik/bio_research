import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Masking
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Function to create a sample 3D array with missing values
def create_sample_data():
    np.random.seed(0)
    data = np.random.choice([0, 1, np.nan], size=(100, 10, 10), p=[0.45, 0.45, 0.1])
    return data

# data is 
def load_data():
    # Load the data
    data = np.load('data.npy')
    return data

# Function to preprocess the data by replacing NaNs with a mask value
def preprocess_data(data):
    mask_value = -1
    data[np.isnan(data)] = mask_value
    return data, mask_value

# Function to build the LSTM model for imputation
def build_model(input_shape, mask_value):
    model = Sequential()
    model.add(Masking(mask_value=mask_value, input_shape=input_shape))
    model.add(LSTM(50, return_sequences=True))
    model.add(LSTM(50, return_sequences=True))
    model.add(Dense(input_shape[-1]))  # Output shape should match the input shape
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Function to impute missing values using the LSTM model
def impute_missing_values(train_data, test_data, mask_value):
    input_shape = (train_data.shape[1], train_data.shape[2])
    model = build_model(input_shape, mask_value)

    # Reshape data for LSTM input
    X_train = train_data.reshape((train_data.shape[0], train_data.shape[1], train_data.shape[2]))
    
    # Train the model
    model.fit(X_train, X_train, epochs=50, batch_size=8, verbose=0)
    
    # Predict missing values in test data
    X_test = test_data.reshape((test_data.shape[0], test_data.shape[1], test_data.shape[2]))
    imputed_test_data = model.predict(X_test)
    
    # Replace masked values with predicted values in test data
    test_data[test_data == mask_value] = imputed_test_data[test_data == mask_value]
    
    return test_data

# Function to evaluate the imputed data
def evaluate_imputation(original_data, imputed_data, mask_value):
    # Only compare the values that were originally masked
    mask = original_data == mask_value
    mse = mean_squared_error(original_data[mask], imputed_data[mask])
    return mse

if __name__ == "__main__":
    # Create sample data with missing values
    data = create_sample_data()

    # Preprocess the data
    data, mask_value = preprocess_data(data)

    # Split the data into training and testing sets
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

    # Impute missing values
    imputed_data = impute_missing_values(train_data, test_data, mask_value)

    # Create a validation set with known values (use float type to allow NaNs)
    validation_data = np.random.choice([0.0, 1.0], size=(20, 10, 10), p=[0.5, 0.5])
    validation_data_with_missing = validation_data.copy()
    validation_data_with_missing[np.random.rand(*validation_data_with_missing.shape) < 0.1] = np.nan

    # Preprocess the validation data
    validation_data_with_missing, _ = preprocess_data(validation_data_with_missing)

    # Impute missing values in the validation set
    imputed_validation_data = impute_missing_values(train_data, validation_data_with_missing, mask_value)

    # Evaluate the imputed data
    mse = evaluate_imputation(validation_data, imputed_validation_data, mask_value)
    print(f"Mean Squared Error of Imputation: {mse}")