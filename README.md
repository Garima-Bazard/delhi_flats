# DELHI FLATS PRICE
## WEBAPP LINK : https://garima-bazard-delhi-flats-app-a0vf9p.streamlit.app/
## Description:

### Objective and Dataset Info
The dataset consists of housing properties(Flats) located in Delhi NCR. The dataset was taken from kaggle.
The objective is to create an ML model that can predict the price of a flat given some input parameters.
The dataset was divided into training and testing data in the ratio 8:2 and the model has been trained using the train data and makes predictions for the test data.

### Data Cleaning
Null values were found, coulmns having NaN values greater than 50% were dropped, conseuqently Furnished and few other columns got dropped and as a result no categorical variables were left in the end.
Duplicate rows were dropped from the data.

### Exploratory Data Analysis (EDA), Data preprocessing and Feature Engineering
Sweetviz and manual exploration was done.
The following were observed:
1. There was a correlation between bathrooms and bedrooms, bedrooms had higher correlation with the target, price and thus bathrooms column was dropped from the data.
2. Price has a strong correlation with area and number of bedrooms (same is intuitively concluded).
3.Address was dropped as longitude and latitude columns were available and as such have been taken as feature columns.
4.Columns with low and high cardinality values were droppped from the dataset.
5.Price per sqft column was dropped to avoid leakage in the model.
6.Separated target(price) and predictor variables.
7.Scaled the train and test data using Standard Scaler, however as it was seen later in model building process, it did not add any value to the model and performance for that mattter and subsequently scaled data was not used for training or testing the models.

### Building the Model
1.A baseline model was defined, which predicted the mean as the price for all the flats. This model was built as a benchmark to beat for the forthcoming models and served no purpose other than that.
2.Linear Regression model was built inside a pipeline along with Simple Imputer to impute the missing values in our data. The r2_score for training and testing data was stored in two separate dictionaries.
3.Ridge model was built in a similar fashion to as described above. Scaled and Unscaled data were both trained and tested on this model, but since that did not create significant difference in the predictions, the decision to go with unscaled data for all the models was made.
4.Lasso model was made next and its r2_score values were updated in the dictionary too.
5.RF or Random Forest model was built in a similar way.
6.Decision Tree model was similarly built next.

To be noted, all these models beat the Baseline model.
Next, the r2_score of all the models were compared and RF was found to be the best model with r2_score of ~0.85 and was thus taken as the final model.

### Communicating Results
1.Streamlit was used to deploy an app for communicating the results, sliders are provided for users to give input values to feature variables and RF model predicts the price of flats.
2.Within the notebook too, sliders are provided for giving in input values for the model to make a prediction of the price of Flat.

