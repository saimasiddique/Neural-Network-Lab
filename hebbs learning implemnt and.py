
print("Enter Input vector :")
input_vector = [float(x) for x in input().split() ]
sum=0
n = len(input_vector)

print("Enter Weight vector :")
weight_vector = [float(x) for x in input().split()]


print(weight_vector)

learning_rate = float(input("Enter Learning Rate :"))
bias = float(input("Enter Bias :"))


sum=0
iteration = 20
pre_out=0
cnt=0
for j in range(iteration):
    total = 0
    for i in range(n):
        total += input_vector[i]*weight_vector[i]
    output = total+bias
    print("Output signal is :" ,output)
    if(output-pre_out<0.0001):
        cnt+=1
        print("value of count ",cnt," output difference ",output-pre_out)
    
    if(cnt>=5):
        break
    """Hebbs Hypotheis"""
    for p in range(n):
        delta = learning_rate*input_vector[p]*output
        weight_vector[p] = weight_vector[i]+delta
        