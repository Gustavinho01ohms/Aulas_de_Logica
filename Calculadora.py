while True:
    print("######## CALCULADORA 2.0 ########")
    op = input("Digite a operação: ")
    print(op)
    sub = op.find("-")
    som = op.find("+")
    mult = op.find("*")
    div = op.find("/")


    if sub >= 1:
        ope = 1
        op = op.replace("-"," ")
    elif som >= 1:
        ope = 2
        op = op.replace("+"," ")
    elif mult >= 1:
        ope = 3
        op = op.replace("*"," ")
    elif div >= 1:
        ope = 4
        op = op.replace("/"," ")
    elif op == "":
        break
    else:
        ope = 5


    match ope:
        case 1:
            op = op.split()
            a = int(op[0])
            b = int(op[1])
            print(a - b)
        case 2:
            op = op.split()
            a = int(op[0])
            b = int(op[1])
            print(a + b)
        case 3:
            op = op.split()
            a = int(op[0])
            b = int(op[1])
            print(a * b)
        case 4:
            op = op.split()
            a = int(op[0])
            b = int(op[1])
            print(a / b)
        case 5:
            print("Você não digitou uma operação válida!")
