# Sauna Business Data Visualization

Data analysis and visualization project for analyzing booking patterns and utilization metrics for a sauna business (Othership).

## Overview

This project analyzes sauna session booking data to uncover insights about:
- Session utilization rates across different time periods
- Peak booking hours and days
- Capacity distribution throughout the day
- Weekly and monthly booking trends

## Data Source

The analysis uses booking data from `othership_schedule_data.xlsx`, which includes:
- Session ID and capacity
- Available spot count
- Start datetime
- Location (Adelaide, Yorkville)
- Utilization rate

## Visualizations

The notebook generates the following visualizations:

1. **Utilization by Time of Day** - Line chart showing how booking rates vary throughout the day
2. **Available Sessions per Hour** - Bar chart displaying session volume distribution by hour
3. **Class Capacity Distribution by Hour** - Box plot showing capacity ranges for different hours
4. **Utilization by Month** - Seasonal booking pattern analysis
5. **Utilization by Day of Week** - Weekly booking pattern trends
6. **Weekly Session Volume Over Time** - Time series showing overall booking volume trends

## Requirements

```
pandas
seaborn
matplotlib
openpyxl
```

## Key Insights

The analysis reveals:
- **Peak hours**: 3-5 PM (15:00-17:00) and 9 PM (21:00) show highest session volume
- **Seasonal patterns**: Bookings are fuller during colder months (November-March)
- **Weekly trends**: Utilization peaks on weekends (Friday-Sunday)
- **Growth trajectory**: Session volume has increased over time, indicating growing demand

