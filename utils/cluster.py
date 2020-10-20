from sklearn.cluster import KMeans

def get_cluster(image, quantity):
    # reshaping to a list of pixels
    pixels = image.reshape((-1, 3))

    kmeans = KMeans(quantity)
    kmeans.fit(pixels)

    return kmeans

def apply_cluster(image, cluster):
    return cluster.predict(image.reshape(-1, 3))