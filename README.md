# Global Digital Payments Analysis

This project analyzes global trends in the use of mobile phones and the internet for paying bills, based on data from the World Bank's Global Findex database.

## Project Overview

The project consists of two main components:

1.  **Exploratory Data Analysis (EDA):** A Jupyter Notebook (`Analysis.ipynb`) that explores the dataset to uncover key insights and trends.
2.  **Interactive Dashboard:** A Streamlit application (`dashboard.py`) that provides an interactive way to visualize and filter the data.

## Data Source

The dataset used in this project is `Used a mobile phone or the internet to pay bills in world.csv`. It contains data on the percentage of adults (15+) who have used a mobile phone or the internet to pay bills in various countries. The data is disaggregated by several dimensions, including:

*   Year (2017, 2021, 2022, 2024)
*   Country
*   Sex
*   Age group
*   Income level
*   Education level

## Installation

To run this project, you need to have Python and the following libraries installed:

*   pandas
*   seaborn
*   matplotlib
*   plotly
*   streamlit

You can install these dependencies using pip:

```bash
pip install -r requriments.txt
```

## Usage

### Exploratory Data Analysis

To view the exploratory data analysis, you can open and run the `Analysis.ipynb` notebook in a Jupyter environment.

### Interactive Dashboard

To launch the interactive dashboard, run the following command in your terminal:

```bash
streamlit run dashboard.py
```

This will open a new tab in your web browser with the dashboard.

## Analysis Highlights

The `Analysis.ipynb` notebook performs the following analysis:

*   **Data Cleaning:** Filters out invalid data and converts data types.
*   **Top Countries:** Identifies the top 10 countries with the highest adoption of digital payments in 2021.
*   **Fastest Growers:** Determines the countries with the fastest growth in digital payment adoption between 2017 and 2021.
*   **Global Distribution:** Shows the global distribution of digital payment adoption in 2017 and 2021.
*   **Gender Gap:** Analyzes the gender gap in digital payment adoption.
*   **Income-Level Analysis:** Examines the relationship between income level and digital payment adoption in Brazil.

## Dashboard Features

The interactive dashboard (`dashboard.py`) allows you to:

*   Filter the data by year, country, sex, age, income level, and education level.
*   View the top 10 countries with the highest digital payment adoption in a bar chart.
*   See a global heatmap of digital payment adoption.
*   Explore the trend of digital payment adoption over time for selected countries.
*   View the raw data in a table.

## Contributing

Contributions to this project are welcome. Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
