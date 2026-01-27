import pandas as pd
from data_cleaning import clean_data
from risk_score import calculate_risk_score
from clustering import perform_clustering
from visualizations import plot_accidents_by_state, plot_fatalities_by_state, plot_clusters
from clustering import assign_risk_labels
print("Loading data...")
df = pd.read_csv("../datasets/accidents_india.csv")

print("Cleaning data...")
df = clean_data(df)

print("Calculating risk score...")
df = calculate_risk_score(df)

print("Clustering...")
df, cluster_labels = perform_clustering(df)
df = assign_risk_labels(df)
print("Plotting graphs...")
plot_accidents_by_state(df)
plot_fatalities_by_state(df)
plot_clusters(df)

print("DONE ✅")
