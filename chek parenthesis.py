pairs_of_parentheses = {")": "(", "]": "["}


def check_parenthesis(string):
    stack = []

    for parenthesis in string:
        if parenthesis in "([":
            stack.append(parenthesis)
        elif parenthesis in "])":
            if len(stack) > 0 and stack[-1] == pairs_of_parentheses[parenthesis]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(check_parenthesis('()(([][])]]]()))()((()'))
# False
print(check_parenthesis('([]()(()(()())))'))
# True
