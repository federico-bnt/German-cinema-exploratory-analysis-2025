import pandas as pd

def compute_avg_annual_pct_change(df, year_col='Years', price_col='Average cinema ticket price',
                                  income_col='Gross receipts from cinema visits',
                                  visits_col='Cinema visits', exclude_years=None):
    """
    Groups cinema data by year, calculates year-over-year percentage changes,
    and computes average annual percentage changes for ticket prices, gross income, and visits.

    Parameters:
        df (pd.DataFrame): Input DataFrame containing cinema data.
        year_col (str): Name of the year column.
        price_col (str): Name of the average ticket price column.
        income_col (str): Name of the gross income column.
        visits_col (str): Name of the cinema visits column.
        exclude_years (list or set): Years to exclude from the calculation (e.g., [2020, 2021]).

    Returns:
        pd.DataFrame: DataFrame with metrics and their average annual percentage changes.
    """
    # exclude specified years
    if exclude_years is not None:
        df = df[~df[year_col].isin(exclude_years)]

    # Group by year and sum/mean relevant columns
    grouped = df.groupby(year_col).agg({
        price_col: 'mean',
        income_col: 'sum',
        visits_col: 'sum'
    }).sort_index()

    # Calculate year-over-year percentage changes
    pct_changes = grouped.pct_change() * 100

    # Compute average annual percentage change for each metric
    avg_pct_changes = pct_changes.mean().round(2)

    # Prepare results DataFrame
    results_df = pd.DataFrame({
        'Metric': ['Average Ticket Price', 'Gross Receipts', 'Cinema Visits'],
        'Average Annual % Change': [
            avg_pct_changes[price_col],
            avg_pct_changes[income_col],
            avg_pct_changes[visits_col]
        ]
    })

    return results_df