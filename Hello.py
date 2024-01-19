# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import time  # Used for simulating a task with a delay

import requests
import json

LOGGER = get_logger(__name__)


import pandas as pd



def call_api(call_id: str, question: str, x_csrf_token: str, g_session: str):

    # Set the URL
    url = "https://us-60052.app.gong.io/ajax/ask-me-anything/get-and-store-answer?call-id=" + call_id + "&tkn="

    headers = {
        'authority': 'us-60052.app.gong.io',
        'accept': 'application/json; charset=utf-8',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://us-60052.app.gong.io',
        'referer': 'https://us-60052.app.gong.io/conversations?workspace-id=9159817827657862290',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        "x-csrf-token": x_csrf_token,  # You need to define x_csrf_token earlier in your code
        'x-requested-with': 'XMLHttpRequest',
        'cookie': 'g-session=' + g_session + ';'
    }

    # Define the body
    body = {
        "messages": [
            {"role": "user", "content": question}
        ]
    }

    # st.write(headers)
    # st.write(body)

    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(body))

    # Check response
    # print(response.status_code)

    # Check if response is successful
    if response.ok:
        # Try parsing JSON
        # print(response.json())
        answer = (response.json())['questions'][0]['answer']
        return answer

    else:
        # Print response text if not successful
        print("Response Text:", response.text)


def run():
    st.set_page_config(
        page_title="Ask Gong AI",
        page_icon="👋",
    )

    token = ''
    g_session = ''

    with st.sidebar:    
        st.write('### Configuration')    
        token = st.text_input(label="Enter Gong's security token", placeholder="example: cewfewfwefewq")

        with st.expander('How to find your security token'):
            st.markdown("""Type ```console.log(document.querySelector('meta[name="_csrf"]').getAttribute('content'))``` in the console after logging into Gong.""")

        g_session = st.text_input(label="Enter Gong's g-session ID", placeholder="IUYB*DWK")

        with st.expander('How to find g-session ID'):
            st.markdown("""Go to the cookie section in your brower and find the cookie named g-session""")


    st.markdown(
        """
        Gong's AI is SOOO powerful. But today, you have to manually ask questions, one call at a time.

        This little project allows you to analyze hundreds of calls still using Gong's AI.
        
        **🤖 What this app does**

        1. You give it a question. Let's say "How did this customer hear about our company?".
        
        2. You give it a list of Gong calls.
                s
        3. This app will ask Gong's AI this question for every call you have provided. 
        -> Then it generates a CSV file with the answers.

    """

    )


    question = st.text_input(label="Question you want Gong.ai to answer about each call", placeholder="How did this customer hear about our company?")

    call_ids_string = st.text_input(label="Enter a list of Gong call Ids, separated by a comma", placeholder="example: 2142342, 43242354325,355235")

    button_area = st.empty()
    result_area = st.empty()        
    
    if button_area.button(
                label="Ask Gong AI",
                type="primary"
            ):
        
        # Creating a progress bar
        progress_bar =     button_area.progress(0)

        call_ids = call_ids_string.split(',')

        results = []

        for index, call_id in enumerate(call_ids):
            progress_percentage = int(100 * (index + 1) / len(call_ids))
            progress_bar.progress(progress_percentage)
            time.sleep(1)  # Remove or adjust this in your actual task            
            answer = call_api(call_id, question, token, g_session)
            results.append({'call_id': call_id, 'answer': answer})

            # Display the table                        
            result_area.empty()
            df = pd.DataFrame(results)
            result_area.write(df)

        result_area.empty()
        button_area.empty()


        st.markdown(
            """ 
            ### Results below! 👇

            You can download the results as a CSV by clicking on the download icon at the top-right side of the table.

            """)
        df = pd.DataFrame(results)
        st.write(df)




if __name__ == "__main__":
    run()
