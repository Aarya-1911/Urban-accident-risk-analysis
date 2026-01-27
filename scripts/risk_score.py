
import pandas as pd

def calculate_risk_score(df):
    # Normalize values
    df['Accident_Score'] = df['Total_Accidents'] / df['Total_Accidents'].max()
    df['Fatality_Score'] = df['Persons_Killed'] / df['Persons_Killed'].max()
    df['Injury_Score'] = df['Persons_Injured'] / df['Persons_Injured'].max()

    # Weighted risk score
    df['Risk_Score'] = (
        0.5 * df['Accident_Score'] +
        0.3 * df['Fatality_Score'] +
        0.2 * df['Injury_Score']
    )

    return df
