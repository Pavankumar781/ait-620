

"""

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
"""
import pandas as pd

file_url="https://raw.githubusercontent.com/PacktWorkshops/The-Applied-Artificial-Intelligence-Workshop/refs/heads/master/Datasets/Sales_Transactions_Dataset_Weekly.csv"

df = pd.read_csv(file_url)

print(df.head())

# Droping first 55 columns
cols_55 = df.columns[:55]

new_df = df.drop(columns=cols_55)

# Columns after dropping
print(new_df.head())

from sklearn.cluster import KMeans
k_means_model = KMeans(n_clusters=8,random_state=8)
print(k_means_model.fit(new_df))

centers = k_means_model.cluster_centers_
print(centers)

labels = k_means_model.labels_
print(labels)

w_cols = df.columns[52:]
df.drop(columns=w_cols, inplace=True)
df.drop(columns=['Product_Code'], inplace=True)
df['label'] = labels
print(df.head())

df_ag_lb = df.groupby('label').sum()
print(df_ag_lb)

df_result = df[['label','W0']].groupby('label').count()
df_result=df_result.rename(columns = {'W0':'count_product'})
df_result['total_sales'] = df_ag_lb.sum(axis = 1)
df_result['yearly_average_sales']= df_result['total_sales'] / df_result['count_product']
df_result.sort_values(by='yearly_average_sales', ascending=False, inplace = True)

print(df_result)