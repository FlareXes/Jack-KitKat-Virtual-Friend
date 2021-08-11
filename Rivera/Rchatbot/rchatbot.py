def importcoroutine():
  import nltk
  from nltk.stem import WordNetLemmatizer
  import pickle
  import numpy as np

  from keras.models import load_model
  import json
  import random
  from Rivera.rvoice import speak

  lemmatizer = WordNetLemmatizer()
  model = load_model(r'C:\Users\as808\OneDrive\Documents\KitKat\Rivera\Rchatbot\chatbot_model.h5')
  intents = json.loads(open(r'C:\Users\as808\OneDrive\Documents\KitKat/Rivera/Rchatbot/intents.json').read())
  words = pickle.load(open(r'C:\Users\as808\OneDrive\Documents\KitKat/Rivera/Rchatbot/mywords.pkl', 'rb'))
  classes = pickle.load(open(r'C:\Users\as808\OneDrive\Documents\KitKat/Rivera/Rchatbot/myclasses.pkl', 'rb'))

  while True:
    text = (yield)
    def clean_up_sentence(sentence):
      # tokenize the pattern - split words int array
      sentence_words = nltk.word_tokenize(sentence)

      # stem each word - create short form for word
      sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
      return sentence_words


    # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
    def bow(sentence, words, show_details=True):
      # tokenize the pattern
      sentence_words = clean_up_sentence(sentence)

      # bag of words - matrix of N words, vocabulary matrix
      bag = [0] * len(words)
      for s in sentence_words:
        for i,w in enumerate(words):
          if w == s:
            # assign 1 if current word is in the vocabulary position
            bag[i] = 1
            if show_details:
              print("found in bag: %s" % w)
      return (np.array(bag))

    def predict_class(sentence, model):
      # filter out predictions below a threshold
      p = bow(sentence, words, show_details=False)
      res = model.predict(np.array([p]))[0]
      ERROR_THRESHOLD = 0.25
      results = [[i ,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

      # sort by strength of probability
      results.sort(key=lambda x: x[1], reverse=True)
      return_list = []
      for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
      return return_list

    # get a random response from the list of intents
    def getResponse(ints, intents_json):
      tag = ints[0]['intent']
      list_of_intents = intents_json['intents']
      for i in list_of_intents:
        if(i['tag'] == tag):
          result = random.choice(i['responses'])
          break
      return result

    ints = predict_class(text, model)
    res = getResponse(ints, intents)
    print(res)
    speak(res)


# search = importcoroutine()
# search.__next__()
#
# search.send("What is python")
# search.send("hey there")
# search.send("how are you")
