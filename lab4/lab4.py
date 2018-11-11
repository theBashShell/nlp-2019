from sklearn.feature_extraction.text import CountVectorizer

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

# print(features);
# print(vectorizer);

