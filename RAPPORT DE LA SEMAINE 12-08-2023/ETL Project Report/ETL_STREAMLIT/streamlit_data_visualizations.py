
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient
from scipy.stats import norm

# Connect to MongoDB and fetch data
# client = MongoClient("YOUR_CONNECTION_STRING_HERE")
# db = client["your_database_name"]
# clients_df = pd.DataFrame(list(db["clients"].find()))
# drivers_df = pd.DataFrame(list(db["drivers"].find()))
# rides_df = pd.DataFrame(list(db["rides"].find()))
#to do : screenshots of the script with mongodb

# For the sake of this script, we'll use the CSV files
clients_df = pd.read_csv("clients_dataset.csv")
drivers_df = pd.read_csv("drivers_dataset.csv")
rides_df = pd.read_csv("rides_dataset.csv")

# App title
st.title("Analyse des données et visualisations")

# 1. Pie chart for client feedback distribution
st.subheader("Distribution des commentaires des clients")
fig, ax = plt.subplots()
clients_df['feedback'].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
st.pyplot(fig)

# 2. Histogram for driver ratings distribution
st.subheader("Distribution des évaluations des conducteurs")
fig, ax = plt.subplots()
sns.histplot(drivers_df['rating'], bins=20, kde=True, ax=ax, color="skyblue")
st.pyplot(fig)

# 3. Bar graph for average trip duration based on traffic issues
st.subheader("Durée moyenne des trajets en fonction des problèmes de circulation")
fig, ax = plt.subplots()
rides_df.groupby('traffic_issues')['trip_duration'].mean().plot(kind='bar', ax=ax, color=['red', 'green'])
ax.set_xticklabels(['Pas de trafic', 'Trafic'])
st.pyplot(fig)

# 4. Pie chart for distribution of rides based on traffic issues
st.subheader("Distribution des trajets en fonction des problèmes de circulation")
fig, ax = plt.subplots()
rides_df['traffic_issues'].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=140, labels=['Pas de trafic', 'Trafic'], colors=['green', 'red'])
st.pyplot(fig)

# 5. Frequency polygon for distribution of drivers based on years of experience
st.subheader("Distribution des conducteurs en fonction de leurs années d'expérience")
fig, ax = plt.subplots()
sns.histplot(drivers_df['years_of_experience'], bins=10, kde=False, cumulative=False, stat="count", element="step", fill=False, ax=ax, color="blue")
st.pyplot(fig)

# 6. Normal distribution of driver ratings
st.subheader("Distribution normale des évaluations des conducteurs")
fig, ax = plt.subplots()
sns.distplot(drivers_df['rating'], hist=False, fit=norm, ax=ax, color="purple")
st.pyplot(fig)

# 7. Stemplot for trip durations (subset)
st.subheader("Stemplot pour les durées des trajets (échantillon de 50 trajets)")
subset_rides = rides_df.sample(50)
fig, ax = plt.subplots()
ax.stem(subset_rides['trip_duration'], use_line_collection=True)
st.pyplot(fig)

# 8. Time plot for daily average trip duration (fictional)
st.subheader("Durée moyenne quotidienne des trajets sur un mois (fictif)")
rides_df['fictional_day'] = pd.cut(rides_df.index, bins=30, labels=range(1, 31))
daily_avg_durations = rides_df.groupby('fictional_day')['trip_duration'].mean()
fig, ax = plt.subplots()
daily_avg_durations.plot(kind='line', marker='o', ax=ax, color="blue")
st.pyplot(fig)

# 9. Bar graph for driver account status
st.subheader("Statut du compte du conducteur")
fig, ax = plt.subplots()
drivers_df['account_status'].value_counts().plot(kind='bar', ax=ax, color=sns.color_palette("deep", 2))
st.pyplot(fig)

# 10. Histogram for trip durations
st.subheader("Distribution des durées des trajets")
fig, ax = plt.subplots()
sns.histplot(rides_df['trip_duration'], bins=20, ax=ax, color="orange")
st.pyplot(fig)

# 11. Pie chart for driver debt status
st.subheader("Statut de la dette du conducteur")
fig, ax = plt.subplots()
drivers_df['debt_paid'].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=140, labels=['Dette payée', 'Dette non payée'], colors=sns.color_palette("husl", 2))
st.pyplot(fig)

# 12. Bar graph for top 5 preferred areas by clients
st.subheader("5 principales zones préférées par les clients")
fig, ax = plt.subplots()
clients_df['preferred_area'].value_counts().head(5).plot(kind='bar', ax=ax, color=sns.color_palette("muted", 5))
st.pyplot(fig)

# 13. Line graph for driver ratings vs. years of experience
st.subheader("Évaluations des conducteurs vs années d'expérience")
fig, ax = plt.subplots()
drivers_df.groupby('years_of_experience')['rating'].mean().plot(kind='line', marker='o', ax=ax, color="green")
st.pyplot(fig)

# 14. Frequency polygon for client preferred areas
st.subheader("Distribution des zones préférées des clients")
fig, ax = plt.subplots()
areas_count = clients_df['preferred_area'].value_counts()
areas_count.sort_index().plot(kind='line', marker='o', ax=ax, color="purple")
st.pyplot(fig)

# 15. Histogram for drivers' years of experience
st.subheader("Années d'expérience des conducteurs")
fig, ax = plt.subplots()
sns.histplot(drivers_df['years_of_experience'], bins=10, ax=ax, color="pink")
st.pyplot(fig)

