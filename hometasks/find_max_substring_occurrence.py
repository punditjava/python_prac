import math
import re


def find_max_substring_occurrence(input_string):
    for k in range(1, int(len(input_string) // 2) + 1):
        reg_exp = r"(\w{" + str(k) + r"})\1{" \
                  + str(math.ceil((len(input_string) / k - 1))) + r"}"
        k = re.findall(reg_exp, input_string)
        if len(k) != 0:
            return int(len(input_string) / len(k[0]))
    return 1
