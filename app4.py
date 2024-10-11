import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Mobile Device Usage & User Behavior Analysis",
    layout="wide"
)

# Function to upload and load dataset
@st.cache_data
def load_data(uploaded_file):
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        return data
    else:
        return None

# Sidebar for navigation
st.sidebar.title("Navigation")
pages = st.sidebar.radio("Go to", ["Upload Dataset", "Overview", "Descriptive Analysis", "Visualizations", "User Behavior Analysis"])

# File upload
uploaded_file = st.sidebar.file_uploader("Upload your CSV dataset", type=["csv"])

# Load the dataset
data = load_data(uploaded_file)

# Define different page functions
def upload_page():
    st.title("Upload Dataset")
    st.write("Please upload a CSV file containing the Mobile Device Usage and User Behavior dataset.")

    if uploaded_file is not None:
        st.write("Dataset successfully uploaded! You can now explore it from the other pages.")
        st.write(data.head())  # Show the first few rows of the dataset
    else:
        st.write("No dataset uploaded yet.")

def overview():
    if data is not None:
        st.title("Dataset Overview")
        st.write("### Mobile Device Usage and User Behavior Dataset")
        st.write("This dataset contains user-level data on mobile device usage and user behavior.")
        
        if st.checkbox("Show Dataset"):
            st.write(data)
        
        st.write("### Basic Information")
        st.write(data.describe())
        
        st.write("### Missing Data Check")
        st.write(data.isnull().sum())
    else:
        st.write("Please upload a dataset to proceed.")

def descriptive_analysis():
    if data is not None:
        st.title("Descriptive Analysis")
        
        st.write("### Basic Statistics")
        st.write(data.describe())

def visualizations():
    if data is not None:
        st.title("Visualizations")
        
        # Distribution plots
        st.write("### Distribution of Numerical Features")
        feature = st.selectbox("Select feature for distribution", data.select_dtypes(include='number').columns)
        fig, ax = plt.subplots()
        sns.histplot(data[feature], kde=True, ax=ax)
        st.pyplot(fig)
        
        # Scatter plots
        st.write("### Scatter Plot")
        x_axis = st.selectbox("Select X-axis", data.select_dtypes(include='number').columns, index=3)
        y_axis = st.selectbox("Select Y-axis", data.select_dtypes(include='number').columns, index=4)
        
        fig = px.scatter(data, x=x_axis, y=y_axis, color='User Behavior Class', title=f"Scatter Plot of {x_axis} vs {y_axis}")
        st.plotly_chart(fig)
        
        # Box plots
        st.write("### Box Plot for User Behavior Class")
        box_feature = st.selectbox("Select feature for Box Plot", data.select_dtypes(include='number').columns)
        fig, ax = plt.subplots()
        sns.boxplot(x='User Behavior Class', y=box_feature, data=data, ax=ax)
        st.pyplot(fig)
    else:
        st.write("Please upload a dataset to proceed.")

def user_behavior_analysis():
    if data is not None:
        st.title("User Behavior Analysis")
        
        st.write("### User Behavior Class Distribution")
        fig, ax = plt.subplots()
        sns.countplot(x='User Behavior Class', data=data, palette="Set2", ax=ax)
        st.pyplot(fig)
        
        st.write("### Age and Behavior Class")
        fig = px.histogram(data, x='Age', color='User Behavior Class', nbins=20, title="Age Distribution by User Behavior Class")
        st.plotly_chart(fig)
        
        st.write("### App Usage and Battery Drain by Behavior")
        fig = px.scatter(data, x='App Usage Time (min/day)', y='Battery Drain (mAh/day)', color='User Behavior Class', title="App Usage vs Battery Drain")
        st.plotly_chart(fig)
    else:
        st.write("Please upload a dataset to proceed.")

# Call the selected page function
if pages == "Upload Dataset":
    upload_page()
elif pages == "Overview":
    overview()
elif pages == "Descriptive Analysis":
    descriptive_analysis()
elif pages == "Visualizations":
    visualizations()
elif pages == "User Behavior Analysis":
    user_behavior_analysis()

