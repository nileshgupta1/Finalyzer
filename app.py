import streamlit as st
import os
import google.generativeai as gen_ai
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
from dotenv import load_dotenv
from edgar import *

# Setting up identity and API key for edgar API
set_identity("Nilesh Gupta nilesh147k@gmail.com")

# Setting up identity and API key for Google Gemini API
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gen_ai.configure(api_key=GOOGLE_API_KEY)

# Initializing Google Gemini API model for text analysis
model = gen_ai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def get_financials(company):
    """
    Retrieve financial statements (Balance sheet, Cash flow statement, Income statement) for a given company.

    Args:
        company: An instance of the Company class from the edgar library.

    Returns:
        str: Concatenated string containing balance sheet, cash flow statement, and income statement.
    """
    fin_str = ""
    if company:
        fin_str = str(company.financials.balance_sheet.to_dataframe()) + str(company.financials.cash_flow_statement.to_dataframe()) + str(company.financials.income_statement.to_dataframe())
    return fin_str


def calc_for_visuals():
    """
    Calculate financial metrics for visualization.

    Returns:
        DataFrame: DataFrame containing financial metrics for visualization.
    """
    prompt = '''Retrieve Year, revenue, net income from previous information. response should only contain a valid 
    JSON string and nothing else. The format of the string should be:
    {
    "Year": [2021, 2022, 2023],
    "Revenue": [1000000, 1200000, 1500000],
    "Net_Income": [200000, 300000, 400000],
    }'''
    response = chat.send_message(prompt)
    try:
        dict = json.loads(response)
        return pd.DataFrame(dict.items(), columns = ["Year", "Revenue", "Net_Income"])
    except:
        pass
    return pd.DataFrame({})

def plot_figure():
    """
    Plot financial metrics visualization.
    """
    df = calc_for_visuals()
    df['Revenue_Growth_Rate'] = df['Revenue'].pct_change() * 100
    df['Profit_Margin'] = df['Net_Income'] / df['Revenue'] * 100

    fig = plt.figure(figsize=(12, 8))
    # Revenue Growth Rate
    plt.subplot(2, 2, 1)
    sns.barplot(x='Year', y='Revenue_Growth_Rate', data=df.iloc[1:], color='blue')
    plt.title('Revenue Growth Rate Over Time')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate (%)')

    # Profit Margin
    plt.subplot(2, 2, 2)
    sns.barplot(x='Year', y='Profit_Margin', data=df, color='green')
    plt.title('Profit Margin Over Time')
    plt.xlabel('Year')
    plt.ylabel('Profit Margin (%)')

    plt.tight_layout()
    st.pyplot(fig)







def main():
    """
    Main function to display Streamlit app interface and interact with users.
    """
    st.set_page_config("Finalyzer")
    st.header("Get Financial Information for Companies")
    filings = {}
    company = {}

    with st.sidebar:
        st.title("Menu:")
        
        ticker = st.text_input('Enter Company Ticker')
        with st.spinner("Processing..."):
            try:
                # Fetching company information based on ticker input
                company = Company(ticker)
                filings = company.get_filings(form="10-K")
                st.write("Selected ticker is: ", ticker)
            except:
                st.write("Enter a valid ticker")

       
    try:
        fin_str = get_financials(company)
        # Requesting financial analysis from the AI model
        prompt = '''Using the below dataframes calculate:
        every Income Statement Metrics, Cash Flow Statement Metrics and Balance Sheet Metrics only 
        which is to be discussed in a c-suite meeting''' + fin_str
        if fin_str:
            st.subheader('Latest Financial metrics', divider='rainbow')
            response = chat.send_message(prompt)
            st.write((response.text))
    except:
        pass

    try:
        Tenk = filings[0].obj()
        # Requesting risk factors analysis from the AI model
        prompt = '''Below is the risk factors section from a 10-K document. Give all the risk factors 
        in brief a financial investor should consider before investing in the company.''' + Tenk['Item 1A'][:min(len(Tenk['Item 1A']), 15000)]
        response = chat.send_message(prompt)
        st.subheader('Risks involved and Competitions: ', divider='rainbow')
        st.write((response.text))
    except:
        pass

    try:
        # Requesting future outlook analysis from the AI model
        prompt = '''You have been provided the management discussion and analysis for a company. What is the company's 
        outlook for next year? Are they optimistic about growth?''' + Tenk['Item 7'][:min(len(Tenk['Item 7']), 20000)]
        response = chat.send_message(prompt)
        st.subheader('Future Outlook: ', divider='rainbow')
        st.write((response.text))
    except:
        pass

    try:
        plot_figure()
    except:
        pass
    

if __name__ == "__main__":
    main()