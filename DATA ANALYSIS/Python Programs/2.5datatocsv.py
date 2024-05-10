import ast
import os

# Assign directories, create output one if it does not exist
directory = '.'
output_directory = 'processed_data'


file_path = ''

# print('filename variable',filename)
# filenamevar = file.split('\\')
# filenamevar = filenamevar[1].split('.')
# filenamevar = filenamevar[0]
# print('file',file)

def find_first_occurrence(dictionary, substring):
    for key in dictionary:
        if substring in key:
            # print(dictionary[key])
            return key
# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# iterate over files in that directory, and create a list of them
files = []
for filename in os.listdir(directory):

    f = os.path.join(directory, filename)
    # checking if it is a file and has a ".csv" extension
    if os.path.isfile(f) and f.lower().endswith('.txt'):
        print(f)
        files.append(f)

# row_dictionaries = {}  
          
for file in files: # iterate through all the files
    # print('filename variable',filename)
    filenamevar = file.split('\\')
    filenamevar = filenamevar[1].split('.')
    filenamevar = filenamevar[0]
    file_path = str(filenamevar)#    file_path = str(filenamevar)+'.txt'
    # print('file',file)
    # file_path = 


    try:
        with open(file_path + '.txt', 'r') as file:
            file_content = file.read()
            experiment_values = ast.literal_eval(file_content)
            # print(experiment_values)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except ValueError as e:
        print(f"Error evaluating file content: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    #dictionary for total occurences:  ## No longer needed, breaking it up by wave seems like a better idea
    totaldict = {'POW.Cz.Theta':0, 'POW.Cz.Alpha':0, 'POW.Cz.BetaL':0, 'POW.Cz.BetaH':0, 'POW.Cz.Gamma':0, 'POW.Fz.Theta':0, 'POW.Fz.Alpha':0, 'POW.Fz.BetaL':0, 'POW.Fz.BetaH':0, 'POW.Fz.Gamma':0, 'POW.Fp1.Theta':0, 'POW.Fp1.Alpha':0, 'POW.Fp1.BetaL':0, 'POW.Fp1.BetaH':0, 'POW.Fp1.Gamma':0, 'POW.F7.Theta':0, 'POW.F7.Alpha':0, 'POW.F7.BetaL':0, 'POW.F7.BetaH':0, 'POW.F7.Gamma':0, 'POW.F3.Theta':0, 'POW.F3.Alpha':0, 'POW.F3.BetaL':0, 'POW.F3.BetaH':0, 'POW.F3.Gamma':0, 'POW.FC1.Theta':0, 'POW.FC1.Alpha':0, 'POW.FC1.BetaL':0, 'POW.FC1.BetaH':0, 'POW.FC1.Gamma':0, 'POW.C3.Theta':0, 'POW.C3.Alpha':0, 'POW.C3.BetaL':0, 'POW.C3.BetaH':0, 'POW.C3.Gamma':0, 'POW.FC5.Theta':0, 'POW.FC5.Alpha':0, 'POW.FC5.BetaL':0, 'POW.FC5.BetaH':0, 'POW.FC5.Gamma':0, 'POW.FT9.Theta':0, 'POW.FT9.Alpha':0, 'POW.FT9.BetaL':0, 'POW.FT9.BetaH':0, 'POW.FT9.Gamma':0, 'POW.T7.Theta':0, 'POW.T7.Alpha':0, 'POW.T7.BetaL':0, 'POW.T7.BetaH':0, 'POW.T7.Gamma':0, 'POW.CP5.Theta':0, 'POW.CP5.Alpha':0, 'POW.CP5.BetaL':0, 'POW.CP5.BetaH':0, 'POW.CP5.Gamma':0, 'POW.CP1.Theta':0, 'POW.CP1.Alpha':0, 'POW.CP1.BetaL':0, 'POW.CP1.BetaH':0, 'POW.CP1.Gamma':0, 'POW.P3.Theta':0, 'POW.P3.Alpha':0, 'POW.P3.BetaL':0, 'POW.P3.BetaH':0, 'POW.P3.Gamma':0, 'POW.P7.Theta':0, 'POW.P7.Alpha':0, 'POW.P7.BetaL':0, 'POW.P7.BetaH':0, 'POW.P7.Gamma':0, 'POW.PO9.Theta':0, 'POW.PO9.Alpha':0, 'POW.PO9.BetaL':0, 'POW.PO9.BetaH':0, 'POW.PO9.Gamma':0, 'POW.O1.Theta':0, 'POW.O1.Alpha':0, 'POW.O1.BetaL':0, 'POW.O1.BetaH':0, 'POW.O1.Gamma':0, 'POW.Pz.Theta':0, 'POW.Pz.Alpha':0, 'POW.Pz.BetaL':0, 'POW.Pz.BetaH':0, 'POW.Pz.Gamma':0, 'POW.Oz.Theta':0, 'POW.Oz.Alpha':0, 'POW.Oz.BetaL':0, 'POW.Oz.BetaH':0, 'POW.Oz.Gamma':0, 'POW.O2.Theta':0, 'POW.O2.Alpha':0, 'POW.O2.BetaL':0, 'POW.O2.BetaH':0, 'POW.O2.Gamma':0, 'POW.PO10.Theta':0, 'POW.PO10.Alpha':0, 'POW.PO10.BetaL':0, 'POW.PO10.BetaH':0, 'POW.PO10.Gamma':0, 'POW.P8.Theta':0, 'POW.P8.Alpha':0, 'POW.P8.BetaL':0, 'POW.P8.BetaH':0, 'POW.P8.Gamma':0, 'POW.P4.Theta':0, 'POW.P4.Alpha':0, 'POW.P4.BetaL':0, 'POW.P4.BetaH':0, 'POW.P4.Gamma':0, 'POW.CP2.Theta':0, 'POW.CP2.Alpha':0, 'POW.CP2.BetaL':0, 'POW.CP2.BetaH':0, 'POW.CP2.Gamma':0, 'POW.CP6.Theta':0, 'POW.CP6.Alpha':0, 'POW.CP6.BetaL':0, 'POW.CP6.BetaH':0, 'POW.CP6.Gamma':0, 'POW.T8.Theta':0, 'POW.T8.Alpha':0, 'POW.T8.BetaL':0, 'POW.T8.BetaH':0, 'POW.T8.Gamma':0, 'POW.FT10.Theta':0, 'POW.FT10.Alpha':0, 'POW.FT10.BetaL':0, 'POW.FT10.BetaH':0, 'POW.FT10.Gamma':0, 'POW.FC6.Theta':0, 'POW.FC6.Alpha':0, 'POW.FC6.BetaL':0, 'POW.FC6.BetaH':0, 'POW.FC6.Gamma':0, 'POW.C4.Theta':0, 'POW.C4.Alpha':0, 'POW.C4.BetaL':0, 'POW.C4.BetaH':0, 'POW.C4.Gamma':0, 'POW.FC2.Theta':0, 'POW.FC2.Alpha':0, 'POW.FC2.BetaL':0, 'POW.FC2.BetaH':0, 'POW.FC2.Gamma':0, 'POW.F4.Theta':0, 'POW.F4.Alpha':0, 'POW.F4.BetaL':0, 'POW.F4.BetaH':0, 'POW.F4.Gamma':0, 'POW.F8.Theta':0, 'POW.F8.Alpha':0, 'POW.F8.BetaL':0, 'POW.F8.BetaH':0, 'POW.F8.Gamma':0, 'POW.Fp2.Theta':0, 'POW.Fp2.Alpha':0, 'POW.Fp2.BetaL':0, 'POW.Fp2.BetaH':0, 'POW.Fp2.Gamma':0}

    # Separate values into wave category dictionaries with original keys
    alpha_dict = {'POW.Cz.Alpha': 0, 'POW.Fz.Alpha': 0, 'POW.Fp1.Alpha': 0, 'POW.F7.Alpha': 0, 'POW.F3.Alpha': 0, 'POW.FC1.Alpha': 0, 'POW.C3.Alpha': 0, 'POW.FC5.Alpha': 0, 'POW.FT9.Alpha': 0, 'POW.T7.Alpha': 0, 'POW.CP5.Alpha': 0, 'POW.CP1.Alpha': 0, 'POW.P3.Alpha': 0, 'POW.P7.Alpha': 0, 'POW.PO9.Alpha': 0, 'POW.O1.Alpha': 0, 'POW.Pz.Alpha': 0, 'POW.Oz.Alpha': 0, 'POW.O2.Alpha': 0, 'POW.PO10.Alpha': 0, 'POW.P8.Alpha': 0, 'POW.P4.Alpha': 0, 'POW.CP2.Alpha': 0, 'POW.CP6.Alpha': 0, 'POW.T8.Alpha': 0, 'POW.FT10.Alpha': 0, 'POW.FC6.Alpha': 0, 'POW.C4.Alpha': 0, 'POW.FC2.Alpha': 0, 'POW.F4.Alpha': 0, 'POW.F8.Alpha': 0, 'POW.Fp2.Alpha': 0}
    beta_l_dict = {'POW.Cz.BetaL': 0, 'POW.Fz.BetaL': 0, 'POW.Fp1.BetaL': 0, 'POW.F7.BetaL': 0, 'POW.F3.BetaL': 0, 'POW.FC1.BetaL': 0, 'POW.C3.BetaL': 0, 'POW.FC5.BetaL': 0, 'POW.FT9.BetaL': 0, 'POW.T7.BetaL': 0, 'POW.CP5.BetaL': 0, 'POW.CP1.BetaL': 0, 'POW.P3.BetaL': 0, 'POW.P7.BetaL': 0, 'POW.PO9.BetaL': 0, 'POW.O1.BetaL': 0, 'POW.Pz.BetaL': 0, 'POW.Oz.BetaL': 0, 'POW.O2.BetaL': 0, 'POW.PO10.BetaL': 0, 'POW.P8.BetaL': 0, 'POW.P4.BetaL': 0, 'POW.CP2.BetaL': 0, 'POW.CP6.BetaL': 0, 'POW.T8.BetaL': 0, 'POW.FT10.BetaL': 0, 'POW.FC6.BetaL': 0, 'POW.C4.BetaL': 0, 'POW.FC2.BetaL': 0, 'POW.F4.BetaL': 0, 'POW.F8.BetaL': 0, 'POW.Fp2.BetaL': 0}
    beta_h_dict = {'POW.Cz.BetaH': 0, 'POW.Fz.BetaH': 0, 'POW.Fp1.BetaH': 0, 'POW.F7.BetaH': 0, 'POW.F3.BetaH': 0, 'POW.FC1.BetaH': 0, 'POW.C3.BetaH': 0, 'POW.FC5.BetaH': 0, 'POW.FT9.BetaH': 0, 'POW.T7.BetaH': 0, 'POW.CP5.BetaH': 0, 'POW.CP1.BetaH': 0, 'POW.P3.BetaH': 0, 'POW.P7.BetaH': 0, 'POW.PO9.BetaH': 0, 'POW.O1.BetaH': 0, 'POW.Pz.BetaH': 0, 'POW.Oz.BetaH': 0, 'POW.O2.BetaH': 0, 'POW.PO10.BetaH': 0, 'POW.P8.BetaH': 0, 'POW.P4.BetaH': 0, 'POW.CP2.BetaH': 0, 'POW.CP6.BetaH': 0, 'POW.T8.BetaH': 0, 'POW.FT10.BetaH': 0, 'POW.FC6.BetaH': 0, 'POW.C4.BetaH': 0, 'POW.FC2.BetaH': 0, 'POW.F4.BetaH': 0, 'POW.F8.BetaH': 0, 'POW.Fp2.BetaH': 0}
    gamma_dict = {'POW.Cz.Gamma': 0, 'POW.Fz.Gamma': 0, 'POW.Fp1.Gamma': 0, 'POW.F7.Gamma': 0, 'POW.F3.Gamma': 0, 'POW.FC1.Gamma': 0, 'POW.C3.Gamma': 0, 'POW.FC5.Gamma': 0, 'POW.FT9.Gamma': 0, 'POW.T7.Gamma': 0, 'POW.CP5.Gamma': 0, 'POW.CP1.Gamma': 0, 'POW.P3.Gamma': 0, 'POW.P7.Gamma': 0, 'POW.PO9.Gamma': 0, 'POW.O1.Gamma': 0, 'POW.Pz.Gamma': 0, 'POW.Oz.Gamma': 0, 'POW.O2.Gamma': 0, 'POW.PO10.Gamma': 0, 'POW.P8.Gamma': 0, 'POW.P4.Gamma': 0, 'POW.CP2.Gamma': 0, 'POW.CP6.Gamma': 0, 'POW.T8.Gamma': 0, 'POW.FT10.Gamma': 0, 'POW.FC6.Gamma': 0, 'POW.C4.Gamma': 0, 'POW.FC2.Gamma': 0, 'POW.F4.Gamma': 0, 'POW.F8.Gamma': 0, 'POW.Fp2.Gamma': 0}
    theta_dict = {'POW.Cz.Theta': 0, 'POW.Fz.Theta': 0, 'POW.Fp1.Theta': 0, 'POW.F7.Theta': 0, 'POW.F3.Theta': 0, 'POW.FC1.Theta': 0, 'POW.C3.Theta': 0, 'POW.FC5.Theta': 0, 'POW.FT9.Theta': 0, 'POW.T7.Theta': 0, 'POW.CP5.Theta': 0, 'POW.CP1.Theta': 0, 'POW.P3.Theta': 0, 'POW.P7.Theta': 0, 'POW.PO9.Theta': 0, 'POW.O1.Theta': 0, 'POW.Pz.Theta': 0, 'POW.Oz.Theta': 0, 'POW.O2.Theta': 0, 'POW.PO10.Theta': 0, 'POW.P8.Theta': 0, 'POW.P4.Theta': 0, 'POW.CP2.Theta': 0, 'POW.CP6.Theta': 0, 'POW.T8.Theta': 0, 'POW.FT10.Theta': 0, 'POW.FC6.Theta': 0, 'POW.C4.Theta': 0, 'POW.FC2.Theta': 0, 'POW.F4.Theta': 0, 'POW.F8.Theta': 0, 'POW.Fp2.Theta': 0}


    alpha_locations ={'POW.Cz.Alpha': 0, 'POW.Fz.Alpha': 0, 'POW.Fp1.Alpha': 0, 'POW.F7.Alpha': 0, 'POW.F3.Alpha': 0, 'POW.FC1.Alpha': 0, 'POW.C3.Alpha': 0, 'POW.FC5.Alpha': 0, 'POW.FT9.Alpha': 0, 'POW.T7.Alpha': 0, 'POW.CP5.Alpha': 0, 'POW.CP1.Alpha': 0, 'POW.P3.Alpha': 0, 'POW.P7.Alpha': 0, 'POW.PO9.Alpha': 0, 'POW.O1.Alpha': 0, 'POW.Pz.Alpha': 0, 'POW.Oz.Alpha': 0, 'POW.O2.Alpha': 0, 'POW.PO10.Alpha': 0, 'POW.P8.Alpha': 0, 'POW.P4.Alpha': 0, 'POW.CP2.Alpha': 0, 'POW.CP6.Alpha': 0, 'POW.T8.Alpha': 0, 'POW.FT10.Alpha': 0, 'POW.FC6.Alpha': 0, 'POW.C4.Alpha': 0, 'POW.FC2.Alpha': 0, 'POW.F4.Alpha': 0, 'POW.F8.Alpha': 0, 'POW.Fp2.Alpha': 0}
    beta_l_locations = {'POW.Cz.BetaL': 0, 'POW.Fz.BetaL': 0, 'POW.Fp1.BetaL': 0, 'POW.F7.BetaL': 0, 'POW.F3.BetaL': 0, 'POW.FC1.BetaL': 0, 'POW.C3.BetaL': 0, 'POW.FC5.BetaL': 0, 'POW.FT9.BetaL': 0, 'POW.T7.BetaL': 0, 'POW.CP5.BetaL': 0, 'POW.CP1.BetaL': 0, 'POW.P3.BetaL': 0, 'POW.P7.BetaL': 0, 'POW.PO9.BetaL': 0, 'POW.O1.BetaL': 0, 'POW.Pz.BetaL': 0, 'POW.Oz.BetaL': 0, 'POW.O2.BetaL': 0, 'POW.PO10.BetaL': 0, 'POW.P8.BetaL': 0, 'POW.P4.BetaL': 0, 'POW.CP2.BetaL': 0, 'POW.CP6.BetaL': 0, 'POW.T8.BetaL': 0, 'POW.FT10.BetaL': 0, 'POW.FC6.BetaL': 0, 'POW.C4.BetaL': 0, 'POW.FC2.BetaL': 0, 'POW.F4.BetaL': 0, 'POW.F8.BetaL': 0, 'POW.Fp2.BetaL': 0}
    beta_h_locations = {'POW.Cz.BetaH': 0, 'POW.Fz.BetaH': 0, 'POW.Fp1.BetaH': 0, 'POW.F7.BetaH': 0, 'POW.F3.BetaH': 0, 'POW.FC1.BetaH': 0, 'POW.C3.BetaH': 0, 'POW.FC5.BetaH': 0, 'POW.FT9.BetaH': 0, 'POW.T7.BetaH': 0, 'POW.CP5.BetaH': 0, 'POW.CP1.BetaH': 0, 'POW.P3.BetaH': 0, 'POW.P7.BetaH': 0, 'POW.PO9.BetaH': 0, 'POW.O1.BetaH': 0, 'POW.Pz.BetaH': 0, 'POW.Oz.BetaH': 0, 'POW.O2.BetaH': 0, 'POW.PO10.BetaH': 0, 'POW.P8.BetaH': 0, 'POW.P4.BetaH': 0, 'POW.CP2.BetaH': 0, 'POW.CP6.BetaH': 0, 'POW.T8.BetaH': 0, 'POW.FT10.BetaH': 0, 'POW.FC6.BetaH': 0, 'POW.C4.BetaH': 0, 'POW.FC2.BetaH': 0, 'POW.F4.BetaH': 0, 'POW.F8.BetaH': 0, 'POW.Fp2.BetaH': 0}
    gamma_locations = {'POW.Cz.Gamma': 0, 'POW.Fz.Gamma': 0, 'POW.Fp1.Gamma': 0, 'POW.F7.Gamma': 0, 'POW.F3.Gamma': 0, 'POW.FC1.Gamma': 0, 'POW.C3.Gamma': 0, 'POW.FC5.Gamma': 0, 'POW.FT9.Gamma': 0, 'POW.T7.Gamma': 0, 'POW.CP5.Gamma': 0, 'POW.CP1.Gamma': 0, 'POW.P3.Gamma': 0, 'POW.P7.Gamma': 0, 'POW.PO9.Gamma': 0, 'POW.O1.Gamma': 0, 'POW.Pz.Gamma': 0, 'POW.Oz.Gamma': 0, 'POW.O2.Gamma': 0, 'POW.PO10.Gamma': 0, 'POW.P8.Gamma': 0, 'POW.P4.Gamma': 0, 'POW.CP2.Gamma': 0, 'POW.CP6.Gamma': 0, 'POW.T8.Gamma': 0, 'POW.FT10.Gamma': 0, 'POW.FC6.Gamma': 0, 'POW.C4.Gamma': 0, 'POW.FC2.Gamma': 0, 'POW.F4.Gamma': 0, 'POW.F8.Gamma': 0, 'POW.Fp2.Gamma': 0}
    theta_locations = {'POW.Cz.Theta': 0, 'POW.Fz.Theta': 0, 'POW.Fp1.Theta': 0, 'POW.F7.Theta': 0, 'POW.F3.Theta': 0, 'POW.FC1.Theta': 0, 'POW.C3.Theta': 0, 'POW.FC5.Theta': 0, 'POW.FT9.Theta': 0, 'POW.T7.Theta': 0, 'POW.CP5.Theta': 0, 'POW.CP1.Theta': 0, 'POW.P3.Theta': 0, 'POW.P7.Theta': 0, 'POW.PO9.Theta': 0, 'POW.O1.Theta': 0, 'POW.Pz.Theta': 0, 'POW.Oz.Theta': 0, 'POW.O2.Theta': 0, 'POW.PO10.Theta': 0, 'POW.P8.Theta': 0, 'POW.P4.Theta': 0, 'POW.CP2.Theta': 0, 'POW.CP6.Theta': 0, 'POW.T8.Theta': 0, 'POW.FT10.Theta': 0, 'POW.FC6.Theta': 0, 'POW.C4.Theta': 0, 'POW.FC2.Theta': 0, 'POW.F4.Theta': 0, 'POW.F8.Theta': 0, 'POW.Fp2.Theta': 0}

    for key, inner_dict in (experiment_values.items()):
        sorted_inner_dict = sorted(inner_dict.items(), key=lambda item: item[1],reverse=True)
        with open('testsorting.txt', 'a') as file:
            print('Did someting with sorted inner dict printing to file')
            # Redirect the print statement to write to the file
            print(sorted_inner_dict, file=file)
        # print(dict(sorted_inner_dict))
        sorted_inner_dict = dict(sorted_inner_dict)
        found_max_alpha = False
        found_max_beta_l = False
        found_max_beta_h = False
        found_max_gamma = False
        found_max_theta = False
        
        for location, value in sorted_inner_dict.items():

            if 'Alpha' in location:
                if found_max_alpha == False:
                    found_max_alpha = True
                    alpha_locations[location] = alpha_locations.get(location,0)+1
                    # totaldict[location] = totaldict.get(location,0) +1
                alpha_dict[location] = value
                    # print('location',location,'value',value)

            elif 'BetaL' in location:
                if found_max_beta_l == False:
                    found_max_beta_l = True
                    beta_l_locations[location] = beta_l_locations.get(location,0)+1
                beta_l_dict[location] = value

            elif 'BetaH' in location:
                if found_max_beta_h == False:
                    found_max_beta_h = True
                    beta_h_locations[location] = beta_h_locations.get(location,0)+1
                beta_h_dict[location] = value

            elif 'Gamma' in location:
                if found_max_gamma == False:
                    found_max_gamma = True
                    gamma_locations[location] = gamma_locations.get(location,0)+1
                gamma_dict[location] = value

            elif 'Theta' in location:
                if found_max_theta == False:
                    found_max_theta = True
                    theta_locations[location] = theta_locations.get(location,0) +1
                    # totaldict[location] = totaldict.get(location,0) +1
                theta_dict[location] = value
                    # print('location',location,'value',value)


        first_alpha_key = find_first_occurrence(alpha_dict, 'Alpha')
        first_beta_l_key = find_first_occurrence(beta_l_dict, 'BetaL')
        first_beta_h_key = find_first_occurrence(beta_h_dict, 'BetaH')
        first_gamma_key = find_first_occurrence(gamma_dict, 'Gamma')
        first_theta_key = find_first_occurrence(theta_dict, 'Theta')


        # print(first_theta_key)
        theta_dict.clear()
        alpha_dict.clear()
        beta_l_dict.clear()
        beta_h_dict.clear()
        gamma_dict.clear()

    with open(file_path+'alpha_max_counts.csv','a') as file:
        for i in alpha_locations:
            print(i,',',alpha_locations[i],file=file)
    # alpha_data = open('alpha_max_counts.txt')
    # print('Alpha locations',alpha_locations)
    # print('Beta L locations',beta_l_locations)

    with open(file_path+'beta_l_max_counts.csv','a') as file:
        for i in beta_l_locations:
            print(i,',',beta_l_locations[i],file=file)

    with open(file_path+'beta_h_max_counts.csv','a') as file:
        for i in beta_h_locations:
            print(i,',',beta_h_locations[i],file=file)

    with open(file_path+'gamma_max_counts.csv','a') as file:
        for i in gamma_locations:
            print(i,',',gamma_locations[i],file=file)

    with open(file_path+'theta_max_counts.csv','a') as file:
        for i in theta_locations:
            print(i,',',theta_locations[i],file=file)
            
