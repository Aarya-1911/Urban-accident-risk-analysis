import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns


def plot_accidents_by_state(df):
    plt.figure(figsize=(12,6))
    sns.barplot(x='State', y='Total_Accidents', data=df)
    plt.xticks(rotation=90)
    plt.title("Total Accidents by State")

    plt.tight_layout()
    plt.show(block=True)


def plot_fatalities_by_state(df):
    plt.figure(figsize=(12,6))
    sns.barplot(x='State', y='Persons_Killed', data=df, color='red')
    plt.xticks(rotation=90)
    plt.title("Fatalities by State")

    plt.tight_layout()
    plt.show(block=True)


def plot_clusters(df):
    plt.figure(figsize=(12,6))
    plt.scatter(df['Total_Accidents'], df['Persons_Killed'], c=df['Cluster'], cmap='viridis', s=100)
    plt.xlabel("Total Accidents")
    plt.ylabel("Persons Killed")
    plt.title("State-wise Accident Clusters (K-Means)")
    for i, state in enumerate(df['State']):
        plt.text(df['Total_Accidents'][i],
                df['Persons_Killed'][i],
                state,
                fontsize=8)


    plt.tight_layout()
    plt.show(block=True)
