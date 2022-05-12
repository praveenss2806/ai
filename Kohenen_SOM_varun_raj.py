def iteration(weights,current_input):
    output=[0,0,0,0,0]
    for i in range(len(weights)):
        for j in range(len(current_input)):
            output[i]=output[i]+(current_input[j]-weights[i][j])*(current_input[j]-weights[i][j])
    return output
            
a=0.2
input=[[0.2,0.4]]
weights=[[0.5,0.2],[0.1,0.4],[0.1,0.4],[0.6,0.9],[0.9,0.1]]
for i in range(len(input)):
    outputs=iteration(weights,input[i])
    mini_index=outputs.index(min(outputs))
    for j in range(0,len(weights[0])):
        weights[mini_index][j]=weights[mini_index][j]+(a*(input[i][j]-weights[mini_index][j]))