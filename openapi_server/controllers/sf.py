def str_to_func(code_str):
    code = compile(code_str, '<string>', 'eval')

    def f(v, params):
        return eval(code, {"p": params, "V": v})
    return f


if __name__ == '__main__':
    code = "v * p[0] + p[1]"
    f = str_to_func(code)
    print(f(3, [2, 1]))
