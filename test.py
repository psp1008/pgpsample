import pandas as pd
import numpy as np

# Creating a sample DataFrame
data = {
    'assignmentId':[1,1,3,4,5,6,7,8,9,10],
    'marketName': ['Market1', 'Market2', 'Market3', 'Market4', 'Market5', 'Market6', 'Market7', 'Market8', 'Market9', 'Market10'],
    'storeId': np.arange(101, 111),
    'orderType': ['Type1', 'Type2'] * 5,
    'deliveryPriority': np.random.choice(['High', 'Medium', 'Low'], 10),
    'pickResourcePool': ['PoolA', 'PoolB', 'PoolC', 'PoolA', 'PoolB', 'PoolC', 'PoolA', 'PoolB', 'PoolC', 'PoolA'],
    'slotStartTimeEpoch': np.random.randint(1600000000, 1700000000, 10),
    'plannedDistanceInMts': np.random.randint(500, 2000, 10),
    'plannedDurationInSec': np.random.randint(300, 6000, 10),
    'preTipping': np.random.choice([True, False], 10),
    'sumOrderLineItemCount': np.random.randint(1, 20, 10),
    'sumTotalOrderLineCount': np.random.randint(1, 20, 10),
    'start_from_surge': np.random.choice([True, False], 10),
    'PO_NBR': [12,23,24,56,78,67,90,89,56,32],
    'XPRS_TYPE_NM': ['Express', 'Standard', 'Express', 'Standard', 'Express', 'Standard', 'Express', 'Standard', 'Express', 'Standard']
}

df_dt_aos = pd.DataFrame(data)
df_dt_aos.to_csv('df_dt_aos.csv')
print(df_dt_aos)
# Renaming columns
df_dt_aos.rename(columns={
    'assignmentId': 'ASSIGNMENT_ID',
    'marketName': 'MARKET_NAME',
    'storeId': 'STORE_ID',
    'orderType': 'ORDER_TYPE',
    'deliveryPriority': 'DELIVERY_PRIORITY',
    'pickResourcePool': 'PICK_RESOURCE_POOL',
    'slotStartTimeEpoch': 'SLOT_START_TIME_UTC',
    'plannedDistanceInMts': 'PLANNED_DISTANCE_MTS',
    'plannedDurationInSec': 'PLANNED_DURATION_SEC',
    'preTipping': 'PRE_TIPPING',
    'sumOrderLineItemCount': 'SUM_ORDER_LINE_ITEM',
    'sumTotalOrderLineCount': 'SUM_TOTAL_ORDER_LINE',
    'start_from_surge': 'START_FROM_SURGE',
    'PO_NBR': 'PO_NBR',
    'XPRS_TYPE_NM': 'XPRS_TYPE_NM'
}, inplace=True)

# Ensure ASSIGNMENT_ID and PO_NBR are of appropriate data types
grouped_ponbrs = df_dt_aos.groupby('ASSIGNMENT_ID')['PO_NBR'].apply(lambda x : x)
df_dt_aos['PO_NBR'] = df_dt_aos['ASSIGNMENT_ID'].map(grouped_ponbrs)

grouped_XPRS_TYPE_NM = df_dt_aos.groupby('ASSIGNMENT_ID')['XPRS_TYPE_NM'].apply(lambda x : x)
df_dt_aos['XPRS_TYPE_NM'] = df_dt_aos['ASSIGNMENT_ID'].map(grouped_XPRS_TYPE_NM)

# df_dt_aos['PONUMBS'] = df_dt_aos.groupby('ASSIGNMENT_ID')['PO_NBR'].transform(lambda x: list(x))
# print(df_dt_aos[['ASSIGNMENT_ID', 'PO_NBR', 'PONUMBS']])


#df_dt_aos['PONUMBS']=df_dt_aos.groupby('ASSIGNMENT_ID')['PO_NBR'].apply(list)
print(df_dt_aos)

