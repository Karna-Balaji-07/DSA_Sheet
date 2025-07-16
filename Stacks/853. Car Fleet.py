# 853. Car Fleet

def solutions(target, position, speed):
    result = 0
    previous = 0
    for pos, speeds in sorted(zip(position, speed), reverse=True):
        time = (target - pos) // speeds
        if previous < time:
            result += 1
            previous = time
    return result

target = 12; position = [10,8,0,5,3]; speed = [2,4,1,1,3]
print(solutions(target, position, speed))