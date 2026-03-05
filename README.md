# Global-GDP-Analysis-Dashboard

## 📌 Project Overview
This project focuses on collecting, cleaning, analyzing, and visualizing global GDP data. The dataset was scraped from Wikipedia and contains nominal GDP estimates from three major international organizations: the International Monetary Fund (IMF), World Bank, and United Nations.
The goal of this project is to transform unstructured web data into a structured dataset and build a dashboard that highlights global economic rankings and comparisons across different GDP estimates.

## 🎯 Objectives
1. Extract real-world GDP data from Wikipedia
2. Clean and transform messy web table data
3. Handle inconsistent column structures
4. Prepare a structured dataset for analysis
5.Build a dashboard to visualize GDP rankings

## 🛠 Tools & Technologies
1. Python
2. Pandas
3. BeautifulSoup
4. Excel
5. Pivot Tables

## 📥 Data Source
Data was collected from the Wikipedia page:
List of Countries by GDP (Nominal)
https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)

The dataset includes GDP estimates from:
1. International Monetary Fund (IMF)
2. World Bank
3. United Nations

## 🔄 Data Processing Steps
### 1️⃣ Web Scraping

The GDP table was scraped from Wikipedia using BeautifulSoup to extract the HTML table containing country GDP estimates.

### 2️⃣ Data Cleaning
Several cleaning steps were performed:
1. Removed reference numbers from column headers (e.g., [1], [2])
2. Stripped unwanted characters and spaces
3. Handled inconsistent column formatting
4. Converted vertical data structure into a structured table

### 3️⃣ Data Transformation
Using Pandas, the dataset was reshaped to ensure:
1. Proper column alignment
2. Consistent row structure
3. Clean column headers

### 4️⃣ Data Export
The cleaned dataset was exported into a CSV file for further analysis and visualization.

## 📊 Dashboard Development
The dashboard was built in Microsoft Excel using PivotTables and charts to visualize GDP rankings and comparisons.
Dashboard Features;
1. Global GDP summary indicators
2. Top 10 countries by GDP
3. Comparison across IMF, World Bank, and UN estimates
4. Bar charts showing economic ranking differences

## 📈 Key Insights
1. The United States consistently ranks as the largest economy across all GDP estimates.
2. China follows as the second-largest economy globally.
3. Major European economies such as Germany, United Kingdom, and France remain among the top global economies.
4. Emerging economies like India and Brazil are significant contributors to global economic growth.

## 📷 Dashboard Preview

<img width="966" height="618" alt="dashboard" src="https://github.com/user-attachments/assets/25e5d470-ce1d-4e61-af76-6382f1e7d347" />

## 🚀 Skills Demonstrated
1. Web scraping
2. Data cleaning
3. Data transformation
4. Data analysis
5. Dashboard creation
6. Data visualization

## 📌 Conclusion

This project demonstrates the process of transforming raw web data into meaningful insights through data cleaning, analysis, and visualization. It highlights the ability to work with real-world datasets and present economic insights through an interactive dashboard.

⭐ If you like this project, feel free to explore the repository and share your feedback.
