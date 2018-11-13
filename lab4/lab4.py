from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression


# open and read file
def open_file(data):
    return open(data, 'r')
    
# assign dataset
file = open_file("test.txt") 
data = [] 
label = []

# assign to categroy
for f in file:                  
    data.append((f[:-3]))
    label.append(f[-2]) 

# normalize dataset
vectorizer = CountVectorizer(
    analyzer='word',
    lowercase=False,
)

# turn into vectors
features = vectorizer.fit_transform(
    data
)

norm_feat = features.toarray()
print(norm_feat)

X_train, X_test, y_train, y_test  = train_test_split(
        norm_feat, 
        label,
        train_size=0.80, 
        random_state=1234)




 
logistic_model = LogisticRegression()
print(logistic_model)
