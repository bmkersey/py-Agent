import os

def write_file(working_directory, file_path, content):
  absolute_path = os.path.join(working_directory, file_path)
  if not os.path.abspath(absolute_path).startswith(os.path.abspath(working_directory)):
    return f'Error: Cannot use "{file_path}" as it is outside the permitted working directory'
  
  try:
    parent_dir = os.path.dirname(absolute_path)
    if not os.path.exists(parent_dir):
      os.makedirs(parent_dir, exist_ok=True)

    with open(absolute_path, "w") as f:
      f.write(content)
  except Exception as e:
    return f'Error: {e}'
  
  return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  


