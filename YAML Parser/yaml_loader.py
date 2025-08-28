import yaml

yaml_file_path = "error_test.yaml"

try:
    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)

    print(data)

except FileNotFoundError:
    print(f"Error: The file '{yaml_file_path}' was not found.")
except yaml.YAMLError as e:
    print(f"Error parsing YAML file: {e}")