import nltk
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.classifiers import DecisionTreeClassifier
from textblob.classifiers import MaxEntClassifier
from nltk.stem.isri import ISRIStemmer
from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
from LoadData import LoadData

data = LoadData
def classify_review(classifier):
    print('Accuracy of :  training_array ==> ', classifier.accuracy(training_array))
    print('Accuracy of :  training_array_without_sw ==> ', classifier.accuracy(training_array_without_sw))
    print('Accuracy of :  training_array_stemmed_without_sw ==> ', classifier.accuracy(training_array_stemmed_without_sw))
    print('Accuracy of :  test_array ==> ', classifier.accuracy(test_array))
    print('Accuracy of :  test_array_without_sw ==> ', classifier.accuracy(test_array_without_sw))
    print('Accuracy of :  test_array_stemmed_without_sw ==> ', classifier.accuracy(test_array_stemmed_without_sw))

training_array=data.get_training_array(data)
# print('training_array')
# print(training_array)
training_array_without_sw= data.get_training_array_without_sw(data)
# print('training_array_without_sw')
# print(training_array_without_sw)
training_array_stemmed_without_sw=data.get_training_array_stemmed_without_sw(data)
# print('training_array_stemmed_without_sw')
# print(training_array_stemmed_without_sw)
test_array = data.get_test_array(data)
print('test_array')
print(test_array)
test_array_without_sw = data.get_test_array_without_sw(data)
print('test_array_without_sw')
print(test_array_without_sw)
test_array_stemmed_without_sw =  data.get_test_array_stemmed_without_sw(data)
print('test_array_stemmed_without_sw')
print(test_array_stemmed_without_sw)

print('\n************ DecisionTreeClassifier ********************\n')
print('Before pre-processing \n')
cl = DecisionTreeClassifier(training_array)
classify_review(cl)
print('\n After removing stop-words \n')
cl = DecisionTreeClassifier(training_array_without_sw)
classify_review(cl)
print('\n After stemming \n')
cl = DecisionTreeClassifier(training_array_stemmed_without_sw)
classify_review(cl)
print('\n ************ NaiveBayesClassifier ********************\n')
print('Before pre-processing\n')
cl = NaiveBayesClassifier(training_array)
classify_review(cl)
print('\n After removing stop-words \n')
cl = NaiveBayesClassifier(training_array_without_sw)
classify_review(cl)
print('\n After stemming \n')
cl = NaiveBayesClassifier(training_array_stemmed_without_sw)
classify_review(cl)

print('\n ************ MaxEntClassifier ********************\n')
cl= MaxEntClassifier(training_array)
print('Before pre-processing\n')
classify_review(cl)
print('\n After removing stop-words \n')
cl = MaxEntClassifier(training_array_without_sw)
classify_review(cl)
print('\n After stemming \n')
cl = MaxEntClassifier(training_array_stemmed_without_sw)
classify_review(cl)
