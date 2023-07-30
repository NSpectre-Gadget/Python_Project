# Module 12 Report Template

## Overview of the Analysis

In this section, describe the analysis you completed for the machine learning models used in this Challenge. This might include:

* Explain the purpose of the analysis.
This a report to assess loans for their viability. We wanted to consider multiple factors and known past outcomes to make predictions about future outcomes, for determining credit risk. We evaluted credit risk, using historical lending activity from a peer-to-peer lending services company to build a model.  We wanted to know the percentage of predictions that the model gets right and how well it predicts each outcome  Also, we wanted to measure a model’s performance based on the differences between its predicted and its actual values.  We will use past data to develop a predictive model.  Siunce models can learn from their mistakes, we will adjust our model to become even better the next time that it gets data.  This model will be a classification model because we will be dividing loan status on past data into two classes. 

* Explain what financial information the data was on, and what you needed to predict.
Our goal was to evaluate influential data that impacted success of a borrower to payback a loan.  The data included loan size sought, interest rate on the loan, individual's income, individual debt-to-income percentage, how accounts the individual has under their name, whether there are prior derogatory remarks related to the individuals use of money, the amount of debt, and the 

We needed to predict
accuracy = (TPs + TNs) ÷ (TPs + TNs + FPs + FNs)
precision = 

* Provide basic information about the variables you were trying to predict (e.g., `value_counts`).
* Describe the stages of the machine learning process you went through as part of this analysis.
To carry out the machine learning process, we needed to preprocess the data.  We ininitally imported all of our libraries that contained relevant modules and dependicies that related to reading in the data, splitting the data before we 

Fit a logistic regression model, establish or train our model off of the data that we prepared for the machine learning environment.  This is the stage where the model learns what we would like for it carry out. The model starts to learn how to adjust (trains) itself to make predictions matching the data.

Make predictions
Similar to a student-training acquiring skills to apply to employment, this model trained to apply the newly formed tool to new data that’s similar to prior (training) data. Ultimately, we will see how well it predicts the outcome for that data.

Evaluate the model
After using the model-fit-predict pattern, we evaluated how well the model makes its predictions, by using the confusion_matrix module from scikit-learn.  We used the predicted values and calculated a confusion matrix.  By formulating a confusion matrix we were able to determine the ** accuracy_score ** function to calculate the accuracy of our model predictions for the testing data, i.e. how many it got right; ** precision  **, i.e. the positive predictive value (PPV) - to measure how confident we are that the model correctly made the positive predictions; and, ** recall ** measures the number of actually fraudulent transactions that the model correctly classified as fraudulent, using the formulas found below:

* Briefly touch on any methods you used (e.g., `LogisticRegression`, or any resampling method).

To oversample the data, we use a new library named imbalanced-learn. Within the inbalanced-learn library, we used the RandomOverSampler function to oversample the data.  Therefore, we instantiated the data using the random_oversampler acquiring resampled data via the fit_resample function, i.e. created an object instance for more balanced data where we chose the previously underrepresented class multiple times to increase the number of times that the model gets it during training

The results 
## Results

Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all machine learning models.

* Machine Learning Model 1:
  * Description of Model 1 Accuracy, Precision, and Recall scores.
 
 Our model predicting a transaction as fraudulent is considered to be a True Positive (TP).
 Selecting a non-fraudulent as fraudulent is considered to be a False Positive (FP).
 Similarly, our model predicting a transaction as not fraudulent that was actually not fraudulent is a True Negative (TN).
 Selecting a fraudulent as non-fraudulent is considered to be a False Negative (FN).
 
Once our confusion matrix provided us with the data, we were able to ascertain the following scores for accuracy, precision, and recall, by applying the classification report which utilized the following equations:

accuracy = (TPs + TNs) ÷ (TPs + TNs + FPs + FNs)
  
precision = TPs ÷ (TPs + FPs)

recall = TPs / (TPs + FNs)


* Machine Learning Model 2:
  * Description of Model 2 Accuracy, Precision, and Recall scores.



## Summary

Summarize the results of the machine learning models, and include a recommendation on the model to use, if any. For example:
* Which one seems to perform best? How do you know it performs best?  
The resampled data using the RandomOverSampler function performed better than the Logistic Regression function.  We know this because when compare the recall numbers the RandomOverSampler performs slightly better at a 99 percent score instead of the 91 percent recall that we see using the Logistic Regression recall score.

* Does performance depend on the problem we are trying to solve? (For example, is it more important to predict the `1`'s, or predict the `0`'s? )

If you do not recommend any of the models, please justify your reasoning.

I recommend the RandomOverSampler model because the accuracy and recall scores are slightly higher.  Our model performed better on the unhealthy loans, which is of greater importance for the concern that we have regarding determing whether to lend to individuals with greater confidence of success that the loan will be repaid.  