import  bayes as by

#used to train the model, supervised learning, comment and review
#neg for negative review, all words inside the comment will be labeled negative
#then the frequency of the word appearing in positive or negative comment is calculated
#for a new comment, the individual frequency is added up and compare
#if there are more negative keywords than positive then the new comment is negative
post_comments_with_labels = [
    ("I love this post.", "pos"),
    ("This post is your best work.", "pos"),
    ("I really liked this post.", "pos"),
    ('I agree 100 percent. This is true', 'pos'),
    ("This post is spot on!", "pos"),
    ("So smart!", "pos"),
    ("What a good point!", "pos"),
    ("Bad stuff.", "neg"),
    ("I hate this.", "neg"),
    ("This post is horrible.", "neg"),
    ("I really disliked this post.", "neg"),
    ("What a waste of time.", "neg"),
    ("I do not agree with this post.", "neg"),
    ("I can't believe you would post this.", "neg"),
]
new_comment = "Love this post"
cl = by.NaiveBayesClassifier(post_comments_with_labels)

result = cl.classify(new_comment)

print(result)