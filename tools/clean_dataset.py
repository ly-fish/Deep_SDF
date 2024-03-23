import os
import json

def handle_json_files(splits_folder, dataset_folder):
    filtered_data = {}
    filtered_sub_sub_value = []
    
    for filename in os.listdir(splits_folder):
        file_path = os.path.join(splits_folder, filename)
        if os.path.isfile(file_path) and filename.endswith('.json'):
            with open(file_path, 'r') as file:

                try:
                    json_data = json.load(file)
                    filtered_data = json_data

                    for key, value in json_data.items():
                        if isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if isinstance(sub_key, str) and isinstance(sub_value, list): 
                                    dataset_subfolder = os.path.join(dataset_folder, sub_key)

                                    if not os.path.exists(dataset_subfolder) or not os.path.isdir(dataset_subfolder):
                                            raise FileNotFoundError(f"The file '{dataset_subfolder}' does not exist. so...sad")
                                    npz_files = os.listdir(dataset_subfolder)
                                    
                                    for sub_sub_value in sub_value:
                                        is_match = is_matched_file(sub_sub_value, npz_files)
                                        if is_match:
                                            continue
                                        else:
                                            filtered_data[key][sub_key].remove(sub_sub_value)
                                            filtered_sub_sub_value.append(sub_sub_value)
                except Exception as e:
                    print(f"An error occurred while processing file {filename}: \n {e}")

        save_filted_info(filename, filtered_sub_sub_value)
        rewrite_splite_file(filtered_data, file_path)

    
    return filtered_data


def save_filted_info(filename, filtered_sub_sub_value):
    file_name = filename + "filtered_sub_sub_value.txt"
    with open(file_name, 'w') as file:
        file.write(json.dumps(filtered_sub_sub_value))


#####################
# Check the item in .json can match with file (.npz)
#####################
def is_matched_file(sub_sub_value, npz_files):
    for file_name in npz_files:
        if file_name.startswith(sub_sub_value) and file_name.endswith(".npz"):
            return True
    return False




#####################
# Rewrite the JSON files with the filtered data
#####################
def rewrite_splite_file(filtered_data, file_path):
    with open(file_path, "w") as file:
        json.dump(filtered_data, file, indent=4)




if __name__ == "__main__":
    splits_folder = "/home/liangyue/project/yly/DeepSDF/examples/splits"
    dataset_folder = "/home/liangyue/project/yly/DeepSDF/data/SdfSamples/ShapeNetV2"
    if not os.path.exists(splits_folder) or not os.path.exists(dataset_folder):
        raise FileNotFoundError(f"The file folderremove_invalid_values does not exist.")
    
    filtered_data = handle_json_files(splits_folder, dataset_folder)


