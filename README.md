# Finalyzer - Financial Analysis Tool



## Overview
This project is a comprehensive financial analysis tool designed to provide insights into companies' financial health and performance based on their SEC filings. It utilizes Generative Large Language Model to extract key information from 10-K filings and presents it in an intuitive dashboard interface.

## Tech Stack
- **Streamlit**: For building interactive web applications with Python. Streamlit allows for easy creation of data-driven apps and dashboards.
- **Pandas**: For data manipulation and analysis. Pandas is a powerful library for handling structured data.
- **Seaborn and Matplotlib**: For data visualization. These libraries provide tools for creating insightful and visually appealing plots and charts.
- **Google GenerativeAI (Gemini)**: For text analysis. The Google GenerativeAI API is used for natural language processing tasks such as extracting insight and summarization.
- **Python-dotenv**: For managing environment variables. Python-dotenv is used to securely load sensitive information such as API keys.
- **Edgar**: For accessing SEC filings. The Edgar library provides a convenient interface for retrieving and parsing SEC filings from the EDGAR database.

## Why These Components?
- **Streamlit**: Chosen for its simplicity and ease of use in building interactive web applications. Streamlit's declarative syntax and rapid prototyping capabilities make it an ideal choice for quickly developing data-driven applications.
- **Pandas**: Widely regarded as the go-to library for data manipulation and analysis in Python. Its powerful data structures and easy-to-use functions make it well-suited for processing financial data.
- **Seaborn and Matplotlib**: Both libraries are highly customizable and offer a wide range of plotting options, allowing for the creation of informative and visually appealing visualizations.
- **Google GenerativeAI (Gemini)**: Leveraged for its advanced text analysis capabilities. The Gemini API provides state-of-the-art natural language processing models, enabling sophisticated analysis of textual data extracted from SEC filings.
- **Python-dotenv**: Essential for securely managing sensitive information such as API keys. By storing API keys in a separate `.env` file, we can ensure that they are not exposed in the codebase.
- **Edgar**: Chosen for its ease of use in accessing SEC filings. The Edgar library abstracts away the complexity of interacting with the EDGAR database, allowing for seamless retrieval and parsing of filings.

## Usage
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application using `streamlit run app.py`.
4. Enter a company ticker symbol in the sidebar to retrieve financial information and analysis.

