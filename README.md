# Project 2 - Ames Housing Data and Kaggle Challenge
---
## Problem Statement
1. I was asked by an internet real estate company (like Zillow) to create a simple linear regression model that can predict the market value of real estate in Ames, Iowa as accurately as possible based on the Ames Housing Dataset.
2. To evaluate the performance of my model, we’re going to look at the RMSE and R2 scores achieved by my model compared to a baseline model.

## Executive Summary
I did a preliminary plot of all the features in our dataset to find the strongest predictors of sale price. After some processing, I created 3 models that had RMSE scores of approximately 30,000 and R2 scores of approximately 80%. I believe these models are decent predictors but could be improved by addressing outliers in the data of my selected features, revisiting the complete dataset to find additional features to include in the model, and experimenting with the data to create new features.

## Description of Data
1. The Ames Housing Dataset contains data covering real estate sold between the years of 2007 through 2010 in Ames, Iowa. 
2. It contains 80 different columns covering various characteristics of the property and its sale price, our target variable.

## Feature Selection
1. To start the build of my model, I created a plot of each of the features contained in the dataset against sale price – scatterplots for the numerical features and boxplots for the categorical features.
2. Based on my review of each of these plots, I selected 7 features as the most likely to be the strongest predictors of sale price.
3. Numerical Features
    1. Out of the numerical features, I selected: 
        1. Overall quality, which rates the quality of the material and finish of the property from 1-10, 
        2. The year in which the property was built, and 
        3. The above ground living area of the property in square feet.
    2. These features had a pretty good linear relationship with sale price. 
    3. However, there are a few noticeable outliers, particularly for the above-ground living area feature.
4. Categorical Features
    1. The categorical features I selected were Exterior Quality, Kitchen Quality, Basement Quality and Neighborhood.
    2. The Exterior Quality and Kitchen Quality variables are ordinal in nature, with ratings starting from Poor and increasing to Excellent.
        - Per my boxplots, as the quality rating went up for these categories, the sale price of the properties tends to increase as well.
    3. The Basement Quality rating is also provided on a scale from Poor to Excellent
        - However, per the data dictionary for this dataset, these ratings actually refer to the ceiling height of the basement.
        - Like the other quality variables, as quality or ceiling height in this case increases, the sale price tends to increase too.
    4. Neighborhood
        - I chose this feature due to the clear relationship you can see between a property’s sale price and the neighborhood in which it is located.

## Preprocessing
After selecting the features, I performed some processing to get the data ready for modeling
- I cleaned the data and resolved missing values.
- For the Exterior, Kitchen and Basement Quality variables, I replaced the Poor to Excellent rating with a number rating.
- I created dummy variables for the Neighborhood column.
- I split the data into a training set and a test set, allocating 75% for the training set, and the remaining 25% as a test set.
- And lastly, I scaled the data so that each of the features were comparable in magnitude.

## Modeling
I created 3 different models:
- a linear regression model,
- a ridge model, and
- a lasso model

Then, I compared each of these models against a baseline null model which predicts that the sale price for each property would be equal to the average of all the sale price values.

### Performance of Models

My models performed decently. Each of my models achieved a RMSE score of a little over 30,000, which is considerably below the baseline model score of close to 80,000
On R2 scores, each of my models scored around 80%, which means that 80% of the variability of the data from the baseline model are explained by my models. It’s worth noting here that my linear regression model predicted values just as well on the training set as the test set, so I found that using the models with regularization, ridge and lasso, did not show much improvement over my original linear regression models.

## Conclusion

To conclude, I created models that can predict the market price of real estate in Ames, Iowa, considerably better than the baseline model. However, I do think there’s room for improvement. To increase the accuracy of my model, my next steps would be:
1. Addressing outliers in the data of my selected features
2. Revisiting the complete dataset to find additional features to include in the model; and
3. Experimenting with the data to create new features that may help improve the accuracy of my model.
