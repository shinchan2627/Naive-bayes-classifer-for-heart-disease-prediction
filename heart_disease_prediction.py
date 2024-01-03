import pandas as pd 
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#data

df=pd.read_csv('/media/praveenkumar/Ace/intern/help files/traning/heart desiase/heart.csv')


x=df.drop(columns=['target'])
y=df['target']


#data spliting
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)  


#model

from sklearn.naive_bayes import MultinomialNB

NB = MultinomialNB()

NB.fit(x_train, y_train)

#train the data
y_pred=NB.predict(x_test)

#input for model
testPrediction = NB.predict([[45,0,1,136,315,0,1,125,1,1.8,1,0,1]])

#output
if testPrediction==1:
    print("The Patient Have Heart Disease,please consult the Doctor")
else:
    print("The Patient Normal")
