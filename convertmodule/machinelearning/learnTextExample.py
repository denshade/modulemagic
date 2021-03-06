import csv
import sys
import random
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

def loadMyData(MyDataFiles, TheirDataFiles):
    allData = []
    allLabels = []
    for MyDataFile in MyDataFiles:
        with open(MyDataFile, "r") as myDataFile:
            values = myDataFile.read().splitlines(keepends=False)
            for key in values:
                keysAsInt = list(map(int, key.split(",")))
                allData.append(keysAsInt)
                allLabels.extend([1])

    for TheirDataFile in TheirDataFiles:
        with open(TheirDataFile, "r") as theirDataFile:
            values = theirDataFile.read().splitlines(keepends=False)
            for key in values:
                keysAsInt = list(map(int, key.split(",")))
                allData.append(keysAsInt)
                allLabels.extend([0])

    trainingData = []
    trainingLabels = []
    testData = []
    testLabels = []
    trainingData.extend(allData)
    trainingLabels.extend(allLabels)

    for i in range(1, len(allData)):
        index = random.random() * 10
        if index < 1:
            testData.append(allData[i])
            testLabels.append(allLabels[i])
        else:
            trainingData.append(allData[i])
            trainingLabels.append(allLabels[i])

    return (trainingData,trainingLabels), (testData,testLabels)

def get_word_index(DictFile):
    with open(DictFile, 'r', encoding="utf8") as dictfile:
        list = dictfile.read().lower().splitlines()
    words = {}
    index = 0
    for word in list:
        words[word] = index
        index += 1
    return words

def execute(row):
    positiveExamples = row["positiveFiles"].split("|")
    negativeExamples = row["negativeFiles"].split("|")
    dictFile = row["DictFile"]
    (train_data, train_labels), (test_data, test_labels) = loadMyData(positiveExamples,
                                                                      negativeExamples)
    print("Training entries: {}, labels: {}".format(len(train_data), len(train_labels)))
    print(train_data[0])
    len(train_data[0]), len(train_data[1])

    # A dictionary mapping words to an integer index
    word_index = get_word_index(dictFile)

    # The first indices are reserved
    word_index = {k:(v+3) for k,v in word_index.items()}
    word_index["<PAD>"] = 0
    word_index["<START>"] = 1
    word_index["<UNK>"] = 2  # unknown
    word_index["<UNUSED>"] = 3

    reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

    def decode_review(text):
        return ' '.join([reverse_word_index.get(i, '?') for i in text])

    decode_review(train_data[0])

    train_data = keras.preprocessing.sequence.pad_sequences(train_data,
                                                            value=word_index["<PAD>"],
                                                            padding='post',
                                                            maxlen=256)

    test_data = keras.preprocessing.sequence.pad_sequences(test_data,
                                                           value=word_index["<PAD>"],
                                                           padding='post',
                                                           maxlen=256)

    # input shape is the vocabulary count used for the movie reviews (10,000 words)
    vocab_size = len(word_index)

    model = keras.Sequential()
    model.add(keras.layers.Embedding(vocab_size, 16))
    model.add(keras.layers.GlobalAveragePooling1D())
    model.add(keras.layers.Dense(16, activation=tf.nn.relu))
    model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

    model.summary()
    model.compile(optimizer=tf.train.AdamOptimizer(),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    validationCutoff = int(2*len(train_data)/10)
    x_val = train_data[:validationCutoff]
    partial_x_train = train_data[validationCutoff:]

    y_val = train_labels[:validationCutoff]
    partial_y_train = train_labels[validationCutoff:]

    history = model.fit(partial_x_train,
                        partial_y_train,
                        epochs=40,
                        batch_size=512,
                        validation_data=(x_val, y_val),
                        verbose=1)
    results = model.evaluate(test_data, test_labels)

    print(results)


    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(1, len(acc) + 1)

    # "bo" is for "blue dot"
    plt.plot(epochs, loss, 'bo', label='Training loss')
    # b is for "solid blue line"
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()

    history_dict = history.history
    history_dict.keys()

    plt.clf()   # clear figure
    acc_values = history_dict['acc']
    val_acc_values = history_dict['val_acc']

    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.show()

def show_params():
    return "positiveFiles,negativeFiles,dictFile\npositiveFiles | separated,negativeFiles | separated,dictFile."

if len(sys.argv) != 2 or sys.argv[1] == "--inputparameters":
    print(show_params())
    sys.exit(2)
if sys.argv[1] == "--validate":
    pass
    #validate(sys.argv[2])



input_file = sys.argv[1]


with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        execute(row)
