## Exploratory data analysis of cinema in Germany

**Author:** Federico Bonato
**Date:** April 2025

## Project Description

This project presents an exploratory data analysis of cinema industry in Germany from 2000 to 2024. It investigates geographic and temporal trends, analyzing how economic factors (like ticket prices) and infrastructure (number of cinemas and screens) influence cinema-going habits.

## Research Questions

* How have average ticket prices changed over time across states?
* Which states have the highest and lowest cinema visits per inhabitant?
* Is there a correlation between ticket prices and attendance?
* How does infrastructure affect audience numbers?
* Are ticket prices correlated with gross revenue?

## Methods Used

* **Line plots** for trends over time
* **Bar plots and heatmaps** for geographic comparisons
* **Scatter plots** and **correlation analysis (Spearman)**
* **Polynomial trend modeling**
* **Lollipop charts** for summarizing annual changes

## Project Structure

```
project_root/
│
├── data/                      
├── docs/
    ├── description.txt                   
├── source/                   
│   ├── plot_polynomial_trends.py
│   ├── cinema_annual_pct_change.py
│   └── ...
├── bin/
    ├── analysis_notebook.ipynb    
├── LICENSE
├── .gitignore
└── README.md
```

## Data Source

German Federal Statistical Office (GENESIS-Online):
[https://www-genesis.destatis.de/datenbank/online/](https://www-genesis.destatis.de/datenbank/online/)

## License

This project is licensed under the MIT License (https://choosealicense.com/licenses/mit/).
See the [LICENSE](LICENSE) file for details.

## How to Run

1. Clone the repository.
2. Run the `analysis_notebook.ipynb`.

## Contact

Federico Bonato
Data science Master degree student at Potsdam University
e-mail: federico.bonato@uni-potsdam.de