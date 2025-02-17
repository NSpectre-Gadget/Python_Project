# Trading Bot using Machine Learning

## Overview of the Analysis

***

* Purpose:
This is an optimal trading algorithm to assess the risk/reward characteristics, we backtested algorithms, or evaluated an algorithms performance by using historical stock data.


Dataset Window Variation
***
6-mos

                precision    recall  f1-score   support

        -1.0       0.44      0.02      0.04      1732
         1.0       0.56      0.98      0.71      2211

    accuracy                           0.56      3943
   macro avg       0.50      0.50      0.38      3943
weighted avg       0.51      0.56      0.42      3943


                    Predicted	Actual Returns	Strategy Returns
date			
2015-10-05 09:45:00      1.0	0.013532	0.013532
2015-10-05 11:30:00      1.0	0.002302	0.002302
2015-10-05 13:15:00      1.0	-0.000919	-0.000919
2015-10-05 14:30:00      1.0	0.000920	0.000920
2015-10-05 14:45:00      1.0	0.002756	0.002756

                   Predicted	Actual Returns	Strategy Returns
date			
2021-01-22 09:30:00      1.0	-0.006866	-0.006866
2021-01-22 11:30:00      1.0	0.002405	0.002405
2021-01-22 13:45:00      1.0	0.002099	0.002099
2021-01-22 14:30:00      1.0	0.001496	0.001496
2021-01-22 15:45:00      1.0	-0.000896	-0.000896

### 6 mos Screenshot
![6_months](http://localhost:8888/lab/tree/Module_14_Challenge/6mos_predictions_df.png)

3-mos
               precision    recall  f1-score   support

        -1.0       0.43      0.04      0.07      1804
         1.0       0.56      0.96      0.71      2288

    accuracy                           0.55      4092
   macro avg       0.49      0.50      0.39      4092
weighted avg       0.50      0.55      0.43      4092


                        Predicted	Actual Returns	Strategy Returns
date			
2015-07-06 10:00:00          1.0	-0.025715	-0.025715
2015-07-06 10:45:00          1.0	0.007237	0.007237
2015-07-06 14:15:00          1.0	-0.009721	-0.009721
2015-07-06 14:30:00          1.0	-0.003841	-0.003841
2015-07-07 11:30:00          1.0	-0.018423	-0.018423

                       Predicted	Actual Returns	Strategy Returns
date			
2021-01-22 09:30:00          1.0	-0.006866	-0.006866
2021-01-22 11:30:00          1.0	0.002405	0.002405
2021-01-22 13:45:00          1.0	0.002099	0.002099
2021-01-22 14:30:00          1.0	0.001496	0.001496
2021-01-22 15:45:00          1.0	-0.000896	-0.000896

### 3 mos Screenshot
http://localhost:8888/lab/tree/Module_14_Challenge/3mos_predictions_df.png


2-mos
                 precision    recall  f1-score   support

        -1.0       0.39      0.04      0.06      1825
         1.0       0.56      0.96      0.70      2318

    accuracy                           0.55      4143
   macro avg       0.47      0.50      0.38      4143
weighted avg       0.48      0.55      0.42      4143

                       Predicted	Actual Returns	Strategy Returns
date			
2015-06-03 10:00:00          1.0	-0.007226	-0.007226
2015-06-03 10:15:00          1.0	0.002426	0.002426
2015-06-03 10:30:00          1.0	0.000403	0.000403
2015-06-03 10:45:00          1.0	0.000000	0.000000
2015-06-04 12:15:00          1.0	-0.011694	-0.011694

                       Predicted	Actual Returns	Strategy Returns
date			
2021-01-22 09:30:00          1.0	-0.006866	-0.006866
2021-01-22 11:30:00          1.0	0.002405	0.002405
2021-01-22 13:45:00          1.0	0.002099	0.002099
2021-01-22 14:30:00          1.0	0.001496	0.001496
2021-01-22 15:45:00          1.0	-0.000896	-0.000896

### 2 mos Screenshot
 http://localhost:8888/lab/tree/Module_14_Challenge/2mos_predictions_df.png
 



                 precision    recall  f1-score   support

        -1.0       0.44      0.19      0.27      1740
         1.0       0.56      0.81      0.66      2227

    accuracy                           0.54      3967
   macro avg       0.50      0.50      0.47      3967
weighted avg       0.51      0.54      0.49      3967


### SMA VARIATIONS
***
[50-day_sma](http://localhost:8888/lab/tree/Module_14_Challenge/50_day_sma.png)


[20-day_sma](http://localhost:8888/lab/tree/Module_14_Challenge/20_day_sma.png)



