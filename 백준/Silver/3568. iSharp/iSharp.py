import sys

def_statement = sys.stdin.readline().strip()

semicolon_removed = def_statement[:-1]
split_with_ws = semicolon_removed.split()
base_var = split_with_ws[0]
variables = [base_var] * (len(split_with_ws) - 1)
for index, variable in enumerate(split_with_ws[1:]):
    j = 0
    while j < len(variable) and variable[j].isalpha():
        j += 1

    var_name, rem = variable[:j], variable[j:]

    k = len(rem) - 1
    var_appendix = ""
    while k >= 0:
        if rem[k] == '&' or rem[k] == '*':
            var_appendix += rem[k]
            k -= 1
        elif rem[k] == ']':
            var_appendix += '[]'
            k -= 2
        else:
            k -= 1

    variables[index] += var_appendix
    variables[index] += " "
    variables[index] += var_name + ";"

for variable in variables:
    print(variable)
