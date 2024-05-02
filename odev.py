points = [(1,2),(3,4),(5,6),(7,8)]

def euclideanDistance(x,y):
    return pow(pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2), 0.5)
    
distances = []

for i in range(len(points) - 1):
    for j in range(i + 1 , len(points)):
        distances.append(euclideanDistance(points[i], points[j]))
        
print(min(distances))
