import numpy as np
import matplotlib.pyplot as plt

def plot_polynomial_trends(data_groups, column_name, years, colors, labels, degree=3, title=None):
    """
    Plot polynomial trends for different groups of data.
    
    Parameters:
    -----------
    data_groups : list of pandas.DataFrame
    column_name : Name of the column to analyze
    years : Array of years for x-axis
    colors : List of colors for each trend line
    labels : List of labels for each trend line
    degree :(default=3) Degree of polynomial fit
    title : Plot title
    """
    
 # Get current axis
    ax = plt.gca()
    
    # Plot trends for each group (no new figure creation)
    for data, color, label in zip(data_groups, colors, labels):
        # Calculate mean values per year
        mean_values = data.groupby('Years')[column_name].mean()
        
        # Fit polynomial
        z = np.polyfit(mean_values.index, mean_values.values, degree)
        p = np.poly1d(z)
        
        # Add trend line to current figure
        ax.plot(
            years,
            p(years),
            '--',
            linewidth=3,
            label=label,
            color=color,
            alpha=0.8
        )
    
    # Update title if provided
    if title:
        ax.set_title(title, fontsize=14, pad=20)