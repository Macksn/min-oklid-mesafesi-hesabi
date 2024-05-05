# Noktaları tanımladık
points = [(2,4),(3,6),(1,5),(8,12),(3,3),(2,9)]

# Öklid Mesafesi fonksiyonunu tanımlıyoruz
def euclideanDistance(point1, point2):
    return pow(pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2), 0.5)

# Noktalar arasındaki mesafeleri saklamak için boş bir liste oluşturuyoruz 
distances = []

# Her bir nokta için diğer noktalarla arasındaki mesafeyi hesaplıyoruz
for i in range(len(points) - 1):
    for j in range(i+1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# minimum mesafeyi bulmak için 
print(min(distances))
