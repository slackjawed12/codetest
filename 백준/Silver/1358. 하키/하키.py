import sys

W, H, X, Y, P = list(map(int, sys.stdin.readline().strip().split()))
positions = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(P)]


def is_in_field(x, y, width, height, origin_x, origin_y):
    is_in_rect = in_rectangle(x, y, width, height, origin_x, origin_y)
    is_in_left_circle = in_left_circle(x, y, height, origin_x, origin_y)
    is_in_right_circle = in_right_circle(x, y, width, height, origin_x, origin_y)
    return is_in_rect or is_in_right_circle or is_in_left_circle


def in_rectangle(x, y, width, height, origin_x, origin_y):
    return origin_x <= x <= origin_x + width and origin_y <= y <= origin_y + height


def in_left_circle(x, y, height, origin_x, origin_y):
    x_diff = (x-origin_x) ** 2
    y_diff = (y-(origin_y+(height//2))) ** 2
    return x_diff + y_diff <= (height//2) ** 2


def in_right_circle(x, y, width, height, origin_x, origin_y):
    x_diff = (x-(origin_x+width)) ** 2
    y_diff = (y-(origin_y+(height//2))) ** 2
    return x_diff + y_diff <= (height//2) ** 2


answer = sum([1 if is_in_field(x, y, W, H, X, Y) else 0 for x, y in positions])
print(answer)
