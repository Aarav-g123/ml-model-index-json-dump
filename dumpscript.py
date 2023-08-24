import json
from safetensors import safe_open

# Load the safetensors file
with safe_open("path/to/model.safetensors", framework="pt", device="cpu") as f:
    tensors = f.get_tensors()

# Create the model_index.json file
model_index = {
    "model": "modelname",
    "files": {
        "safetensors": "path/to/model.safetensors"
    },
    "tensors": tensors
}

# Save the model_index.json file
with open("path/to/model_index.json", "w") as f:
    json.dump(model_index, f)
