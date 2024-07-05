import sys

#reads from text from standard input
input_code = ""
for line in sys.stdin:
    input_code += line  
echo_code = input_code + "Success!"
print(echo_code)


