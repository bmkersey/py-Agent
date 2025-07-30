from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# result = get_files_info("calculator", ".")
# print(f'Result for current directory:\n{result}')

# result = get_files_info("calculator", "pkg")
# print(f'Result for pkg directory:\n{result}')

# result = get_files_info("calculator", "/bin")
# print(f'Result for /bin directory:\n{result}')

# result = get_files_info("calculator", "../")
# print(f'Result for ../ directory:\n{result}')

result = get_file_content("calculator", "main.py")
print(f'Result for main.py: {result}')
result = get_file_content("calculator", "pkg/calculator.py")
print(f'Result for pkg/calculator.py: {result}')
result = get_file_content("calculator", "/bin/cat")
print(f'Result for /bin/cat: {result}')
result = get_file_content("calculator", "pkg/does_not_exist.py")
print(f'Result for pkg/does_not_exist.py: {result}')