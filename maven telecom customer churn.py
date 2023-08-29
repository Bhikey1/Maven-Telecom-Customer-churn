"""RECOMMENDED ANALYSIS 
1. How many customers joined the company during the last quarter? How many customers joined?
2. What is the customer profile for a customer that churned, joined, and stayed? Are they different?
3. What seems to be the key driver for customer churn?
4. Is the company losing high value customers? If so, how can they retain them?
"""
import numpy as np
import pandas as pd
df = pd.read_csv('telecom_customer_churn.csv')
df.head()
  Customer ID  Gender  ...   Churn Category                   Churn Reason
0  0002-ORFBO  Female  ...              NaN                            NaN
1  0003-MKNFE    Male  ...              NaN                            NaN
2  0004-TLHLJ    Male  ...       Competitor  Competitor had better devices
3  0011-IGKFF    Male  ...  Dissatisfaction        Product dissatisfaction
4  0013-EXCHZ  Female  ...  Dissatisfaction            Network reliability

[5 rows x 38 columns]
df.isnull().sum()
Customer ID                             0
Gender                                  0
Age                                     0
Married                                 0
Number of Dependents                    0
City                                    0
Zip Code                                0
Latitude                                0
Longitude                               0
Number of Referrals                     0
Tenure in Months                        0
Offer                                3877
Phone Service                           0
Avg Monthly Long Distance Charges     682
Multiple Lines                        682
Internet Service                        0
Internet Type                        1526
Avg Monthly GB Download              1526
Online Security                      1526
Online Backup                        1526
Device Protection Plan               1526
Premium Tech Support                 1526
Streaming TV                         1526
Streaming Movies                     1526
Streaming Music                      1526
Unlimited Data                       1526
Contract                                0
Paperless Billing                       0
Payment Method                          0
Monthly Charge                          0
Total Charges                           0
Total Refunds                           0
Total Extra Data Charges                0
Total Long Distance Charges             0
Total Revenue                           0
Customer Status                         0
Churn Category                       5174
Churn Reason                         5174
dtype: int64
# Checking for duplicates
df.duplicated().sum()
0
# Checking for the amount of customers that joined the company in the last quarter
customer_added = df[df['Customer Status'] == 'Joined']
customer_added = customer_added['Customer ID'].count()
customer_added
454
# Checking for churned customers' profile
churned_customer = df[df['Customer Status'] == 'Churned']
churned_profile = churned_customer.groupby(['Offer', 'Internet Type', 'Contract'])['Customer ID'].count()
churned_profile
Offer    Internet Type  Contract      
Offer A  Cable          Month-to-Month      1
                        One Year            1
                        Two Year            1
         DSL            One Year            2
                        Two Year            1
         Fiber Optic    Month-to-Month      5
                        One Year           11
                        Two Year           13
Offer B  Cable          Month-to-Month      4
                        One Year            7
         DSL            Month-to-Month      6
                        One Year            4
                        Two Year            3
         Fiber Optic    Month-to-Month     43
                        One Year           28
                        Two Year            2
Offer C  Cable          Month-to-Month      6
                        One Year            2
         DSL            Month-to-Month      6
                        One Year            3
         Fiber Optic    Month-to-Month     71
                        One Year            5
Offer D  Cable          Month-to-Month     13
                        One Year            3
         DSL            Month-to-Month     22
                        One Year            1
         Fiber Optic    Month-to-Month    111
                        One Year            1
Offer E  Cable          Month-to-Month     54
         DSL            Month-to-Month     89
                        One Year            2
         Fiber Optic    Month-to-Month    236
Name: Customer ID, dtype: int64
# Checking for joined customers' profile
joined_customer = df[df['Customer Status'] == 'Joined']
joined_profile = joined_customer.groupby(['Offer', 'Internet Type', 'Contract'])['Customer ID'].count()
joined_profile
Offer    Internet Type  Contract      
Offer E  Cable          Month-to-Month    21
                        One Year           2
         DSL            Month-to-Month    49
                        One Year           1
                        Two Year           5
         Fiber Optic    Month-to-Month    29
                        One Year           3
                        Two Year           6
Name: Customer ID, dtype: int64
# Checking for stayed customers' profile
stayed_customer = df[df['Customer Status'] == 'Stayed']
stayed_profile = stayed_customer.groupby(['Offer', 'Internet Type', 'Contract'])['Customer ID'].count()
stayed_profile
Offer    Internet Type  Contract      
Offer A  Cable          One Year           12
                        Two Year           53
         DSL            One Year           17
                        Two Year          108
         Fiber Optic    Month-to-Month      9
                        One Year           47
                        Two Year          147
Offer B  Cable          Month-to-Month     14
                        One Year           33
                        Two Year           34
         DSL            Month-to-Month     35
                        One Year           72
                        Two Year           71
         Fiber Optic    Month-to-Month    110
                        One Year          133
                        Two Year           63
Offer C  Cable          Month-to-Month     21
                        One Year           17
                        Two Year            5
         DSL            Month-to-Month     28
                        One Year           37
                        Two Year           14
         Fiber Optic    Month-to-Month     56
                        One Year           40
                        Two Year           23
Offer D  Cable          Month-to-Month     28
                        One Year            8
                        Two Year            5
         DSL            Month-to-Month     88
                        One Year           27
                        Two Year            5
         Fiber Optic    Month-to-Month    100
                        One Year           14
                        Two Year           11
Offer E  Cable          Month-to-Month     29
                        One Year            2
                        Two Year            3
         DSL            Month-to-Month     37
                        One Year            5
                        Two Year            5
         Fiber Optic    Month-to-Month     39
                        One Year            8
                        Two Year            7
Name: Customer ID, dtype: int64
churned_profile.to_csv('churned profile.txt')
joined_profile.to_csv('joined profile.txt')
stayed_profile.to_csv('stayed profile.txt')

# Checking for key drivers of customer churn
churn_driver = churned_customer.groupby(['Churn Category', 'Churn Reason'])['Customer ID'].count()
churn_driver
Churn Category   Churn Reason                             
Attitude         Attitude of service provider                  94
                 Attitude of support person                   220
Competitor       Competitor had better devices                313
                 Competitor made better offer                 311
                 Competitor offered higher download speeds    100
                 Competitor offered more data                 117
Dissatisfaction  Lack of self-service on Website               29
                 Limited range of services                     37
                 Network reliability                           72
                 Poor expertise of online support              31
                 Poor expertise of phone support               12
                 Product dissatisfaction                       77
                 Service dissatisfaction                       63
Other            Deceased                                       6
                 Don't know                                   130
                 Moved                                         46
Price            Extra data charges                            39
                 Lack of affordable download/upload speed      30
                 Long distance charges                         64
                 Price too high                                78
Name: Customer ID, dtype: int64
>>> churn_driver.to_csv('churn driver.txt')
#Checking for high value customers 
>>> high_value_customer = df[df['Tenure in Months'] > 3]
>>> high_value_customer
     Customer ID  Gender  ...   Churn Category                   Churn Reason
0     0002-ORFBO  Female  ...              NaN                            NaN
1     0003-MKNFE    Male  ...              NaN                            NaN
2     0004-TLHLJ    Male  ...       Competitor  Competitor had better devices
3     0011-IGKFF    Male  ...  Dissatisfaction        Product dissatisfaction
5     0013-MHZWF  Female  ...              NaN                            NaN
...          ...     ...  ...              ...                            ...
7037  9986-BONCE  Female  ...       Competitor   Competitor made better offer
7038  9987-LUTYD  Female  ...              NaN                            NaN
7039  9992-RRAMN    Male  ...  Dissatisfaction        Product dissatisfaction
7041  9993-LHIEB    Male  ...              NaN                            NaN
7042  9995-HOTOH    Male  ...              NaN                            NaN

[5992 rows x 38 columns]
# Checking if the comapany lost high value customers 
>>> high_value_customer['Customer Status'].value_counts()
Customer Status
Stayed     4720
Churned    1272
Name: count, dtype: int64
>>> high_value_customer['Customer Status'].value_counts(normalize=True)
Customer Status
Stayed     0.787717
Churned    0.212283
Name: proportion, dtype: float64

""" CONCLUSIONS
1. 454 customers were added during the last quarter.
2. Churned customer profile: Churned customers used Offer E the most, then Offer D and B. Also, they used Month-to-Month contract.
   Joined customer profile: Joined customers used only Offer E and mostly Month-to-Month contract.
   Stayed customer profile: Customers that stayed used Offer A, B, C, D and all the contracts: Two Year, One Year, Month-to-Month.
   There is similarity between the offers and contracts used by joined and churned customers, they both used Offer E and Month-to-Month contracts.
   While stayed customers' profile is different because they used mostly Offer A, B, C, D in combination with all contracts.
3. The key drivers of customer churn are competitors; they have better devices, made better offers, offered
   more data, and more download speed. Also, attitude of support person and service provider.
4. The company lost a little above 21 percent of high value customers. They can be retained by offering better offers such as Offer A, B, C, D,
   offering better devices, data and invreasing download speed. Furthermore, new customers should be offered other Offers and contracts except Offer E
   and Month-to-Month respectively.
"""
