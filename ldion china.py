def idiom_game():
    idiom_list = []  # 存储已经使用过的成语

    while True:
        if not idiom_list:
            idiom = input("请输入一个成语：")
            idiom_list.append(idiom)
        else:
            last_idiom = idiom_list[-1]
            first_char = last_idiom[-1]
            idiom = input("请输入一个以'" + first_char + "'开头的成语：")
            idiom_list.append(idiom)

        if not validate_idiom(idiom):
            print("输入的成语无效，请重新输入！")
            idiom_list.pop()  # 移除无效的成语
            continue

        if idiom in idiom_list[:-1]:
            print("你输入的成语已经使用过了，请重新输入！")
            idiom_list.pop()  # 移除重复的成语
            continue

        if idiom == "退出":
            print("游戏结束！")
            break

        print("电脑回答：" + get_computer_response(idiom))
    
def validate_idiom(idiom):
    # 在这里添加验证成语的逻辑，比如判断长度、首尾字等
    return True  # 假设所有输入都是有效的成语

def get_computer_response(idiom):
    # 在这里添加电脑生成回答的逻辑，比如随机选择一个成语
    return "电脑回答的成语"

idiom_game()
