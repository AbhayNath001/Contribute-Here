import pandas as pd                             #pip install pandas
from sklearn.tree import DecisionTreeRegressor  #pip install sklearn

def Prediction():
    FileName = "USA_Housing.csv"
    FilePath = pd.read_csv(FileName)

    FilePath.columns
    Data = FilePath.dropna(axis=0)
    Y = Data.Price
    Data_Features = ["Avg. Area Income","Avg. Area House Age","Avg. Area Number of Rooms","Avg. Area Number of Bedrooms","Area Population"]
    X = Data[Data_Features]

    Model = DecisionTreeRegressor(random_state=1)
    Model.fit(X,Y)

    print("Predicting the price of random 5 houses\n")
    print("This are the houses\n")
    print(X.head())
    print("Now, predicting the price of houses\n")
    print(Model.predict(X.head()))
    
Prediction()