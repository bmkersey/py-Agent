from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

# result = get_files_info("calculator", ".")
# print(f'Result for current directory:\n{result}')

# result = get_files_info("calculator", "pkg")
# print(f'Result for pkg directory:\n{result}')

# result = get_files_info("calculator", "/bin")
# print(f'Result for /bin directory:\n{result}')

# result = get_files_info("calculator", "../")
# print(f'Result for ../ directory:\n{result}')

# result = get_file_content("calculator", "main.py")
# print(f'Result for main.py: {result}')
# result = get_file_content("calculator", "pkg/calculator.py")
# print(f'Result for pkg/calculator.py: {result}')
# result = get_file_content("calculator", "/bin/cat")
# print(f'Result for /bin/cat: {result}')
# result = get_file_content("calculator", "pkg/does_not_exist.py")
# print(f'Result for pkg/does_not_exist.py: {result}')

result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(f'Result for lorem.txt: {result}')

result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(f'Result for pkg/morelorem.txt: {result}')

result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(f'Result for /tmp/temp.txt: {result}')