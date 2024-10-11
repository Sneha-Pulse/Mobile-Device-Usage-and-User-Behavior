# Mobile Device Usage and User Behavior Analysis

This project provides a comprehensive analysis of user behavior based on mobile device usage patterns. By analyzing factors like screen time, app usage, battery consumption, and data usage, this project helps to understand the behavior of different user segments. The analysis also explores how demographic features such as age and gender are related to user behavior classes. The tool offers multiple visualization options, descriptive analysis, and detailed insights into user behavior.

The project is built using **Streamlit** to offer an interactive and user-friendly dashboard for data exploration and analysis. Users can upload their own datasets to perform analysis and generate visualizations.

### Key Features
- **Upload Dataset**: Users can upload their own CSV dataset with information on mobile device usage and user behavior.
- **Dataset Overview**: Explore the dataset's structure, basic statistics, and missing data.
- **Descriptive Analysis**: Get quick insights into statistical summaries of the dataset.
- **Visualizations**: Explore the relationships between different variables using histograms, scatter plots, and box plots.
- **User Behavior Analysis**: Delve into deeper insights, such as user behavior class distributions and relationships between usage metrics and user behavior classes.

### Why This Analysis is Important
Mobile devices have become an integral part of modern life, influencing how we interact with technology and each other. Understanding how people use their devices and what drives certain behaviors can provide critical insights for developers, marketers, and researchers. For example:
- **Product Development**: Knowing which features users engage with most can help in prioritizing app development.
- **Targeted Marketing**: Understanding user behavior allows businesses to target specific user groups more effectively.
- **Battery and Resource Management**: Insights into battery consumption and data usage can help optimize devices for performance and energy efficiency.
- **User Experience**: Behavioral insights can help in creating better user experiences by understanding how different demographics use their devices.

## Dataset Structure

The dataset used in this project includes the following columns:
- **User ID**: Unique identifier for each user.
- **Device Model**: The model of the mobile device.
- **Operating System**: The operating system used (e.g., Android, iOS).
- **App Usage Time (min/day)**: The total time spent on apps per day.
- **Screen On Time (hours/day)**: The total time the device's screen is on per day.
- **Battery Drain (mAh/day)**: The amount of battery consumed per day.
- **Number of Apps Installed**: The total number of apps installed on the device.
- **Data Usage (MB/day)**: The amount of mobile data used per day.
- **Age**: The user's age.
- **Gender**: The user's gender.
- **User Behavior Class**: Classifying users into behavioral categories (e.g., Heavy User, Moderate User, Light User).

## How to Work with This Project

### Prerequisites
- Python 3.7+
- Streamlit
- Pandas
- Seaborn
- Plotly
- Matplotlib

You can install all necessary dependencies using:

```bash
pip install -r requirements.txt
```

### Running the App

To run this analysis locally on your machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mobile-usage-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd mobile-usage-analysis
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and go to `http://localhost:8501/`.

6. Upload your dataset using the sidebar and start exploring the data.

