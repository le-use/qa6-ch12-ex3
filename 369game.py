for i in range(100, 1, -1):
    print(i, "번째 실행 : ", end="")

    str_i = str(i)
    if "3" in str_i or "6" in str_i or "9" in str_i:
        print("짝" * (str_i.count("3") + str_i.count("6") + str_i.count("9")))
    else:
        print(i)
