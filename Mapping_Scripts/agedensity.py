import pandas as pd
import matplotlib.pyplot as plt

def plot_age_distribution(zipcode):
    """
    Plot a bar graph of age brackets vs. their respective values for a given zipcode.
    
    Parameters:
    zipcode (int or str): Zipcode to filter the data.
    """
    # Load the dataset
    df = pd.read_csv('AgeDatasetPA.csv')
    
    # Filter the DataFrame for the given zipcode
    df_zipcode = df[df['ZipCode'] == zipcode]
    
    # Check if the dataframe is empty after filtering
    if df_zipcode.empty:
        print(f"No data found for zipcode: {zipcode}")
        return
    
    # Extract the age brackets and their respective values
    age_brackets = df.columns[1:]  # Exclude the ZipCode column
    values = df_zipcode.iloc[0, 1:]  # Get the first row's age bracket values
    
    # Plot the bar graph
    plt.figure(figsize=(12, 6))
    plt.bar(age_brackets, values, color='skyblue')
    plt.xlabel('Age Bracket')
    plt.ylabel('Values')
    plt.title(f'Age Distribution for Zipcode {zipcode}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example usage
# plot_age_distribution(12345)

