from string import punctuation
from collections import Counter
from collections import defaultdict



class NaiveBayesClassifier:
    def __init__(self, samples):
        self.mapping = {"pos": [], "neg": []}
        self.neg_mapping = defaultdict(lambda: 0)
        self.sample_count = len(samples)
        #record first the review classifier label
        #all words in the given comment has the same label
        for text, label in samples:
            self.mapping[label] += self.tokenize(text)

        #total of positive/negative keywords in the  comments
        self.pos_counter = Counter(self.mapping["pos"])
        self.neg_counter = Counter(self.mapping["neg"])

    @staticmethod
    def tokenize(text):
        return (
            text.lower().translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def classify(self, text):
        tokens = self.tokenize(text)
        pos = []
        neg = []

        #calculate the frequency of each word belonging to positive or negative comment
        #sum up the negative counterpart and the positive then compare
        for token in tokens:
            pos.append(self.pos_counter[token]/ self.sample_count)
            neg.append(self.neg_counter[token]/self.sample_count)
        if sum(pos) == sum(neg):
            return "neutral"
        elif sum(pos) > sum(neg):
            return "pos"
        else:
            return "neg"

        # rerturn "neg", "pos" or "nutral"





