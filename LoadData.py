import nltk
from nltk.stem.isri import ISRIStemmer
class LoadData:
    # Load positive reviews
    def get_positive_reviews(self):
        positive_reviews_array = open("Positive.txt", 'r').read().split('\n')
        return positive_reviews_array

    # Load negative reviews
    def get_negative_reviews(self):
        negative_reviews_array = open("Negative.txt", 'r').read().split('\n')
        return negative_reviews_array

    # Load test negative reviews
    def get_test_negative_array(self):
        test_negative_array = open("NegativeTest.txt", 'r').read().split('\n')
        return test_negative_array

    # Load test positive reviews
    def get_test_positive_array(self):
        test_positive_array = open("PositiveTest.txt", 'r').read().split('\n')
        return test_positive_array

    def get_arabic_sw(self):
        with open("arabic_sw", "r") as myfile:
             arabic_sw = myfile.read()
        return arabic_sw

    def get_training_array(self):
        training_array = []
        for review in self.get_positive_reviews(self):
            training_array.append((review, 'pos'))
        for review in self.get_negative_reviews(self):
            training_array.append((review, 'neg'))
        return training_array

    def get_positive_reviews_without_sw(self):
        positive_array_without_sw=[]
        for review in self.get_positive_reviews(self):
            review_words = nltk.word_tokenize(review)
            review_words_without_sw = [i for i in review_words if not i in self.get_arabic_sw(self)]
            positive_array_without_sw.append(" ".join(str(x) for x in review_words_without_sw))
        return positive_array_without_sw

    def get_negative_reviews_without_sw(self):
        negative_array_without_sw=[]
        for review in self.get_negative_reviews(self):
            review_words = nltk.word_tokenize(review)
            review_words_without_sw = [i for i in review_words if not i in self.get_arabic_sw(self)]
            negative_array_without_sw.append(" ".join(str(x) for x in review_words_without_sw))
        return negative_array_without_sw

    def get_training_array_without_sw(self):
        training_array_without_sw = []
        for review in self.get_positive_reviews_without_sw(self):
            training_array_without_sw.append((review, 'pos'))
        for review in self.get_negative_reviews_without_sw(self):
            training_array_without_sw.append((review, 'neg'))
        return training_array_without_sw

    def get_test_positive_array_without_sw(self):
        test_positive_array_without_sw=[]
        for review in self.get_test_positive_array(self):
            review_words = nltk.word_tokenize(review)
            review_words_without_sw = [i for i in review_words if not i in self.get_arabic_sw(self)]
            test_positive_array_without_sw.append(" ".join(str(x) for x in review_words_without_sw))
        return test_positive_array_without_sw

    def get_test_negative_array_without_sw(self):
        test_negative_array_without_sw = []
        for review in self.get_test_negative_array(self):
            review_words = nltk.word_tokenize(review)
            review_words_without_sw = [i for i in review_words if not i in self.get_arabic_sw(self)]
            test_negative_array_without_sw.append(" ".join(str(x) for x in review_words_without_sw))
        return test_negative_array_without_sw

    def get_test_array(self):
        test_array = []
        for review in self.get_test_positive_array(self):
            test_array.append((review, 'pos'))
        for review in self.get_test_negative_array(self):
            test_array.append((review, 'neg'))
        return test_array

    def get_test_array_without_sw(self):
        test_array_without_sw=[]
        for review in self.get_test_positive_array_without_sw(self):
            test_array_without_sw.append((review, 'pos'))
        for review in self.get_test_negative_array_without_sw(self):
            test_array_without_sw.append((review, 'neg'))
        return test_array_without_sw

    def get_positive_reviews_stemmed_without_sw(self):
        positive_array_stemmed_without_sw = []
        stemmer = ISRIStemmer()
        for review in self.get_positive_reviews(self):
            review_words_stemmed_without_sw=[]
            review_words = nltk.word_tokenize(review)
            review_words_without_sw = [i for i in review_words if not i in self.get_arabic_sw(self)]
            review_words_stemmed_without_sw=[]
            for word in review_words_without_sw:
                review_words_stemmed_without_sw .append(stemmer.stem(word))
            positive_array_stemmed_without_sw.append(" ".join(str(x) for x in review_words_stemmed_without_sw))
        return positive_array_stemmed_without_sw

    def get_negative_reviews_stemmed_without_sw(self):
        stemmer = ISRIStemmer()
        negative_array_stemmed_without_sw=[]
        for review in self.get_negative_reviews(self):
            review_words_stemmed_without_sw = []
            review_words = nltk.word_tokenize(review)
            review_words_without_sw = [i for i in review_words if not i in self.get_arabic_sw(self)]
            review_words_stemmed_without_sw
            for word in review_words_without_sw:
                review_words_stemmed_without_sw .append(stemmer.stem(word))
            negative_array_stemmed_without_sw.append(" ".join(str(x) for x in review_words_stemmed_without_sw))
        return negative_array_stemmed_without_sw

    def get_training_array_stemmed_without_sw(self):
        stemmer = ISRIStemmer()
        training_array_stemmed_without_sw = []
        for review in self.get_positive_reviews_stemmed_without_sw(self):
            training_array_stemmed_without_sw.append((review, 'pos'))
        for review in self.get_negative_reviews_stemmed_without_sw(self):
            training_array_stemmed_without_sw.append((review, 'neg'))
        return training_array_stemmed_without_sw

    def get_test_positive_array_stemmed_without_sw(self):
        stemmer = ISRIStemmer()
        test_positive_array_stemmed_without_sw=[]
        review_words_stemmed_without_sw=[]
        for review in self.get_test_positive_array(self):
            review_words = nltk.word_tokenize(review)
            review_words_without_sw = [i for i in review_words if not i in self.get_arabic_sw(self)]
            review_words_stemmed_without_sw = []
            for word in review_words_without_sw:
                review_words_stemmed_without_sw .append(stemmer.stem(word))
            test_positive_array_stemmed_without_sw.append(" ".join(str(x) for x in review_words_stemmed_without_sw))
        return test_positive_array_stemmed_without_sw

    def get_test_negative_array_stemmed_without_sw(self):
        stemmer = ISRIStemmer()
        test_negative_array_stemmed_without_sw = []
        review_words_stemmed_without_sw = []
        for review in self.get_test_negative_array(self):
            review_words = nltk.word_tokenize(review)
            review_words_without_sw = [i for i in review_words if not i in self.get_arabic_sw(self)]
            review_words_stemmed_without_sw = []
            for word in review_words_without_sw:
                review_words_stemmed_without_sw .append(stemmer.stem(word))
            test_negative_array_stemmed_without_sw.append(" ".join(str(x) for x in review_words_stemmed_without_sw))
        return test_negative_array_stemmed_without_sw

    def get_test_array_stemmed_without_sw(self):
        test_array_stemmed_without_sw=[]
        for review in self.get_test_positive_array_stemmed_without_sw(self):
            test_array_stemmed_without_sw.append((review, 'pos'))
        for review in self.get_test_negative_array_stemmed_without_sw(self):
            test_array_stemmed_without_sw.append((review, 'neg'))
        return test_array_stemmed_without_sw
