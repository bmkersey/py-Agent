import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
  absolute_path = os.path.join(working_directory, file_path)
  if not os.path.abspath(absolute_path).startswith(os.path.abspath(working_directory)):
    return f'Error: Cannot read "{file_path}" as it is outside the working directory'
  
  if not os.path.isfile(absolute_path):
    return f'File not found or is not a regular file: "{file_path}"'
  

  try:
    with open(absolute_path, "r") as f:
      file_content_string = f.read(MAX_CHARS)
      if len(file_content_string) == MAX_CHARS:
        file_content_string = file_content_string + f'[...File "{file_path}" truncated at 10000 characters]'    
  except Exception as e:
    return f'Error: {e}'

  return file_content_string