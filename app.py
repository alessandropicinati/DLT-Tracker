import streamlit as st
import google.generativeai as genai
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="DeFi Strategy Repo", page_icon="🏦", layout="wide")

# --- HEADER ---
st.title("🏦 Digital Assets & RegTech Intelligence")
st.markdown("""
Welcome to the knowledge repository. This tool synthesizes raw articles into structured 
consulting insights, focusing on regulatory frameworks and quantitative developments.
""")

# --- SIDEBAR: API KEY ---
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")
st.sidebar.markdown("""
*Get a free API key at [Google AI Studio](https://aistudio.google.com/).* *(Never hardcode your API key in GitHub!)*
""")

# --- MAIN DASHBOARD ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Input Article")
    article_title = st.text_input("Article Title:")
    article_text = st.text_area("Paste Article Text Here:", height=300)
    analyze_button = st.button("Synthesize & Extract Insights")

with col2:
    st.subheader("2. Strategic Synthesis")
    
    if analyze_button:
        if not api_key:
            st.error("⚠️ Please enter your API key in the sidebar first.")
        elif not article_text:
            st.warning("⚠️ Please paste some article text to analyze.")
        else:
            with st.spinner("Consulting AI is analyzing..."):
                try:
                    # Configure the Gemini API
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    # The Prompt Framework
                    prompt = f"""
                    You are a senior strategy consultant at a top-tier firm like Strategy&. 
                    Analyze the following article about blockchain/finance. Extract and format the insights strictly using this Markdown structure:

                    ### Executive Summary (TL;DR)
                    (3-4 sentences summarizing the core thesis and impact)

                    ### 1. Regulatory Perspective
                    (What are regulators doing? What are the compliance hurdles or frameworks mentioned, e.g., MiCA, SEC?)

                    ### 2. Quantitative/Technical Development
                    (What is the underlying technological change or quantitative metric? e.g., tokenization standards, liquidity shifts)

                    ### 3. Strategic Positioning
                    (How are traditional players or crypto-native firms responding to this? Where is the market opportunity or threat?)
                    
                    **Article Text:**
                    {article_text}
                    """
                    
                    # Generate the response
                    response = model.generate_content(prompt)
                    
                    # Display the result
                    st.markdown(response.text)
                    
                    # Create a downloadable Markdown file
                    filename = f"{article_title.replace(' ', '_').lower()}_{datetime.now().strftime('%Y%m%d')}.md"
                    st.download_button(
                        label="Download Markdown for GitHub Repo",
                        data=f"# {article_title}\n\n{response.text}",
                        file_name=filename,
                        mime="text/markdown"
                    )
                except Exception as e:
                    st.error(f"An error occurred: {e}")
