def convert_text_to_json(input_file, output_file):
    # Read the file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by <data> tags and clean up
    paragraphs = content.split('<data>')

    # Create json format
    json_data = []

    for para in paragraphs:
        # Clean the paragraph
        para = para.strip()

        # Skip empty paragraphs
        if para:
            json_data.append({
                "text": para
            })

    # Write to JSON file
    import json
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully converted {len(json_data)} paragraphs to JSON format")
    return json_data


# Example usage
input_file = "data"  # Replace with your input file name
output_file = "entity_Data.json"

data = convert_text_to_json(input_file, output_file)
print(data)

