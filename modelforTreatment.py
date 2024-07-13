from sklearn.feature_extraction.text import CountVectorizer
import pickle
import pandas as pd
import random
from collections import Counter
from scipy.sparse import csr_matrix

vectorizer = CountVectorizer()


def modelTreament(disease):
    dictOutOfSample = {70: disease}
    seriesDictOutOfSample = pd.Series(dictOutOfSample, name='Symptoms')

    outOfSample = vectorizer.fit_transform(seriesDictOutOfSample)

    data = outOfSample.data.tolist()
    col_inds = [i for i, length in enumerate(outOfSample.indptr[1:]) for _ in range(length)]  # Row indices
    row_inds = outOfSample.indices.tolist()

    vector_matrix = csr_matrix((data, (row_inds, col_inds)), shape=(50, 65))

    with open('models for Treatment/rf_classifier.pkl', 'rb') as f:
        model = pickle.load(f)
    modelRF = model.predict(vector_matrix)[:2]

    with open('models for Treatment/svm_classifier.pkl', 'rb') as f:
        model = pickle.load(f)
    modelSvm = model.predict(vector_matrix)[:2]

    lists = [modelSvm, modelRF][0][0]
    lists1 = [modelSvm, modelRF][1][0]

    shuffledList = [lists, lists1]
    # print(shuffledList)

    random.shuffle(shuffledList)
    # print(shuffledList)

    # counter = Counter(mainList)
    # most_common_element = counter.most_common()

    return shuffledList[0]



