# import requests
#
# flacFile = "output.flac"
#
# API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
# headers = {"Authorization": "Bearer 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"}
#
#
# def query(filename):
#     with open(filename, "rb") as f:
#         info = f.read()
#     response = requests.post(API_URL, headers=headers, data=info)
#     return response.json()
#
#
# sentence = query(flacFile)["text"]
# print(sentence)
# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.utils import np_utils
#
# # Load the Iris dataset (replace with your own data)
# data = pd.read_csv("iris.csv")
# X = data.iloc[:, :-1].values
# y = data.iloc[:, -1].values
#
# # Encode the output variable (species)
# encoder = LabelEncoder()
# y_encoded = encoder.fit_transform(y)
# y_one_hot = np_utils.to_categorical(y_encoded)
#
# # Split data into train and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y_one_hot, test_size=0.2, random_state=42)
#
# # Create a simple neural network
# model = Sequential()
# model.add(Dense(8, input_dim=4, activation='relu'))
# model.add(Dense(3, activation='softmax'))  # Three output neurons for three classes
#
# # Compile the model
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#
# # Train the model
# model.fit(X_train, y_train, epochs=50, batch_size=10, verbose=0)
#
# # Evaluate the model
# _, accuracy = model.evaluate(X_test, y_test)
# print(f"Accuracy: {accuracy * 100:.2f}%")

import numpy as np
import matplotlib.pyplot as plt

# assuming new_data is your numpy array
new_data = np.array([1, 2, 3, 4, 5])

plt.figure(figsize=(12, 6))

# plot for new_data.reshape(1, -1)
plt.subplot(1, 2, 1)
plt.plot(new_data.reshape(1, -1)[0])
plt.title('Plot for new_data.reshape(1, -1)')

# plot for new_data.reshape(1, 1)
plt.subplot(1, 2, 2)
plt.plot(new_data[0].reshape(1, 1)[0], 'bo')
plt.title('Plot for new_data.reshape(1, 1)')

plt.show()
