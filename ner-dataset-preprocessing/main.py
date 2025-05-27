def convert_ner_format(input_json_list):
    """
    Convert a list of Label Studio NER annotations to spaCy-like format.

    Args:
        input_json_list (list): List of input JSONs from Label Studio export

    Returns:
        list: List of converted documents in the desired format
    """
    converted_documents = []

    for document in input_json_list:
        # Extract the text
        text = document['data']['text']

        # Extract entities from annotations
        entities = []
        if document['annotations']:
            # Get the first annotation result (assuming one annotation per document)
            for result in document['annotations'][0]['result']:
                if result['type'] == 'labels':
                    # Extract start, end, and label
                    start = result['value']['start']
                    end = result['value']['end']
                    label = result['value']['labels'][0]  # Taking first label if multiple

                    # Add tuple to entities list
                    entities.append((start, end, label))

        # Sort entities by start position
        entities.sort(key=lambda x: x[0])

        # Add the converted document to our list
        converted_documents.append({
            "text": text,
            "entities": entities
        })

    return converted_documents


# Example usage
import json

# Load your JSON file
with open('project-2-at-2024-11-01-11-20-d91a70be.json', 'r', encoding='utf-8') as file:
    input_data = json.load(file)  # This will be a list of documents

# If your JSON file contains a single document wrapped in a list
if not isinstance(input_data, list):
    input_data = [input_data]

# Convert to new format
converted_data = convert_ner_format(input_data)
print(converted_data)
