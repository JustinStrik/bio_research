import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import Adam
from multiprocessing import Pool

# Create the 4x4x4 binary matrix
matrix = np.zeros((4, 4, 4), dtype=int)

# Fill the matrix according to the given pattern
for i in range(4):
    matrix[i, i, :] = 1

# Mask the third cross-section (set it to zeros)
masked_matrix = matrix.copy()
masked_matrix[2, :, :] = 0

# Prepare the training data excluding the third cross-section
X_train = np.delete(masked_matrix, 2, axis=0).reshape(3, -1)
y_train = np.delete(matrix, 2, axis=0).reshape(3, -1)

# Define the model
def create_model():
    model = Sequential()
    model.add(Flatten(input_shape=(64,)))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(16, activation='sigmoid'))
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Train the model in parallel
def train_model(_):
    model = create_model()
    model.fit(X_train, y_train, epochs=100, verbose=0)
    return model

if __name__ == '__main__':
    with Pool() as pool:
        models = pool.map(train_model, range(4))

    # Predict the third cross-section using the first model (as an example)
    predicted_section = models[0].predict(masked_matrix.reshape(1, -1)).reshape(4, 4)

    print("Original third cross-section:")
    print(matrix[2, :, :])
    print("\nPredicted third cross-section:")
    print(predicted_section)
