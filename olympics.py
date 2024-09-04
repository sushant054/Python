# How many total countries are listed in the table?
# How many golds, silver and bronze have India won?
# Plot a boxplot of ages of all athletes. Same for India.
# What is the median and mean ages of the male and female athelets
# Plot the ratio of male:female athletes for each Olympic

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('olympics.csv')

with open('output.txt', 'w') as output_file:

    # 1. Total number of countries listed
    total_countries = df['noc'].nunique()
    output_file.write(f"Total countries listed: {total_countries}\n")

    # 2. Gold, Silver, and Bronze Medals Won by India
    india_medals = df[df['team'] == 'India']['medal'].value_counts()
    gold_count = india_medals.get('Gold', 0)
    silver_count = india_medals.get('Silver', 0)
    bronze_count = india_medals.get('Bronze', 0)
    output_file.write(f"India has won {gold_count} Gold, {silver_count} Silver, and {bronze_count} Bronze medals.\n")

    # 3. Median and Mean Ages of Male and Female Athletes
    median_ages = df.groupby('sex')['age'].median()
    mean_ages = df.groupby('sex')['age'].mean()

    output_file.write("\nMedian Ages of Athletes by Gender:\n")
    output_file.write(median_ages.to_string())
    output_file.write("\n\nMean Ages of Athletes by Gender:\n")
    output_file.write(mean_ages.to_string())

# 4. Boxplot of Ages of All Athletes
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['age'])
plt.title('Boxplot of Ages of All Athletes')
plt.xlabel('Age')
plt.savefig('boxplot_all_athletes.png')  # Save plot as an image

# Boxplot for Indian Athletes
plt.figure(figsize=(8, 6))
sns.boxplot(x=df[df['team'] == 'India']['age'])
plt.title('Boxplot of Ages of Indian Athletes')
plt.xlabel('Age')
plt.savefig('boxplot_indian_athletes.png')  # Save plot as an image

# 5. Ratio of Male to Female Athletes for Each Olympic
athlete_counts = df.groupby(['year', 'sex']).size().unstack(fill_value=0)
athlete_counts['Ratio'] = athlete_counts['M'] / athlete_counts['F']

# Plotting the ratio of Male to Female Athletes for Each Olympic
plt.figure(figsize=(10, 6))
athlete_counts['Ratio'].plot(kind='bar', color='skyblue')
plt.title('Ratio of Male to Female Athletes for Each Olympic')
plt.ylabel('Male:Female Ratio')
plt.xlabel('Olympic Year')
plt.xticks(rotation=45)
plt.savefig('ratio_male_female_athletes.png')  # Save plot as an image




