# Survey Analysis

### Objective

The objective of this project is to analyze survey data related to user satisfaction levels. The program counts how many people selected each satisfaction category, calculates their percentages, and presents the results visually in a clear bar chart.

### Tools Used

* Python
* Pandas
* Matplotlib
* Seaborn

### Features

1. **Load Dataset**
   Reads a CSV file containing survey responses.

2. **Count Satisfaction Levels**
   Counts the number of responses for each satisfaction category.

3. **Maintain Proper Order**
   Displays satisfaction levels in a meaningful order:

   * Very Satisfied
   * Satisfied
   * Neutral
   * Dissatisfied
   * Very Dissatisfied

4. **Calculate Percentages**
   Calculates the percentage of total responses for each category.

5. **Data Visualization**

   * Creates a **bar chart** of satisfaction levels
   * Displays **count and percentage labels inside each bar**
   * Uses a clean and professional chart style for better readability

### Key Concepts

* DataFrames
* value_counts()
* reindex()
* percentage calculation
* Seaborn barplot()
* Matplotlib text labels
