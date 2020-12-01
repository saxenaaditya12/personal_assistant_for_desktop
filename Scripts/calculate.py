import the_voice

add_exp = ["+",
           "add",
           "plus",
           "sum"]
sub_exp = ["-",
           "subtract",
           "minus",
           "sub"]
mul_exp = ["*",
           ".",
           "x",
           "multiply",
           "multiplied by",
           "into",
           "times",
           "product"]
pow_exp = ["**",
           "^",
           "power",
           "raise"]
percent_exp = ["percent",
               "% of",
               "%of"]
rem_exp = ["%",
           "remainder",
           "modulus"]
div_exp = ["/",
           "divide",
           "divisor",
           "by",
           "divided by"]

all_operations = [add_exp,
                  sub_exp,
                  mul_exp,
                  pow_exp,
                  percent_exp,
                  rem_exp,
                  div_exp]


def calc(exp):
    op = []
    operation = []
    try:
        exp_list = exp.split()
        for i in exp_list:
            try:
                op.append(float(i))
            except:
                operation.append(i)

        if 0 <= len(op) < 2:
            temp_num = []
            temp_operator = []
            for i in operation:
                for digit in i:
                    if digit.isdigit():
                        temp_num.append(digit)
                        if len(temp_operator) != 0:
                            temp_operator = "".join(temp_operator)
                            operation.append(temp_operator)
                            temp_operator = list()
                    else:
                        temp_operator.append(digit)
                        if len(temp_num) != 0:
                            temp_num = float("".join(temp_num))
                            op.append(temp_num)
                            temp_num = list()

            if len(temp_num) != 0:
                temp_num = float("".join(temp_num))
                op.append(temp_num)
            if len(temp_operator) != 0:
                temp_operator = "".join(temp_operator)
                operation.append(temp_operator)
            operation = operation[1:]

        if len(operation) != 0:
            operation = " ".join(operation)
        else:
            print("No operation found!")
            return
        if len(op) != 2:
            print("Only 2 operands are allowed, found " + str(len(op)))
            return
    except:
        print("Not a valid mathematical expression!")
        return

    op_to_do = None
    flag = 0
    for one_op in all_operations:
        for j in one_op:
            if j in operation:
                op_to_do = one_op[0]
                flag = 1
                break
        if flag == 1:
            break
    res = None
    if op_to_do is None:
        print("Sorry don't know how to do that!")
        return
    elif op_to_do == "+":
        res = op[0] + op[1]
    elif op_to_do == "-":
        res = op[0] - op[1]
    elif op_to_do == "*":
        res = op[0] * op[1]
    elif op_to_do == "/":
        res = op[0] / op[1]
    elif op_to_do == "**":
        res = op[0] ** op[1]
    elif op_to_do == "percent":
        res = (op[0] / 100) * op[1]
    elif op_to_do == "%":
        res = int(op[0]) % int(op[1])
    return res


def start():
    the_voice.say_and_print("Say what you want to calculate?")
    ex = the_voice.listening()
    while True:
        try:
            ex.lower()
        except:
            print("Say the expression or \"CANCEL\" to cancel")
            ex = the_voice.listening()
            continue
        if ex == "cancel":
            the_voice.say_and_print("okay!")
            return
        result = (calc(ex))
        if result is not None:
            the_voice.say_and_print(str(result))
        print("Say the expression or \"CANCEL\" to cancel")
        ex = the_voice.listening()
