FreezingPoint = 0
BoilingPoint = 100

def get_state(temp):
    if temp <= FreezingPoint:
        state = 'Solid'
    elif temp >= BoilingPoint:
        state = 'Gas'
    else:
        state = 'Liquid'
    return state