
#%%
import csv
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

#%%
location_dict = {'POW.Cz.Theta ': [321, 342, 0], 'POW.Cz.Alpha ': [321, 342, 0], 'POW.Cz.BetaL ': [321, 342, 0], 'POW.Cz.BetaH ': [321, 342, 0], 'POW.Cz.Gamma ': [321, 342, 0], 'POW.Fz.Theta ': [319, 216, 0], 'POW.Fz.Alpha ': [319, 216, 0], 'POW.Fz.BetaL ': [319, 214, 0], 'POW.Fz.BetaH ': [319, 214, 0], 'POW.Fz.Gamma ': [319, 214, 0], 'POW.Fp1.Theta ': [257, 124, 0], 'POW.Fp1.Alpha ': [257, 122, 0], 'POW.Fp1.BetaL ': [257, 122, 0], 'POW.Fp1.BetaH ': [257, 122, 0], 'POW.Fp1.Gamma ': [257, 122, 0], 'POW.F7.Theta ': [141, 197, 0], 'POW.F7.Alpha ': [141, 197, 0], 'POW.F7.BetaL ': [141, 197, 0], 'POW.F7.BetaH ': [141, 197, 0], 'POW.F7.Gamma ': [141, 197, 0], 'POW.F3.Theta ': [226, 211, 0], 'POW.F3.Alpha ': [226, 211, 0], 'POW.F3.BetaL ': [226, 209, 0], 'POW.F3.BetaH ': [226, 209, 0], 'POW.F3.Gamma ': [226, 209, 0], 'POW.FC1.Theta ': [252, 278, 0], 'POW.FC1.Alpha ': [252, 276, 0], 'POW.FC1.BetaL ': [252, 276, 0], 'POW.FC1.BetaH ': [252, 276, 0], 'POW.FC1.Gamma ': [252, 276, 0], 'POW.C3.Theta ': [195, 342, 0], 'POW.C3.Alpha ': [195, 342, 0], 'POW.C3.BetaL ': [195, 342, 0], 'POW.C3.BetaH ': [195, 342, 0], 'POW.C3.Gamma ': [195, 342, 0], 'POW.FC5.Theta ': [156, 273, 0], 'POW.FC5.Alpha ': [156, 273, 0], 'POW.FC5.BetaL ': [156, 271, 0], 'POW.FC5.BetaH ': [156, 271, 0], 'POW.FC5.Gamma ': [156, 271, 0], 'POW.FT9.Theta ': [51, 256, 0], 'POW.FT9.Alpha ': [51, 256, 0], 'POW.FT9.BetaL ': [51, 254, 0], 'POW.FT9.BetaH ': [51, 254, 0], 'POW.FT9.Gamma ': [51, 254, 0], 'POW.T7.Theta ': [94, 340, 0], 'POW.T7.Alpha ': [94, 339, 0], 'POW.T7.BetaL ': [94, 337, 0], 'POW.T7.BetaH ': [94, 337, 0], 'POW.T7.Gamma ': [94, 335, 0], 'POW.CP5.Theta ': [160, 411, 0], 'POW.CP5.Alpha ': [160, 411, 0], 'POW.CP5.BetaL ': [160, 411, 0], 'POW.CP5.BetaH ': [160, 411, 0], 'POW.CP5.Gamma ': [160, 411, 0], 'POW.CP1.Theta ': [257, 406, 0], 'POW.CP1.Alpha ': [257, 406, 0], 'POW.CP1.BetaL ': [257, 406, 0], 'POW.CP1.BetaH ': [257, 406, 0], 'POW.CP1.Gamma ': [257, 406, 0], 'POW.P3.Theta ': [226, 472, 0], 'POW.P3.Alpha ': [226, 472, 0], 'POW.P3.BetaL ': [226, 470, 0], 'POW.P3.BetaH ': [226, 470, 0], 'POW.P3.Gamma ': [226, 470, 0], 'POW.P7.Theta ': [143, 477, 0], 'POW.P7.Alpha ': [143, 477, 0], 'POW.P7.BetaL ': [143, 477, 0], 'POW.P7.BetaH ': [143, 477, 0], 'POW.P7.Gamma ': [143, 477, 0], 'POW.PO9.Theta ': [148, 565, 0], 'POW.PO9.Alpha ': [148, 565, 0], 'POW.PO9.BetaL ': [148, 565, 0], 'POW.PO9.BetaH ': [148, 565, 0], 'POW.PO9.Gamma ': [148, 565, 0], 'POW.O1.Theta ': [148, 565, 0], 'POW.O1.Alpha ': [258, 555, 0], 'POW.O1.BetaL ': [258, 555, 0], 'POW.O1.BetaH ': [258, 555, 0], 'POW.O1.Gamma ': [258, 555, 0], 'POW.Pz.Theta ': [321, 472, 0], 'POW.Pz.Alpha ': [321, 470, 0], 'POW.Pz.BetaL ': [321, 470, 0], 'POW.Pz.BetaH ': [321, 470, 0], 'POW.Pz.Gamma ': [321, 470, 0], 'POW.Oz.Theta ': [321, 572, 0], 'POW.Oz.Alpha ': [321, 572, 0], 'POW.Oz.BetaL ': [321, 572, 0], 'POW.Oz.BetaH ': [321, 572, 0], 'POW.Oz.Gamma ': [321, 572, 0], 'POW.O2.Theta ': [392, 558, 0], 'POW.O2.Alpha ': [392, 558, 0], 'POW.O2.BetaL ': [392, 558, 0], 'POW.O2.BetaH ': [392, 558, 0], 'POW.O2.Gamma ': [392, 558, 0], 'POW.PO10.Theta ': [559, 496, 0], 'POW.PO10.Alpha ': [559, 494, 0], 'POW.PO10.BetaL ': [559, 494, 0], 'POW.PO10.BetaH ': [559, 494, 0], 'POW.PO10.Gamma ': [559, 494, 0], 'POW.P8.Theta ': [499, 480, 0], 'POW.P8.Alpha ': [499, 480, 0], 'POW.P8.BetaL ': [499, 480, 0], 'POW.P8.BetaH ': [499, 480, 0], 'POW.P8.Gamma ': [499, 480, 0], 'POW.P4.Theta ': [414, 473, 0], 'POW.P4.Alpha ': [414, 472, 0], 'POW.P4.BetaL ': [414, 472, 0], 'POW.P4.BetaH ': [414, 472, 0], 'POW.P4.Gamma ': [414, 472, 0], 'POW.CP2.Theta ': [388, 403, 0], 'POW.CP2.Alpha ': [388, 403, 0], 'POW.CP2.BetaL ': [388, 403, 0], 'POW.CP2.BetaH ': [388, 403, 0], 'POW.CP2.Gamma ': [388, 403, 0], 'POW.CP6.Theta ': [482, 413, 0], 'POW.CP6.Alpha ': [482, 413, 0], 'POW.CP6.BetaL ': [482, 413, 0], 'POW.CP6.BetaH ': [482, 413, 0], 'POW.CP6.Gamma ': [482, 413, 0], 'POW.T8.Theta ': [544, 340, 0], 'POW.T8.Alpha ': [544, 339, 0], 'POW.T8.BetaL ': [544, 337, 0], 'POW.T8.BetaH ': [544, 337, 0], 'POW.T8.Gamma ': [544, 337, 0], 'POW.FT10.Theta ': [585, 250, 0], 'POW.FT10.Alpha ': [585, 250, 0], 'POW.FT10.BetaL ': [585, 250, 0], 'POW.FT10.BetaH ': [585, 250, 0], 'POW.FT10.Gamma ': [585, 250, 0], 'POW.FC6.Theta ': [483, 268, 0], 'POW.FC6.Alpha ': [483, 268, 0], 'POW.FC6.BetaL ': [483, 268, 0], 'POW.FC6.BetaH ': [483, 268, 0], 'POW.FC6.Gamma ': [483, 268, 0], 'POW.C4.Theta ': [442, 339, 0], 'POW.C4.Alpha ': [442, 337, 0], 'POW.C4.BetaL ': [442, 335, 0], 'POW.C4.BetaH ': [438, 342, 0], 'POW.C4.Gamma ': [438, 342, 0], 'POW.FC2.Theta ': [386, 278, 0], 'POW.FC2.Alpha ': [386, 278, 0], 'POW.FC2.BetaL ': [386, 278, 0], 'POW.FC2.BetaH ': [386, 276, 0], 'POW.FC2.Gamma ': [386, 276, 0], 'POW.F4.Theta ': [416, 211, 0], 'POW.F4.Alpha ': [416, 209, 0], 'POW.F4.BetaL ': [416, 209, 0], 'POW.F4.BetaH ': [416, 209, 0], 'POW.F4.Gamma ': [416, 209, 0], 'POW.F8.Theta ': [501, 202, 0], 'POW.F8.Alpha ': [501, 202, 0], 'POW.F8.BetaL ': [501, 200, 0], 'POW.F8.BetaH ': [501, 200, 0], 'POW.F8.Gamma ': [501, 200, 0], 'POW.Fp2.Theta ': [385, 122, 0], 'POW.Fp2.Alpha ': [385, 122, 0], 'POW.Fp2.BetaL ': [385, 122, 0], 'POW.Fp2.BetaH ': [385, 121, 0], 'POW.Fp2.Gamma ': [385, 121, 0]}

# ... (your existing code above)
# Load the existing image
image_path = 'emotivdiagram.jpg'
img = Image.open(image_path)

# Create a figure and axes
fig, ax = plt.subplots(1)
# Read alpha_max counts from the CSV file and update location_dict
max_alpha_counts = 0  # Variable to store the maximum alpha_max count

with open('happy_michael.csvdictionaryoutput.txtalpha_max_counts.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Row is{", ".join(row)}')
            line_count += 1
        try:
            location_dict[row[0]][2] += int(row[1])
            
            # Update max_alpha_counts if a new maximum is found
            if int(row[1]) > max_alpha_counts:
                max_alpha_counts = int(row[1])
        except:
            continue
        continue

    print(f'Processed {line_count} lines.')

# Calculate scaling factor
scaling_factor = 35 / max_alpha_counts

# Plot circles on the image
for key, circle in location_dict.items():
    x, y, radius = [int(val) for val in circle]  # Convert floats to integers
    
    # Scale radius based on alpha_max counts
    scaled_radius = radius * scaling_factor
    
    # Create a circle patch
    circle_patch = patches.Circle((x, y), scaled_radius, edgecolor='r', facecolor='r', label=key)
    
    # Add the circle patch to the axes
    ax.add_patch(circle_patch)

# Display the image with circles
ax.imshow(img)
# ax.legend(loc='upper right')  # Add legend for labels
plt.show()
