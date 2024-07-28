# Tweets Extractor

## Description

This Python script extracts the full text of non-retweeted tweets from a JavaScript file containing deleted tweets data. It's designed to work with files exported from Twitter that contain deleted tweet information.

## Requirements

- Python 3.6 or higher
- No additional libraries required (uses only built-in Python modules)

## Usage

1. Save the script as `js-array-to-text-converter.py` (or any name you prefer).

2. Run the script from the command line using the following format:

   ```
   python js-array-to-text-converter.py <input_file> <output_file>
   ```

   Where:
   - `<input_file>` is the path to your JavaScript file containing the deleted tweets data.
   - `<output_file>` is the path where you want the extracted tweets to be saved.

   Example:
   ```
   python js-array-to-text-converter.py tweets.js extracted_tweets.txt
   ```

3. The script will process the input file and create a new text file containing the extracted tweets.

## Input File Format

The script expects the input file to be a JavaScript file with the following structure:

```javascript
window.YTD.tweets.part0 = [
  {
    "tweet": {
      // tweet data
    }
  },
  // more tweet objects...
];
```

## Output

The script will create a text file containing the full text of each non-retweeted tweet, with each tweet separated by a blank line.

## Error Handling

If the script encounters any errors while processing the file, it will print an error message to the console. Common errors include:

- File not found
- Invalid file format
- JSON parsing errors

## Limitations

- The script only extracts tweets where the 'retweeted' field is false.
- It assumes the 'full_text' field contains the tweet content.
- Very large input files may take some time to process.

## Troubleshooting

If you encounter any issues:

1. Ensure your input file has the correct format.
2. Check that you have the necessary permissions to read the input file and write to the output location.
3. Verify that you're using a compatible version of Python.

If problems persist, run the script and provide the full console output for further assistance.

## License

This script is provided "as is", without warranty of any kind. Feel free to use and modify it as needed.

