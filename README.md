# heart_disease_UCI

## The dataset is taken from Kaggle, url is provided below:
https://www.kaggle.com/ronitf/heart-disease-uci

## Different notebooks and their contents:
### Data_cleaning_visualisation.ipynb
Basic data visualisation using seaborn and feature selection at the end.

### Data_preprocessing.ipynb
Using various techniques to scale the data using min max scaling and standard normalization of the data. Building the model using various algorithms to decide for best accuracy score.

* **RFModel_5_in.pkl**  
The pickled model for later use. (deploymeent)

* **min_max_heart_data**  
The min max scaled csv file

* **std_scaler_heart_data**  
csv file containing data with standard normal distribution with mean=0 and variance=1.

* **app.py**
The flask app module which is to be deployed.

