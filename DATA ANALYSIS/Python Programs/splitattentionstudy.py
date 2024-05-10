import csv
import os

def filter_csv(input_file, output_file, ranges_to_keep):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, input_file)
    output_path = os.path.join(script_dir, output_file)
    
    with open(input_path, 'r', newline='') as infile, \
         open(output_path, 'w', newline='') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row_num, row in enumerate(reader):
            keep_row = False
            for start, end in ranges_to_keep:
                if start <= row_num < end:
                    keep_row = True
                    break
            if keep_row or row_num < 2:  # Always keep the first two rows
                writer.writerow(row)

# Example usage:
headers = (1,2)
input_file_name = '013127'
input_file_extension = '.csv.txt'
input_file = input_file_name + input_file_extension

start_row = 2011
end_row = 7000
output_file = 'baseline'+ input_file_name + '.csv'
ranges_to_keep = [headers,(start_row,end_row)]  # Example ranges to keep
filter_csv(input_file, output_file, ranges_to_keep)


start_row = 7259
end_row = 4
output_file = 'math'+ input_file_name + '.csv'
ranges_to_keep = [headers,(start_row,end_row)]  # Example ranges to keep
filter_csv(input_file, output_file, ranges_to_keep)


start_row = 3
end_row = 4
output_file = 'navon'+ input_file_name + '.csv'
ranges_to_keep = [headers,(start_row,end_row)]  # Example ranges to keep
filter_csv(input_file, output_file, ranges_to_keep)

start_row = 3
end_row = 4
output_file = 'stroop'+ input_file_name + '.csv'
ranges_to_keep = [headers,(start_row,end_row)]  # Example ranges to keep
filter_csv(input_file, output_file, ranges_to_keep)

start_row = 3
end_row = 4
output_file = 'corsi'+ input_file_name + '.csv'
ranges_to_keep = [headers,(start_row,end_row)]  # Example ranges to keep
filter_csv(input_file, output_file, ranges_to_keep)




start_row = 2011
end_row = 7000
output_file = 'binuralBeats'+ input_file_name + '.csv'
ranges_to_keep = [headers,(start_row,end_row)]  # Example ranges to keep
filter_csv(input_file, output_file, ranges_to_keep)


start_row = 7259
end_row = 4
output_file = 'math_after_binural_beats'+ input_file_name + '.csv'
ranges_to_keep = [headers,(start_row,end_row)]  # Example ranges to keep
filter_csv(input_file, output_file, ranges_to_keep)


start_row = 3
end_row = 4
output_file = 'navon_after_binural_beats'+ input_file_name + '.csv'
ranges_to_keep = [headers,(start_row,end_row)]  # Example ranges to keep
filter_csv(input_file, output_file, ranges_to_keep)

start_row = 3
end_row = 4
output_file = 'stroop_after_binural_beats'+ input_file_name + '.csv'
ranges_to_keep = [headers,(start_row,end_row)]  # Example ranges to keep
filter_csv(input_file, output_file, ranges_to_keep)

start_row = 3
end_row = 4
output_file = 'corsi_after_binural_beats'+ input_file_name + '.csv'
ranges_to_keep = [headers,(start_row,end_row)]  # Example ranges to keep
filter_csv(input_file, output_file, ranges_to_keep)
