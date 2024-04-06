def solution(m, n, startX, startY, balls):
    answer = [min_dist(m, n, startX, startY, ball) for ball in balls]
    return answer

def min_dist(width, height, startX, startY, ball):
    start = (startX, startY)
    symmetry_points = get_all_symmetry_points(width, height, start, ball)
    dists = [line_dist(start, target) for target in symmetry_points]
    return min(dists)
    
def get_all_symmetry_points(width, height, start, ball):
    x, y = ball
    point_symmetries = [(-x, -y), (-x, 2*height-y), (2*width-x, -y), (2*width, 2*height-y)]
    line_symmetries = []
    if not is_blocked_from(start, ball, 'bottom'):
        line_symmetries.append((x,-y))
    if not is_blocked_from(start, ball, 'left'):
        line_symmetries.append((-x,y))
    if not is_blocked_from(start, ball, 'top'):
        line_symmetries.append((x,2*height-y))
    if not is_blocked_from(start, ball, 'right'):
        line_symmetries.append((2*width-x,y))
    
    return point_symmetries+line_symmetries

def is_blocked_from(start, ball, side):
    if side == 'bottom':
        return start[0] == ball[0] and start[1] > ball[1]
    if side == 'left':
        return start[1] == ball[1] and start[0] > ball[0]
    if side == 'top':
        return start[0] == ball[0] and start[1] < ball[1]
    if side == 'right':
        return start[1] == ball[1] and start[0] < ball[0]
    
    return True
    
def line_dist(start, target):
    return (start[0]-target[0])**2 + (start[1]-target[1])**2