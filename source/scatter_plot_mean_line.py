import matplotlib.pyplot as plt

def plot_price_attendance_over_time(
    df,
    year_col='Years',
    price_col='Average cinema ticket price',
    attendance_col='Cinema visits per inhabitant',
    title='Price and Attendance Evolution Over Time',
    price_color='blue',
    attendance_color='red',
    price_mean_color='#00008B',
    attendance_mean_color='#8B0000',
    legend_loc='upper left'
):
    """
    Plots ticket price and attendance over time with mean lines.
    Plots ALL points in the dataframe, no region grouping.
    """
    plt.figure(figsize=(12, 8))

    # Plot all price points
    plt.scatter(
        df[year_col],
        df[price_col],
        color=price_color,
        alpha=0.6,
        label='Average Ticket Price'
    )

    # Plot all attendance points
    plt.scatter(
        df[year_col],
        df[attendance_col],
        color=attendance_color,
        alpha=0.6,
        label='Visits per Inhabitant'
    )

    # Plot mean lines
    mean_prices_per_year = df.groupby(year_col)[price_col].mean()
    mean_attendance_per_year = df.groupby(year_col)[attendance_col].mean()
    plt.plot(
        mean_prices_per_year.index,
        mean_prices_per_year.values,
        color=price_mean_color,
        linestyle='-',
        linewidth=2,
        label='Average Ticket Price (Mean Line)'
    )
    plt.plot(
        mean_attendance_per_year.index,
        mean_attendance_per_year.values,
        color=attendance_mean_color,
        linestyle='-',
        linewidth=2,
        label='Visits per Inhabitant (Mean Line)'
    )

    plt.title(title, pad=20)
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend(loc=legend_loc)
    plt.tight_layout()
    plt.show()