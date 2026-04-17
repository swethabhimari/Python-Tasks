import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps=np.array([28,30,32,35,33,31,29])
days=["Mon","Tue","wed","Thu","Fri","Sat","Sun"]

df=pd.DataFrame({"Day":days,"Temp":temps})
print(df)

#line
plt.plot(days,temps,marker='o')
plt.title("Temperature Trend")
plt.show()

#bar 
plt.bar(days,temps)
plt.title("Day-wise Temp")
plt.show()

#pie
labels=["High","Low"]
counts=[sum(temps>30),sum(temps<=30)]
plt.pie(counts,labels=labels,autopct='%1.1f%%')
plt.title("High vs Low Temp")
plt.show()

#hist
plt.hist(temps,bins=5)
plt.title("Temp Distribution")
plt.show()

#scatterplot
plt.scatter(temps,days)
plt.title("Index vs Temp")
plt.show()