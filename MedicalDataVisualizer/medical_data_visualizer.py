# Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("medical_examination.csv")

# Calculate BMI and add a new column 'overweight'
df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25).astype(int)

# Normalize 'cholesterol' and 'gluc' values to 0 and 1
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Function to draw a categorical plot
def draw_cat_plot():
    # Reshape the data for categorical plot
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    
    # Group and reformat the data for seaborn plotting
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")
    
    # Convert 'value' column to strings to avoid AttributeError in Seaborn
    df_cat['value'] = df_cat['value'].astype(str)
    
    # Create a categorical plot
    fig = sns.catplot(data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar").fig
    
    # Save the plot
    fig.savefig('catplot.png')
    return fig

# Function to draw a heat map
def draw_heat_map():
    # Filter the data for heatmap
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # Calculate the correlation matrix
    corr = df_heat.corr()
    
    # Create a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Draw the heatmap
    sns.heatmap(corr, annot=True, fmt=".1f", mask=mask, square=True, cmap="coolwarm", cbar_kws={'shrink': .5}, ax=ax)
    
    # Save the plot
    fig.savefig('heatmap.png')
    return fig