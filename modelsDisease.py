from sklearn.feature_extraction.text import CountVectorizer
import pickle
import random
from collections import Counter
import pandas as pd
from scipy.sparse import csr_matrix
import requests

import requests
#
# API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B"
# headers = {"Authorization": "Bearer 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"}

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}

# API_URL = "https://api-inference.huggingface.co/models/google/gemma-7b-it"
# headers = {"Authorization": "Bearer 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"}


# API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
# headers = {"Authorization": "Bearer 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"}

vectorizer = CountVectorizer()


def models(symptom):
    dictOutOfSample = {70: symptom}

    seriesDictOutOfSample = pd.Series(dictOutOfSample, name='Symptoms')

    outOfSample = vectorizer.fit_transform(seriesDictOutOfSample)

    data = outOfSample.data.tolist()  # Non-zero values
    colInds = [i for i, length in enumerate(outOfSample.indptr[1:]) for _ in range(length)]  # Row indices
    rowInds = outOfSample.indices.tolist()

    vector_matrix = csr_matrix((data, (rowInds, colInds)), shape=(50, 145))

    with open('models for Disease/rf_classifier.pkl', 'rb') as f:
        model = pickle.load(f)

    modelRF = model.predict(vector_matrix)[:2]

    # print(modelRF)

    with open('models for Disease/naive_bayes_classifier.pkl', 'rb') as f:
        model = pickle.load(f)

    modelNB = model.predict(vector_matrix)[:2]

    # print(modelNB)

    with open('models for Disease/Decision_clf.pkl', 'rb') as f:
        model = pickle.load(f)

    modelDT = model.predict(vector_matrix)[:2]

    # print(modelDT)

    with open('models for Disease/svm_classifier.pkl', 'rb') as f:
        model = pickle.load(f)

    modelSVM = model.predict(vector_matrix)[:2]

    # print(modelSVM)

    lists = [modelNB, modelSVM, modelDT, modelRF][0][0]
    lists1 = [modelNB, modelSVM, modelDT, modelRF][1][0]
    lists2 = [modelNB, modelSVM, modelDT, modelRF][2][0]
    lists3 = [modelNB, modelSVM, modelDT, modelRF][3][0]
    shuffledList = [lists, lists1, lists2, lists3]
    # print(shuffledList)

    random.shuffle(shuffledList)
    # print(shuffledList)

    # counter = Counter(mainList)
    # most_common_element = counter.most_common()

    return shuffledList[0]


def filter_text(original_text: str) -> str:
    filter_phrase = "Assume you are a Dentist, What medicine and Diet do you prescribe for '"
    filtered_text = original_text.replace(filter_phrase, '')
    return filtered_text


def queryFlan(disease):
    payload = {
        "inputs": f"Assume you are a Dentist, What medicine and Diet do you prescribe for '{disease}'"}
    response = requests.post(API_URL, headers=headers, json=payload)

    response = response.json()

    return response
