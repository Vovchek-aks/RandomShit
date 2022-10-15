class Parser:
    order = {
        '^': (lambda x, y: x**y, None),
        '*': (lambda x, y: x * y, lambda x: x),
        '/': (lambda x, y: x / y, lambda x: x + '^(-1)'),
        '+': (lambda x, y: x + y, lambda x: x),
        '-': (lambda x, y: x - y, lambda x: x + '*(-1)')
    }

    @classmethod
    def parse(cls, s: str | float) -> float:
        if isinstance(s, str):
            s = ''.join(s.split())

        if s == '':
            return 0

        try:
            return float(s)
        except ValueError:
            pass

        if s[0] == '(' and s[-1] == ')':
            return Parser.parse(s[1:-1])

        shit = []
        r = ''
        c = 0
        while s:
            r += s[0]
            s = s[1:]

            if r[-1] != r and r[-1] in cls.order and c == 0:
                shit.append(r[:-1])
                shit.append(r[-1])
                r = ''
                continue

            if r[-1] == '(':
                c += 1
                if c == 1 and r[0] in ['+', '-']:
                    shit.append(r[0])
                    r = r[1:]
            elif r[-1] == ')':
                c -= 1
        shit.append(r)
        shit = list(filter(lambda x: x, shit))

        ss = []
        for j, jj in enumerate(shit):
            if jj in ('-', '/'):
                ss.append(cls.order[jj][1](shit[j + 1]))
                continue
            ss.append(jj)
        shit = ss

        for i in cls.order:
            while i in shit:
                n = shit.index(i) - 1
                if n < 0:
                    shit.insert(0, shit.pop(0) + str(Parser.parse(shit.pop(0))))
                if len(shit) < 3:
                    break
                g = []
                for j in range(3):
                    g.append(shit.pop(n))
                shit.insert(n, cls.order[g[1]][0](Parser.parse(g[0]), Parser.parse(g[-1])))

        return shit[0]


if __name__ == '__main__':
    f = input("введите математическое выражение\nдоступные операции - (+, -, *, /, ^)\n")
    print(f'{f} = {Parser.parse(f)} =\n{" " * len(f)} = {eval(f.replace("^", "**"))} (eval для проверки)')
