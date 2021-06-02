"""
Function which find first repeated symbol in list
"""


def repeat_symbol(symbol_list):
    for i in range(len(symbol_list)):
        if i != symbol_list.index(symbol_list[i]):
            return symbol_list[i]  # return repeated symbol
            break


"""
Solutions for testing function
Output will be "a"
"""
symbols = ['b', 'a', 'c', 'a', 'd']  # tested list
print(c)
print(repeat_symbol(symbols))  # output repeated symbol
