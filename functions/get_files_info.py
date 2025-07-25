import os


def get_files_info(working_directory, directory="."):
  absolute_path = os.path.join(working_directory, directory)
  if not os.path.abspath(absolute_path).startswith(os.path.abspath(working_directory)):
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
  
  if not os.path.isdir(absolute_path):
    return f'Error: "{directory}" is not a directory'
  
  try:
    files = os.listdir(absolute_path)
    return_string = ""
    for file in files:
      return_string = return_string + f'-{file}: file_size={os.path.getsize(os.path.join(absolute_path, file))} bytes, is_dir={os.path.isdir(os.path.join(absolute_path, file))}\n'
  except Exception as e:
    return f'Error: {e}'
  
  return return_string