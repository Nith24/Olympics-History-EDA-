import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns

# Load data
df=pd.read_csv(r"D:\Data\NS\Data Analytics\My Projetcs\github\Olympics Dataset\athlete_events.csv")
df.head()


df.info()

df.describe()

df.isnull().any().sum()

df.isnull().sum()

nan_values=df.isna()
nan_cols=nan_values.any()
nan_cols

df.loc[:,'Name'].value_counts()


# Data Analysis

df.columns

df[['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC', 'Games',
       'Year', 'Season', 'City', 'Sport', 'Event', 'Medal']].corr()


df['Year'].value_counts().plot(kind = 'pie',
                                title = 'Age', figsize = (10,10), layout=(20,2))

fig=plt.figure(figsize=(30,15))
sns.countplot('Sport',data=df)
x=plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(80)
    plt.subplots_adjust(bottom=0.25)
plt.show()



# Heatmap

num_df = df.select_dtypes(include=['int64','float64'])
sns.heatmap(num_df.corr(),annot=True);

teams=df.Team.value_counts().sort_values(ascending=False).head(10)
teams

#Barplot

plt.figure(figsize=(10,5))

plt.title("Top countries")
sns.barplot(x=teams.index , y= teams, palette='Set3')

#Boxplot

plt.figure(figsize = (10,6))
sns.boxplot(x = "Season", y = "Height", data = df)
plt.show()


# Pairplot

sns.pairplot(df)
plt.show()

# Pieplot- Gender

df['Sex'].value_counts().plot(kind = 'pie',
                                title = 'Sex', figsize = (5,10), layout=(10,2))


#Pieplot- Medal

df['Medal'].value_counts().plot(kind = 'pie',
                                title = 'MEDAL', figsize = (5,10), layout=(10,2))

# Medal list
medalsT = df_ath.groupby(['Year','Team','Sport','Season'])['Medal'].value_counts() \
                                                                         .to_frame(name='Count') \
                                                                         .reset_index
medalsT


# **********  Data cleaning

for column in df.columns:
    df = df.rename(columns={column: column.lower()})

df

for column in df.columns:
    df = df.rename(columns={column: column.lower()})
    df = df.rename(columns={column: column.replace('.', '_')})

df = df.rename(columns={'City': 'tempo'})

df.columns


