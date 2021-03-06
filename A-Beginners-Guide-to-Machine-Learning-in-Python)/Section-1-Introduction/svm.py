# import Libraries
import pandas as pd
from sklearn import svm

# load data and splitting
data = pd.read_csv("spambase/spambase.data")
data = data.sample(frac=1)


x = data.drop(['1'], axis=1)
y = pd.DataFrame(data, columns=['1'])
# prepare and fit the model
model = svm.SVC()
model.fit(x, y)
accuracy =model.score(x,y)
print(accuracy)
