import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def main():
    # Load the dataset from MOCK_DATA.csv
    filepath = 'MOCK_DATA.csv'  # Ensure this is the correct path to your CSV file
    df = pd.read_csv(filepath)
    
    # Print the columns to check their names (optional, for debugging)
    print("Columns in DataFrame:", df.columns)
    
    # Ensure 'price' column is numeric
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    
    # Call plotting functions
    plot_bar_chart(df)
    plot_pie_chart(df)
    plot_scatter_plot(df)
    plot_heatmap(df)

# Define plotting functions
def plot_bar_chart(df):
    fig = px.bar(df, x='first_name', y='price', color='gender', title='Bar Chart of Prices by First Name and Gender')
    fig.update_layout(xaxis_title='First Name', yaxis_title='Price')
    fig.show()

def plot_pie_chart(df):
    fig = px.pie(df, names='gender', values='price', title='Pie Chart of Prices by Gender')
    fig.show()

def plot_scatter_plot(df):
    fig = px.scatter(df, x='first_name', y='price', color='gender', title='Scatter Plot of Prices by First Name')
    fig.update_layout(xaxis_title='First Name', yaxis_title='Price')
    fig.show()

def plot_heatmap(df):
    pivot_table = df.pivot_table(values='price', index='first_name', columns='gender', fill_value=0)
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, cmap='viridis', annot=True)
    plt.title('Heatmap of Prices by First Name and Gender')
    plt.show()

if __name__ == "__main__":
    main()
