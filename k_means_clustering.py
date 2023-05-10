# Import numpy for numerical operations
import numpy as np

# Define a function to calculate the Euclidean distance between two points


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


# Define a function to initialize k random centroids from the data


def initialize_centroids(X, k):
    # Get the number of samples and features
    n_samples, n_features = X.shape
    # Randomly choose k samples as initial centroids
    centroids = X[np.random.choice(n_samples, k, replace=False)]
    return centroids


# Define a function to assign each sample to the nearest centroid


def assign_clusters(X, centroids):
    # Get the number of samples and clusters
    n_samples, n_clusters = X.shape[0], centroids.shape[0]
    # Initialize an array to store the cluster indices
    clusters = np.zeros(n_samples)
    # Loop through each sample
    for i in range(n_samples):
        # Calculate the distances to each centroid
        distances = [euclidean_distance(X[i], c) for c in centroids]
        # Find the index of the closest centroid
        closest = np.argmin(distances)
        # Assign the sample to that cluster
        clusters[i] = closest
    return clusters


# Define a function to update the centroids by taking the mean of the samples in each cluster


def update_centroids(X, clusters, k):
    # Get the number of features
    n_features = X.shape[1]
    # Initialize an array to store the new centroids
    new_centroids = np.zeros((k, n_features))
    # Loop through each cluster
    for i in range(k):
        # Find the samples in that cluster
        cluster_samples = X[clusters == i]
        # Calculate the mean of those samples
        cluster_mean = np.mean(cluster_samples, axis=0)
        # Assign the mean as the new centroid
        new_centroids[i] = cluster_mean
    return new_centroids


# Define a function to implement kmeans algorithm


def kmeans(X, k, max_iters=100):
    # Initialize the centroids
    centroids = initialize_centroids(X, k)
    # Initialize an array to store the previous centroids for convergence check
    prev_centroids = np.zeros(centroids.shape)
    # Initialize a variable to store the number of iterations
    iters = 0
    # Loop until convergence or maximum iterations
    while not np.allclose(centroids, prev_centroids) and iters < max_iters:
        # Assign clusters to samples based on current centroids
        clusters = assign_clusters(X, centroids)
        # Store the current centroids as previous centroids
        prev_centroids = centroids.copy()
        # Update the centroids based on current clusters
        centroids = update_centroids(X, clusters, k)
        # Increment the number of iterations
        iters += 1

    return clusters, centroids
