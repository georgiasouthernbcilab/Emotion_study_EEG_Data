
# import required module
import os
import csv

# Assign directory
directory = r'C:\Users\micha\OneDrive - Georgia Southern University\5_RESEARCH\1 EEG\data Analysis\2_ATTENTION\013127\split\processme' # 2_ATTENTION\\013127\\split
output_directory = r'C:\Users\micha\OneDrive - Georgia Southern University\5_RESEARCH\1 EEG\data Analysis\2_ATTENTION\013127\split\processed_data'

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# iterate over files in that directory
files = []
for filename in os.listdir(directory):
    print('filename',filename)
    f = os.path.join(directory, filename)
    # checking if it is a file and has a ".csv" extension
    if os.path.isfile(f) and f.lower().endswith('.csv'):
        print(f)
        files.append(f)

row_dictionaries = {}            
for file in files: # iterate through all the files
    print('Processing file: ', file)

#%%
    row_start = 1 #IGNORE THE FIRST ROW!!!
    column_start = 124

    # Create an empty dictionary to store the column values
    column_dict = {}
    # create a list of all column headers for the dictionary and
    # mapping values to correct list in dictionary
    column_headers = []

    with open(file) as csvfile:
        experiment_data = csv.reader(csvfile)

        # Ignore the first row
        for index, row in enumerate(experiment_data):
            if index < row_start:
                continue

            # Initialize lists for each column header
            if index == row_start:
                column_headers = row[column_start:]
                for header in column_headers:
                    # Initialize a list in the dictionary for the header
                    column_dict[header] = []

            # Append float values to corresponding lists, this ignores non-floats
            for col_index, column in enumerate(row[column_start:]):
                try:
                    float_value = float(column) # If this fails, we skip the value
                    column_dict[column_headers[col_index]].append(float_value)
                    row_dictionaries[index] = {row[column_start + col_index] }
                    # row_dictionaries[column+str(index-1)]=float_value
                except ValueError:
                    # Handle the case where the value is not a float
                    continue    
 
            # Create a dictionary for the current row
            current_row_dict = {}
            for i in range(len(column_headers)):
                cell_value = row[column_start + i]
                if is_float(cell_value):
                    current_row_dict[column_headers[i]] = float(cell_value)

            if current_row_dict:
            # Add the current row dictionary to the main dictionary
                row_dictionaries[index] = current_row_dict

            # print(row_dictionaries)            
            #     except ValueError:
            #         # Handle the case where the value is not a float
            #         continue
            #     # column_dict[row] = 1 column_headers[#] returns column header
                
            # row_dictionaries[index] = {column_headers[i] : row[column_start + i] for i in range(len(column_headers))} #row_dictionaries[index] = {index: row}  #rowdict[] = {index: row}
            # print(row_dictionaries)# row_dictionaries[(index-1)]=row  # column_dict
#%% 

        # Create an empty dictionary to store the total values
        column_sums = {}

        # Iterate over the keys in column_dict
        for key in column_dict:
            # Calculate the sum of values in the list
            total_value = sum(column_dict[key])

            # Store the total value in the new dictionary
            column_sums[key] = total_value
        # print(column_sums)

        #%%
        theta_sum = 0
        alpha_sum = 0
        beta_low_sum = 0
        beta_high_sum = 0
        gamma_sum = 0

        for key in column_sums:
            # print('key',key)
            if 'Alpha' in key:
                alpha_sum += column_sums[key]
                # print('Alpha Sum',alpha_sum)
            if 'BetaL' in key:
                beta_low_sum += column_sums[key]
                # print('Beta_Low value', beta_low_sum)
            if 'BetaH' in key:
                beta_high_sum += column_sums[key]
                # print('Beta_High',beta_high_sum)
            if 'Gamma' in key:
                gamma_sum += column_sums[key]
                # print('Gamma',gamma_sum)
            if 'Theta' in key:
                theta_sum += column_sums[key]
                # print('Theta',theta_sum)


            # print(column_sums[key])
        # %%
        # print('Alpha Sum',alpha_sum)
        # print('Beta_High',beta_high_sum)
        # print('Beta_Low value', beta_low_sum)
        # print('Gamma',gamma_sum)
        # print('Theta',theta_sum)
        # %%

        total_file_name = os.path.join(output_directory, os.path.basename(file) + 'output.txt')
        print('total_file_name ',total_file_name )
        with open(total_file_name,'a')as outputfile:
            print('Alpha Sum',alpha_sum,file=outputfile)
            print('Beta_High',beta_high_sum,file=outputfile)
            print('Beta_Low value', beta_low_sum,file=outputfile)
            print('Gamma',gamma_sum,file=outputfile)
            print('Theta',theta_sum,file=outputfile)

        # %%
        elements = len(column_dict[key])
        try:
            with open(total_file_name,'a')as outputfile:
                print('Normalized Alpha Sum',alpha_sum/elements,file=outputfile)
                print('Normalized Beta_High',beta_high_sum/elements,file=outputfile)
                print('Normalized Beta_Low value', beta_low_sum/elements,file=outputfile)
                print('Normalized Gamma',gamma_sum/elements,file=outputfile)
                print('Normalized Theta',theta_sum/elements,file=outputfile)
        except Exception as e:
            print(f'Exception:{e}while processing file: {total_file_name}')

        len(column_dict)
        # %%

        # Create the correct variables for the output filename
        print('filename variable',filename)
        filenamevar = file.split('\\')
        filenamevar = filenamevar[1].split('.')
        filenamevar = filenamevar[0]
        print('file',file)
        
        # Open a file in write mode ('w')
        with open(str(filenamevar) + 'dict.txt', 'w') as txtfile:
            print('filename variable',filename)
            # filenamevar = file.split('\\')
            # filenamevar = filenamevar[1].split('.')
            # filenamevar = filenamevar[0]
            # print('file',file)
            # Redirect the print statement to write to the file
            print(row_dictionaries, file=txtfile)
        row_dictionaries.clear()