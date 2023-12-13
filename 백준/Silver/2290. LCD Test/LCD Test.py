import sys


def draw_lcd(dash, num):
    board_row = 2 * dash + 3
    board = [get_row(row, num, dash) for row in range(board_row)]
    return board


def get_row(row_index, num, dash):
    result = ""
    for number in list(map(int, list(str(num)))):
        if is_upper_horizontal_row(row_index, dash):
            if number != 1 and number != 4:
                result += " " + "-" * dash + " "
            else:
                result += " " * (dash + 2)
        elif is_center_horizontal_row(row_index, dash):
            if number != 1 and number != 7 and number != 0:
                result += " " + "-" * dash + " "
            else:
                result += " " * (dash + 2)
        elif is_lower_horizontal_row(row_index, dash):
            if number != 1 and number != 4 and number != 7:
                result += " " + "-" * dash + " "
            else:
                result += " " * (dash + 2)
        elif is_upper_vertical_row(row_index, dash):
            if number == 1 or number == 2 or number == 3 or number == 7:
                result += " " * (dash + 1) + "|"
            elif number == 5 or number == 6:
                result += "|" + " " * (dash + 1)
            else:
                result += "|" + " " * dash + "|"
        else:
            if number == 2:
                result += "|" + " " * (dash + 1)
            elif number == 6 or number == 8 or number == 0:
                result += "|" + " " * dash + "|"
            else:
                result += " " * (dash + 1) + "|"
        result += ' '

    return result


def is_upper_horizontal_row(row_index, dash):
    return row_index == 0


def is_center_horizontal_row(row_index, dash):
    return row_index == dash + 1


def is_lower_horizontal_row(row_index, dash):
    return row_index == 2 * dash + 2


def is_upper_vertical_row(row_index, dash):
    return 1 <= row_index <= dash


s, n = list(map(int, sys.stdin.readline().strip().split()))
answer = draw_lcd(s, n)
expect = ['      --   --        --   --   --   --   --   --  ',
          '   |    |    | |  | |    |       | |  | |  | |  | ',
          '   |    |    | |  | |    |       | |  | |  | |  | ',
          '      --   --   --   --   --        --   --       ',
          '   | |       |    |    | |  |    | |  |    | |  | ',
          '   | |       |    |    | |  |    | |  |    | |  | ',
          '      --   --        --   --        --   --   --  ']
for i, row in enumerate(answer):
    # print(expect[i] == row)
    print(row)
