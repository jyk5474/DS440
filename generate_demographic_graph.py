import sys
import pandas as pd
import matplotlib.pyplot as plt

def plot_age_distribution(zipcode, output_path):
    """
    Plot a bar graph of age brackets vs. their respective values for a given zipcode.
    
    Parameters:
    zipcode (int or str): Zipcode to filter the data.
    output_path (str): Path to save the plot.
    """
    # Load the dataset
    df = pd.read_csv('AgeDatasetPA.csv')
    
    # Filter the DataFrame for the given zipcode
    df_zipcode = df[df['ZipCode'] == int(zipcode)]
    
    # Check if the dataframe is empty after filtering
    if df_zipcode.empty:
        print(f"No data found for zipcode: {zipcode}")
        return
    
    # Extract the age brackets and their respective values
    age_brackets = df.columns[2:-1].astype(str)  
    values = df_zipcode.iloc[0, 2:-1]    # Get the first row's age bracket values
    
    # Plot the bar graph
    plt.figure(figsize=(12, 6))
    plt.bar(age_brackets, values, color='skyblue')
    plt.xlabel('Age Bracket')
    plt.ylabel('Values')
    plt.title(f'Age Distribution for Zipcode {zipcode}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    

    # Save the plot to the output path
    plt.savefig(output_path)
    plt.close()

def create_demographic_plot(zip_code, demographic_type, output_path):
    """
    Create a demographic plot (either income or age) based on the given demographic type.
    
    Parameters:
    zip_code (str): The zip code to generate data for.
    demographic_type (str): The demographic type (either 'income' or 'age').
    output_path (str): Path to save the plot.
    """
    if demographic_type == 'income':
        # Generate a sample income plot
        plt.figure()
        plt.title(f'Income Data for Zip Code {zip_code}')
        plt.bar(['Low', 'Medium', 'High'], [25, 50, 25])
        plt.savefig(output_path)
        plt.close()
    elif demographic_type == 'age':
        # Call the plot_age_distribution function for the age demographic type
        plot_age_distribution(zip_code, output_path)

if __name__ == "__main__":
    # Get arguments: zip code, demographic type, and output path
    zip_code = sys.argv[1]
    demographic_type = sys.argv[2]
    output_path = sys.argv[3]

    # Generate the plot
    create_demographic_plot(zip_code, demographic_type, output_path)
