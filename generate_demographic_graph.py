import sys
import matplotlib.pyplot as plt

# Get arguments: zip code, demographic type, and output path
zip_code = sys.argv[1]
demographic_type = sys.argv[2]
output_path = sys.argv[3]

# Generate a sample plot (customize with real data for each demographic type)
plt.figure()
if demographic_type == 'income':
    plt.title(f'Income Data for Zip Code {zip_code}')
    plt.bar(['Low', 'Medium', 'High'], [25, 50, 25])
elif demographic_type == 'age':
    plt.title(f'Age Data for Zip Code {zip_code}')
    plt.bar(['18-25', '26-40', '41-65', '65+'], [20, 30, 35, 15])

plt.savefig(output_path)