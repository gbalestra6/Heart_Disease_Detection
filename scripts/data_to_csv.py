import pandas as pd
import numpy as np
import os

cleveland_path = os.path.join('../data','cleveland.data')
hungarian_path = os.path.join('../data','hungarian.data')
switzerland_path = os.path.join('../data','switzerland.data')
long_beach_path = os.path.join('../data','long-beach-va.data')
cleveland_data = open(cleveland_path,'r')
cleveland_data = cleveland_data.read()
cleveland_data = np.array(cleveland_data.split())
hungarian_data = open(hungarian_path,'r')
hungarian_data = hungarian_data.read()
hungarian_data = np.array(hungarian_data.split())
switzerland_data = open(switzerland_path,'r')
switzerland_data = switzerland_data.read()
switzerland_data = np.array(switzerland_data.split())
long_beach_data = open(long_beach_path,'r')
long_beach_data = long_beach_data.read()
long_beach_data = np.array(long_beach_data.split())
num_cols = 76
num_cleveland_rows = int(cleveland_data.shape[0]/num_cols)
print("cleveland rows: " + str(num_cleveland_rows))
cleveland_data = np.reshape(cleveland_data,(num_cleveland_rows,num_cols))
num_hungarian_rows = int(hungarian_data.shape[0]/num_cols)
print("hungarian rows: " + str(num_cleveland_rows))
hungarian_data = np.reshape(hungarian_data,(num_hungarian_rows,num_cols))
num_switzerland_rows = int(switzerland_data.shape[0]/num_cols)
print("switzerland rows: " + str(num_cleveland_rows))
switzerland_data = np.reshape(switzerland_data,(num_switzerland_rows,num_cols))
num_long_beach_rows = int(long_beach_data.shape[0]/num_cols)
print("long beach rows: " + str(num_long_beach_rows))
long_beach_data = np.reshape(long_beach_data,(num_long_beach_rows,num_cols))
all_data = np.concatenate([cleveland_data,hungarian_data,switzerland_data,long_beach_data])
print("all rows: " + str(all_data.shape[0]))
indices=['id','ccf','age','sex','painloc','painexer','relrest','pncaden','cp',
'trestbps','htn','chol','smoke','cigs','years','fbs','dm','famhist','restecg',
'ekgmo','ekgday','ekgyr','dig','prop','nitr','pro','diuretic','proto','thaldur',
'thaltime','met','thalach','thalrest','tpeakbps','tpeakbpd','dummy','trestbpd',
'exang','xhypo','oldpeak','slope','rldv5','rldv5e','ca','restckm','exerckm',
'restef','restwm','exeref','exerwm','thal','thalsev','thalpul','earlobe',
'cmo','cday','cyr','num','lmt','ladprox','laddist','diag','cxmain','ramus',
'om1','om2','rcaprox','rcadist','lvx1','lvx2','lvx3','lvx4','lvf','cathef',
'junk','name']
all_data = pd.DataFrame(all_data,columns=indices)

#drop dummy/unused/'irrelevant' columns 
all_data = all_data.drop(columns=['id','ccf','dummy','restckm',
	'exerckm', 'thalsev', 'thalpul','earlobe','lvx1','lvx2','lvx3','lvx4',
	'lvf','cathef','junk','name'])


for column in all_data.columns:
    if(all_data[column].tolist().count("-9") > 100):
        all_data = all_data.drop(columns=column)


for column in all_data.columns:
    all_data = all_data[all_data[column]!="-9"]



csv_file = open(os.path.join('../data','data.csv'),'w+')
all_data.to_csv(csv_file,index=False)
