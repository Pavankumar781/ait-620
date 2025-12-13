# 7.1
GitHub URL: https://github.com/Pavankumar781/ait-620/blob/main/week7/assignment7.1.ipynb
week7/assignment7.1.ipynb
https://github.com/Pavankumar781/ait-620/blob/main/week7/assignment7.1.ipynb
# 7.2

Activity 5.01: Clustering Sales Data Using K-Means

In this activity, you will work on the Sales Transaction Dataset Weekly dataset, which contains the weekly sales data of 800 products over 1 year. Our dataset won't contain any information regarding the product except sales.

1. Open a new Jupyter Notebook file.
2. Load the dataset as a DataFrame and inspect the data.
3. Create a new DataFrame without the unnecessary columns using the drop
function from pandas (that is, the first 55 columns of the dataset) and use the
inplace parameter, which is a part of pandas.
4. Create a k-means clustering model with 8 clusters and with
random_state = 8.
5. Retrieve the labels from the first clustering model.

6. From the first DataFrame, df, keep only the W columns and the labels as a
new column.
7. Perform the required aggregation using the groupby function from pandas in
order to obtain the yearly average sale of each cluster.