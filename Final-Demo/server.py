from flask import Flask, redirect, request
from keras import models
from keras import layers
from keras import optimizers
from keras import losses
from keras import metrics
from keras import backend as K
from keras.models import model_from_json
import numpy as np
import nltk
import textmining
import crawling
import textrank
import json
from collections import OrderedDict

app = Flask(__name__)

x_train = []
x_test = []
y_train = []
y_test = []
train_data = textmining.read_data('training_set/ratings_train.txt')
test_data = textmining.read_data('training_set/ratings_test.txt')

class MachineL :

    def set_training(train_docs,test_docs):
        global x_train,y_train,x_test,y_test
        train_x = [textmining.term_frequency(d,selected_words) for d, _ in train_docs]
        test_x = [textmining.term_frequency(d,selected_words) for d, _ in test_docs]
        train_y = [c for _, c in train_docs]
        test_y = [c for _, c in test_docs]

        x_train = np.asarray(train_x).astype('float32')
        x_test = np.asarray(test_x).astype('float32')

        y_train = np.asarray(train_y).astype('float32')
        y_test = np.asarray(test_y).astype('float32')


    def Machine_learning(self) :
        global x_train,y_train,x_test,y_test
        model = models.Sequential()
        model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(1, activation='sigmoid'))

        model.compile(optimizer=optimizers.SGD(lr=0.01, momentum=0.9),
                      loss=losses.binary_crossentropy,
                      metrics=[metrics.binary_accuracy])
        model_json = model.to_json()
        with open("model.json","w") as json_file :
            json_file.write(model_json)
        model.fit(x_train, y_train, epochs=10, batch_size=512)
        model.save_weights('model.h5')

        results = model.evaluate(x_test, y_test)

    def load_model(self):
        json_file = open('model.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)

        loaded_model.compile(optimizer=optimizers.SGD(lr=0.01, momentum=0.9),
                      loss=losses.binary_crossentropy,
                      metrics=[metrics.binary_accuracy])
        loaded_model.load_weights('model.h5')

        return loaded_model

    def predict(self,review):
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)

        loaded_model.compile(optimizer=optimizers.SGD(lr=0.01, momentum=0.9),
                             loss=losses.binary_crossentropy,
                             metrics=[metrics.binary_accuracy])
        loaded_model.load_weights('model.h5')

        token = textmining.tokenize(review)
        tf = textmining.term_frequency(token,selected_words)
        data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
        score = float(loaded_model.predict(data))
        return score * 100

    def term_frequency(doc):
        return [doc.count(word) for word in selected_words]


machine = MachineL()
textmining.load_docs()
tokens = [t for d in textmining.train_docs for t in d[0]]
text = nltk.Text(tokens, name='NMSC')
selected_words = [f[0] for f in text.vocab().most_common(10000)]
print("Server ready...")


@app.route('/capstone',methods=['POST'])
def hello():
    data = request.get_json()
    RequestURL = data['url']
    contents = crawling.run(RequestURL)
    if contents == "":
        return 0
    textrank_return = textrank.run(contents)

    sum = 0
    total = 0


    for k in sorted(textrank_return[1], key=textrank_return[1].get, reverse=True)[:6]:
        K.clear_session()
        sum = sum + (machine.predict(textrank_return[0][k]) * (textrank_return[1][k]))
        total = total + textrank_return[1][k]

    average = sum/total

    if(average > 80):
        result = "키워드에 대해 매우 우호적인 기사입니다!"
    elif(average <= 80 and average >60):
        result = "키워드에 대해 약간 우호적인 기사입니다!"
    elif(average <= 60 and average > 40) :
        result = "키워드에 대해 중립적인 기사입니다!"
    elif(average <= 40 and average >20) :
        result = "키워드에 대해 약간 적대적인 기사입니다!"
    else:
        result = "키워드에 대해 매우 적대적인 기사입니다!"

    file_data = OrderedDict()

    file_data["result"] = result
    file_data["summarize"] = str(textrank_return[2])
    file_data["keywords"] = str(textrank_return[3])

    return_json = json.dumps(file_data, ensure_ascii=False, indent='\t')
	####
	# Insert proper code in here
	####
    return return_json


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000,debug=True)
