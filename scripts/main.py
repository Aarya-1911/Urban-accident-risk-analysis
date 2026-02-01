import os
import pandas as pd
from data_cleaning import clean_data, load_data, save_data
from risk_score import calculate_risk_score
from clustering import perform_clustering, assign_risk_labels
from visualizations import plot_accidents_by_state, plot_fatalities_by_state, plot_clusters

print("Loading data...")
df = load_data("../datasets/accidents_india.csv")

print("Cleaning data...")
df = clean_data(df)

cleaned_path = "../datasets/accidents_cleaned.csv"
os.makedirs(os.path.dirname(cleaned_path), exist_ok=True) 
save_data(df, cleaned_path)

print("Calculating risk score...")
df = calculate_risk_score(df)

print("Clustering...")
df, cluster_labels = perform_clustering(df)
df = assign_risk_labels(df)

final_path = "../datasets/accidents_cleaned.csv" 
os.makedirs(os.path.dirname(final_path), exist_ok=True)
save_data(df, final_path)

print("Plotting graphs...")
plot_accidents_by_state(df)
plot_fatalities_by_state(df)
plot_clusters(df)

print("DONE ✅")
