import jsonFileHandler
import os

# Build the correct absolute path dynamically
base_dir = os.path.dirname(__file__)
json_path = os.path.join(base_dir, "files", "insulin.json")

data = jsonFileHandler.readJsonFile(json_path)

if data:
    weights = data["weights"]
    amino_acids = data["amino_acids"]

    total_weight = sum(weights[aa] * count for aa, count in amino_acids.items())
    print(f"Total molecular weight of insulin: {total_weight:.2f}")
else:
    print("Error. Exiting program")
