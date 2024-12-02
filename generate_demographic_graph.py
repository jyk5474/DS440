import sys
import pandas as pd
import matplotlib.pyplot as plt

# These methods control the main function of our program that being dynamically creating and showing demographics from pennsylvannia 

def plot_age_distribution(zipcode, output_path):
    
    df = pd.read_csv('Datasets\ExpandedPA_Age.csv')
    
    df_zipcode = df[df['ZipCode'] == int(zipcode)]
    
    if df_zipcode.empty:
        print(f"No data found for zipcode: {zipcode}")
        return
    
    age_brackets = ['Under5', '5to9', '10to14', '15to19', '20to24', '25to29', '30to34', '35to39', '40to44', '45to49', '50to54', '55to59', '60to64', '65to69', '70to74', '75to79', '80to84', 'over85']
    
    values = df_zipcode[age_brackets].iloc[0].values 
    
    plt.figure(figsize=(12, 6))
    plt.bar(age_brackets, values, color='skyblue')
    plt.xlabel('Age Bracket')
    plt.ylabel('Population')
    plt.title(f'Age Distribution for Zipcode {zipcode}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig(output_path)
    plt.close()



def plot_income_distribution(zipcode,output_path):

    df = pd.read_csv('Datasets\IncomeBracketPA.csv')
    
    df_zipcode = df[df['ZipCode'] == int(zipcode)]
    
    if df_zipcode.empty:
        print(f"No data found for zipcode: {zipcode}")
        return
    
    age_brackets = df.columns[2:-1].astype(str)  
    values =  df_zipcode.iloc[0, 2:-1].astype(int) 
    
    values.fillna(0, inplace=True)

    plt.figure(figsize=(12, 6))
    plt.bar(age_brackets, values, color='skyblue')
    plt.xlabel('Age Group')
    plt.ylabel('Median Income')
    plt.title(f'Median Income by Age Group for Zipcode {zipcode}')
    plt.xticks(rotation=45)
    plt.ylim(0, max(values) * 1.1)
    plt.tight_layout()


    plt.savefig(output_path)
    plt.close()

# We discussed the necessity of this final method but decided to include it as it simplifies the code slightly instead of calling two different methods for the different graphs
# we call this method which calls the method that the user selected
def create_demographic_plot(zip_code, demographic_type, output_path):
    
    if demographic_type == 'income':
        plot_income_distribution(zip_code,output_path)
    elif demographic_type == 'age':
        plot_age_distribution(zip_code, output_path)

if __name__ == "__main__":
    zip_code = sys.argv[1]
    demographic_type = sys.argv[2]
    output_path = sys.argv[3]

    # Generate the plot
    create_demographic_plot(zip_code, demographic_type, output_path)
