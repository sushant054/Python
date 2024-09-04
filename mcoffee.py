#extended..coffee.py
#plots..

import pandas as pd
import matplotlib.pyplot as plt

file_path = "coffee_survey.csv"  
data = pd.read_csv(file_path)

# Plot 1: Coffee Drinkers by Age Group
plt.figure(figsize=(12, 8))  
data['age'].value_counts().plot(kind='bar')
plt.title('Coffee Drinkers by Age Group')
plt.xlabel('Age')
plt.ylabel('Count')
# Rotate and reduce font size of x-axis labels
plt.xticks(rotation=45, fontsize=8)  
plt.tight_layout() 
plt.show()

# Plot 2: Coffee Brewing Methods
brew_methods = data['brew'].value_counts()
plt.figure(figsize=(12, 8)) 
brew_methods.plot(kind='bar')
plt.title('Coffee Brewing Methods')
plt.xlabel('Brewing Method')
plt.ylabel('Count')
plt.xticks(rotation=45, fontsize=8)  
plt.tight_layout()  
plt.show()

# Plot 3: Favorite Coffee Drinks
favorite_drinks = data['favorite'].value_counts()
# increase figure size
plt.figure(figsize=(12, 8))
favorite_drinks.plot(kind='bar')
plt.title('Favorite Coffee Drinks')
plt.xlabel('Favorite Drink')
plt.ylabel('Count')
plt.xticks(rotation=45, fontsize=8)   
plt.tight_layout()  
plt.show()

# Plot 4: Coffee Purchasing Habits
purchase_habits = data['purchase'].value_counts()
plt.figure(figsize=(12, 8))  
purchase_habits.plot(kind='bar')
plt.title('Coffee Purchasing Habits')
plt.xlabel('Purchasing Habit')
plt.ylabel('Count')
plt.xticks(rotation=45, fontsize=8)  
plt.tight_layout()  
plt.show()

# Plot 5: Coffee Roast Level Preferences
roast_levels = data['roast_level'].value_counts()
plt.figure(figsize=(12, 8))  
roast_levels.plot(kind='bar')
plt.title('Coffee Roast Level Preferences')
plt.xlabel('Roast Level')
plt.ylabel('Count')
plt.xticks(rotation=45, fontsize=8)   
plt.tight_layout()   
plt.show()

# Plot 6: Coffee Strength Preferences
strength_preferences = data['strength'].value_counts()
plt.figure(figsize=(12, 8))   
strength_preferences.plot(kind='bar')
plt.title('Coffee Strength Preferences')
plt.xlabel('Strength Preference')
plt.ylabel('Count')
# Rotate and reduce font size of x-axis labels
plt.xticks(rotation=45, fontsize=8)   
plt.tight_layout() 
plt.show()