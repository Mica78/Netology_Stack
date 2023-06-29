class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if self.stack:
            return False
        return True

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        result = self.stack[-1]
        del self.stack[-1]
        return result

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def main(string):
    dct = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    stack = Stack()
    for simbol in string:
        if simbol in dct.keys():
            stack.push(simbol)
        else:
            if stack.isEmpty():
                if simbol in dct.keys():
                    stack.push(simbol)
                else:
                    return "Not balanced"
            else:
                if dct.get(stack.peek()) == simbol:
                    stack.pop()
                else:
                    break

    if stack.isEmpty():
        return "Balanced"
    return "Not balanced"


if __name__ == '__main__':
    assert main("(((([{}]))))") == "Balanced"
    assert main("[([])((([[[]]])))]{()}") == "Balanced"
    assert main("{{[()]}}") == "Balanced"
    assert main("}{}") == "Not balanced"
    assert main("{{[(])]}}") == "Not balanced"
    assert main("[[{())}]") == "Not balanced"
    assert main("()[]}") == "Not balanced"
    assert main("{{[()]]") == "Not balanced"
    assert main("{{{[][][]") == "Not balanced"
    assert main("{{{}") == "Not balanced"
    assert main("[[") == "Not balanced"
    assert main("{}") == "Balanced"
    assert main("{{") == "Not balanced"
    assert main("") == "Balanced"
    assert main("}") == "Not balanced"
    assert main('{}[]') == "Balanced"
    assert main('[()]') == "Balanced"
    assert main('(())') == "Balanced"
    assert main('{[]}()') == "Balanced"
    assert main('([](){([])})') == "Balanced"
    assert main('{') == "Not balanced"
    assert main('{[}') == "Not balanced"
    assert main('()[]}') == "Not balanced"
    assert main('{{[()]]') == "Not balanced"
    assert main('[]([]') == "Not balanced"
