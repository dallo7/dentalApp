import re
import requests
import nltk


def remove_nouns(text):
    tokens = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    verbs = [word for word, tag in pos_tags if tag.startswith('VB')]

    return verbs


def remove_stop_words(text):
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')

    tokens = nltk.word_tokenize(text)

    stop_words = nltk.corpus.stopwords.words('english')

    filtered_words = [word for word in tokens if word not in stop_words]

    result = " ".join(filtered_words)

    return result


def reduce_spaces(text):
    result = re.sub(r"\s+", " ", text)
    return result


# Userinput = """The old clock on the wall ticked relentlessly, each tick echoing through the dusty attic. Sarah crept cautiously through the cobwebs, her heart pounding in her chest. Sunlight streamed weakly through a grimy window, casting long shadows across the room. Her flashlight flickered in her hand, illuminating forgotten toys and forgotten dreams.
#
# Suddenly, a floorboard creaked beneath her foot. Sarah gasped and spun around, the beam of light frantically searching the darkness. Nothing. But the silence that followed the creak seemed even louder, oppressing her with its weight.
# """

# API_URL = "https://api-inference.huggingface.co/models/google/gemma-2b-it"
# headers = {"Authorization": "Bearer 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"}

# API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
# headers = {"Authorization": "Bearer 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"}
#
# API_URL = "https://api-inference.huggingface.co/models/google/gemma-7b-it"
# headers = {"Authorization": "Bearer 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"}

API_URL = "https://api-inference.huggingface.co/models/JulesBelveze/t5-small-headline-generator"
headers = {"Authorization": "Bearer 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"}


def formatInput(Userinput):
    def allProcess(text):
        response = requests.post(API_URL, headers=headers, json=text)
        return response.json()

    output = allProcess({
        "inputs": f"{Userinput}",
    })

    finalText = output[0]['summary_text']

    result = remove_nouns(finalText)

    allStrings = ", ".join(result)

    return allStrings

#
# print(formatInput(Userinput))

# print(result)

# def allProcess(Userinput):
#
#     def query(payload):
#         response = requests.post(API_URL, headers=headers, json=payload)
#         return response.json()
#
#     output = query({
#         "inputs": f"{Userinput}",
#     })
#
#     print(output)
#
#     finalText = output[0]['summary_text']
#
#     def filter_text_between_brackets(text):
#         matches = re.findall(r"\[(.*?)\]", text)[2:6]
#         print(matches)
#
#         return matches
#
#     filtered_text = filter_text_between_brackets(finalText)
#     print(filtered_text)
#
#     text_without_quotes = [element.strip("'").replace("'", "") for element in filtered_text]
#
#     result = ", ".join(text_without_quotes)
#
#     result = remove_stop_words(result).replace(',', '')
#
#     result = reduce_spaces(result)
#
#     return result
#
#
# print(allProcess(Userinput))
