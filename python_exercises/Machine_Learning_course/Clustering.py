from sklearn.cluster import KMeans
import numpy as np


kmeans = KMeans(n_clusters=3, init=np.array([[11.8, 11.6], [8.5, 9.83], [14.0, 14.5]]), max_iter=100, n_init=1)

X_Y = []

with open("Module10_data.txt", "r") as data:
    lines = data.readlines()
    
for line in lines[1:]:
    row = line.split(",")
    x = int(row[1])
    y = int(row[2])
    X_Y.append([x, y])

print("Coordinates:", X_Y)


clusters = list(kmeans.fit_predict(X_Y))
print(clusters)


centers_ar = kmeans.cluster_centers_
centers = [list(ar) for ar in centers_ar]
print(centers)


dists_ar = kmeans.fit_transform(X_Y)
dists = centers = [list(ar) for ar in dists_ar]
print(dists)


cluster = 0
cluster_dists = []
for i in range(len(clusters)):
    if clusters[i] == cluster:
        cluster_dists.append(dists[i][0])

print(cluster_dists)


av_dist = sum(cluster_dists) / len(cluster_dists)
print(av_dist)
