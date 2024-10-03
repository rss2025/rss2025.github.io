import csv

# Replace these with your actual file paths
source_csv_path = 'rss2024CameraReadyPS.csv'
output_csv_path = 'RSS24-CameraReadyIntegration.csv'


with open(source_csv_path, newline='') as source_file:
    csvreader = csv.reader(source_file)
    
    with open(output_csv_path, 'w', newline='') as output_file:
        csvwriter = csv.writer(output_file)
        
        for row in csvreader:
            # Ensure there are at least 3 columns to concatenate
            if len(row) >= 3:
                # Concatenate the first three columns
                abstract = row[2].replace('\n', ' ')
                print(abstract)
                concatenated_columns = f"{row[0]}#{row[1]}#{abstract}"
                
                # If there's a fourth column, replace commas with semicolons in it
                if len(row) > 3:
                    names_list = row[3].split(',')
                    # For each name, get the surname (last part after splitting by space)
                    surnames = [name.strip().split(' ')[-1] for name in names_list]

                    fourth_column_modified = row[3].replace(',', ';')
                    # Concatenate the modified fourth column with the first three
                    concatenated_columns += f"#{fourth_column_modified}"
                    concatenated_columns += f"#{surnames[0]}"
                    
                
                # Write the concatenated data, followed by any remaining columns
                csvwriter.writerow([concatenated_columns] + row[4:])
            else:
                # If there are less than 3 columns, just write the original row
                csvwriter.writerow(row)