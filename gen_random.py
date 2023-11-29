def logical_xor(str1, str2):
    return bool(str1) != bool(str2)


def find_gen_str1(x):
    answer = []
    x = [int(_) for _ in list(x)]
    for i in range(14):
        # print(x[0], end='')
        answer.append(x[0])
        buf0 = x[0]
        buf1 = x[1]
        buf2 = x[2]
        x[0] = x[1]
        x[1] = x[2]
        x[2] = int(logical_xor(buf0, buf2))
    # print('')
    return answer


def find_gen_str3(x):
    answer = []
    x = [int(_) for _ in list(x)]
    for i in range(14):
        # print(x[0], end='')
        answer.append(x[0])
        buf0 = x[0]
        buf1 = x[1]
        buf2 = x[2]
        x[0] = x[1]
        x[1] = x[2]
        x[2] = int(logical_xor(buf0, buf1))
    # print('')
    return answer


def find_gen_str2(x):
    answer = []
    x = [int(_) for _ in list(x)]
    for i in range(14):
        # print(x[0], end='')
        answer.append(x[0])
        buf0 = x[0]
        buf1 = x[1]
        buf2 = x[2]
        x[0] = x[1]
        x[1] = x[2]
        x[2] = int(logical_xor(buf0, buf1))
        x[2] = int(logical_xor(x[2], buf2))
    # print('')
    return answer


def f(x1, x2, x3):
    answer = logical_xor(x1, x1 * x2)
    return int(logical_xor(answer, x2 * x3))


def generator_and_analyze(x1, x2, x3):
    answer = list('10110001111000')
    answer = [int(_) for _ in answer]
    # print(f'x1={x1} x2={x2} x3={x3}')
    x1_part = find_gen_str1(x1)
    x2_part = find_gen_str2(x2)
    x3_part = find_gen_str3(x3)
    your_answer = []
    for i in range(len(x1_part)):
        your_answer.append(f(x1_part[i], x2_part[i], x3_part[i]))
    print(f'y={your_answer}')
    # print(f'a={answer}')
    # print(answer==your_answer)
    # print('')
    return answer == your_answer


if __name__ == '__main__':
    x1 = ['001', '010', '011', '100', '101', '110', '111']
    x3 = ['001', '010', '011', '100', '101', '110', '111']
    x2 = ['001', '010', '011', '100', '101', '110', '111']
    for x1_ in x1:
        for x2_ in x2:
            for x3_ in x3:
                if (generator_and_analyze(x1_, x2_, x3_)):
                    print(x1_, x2_, x3_)
                    break
    x11 = '110'
    x22 = '011'
    x33 = '101'
    for x2_ in x2:
        print(find_gen_str2(x2_))
