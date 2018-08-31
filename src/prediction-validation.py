#==============================================
#Cross reference actual data and predicted data
#==============================================
actual_list = []
with open('input/actual.txt') as a:
    for line in a:
        #split each line into a list.
        line = line.strip().split("|")
        #append for each row.
        actual_list.append([int(line[0]), line[0]+line[1],float(line[2])])


pred_list = []
with open('input/predicted.txt') as p:
    for line in p:
        #split each line into a list.
        line = line.strip().split("|")
        #append for each row.
        pred_list.append([int(line[0]), line[0]+line[1],float(line[2])])

with open('input/window.txt') as w:
    for line in w:
        window = int(line.strip())

actual_tstock = zip(*actual_list)[1]
actual_time = zip(*actual_list)[0]
actual_price = zip(*actual_list)[2]
pred_tstock = zip(*pred_list)[1]
pred_time = zip(*pred_list)[0]
pred_price = zip(*pred_list)[2]

pred_tstock_dict = {}
for i in range(0,len(pred_tstock)):
    pred_tstock_dict[pred_tstock[i]] = pred_price[i]

ind_dict = dict((k,i) for i,k in enumerate(pred_tstock))

df = actual_list

for i in range(0,len(actual_time)):
    if actual_tstock[i] in pred_tstock_dict:
        pred_pricei = pred_price[ind_dict[actual_tstock[i]]]
        df[i].append(pred_pricei)
        df[i].append(abs(pred_pricei-actual_price[i]))
    else:
        df[i].append("no data present")
        df[i].append("ignore")

#===================================================
#Calculate average error over a sliding time window:
#===================================================
max_time = max(actual_time)
min_time = min(actual_time)
start_time = []
end_time = []
avg_error = []
i = min_time-1
df_time = list(zip(*df)[0])


while i < max_time-window+1:
    bag = [df[j][4] for j in range(0,len(df)) if (df_time[j]-1-i)//window == 0 and df[j][4] != "NA"]
    if len(bag):
        avg_error.append(round(sum(bag)/len(bag),2))
    else:
        avg_error.append('NA')
    start_time.append(int(i+1))
    end_time.append(int(i+window))
    i += 1
lines = ["|".join([str(start_time[i]), str(end_time[i]), str(avg_error[i])]) for i in range(0,len(avg_error))]
with open("output/comparison.txt", 'w') as f:
    f.writelines("%s\n" % l for l in lines)

#============================
#Approach with Pandas Library
#============================



#============
#Import Data
#============
#import pandas as pd
#import numpy as np

#actual = pd.read_csv('input/actual.txt',sep="|" , header = None, names = ["time","stock","price"])
#predicted = pd.read_csv('input/predicted.txt',sep="|" , header = None, names = ["time","stock","pred_price"])
#window = int(open('input/window.txt',"r").read())

#df = pd.merge(actual,predicted, on = ['time','stock'])
#error = abs(df['pred_price']-df['price'])
#df = pd.concat((df,error.rename('error')),axis = 1)

#---------
#Main Code
#---------
#max_time = max(df['time'])
#min_time = min(df['time'])
#start_time = []
#end_time = []
#avg_error = []
#i = min_time-1
#while i < max_time-window+1:
#    bag = df.loc[(df['time']-1-i)//window == 0]
#    if len(bag):
#        avg_error.append(round(np.mean(bag['error']),2))
#    else:
#        avg_error.append('NA')
#    start_time.append(int(i+1))
#    i += 1

#output = pd.DataFrame({'start':start_time})
#output['end'] = end_time
#output['avg_error'] = avg_error


#output.to_csv(r'output/comparison.txt',sep='|', index=False, header=False)
