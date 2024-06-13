# Real Estate EDA

This repository contains an exploratory data analysis (EDA) of a real estate dataset. The analysis includes data cleaning, visualization, and insights into various aspects of the real estate market across different cities.

## Dataset

The dataset used in this analysis contains information about real estate properties from various cities. The key columns in the dataset are:
- `city`: The city where the property is located
- `bedroom`: The number of bedrooms in the property
- `facing`: The direction the property is facing
- `total_area`: The total area of the property
- `Price`: The price of the property

## Analysis

The analysis is divided into several sections:

### 1. Data Cleaning

- Checking for null values and ensuring the data is clean.
- Displaying basic statistics of the dataset.

### 2. Supply of Houses by City

- A histogram showing the number of houses available for sale in different cities.
- Insight: Most houses available for sale are in Delhi compared to other cities.

### 3. Distribution of Houses by Direction

- A pie chart showing the distribution of houses based on the direction they are facing.
- Insight: The direction of houses is an important factor in the Indian real estate market.

### 4. Houses with Number of Bedrooms

- A histogram showing the distribution of houses based on the number of bedrooms.
- Insight: Houses with 3 bedrooms are the most common, followed by houses with 2 and 4 bedrooms.

### 5. Comparing the Cost of Houses by Area and City

- A scatter plot comparing the total area and price of houses in different cities.
- Insight: Provides a visual comparison of the cost of houses relative to their area across various cities.

## Visualizations

The analysis includes various visualizations to aid in understanding the dataset:
- Histograms
- Pie charts
- Scatter plots

## Usage

To run the analysis, you need to have Python installed along with the following libraries:
- pandas
- numpy
- matplotlib
- seaborn

You can install these libraries using pip:
```bash
pip install pandas numpy matplotlib seaborn
```

Load the dataset and run the analysis by executing the cells in the Jupyter Notebook.

## Conclusion

This exploratory data analysis provides insights into the real estate market across different cities. It highlights key factors such as the supply of houses, distribution by direction, and the relationship between area and price.

## License

This project is licensed under the MIT License.

## Acknowledgements

- The dataset was provided for educational purposes.
- The analysis was conducted using Python and various data visualization libraries.

For any queries or contributions, feel free to open an issue or submit a pull request.
