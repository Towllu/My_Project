import matplotlib.pyplot as plt 

import pandas as pd

import seaborn as sns
df_original = pd.read_csv(r"C:\Users\DELL\Documents\sample_data_matplotlib_seaborn.csv")

df_visual = df_original.copy()

df_visual
df_visual.columns
df_visual.info()
df_visual.describe()
# Line Plot
sns.set_style("darkgrid") # To create dashboard backgoround
plt.plot(df_visual["Year"], df_visual["Sales"], color = "red", marker = "o", linestyle = "--",)
plt.title("Sales over Years")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()
# Bar Chart
plt.Figure(figsize=(8,4))
plt.bar(df_visual["Product"], df_visual["Revenue"], color="orange")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.savefig("bar.png") # to save your chart and it must come first before plt.show()
plt.show()
# Histogram
plt.hist(df_visual["Experience"], color="navy", edgecolor="orange")
plt.title("Experience Distribution")
plt.xlabel("Experience")
plt.ylabel("Frequency")
plt.show()
# Scatter Plot
R = df_visual['Salary'].corr(df_visual['Experience']) # .corr() gives you the R value after correlating.

plt.scatter(df_visual['Salary'], df_visual['Experience'], color="blue")
plt.title(f"Salary vs Experience (R = {R:.2f})")
plt.xlabel("Salary")
plt.ylabel("Experience")
plt.show()
# Pie Chart
# Group by Region and sum Sales
grouped = df_visual.groupby("Region")["Sales"].sum()       # Groups rows by 'Region' and adds up all Sales for each region

# Plot the pie chart
plt.pie(
    grouped,                                 # The values for the pie slices (total sales per region)
    labels=grouped.index,                    # The labels for each slice (the region names)
    autopct="%1.1f%%",
    colors=(["blue", "red", "purple", "green"])                                               # Shows the percentage value on each slice (1 decimal place)
) 
plt.title("Sales by Region")                        
plt.show()

# autopct="%1.1f%%"
# autopct means automatic percentage labeling.

# % → formatting starts

# 1 → minimum number of characters

# .1 → show 1 decimal place

# f → format as a floating-point number

# %% → print a percent sign (escaped %)

# So %1.1f%% means:“Display the slice as a percentage with one decimal place, e.g.:23.4%, 10.0%, 45.9%”
# HeatMap Correlation
corr = df_visual.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
# plt.savefig("tolu.png")  # Saves it in the same folder as your script
plt.show()
# if statement
# Executes code only when 


