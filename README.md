# prediction-validation
Jialu You

1. [Programming Language](README.md#programming-language)
1. [Approach Summary](README.md#approach-summary)
1. [Edge Cases](README.md#edge-cases)
1. [Notes](README.md#notes)


## Programming Language

This project is written in Python without using additional libraries.

## Approach Summary

1. Cross reference actual data and predicted data:

I first import the two datasets as two lists of lists, with each line containing variables of "Time", "Time + Stock Name", and "Price", and then store each variable as a list. The defined variable `tstock` is a list of concatenated strings of "Time + Stock Name" to cross reference the two datasets more conveniently. For instance, `actual_tstock = ['1EDMMCA', '1AMDDPW', '1YZSGPL', '1CCKENL' ...]`.

I then pair predicted `pred_tstock` and predicted price into a dictionary called `pred_tstock_dict` instead of a list to reduce complexity, and store their orders in a variable called `ind_dict`, which captures the index of each pair of key/value in the predicted dictionary. To cross reference actual data and predicted data, I run through the `actual_tstock` and pair each stock at different time its corresponding predicted price and absolute error (if any). And if the `actual_tstock` is not in the `pred_tstock_dict`, the predicted price and absolute will be noted as "no data present" and "ignore" respectively.

2. Calculate average error over a sliding time window:

To obtain the `average error` by calculating the average difference between the actual stock prices and predicted values over a specified sliding time window, I decide to run through all possible time windows and average all the absolute errors in that window. Therefore, I built up a while loop starting from the min predicted time till all possible time windows. The number of possible windows can be calculated as `# of windows = max actual time - min actual time - window + 2`.

Denote that `i = min actual time -1` (since the ith object of a list has the index of i-1). And the condition an absolute error must satisfy to be in the ith window is that: `(time-1-i)//window == 0`. Specifically:

```
Suppose window = 3
Time:                                 1  1  1 | 2 2 2 3 3 3 | 4 4 4   5 5 5 6 6 6 | 7 7 7 ...
Expected parameter for window 1:      0  0  0 | 0 0 0 0 0 0 | 1 1 1   1 1 1 1 1 1 | 2 2 2 ...
Expected parameter for window 2:     -1 -1 -1 | 0 0 0 0 0 0   0 0 0 | 1 1 1 1 1 1   1 1 1 | 2 2 2 ...
...
Time//window:                         0  0  0   0 0 0 1 1 1   1 1 1   1 1 1 2 2 2   2 2 2 ...
(time-1-i)//window for window 1:      0  0  0 | 0 0 0 0 0 0 | 1 1 1   1 1 1 1 1 1 | 2 2 2 ... (i = 0)
(time-1-i)//window for window 2:     -1 -1 -1 | 0 0 0 0 0 0   0 0 0 | 1 1 1 1 1 1   1 1 1 | 2 2 2 ... (i = 1)
...
```

In this way, I obtain the `average error` by calculating the average difference between the actual stock prices and predicted values in each specified sliding time window. Finally I produce the following output file `comparison.txt`: A time-ordered file containing the average error of stock predictions for a certain time period.


## Edge cases

1. The start time may not always be 1 for every cases. Therefore, the number of windows is `# of windows = max actual time - min actual time - window + 2` instead of `# of windows = max actual time - window + 1`. Designed test_2 in test suite covers this case.
2. There might be missing window in predicted data, since it contains only **high confidence predictions**. When I am not able to find a match between stock and price for a given window, I output "NA" to be the average error. Designed test_3 in test suite covers this case.

## Notes

I first approached to this project using library `pandas`. But then I was informed that your team has a strong preference on completing it without additional libraries. I will comment my codes with pandas in the `prediction-validation.py` file just for your reference in case.

Thank you so much for reviewing my work and best wishes!
