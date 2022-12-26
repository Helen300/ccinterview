def isBalanced(s):
    stack = [] 
    mapping = {'(': ')', '[': ']', '{': '}'}
    for p in s: 
        if p in mapping.keys(): 
            stack.append(p)
        else:
            if stack: 
                prev = stack.pop()
                if mapping[prev] != p:
                    return 'NO'
            else: 
                return 'NO'
    if stack: 
        return 'NO'
    return 'YES'

if __name__ == '__main__':

    t = 6
    s = ['}][}}(}][))]', '[](){()}', '()', '({}([][]))[]()', '{)[](}]}]}))}(())(', '([[)]']

    for p in s:

        result = isBalanced(p)

        print(result + '\n')



