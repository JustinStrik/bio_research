import numpy as np
import tensorflow as tf
from read_input import read_adj_matrix_input, test_mod, read_edge_list_input, get_full_matrix
from get_adj_matrix_files import get_adj_matrix_files, get_edge_list_files
model = tf.keras.models.Sequential()

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Masking
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# Function to create a sample 3D array with missing values
def create_sample_data():
    np.random.seed(0)
    data = np.random.choice([0, 1, np.nan], size=(100, 10, 10), p=[0.45, 0.45, 0.1])
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
    model.add(LSTM(50))
    model.add(Dense(input_shape[-1], activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy')
    return model

# Function to train the model and impute missing values
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


if __name__ == "__main__":
    # Create sample data with missing values
    data = create_sample_data()

    # files = get_edge_list_files()
    # A, mask = get_full_matrix(files, 2)

    # Preprocess the data
    data, mask_value = preprocess_data(data)

    # Split the data into training and testing sets
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

    # Impute missing values using the LSTM model
    imputed_test_data = impute_missing_values(train_data, test_data, mask_value)

    # Calculate the mean squared error between original and imputed test data for evaluation
    mse = mean_squared_error(test_data[test_data != mask_value], imputed_test_data[test_data != mask_value])

    print("Mean Squared Error between original and imputed test data:", mse)
