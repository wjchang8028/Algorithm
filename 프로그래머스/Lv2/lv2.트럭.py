def solution(bridge_length, weight, truck_weights):
    answer = 0 
    bridge = []

    bridge = [0] * bridge_length
    
    while len(bridge):
        bridge.pop(0)

        if truck_weights:
            print(truck_weights[0],truck_weights)
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        print(bridge,truck_weights)

    return answer

solution(2,10,[7])