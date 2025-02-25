# Import necessary module from oocana
from oocana import Context

# Function to read a markdown file
def read_markdown_file(file_path):
  try:
      with open(file_path, 'r', encoding='utf-8') as file:
          return file.read()
  except FileNotFoundError:
      print(f"Error: File {file_path} not found.")
      return None
  except Exception as e:
      print(f"Error: An error occurred while reading the file - {e}")
      return None

# Main function that takes parameters and context as input
def main(params: dict, context: Context):
  # Extract required parameters
  csv_file_3d = params.get("csv_file_3d")
  markdown_file = params.get("markdown")

  # Check if required parameters are present
  if csv_file_3d is None or markdown_file is None:
    raise ValueError("The parameter 3d_csv_filr is required")

  # Return a dictionary containing various media URLs and markdown content
  return { 
    "csv_file_3d": csv_file_3d,
    "image": "https://oomol-flows.oss-cn-hangzhou.aliyuncs.com/colin-watts-2fWZ9jsoIe0-unsplash.jpg",
    "video": "https://oomol-flows.oss-cn-hangzhou.aliyuncs.com/204565-924698132_small.mp4",
    "audio": "https://oomol-flows.oss-cn-hangzhou.aliyuncs.com/celebrated.mp3",
    "markdown": read_markdown_file(markdown_file),
  }