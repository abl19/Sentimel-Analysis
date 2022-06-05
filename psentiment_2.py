
from sklearn.feature_extraction.text import CountVectorize
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.base import TransformerMixin
from sklearn.svm import LinearSVC 
from sklearn.pipeline import Pipeline

text="Hello my name is james"
count_vect=CountVectorize()
count_matrix=count_vect.fit_transform(text)
count_array=count_matrix.toarray()
df=pd.DataFrame(data=count_array)
print(df)    