import streamlit as st

st.set_page_config(
    page_title="Tutorial: Revenue Attribution",
    page_icon="💡",
)


st.markdown("""
            ### Tutorial for "Conversational Attribution"
            
            One great use case for Gong AI is to understand from calls what brought customers to you (aka "marketing attribution").
            
            MadKudu and a few other companies have done this. The results are surprising:
            - There is surprising high percentage of calls where a prospect will tell the sellers where they came from (for MadKudu, it is 40 percent of the time)
            - The reported attribution is often very different from the traditional digital attribution.

            Here is how to do this analysis for your company.

            #### Step-by-step

            **1. Get a list of 1st calls to analyze**

            You can do this in Gong directly:
            - Go to the ["Conversations" tab](https://us-60052.app.gong.io/conversations) in Gong. 
            - Download the list of calls (click "download call data").
            - Flag the first calls and create a comma-separated list of Gong call IDs (eg. 5249106803003406340,5760079641785322301,3926864059709633053)        
""")   

st.image('./assets/gong_call_list.png')

st.markdown("""
            **2. Run those calls through this app**
            
            Use a prompt like "What made them want to talk to us in the first place?". Try a few prompts with a sample of call ids. When satisfied, run Gong AI on all the call IDs from step 1.

            Download the results as a CSV and load it into Excel or Google Sheet. The results will look something like that:

            """)

st.image('./assets/call_results_example.png')


st.markdown("""
            **3. Classify the results by reported source**
            
            In Excel, create a summary of the main sources reported by prospects in call. Here is a real-life example:

            """)

st.image('./assets/results_example.png')

