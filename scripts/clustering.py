import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def perform_clustering(df, n_clusters=3):
    features = df[['Total_Accidents', 'Fatal_Accidents', 'Persons_Killed', 'Persons_Injured']]
    
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(scaled_features)

    return df, kmeans.labels_

def assign_risk_labels(df):
    cluster_labels = {
        0: "Low Risk",
        1: "Medium Risk",
        2: "High Risk"
    }
    df['Risk_Level'] = df['Cluster'].map(cluster_labels)
    return df
