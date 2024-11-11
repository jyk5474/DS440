import pandas as pd
import matplotlib.pyplot as plt

def plot_income_distribution(zipcode):
    """
    Plot a bar graph of median income information for different age groups for a given zipcode.
    
    Parameters:
    zipcode (int or str): Zipcode to filter the data.
    """
    # Load the dataset
    df = pd.read_csv('IncomeBracketPA.csv')
    
    # Filter the DataFrame for the given zipcode
    df_zipcode = df[df['ZipCode'] == int(zipcode)]
    
    # Check if the dataframe is empty after filtering
    if df_zipcode.empty:
        print(f"No data found for zipcode: str(zipcode)")
        return
    
    # Extract the age brackets and their respective values
    age_brackets = df.columns[0:-1]  # Exclude the ZipCode column
    values = df_zipcode.iloc[, 2:]  # Get the first row's income values for the given zipcode
    
    # Plot the bar graph
    plt.figure(figsize=(12, 6))
    plt.bar(age_brackets, values, color='skyblue')
    plt.xlabel('Age Group')
    plt.ylabel('Median Income')
    plt.title(f'Median Income by Age Group for Zipcode {zipcode}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example usage
# plot_income_distribution(12345)
