import json
import sys
import re

def extract_json_from_js(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    print("File starts with:", content[:200])
    
    # Try to find the assignment
    match = re.search(r'window\.YTD\.tweets\.part0\s*=\s*(\[[\s\S]*)', content, re.DOTALL)
    if not match:
        raise ValueError("Could not find window.YTD.deleted_tweets.part0 assignment in the file")
    
    json_str = match.group(1)
    
    # Try to find the end of the JSON array
    bracket_count = 0
    for i, char in enumerate(json_str):
        if char == '[':
            bracket_count += 1
        elif char == ']':
            bracket_count -= 1
            if bracket_count == 0:
                json_str = json_str[:i+1]
                break
    
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {str(e)}")
        print("Problematic JSON string:", json_str[:200])  # Print the first 200 characters of the JSON string
        raise

def process_deleted_tweets(input_file, output_file):
    data = extract_json_from_js(input_file)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in data:
            tweet = item.get('tweet', {})
            if not tweet.get('retweeted', True):
                full_text = tweet.get('full_text', '')
                if full_text:
                    f.write(full_text + '\n\n')

    print(f"Processing complete. Output written to {output_file}")
    print(f"Total tweets processed: {len(data)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.js output.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        process_deleted_tweets(input_file, output_file)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)
