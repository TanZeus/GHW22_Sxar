import random

with open("spacy/assets/dataset.txt", "r") as f:
    data = f.read().split('\n')

random.shuffle(data)

train_data = data[:40]
test_data = data[60:]

with open("spacy/assets/data.train.jsonl", "w") as f:
    for i in range(len(train_data)):
        f.write(train_data[i])
with open("spacy/assets/data.test.jsonl", "w") as f:
    for i in range(len(test_data)):
        f.write(test_data[i])
