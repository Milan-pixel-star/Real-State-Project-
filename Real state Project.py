
# In[101]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# In[102]:


df=pd.read_csv("F:\\New folder\\ML\\CSV files\\real_estate_main.csv")
df


# In[103]:


df.info()


# In[104]:


df.shape


# In[105]:


df.isnull().sum()


# In[106]:


df.describe()


# In[107]:


df=df.drop(['S.no'],axis=1)


# In[108]:


df=df.drop(["Rate Per_sq_feet"],axis=1)


# In[109]:


df=df.drop(["carpet_area_sqft"],axis=1)


# In[110]:


df=df.drop(["parking"],axis=1)


# In[111]:


df["property"].fillna("Unknown",inplace=True)


# In[112]:


df["facing"].fillna("Not specified",inplace=True)


# In[113]:


df["ownership"].fillna("Not specified",inplace=True)


# In[114]:


df["overlooking"].fillna("Road",inplace=True)


# In[115]:


df['balcony'].value_counts()


# In[116]:


df["balcony"].median()


# In[117]:


df["balcony"].mean()


# In[118]:


df["balcony"].fillna(2,inplace=True)


# In[119]:


df.isnull().sum()


# In[120]:


df["bedroom"].value_counts()


# In[121]:


df["bathroom"].value_counts()


# In[122]:


df["bathroom"].fillna(2.0,inplace=True)


# In[123]:


df.isnull().sum()


# In[124]:


df["floor"].value_counts()


# In[125]:


df["status"].value_counts()


# In[126]:


df["status"].fillna("Ready to move",inplace=True)


# In[127]:


df.isnull().sum()


# In[128]:


df.shape


# In[129]:


df["Rate_per_sqft"].median()


# In[130]:


df["Rate_per_sqft"].fillna(7631,inplace=True)


# In[131]:


df["total_area"].fillna(df["Price"]/df["Rate_per_sqft"],inplace=True)


# In[132]:


df.isnull().sum()


# In[133]:


df["transaction"].value_counts()


# In[134]:


df["transaction"].fillna("Other",inplace=True)


# In[135]:


df["floor"].fillna("2 out of 4",inplace=True)


# In[136]:


df.isnull().sum()


# In[137]:


df["city"].value_counts()


# In[138]:


houses=df['city'].values
plt.hist(houses,color="orange")
plt.xticks(["Delhi","Gurgaon","Noida","Ghaziabad","Faridabad"])
plt.title("No of houses from different cities")
plt.xlabel("Cities")
plt.ylabel("frequences")
plt.show()


# In[201]:


count=pd.value_counts(df["city"].values)
plt.pie(count,labels=count.index,autopct='%1.1f%%')
plt.title("Distribution of houses by Facing")
plt.show()


# In[139]:


bedroom=df["bedroom"].values
plt.hist(bedroom, bins=range(min(bedroom), max(bedroom) + 2), rwidth=0.8, align='left',color='g')
plt.xticks(range(min(bedroom), max(bedroom) + 1))
plt.title("Bedroom")
plt.xlabel("Number of bedrooms")
plt.ylabel("frequency in data")
plt.show()


# In[140]:


facing=df["facing"].values
count=pd.value_counts(facing)
plt.pie(count,labels=count.index,autopct='%1.1f%%')
plt.title("Distribution of houses by Facing")
plt.show()


# In[141]:


area=df["total_area"].values
price=df["Price"].values

city_color={"Delhi":'r',"Noida":'g',"Gurgaon":'b',"Ghaziabad":'y',"Faridabad":'m'}
cities=df["city"].map(city_color)
for city, color in city_color.items():
    plt.scatter(area[df["city"]==city], price[df["city"]==city], c=color,alpha=0.7, label=city)
plt.legend()
plt.title('Scatter Plot of Total Area vs Price by City')
plt.xlabel("Area of the house")
plt.ylabel("Price of the house")
plt.show()


# In[142]:


plt.bar(bedroom,price,color='g')
plt.title("Price vs Number of bedrooms")
plt.xlabel("Number of bedrooms")
plt.ylabel("Price")
plt.show()


# In[143]:


bath=df["bathroom"]
plt.bar(bath,price,color='r')
plt.title("Price vs Number of bedrooms")
plt.xlabel("Number of bedrooms")
plt.ylabel("Price")
plt.show()


# In[153]:


y=df["total_area"]
x=df["Price"]

plt.plot(x, y)
plt.xlabel("Price of house")  
plt.ylabel("Area of house") 
plt.title("Increase of Price by area") 
plt.show()


# In[161]:


for city in df['city'].unique():
    city_data = df[df['city'] == city]
    plt.plot(df['total_area'], df["Rate_per_sqft"], label=city)

plt.xlabel('Total Area (sq ft)')
plt.ylabel('Price per Square Foot')
plt.title('Price Increase by Area for Different Cities')
plt.legend()
plt.grid(True)
plt.show()


# In[165]:


count=pd.value_counts(df["transaction"].values)
plt.pie(count,labels=count.index,autopct='%1.1f%%')
plt.title("Type of Propert by sale")
plt.show()


# In[174]:


df['overlooking'].value_counts().plot(kind='bar')
plt.xlabel('Overlooking')
plt.ylabel('Count')
plt.title('Overlooking of the type of property')
plt.show()


# In[190]:


df["Price"].max()


# In[192]:


df["Price"].min()


# In[193]:


df1=pd.read_csv('F:\\New folder\\ML\\CSV files\\property_data.csv')


# In[194]:


df1


# In[196]:


df1.describe()


# In[197]:


df1.info()


# In[198]:


df1.isnull().sum()


# In[203]:


count=pd.value_counts(df1["city"].values)
plt.pie(count,labels=count.index,autopct='%1.1f%%')
plt.title("Distribution of houses by Facing")
plt.show()


# In[209]:


combined_counts = pd.concat([df["city"].value_counts(), df1["city"].value_counts()], axis=1)
combined_counts.columns = ["Supply", "Demand"]
combined_counts.plot(kind="bar", figsize=(10, 6))
plt.xlabel("City")
plt.ylabel("Count")
plt.title("Comparison of House Distribution by city demand")
plt.legend(title="Datasets", loc="upper right")
plt.show()


# In[210]:


combined_counts = pd.concat([df["facing"].value_counts(), df1["facing"].value_counts()], axis=1)
combined_counts.columns = ["Supply", "Demand"]
combined_counts.plot(kind="bar", figsize=(10, 6))
plt.xlabel("facing")
plt.ylabel("Count")
plt.title("Comparison of House Distribution by Facing")
plt.legend(title="Datasets", loc="upper right")
plt.show()


# In[213]:


df1["min-price"].min()


# In[214]:


df1["max-price"].min()


# In[215]:


df1["min-price"].max()


# In[216]:


df1["max-price"].max()


# ## A customer wants th 3BHK with balcony

# In[226]:


ans=df.filter(["bedroom", "bathroom", "balcony"]) 


# In[230]:


ans.astype(int)


# In[246]:


ans["Name"]=df["Name"]
ans["Price"]=df["Price"]
ans["area"]=df["total_area"]
ans["Rate_per_sqft"]=df["Rate_per_sqft"]


# In[ ]:





# In[235]:





# In[247]:


a=ans[(ans["bedroom"]==3) & (ans["bathroom"]==3) & (ans["balcony"]==1)]
a


# ## Now customer says his budget is 25000000 Rs and area upto 4000 sqft

# In[249]:


a["area"]=a["area"].astype(int)
a


# In[258]:


on_price = a[(a["Price"] <= 25000000) & (a["area"] <= 4000)]
on_price


# In[ ]:





# In[ ]:




