# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 23:06:38 2023

@author: Anas
"""


import os
import openai
import streamlit as st

openai.organization = "org-#####################"
openai.api_key = os.getenv("OPENAI_API_KEY")

# st.title('All models available at OpenAI')
# data = openai.Model.list()
# model_list = [entry["id"] for entry in data["data"]]


# # if st.button("Show List"):
# #     st.write(model_list)

# if st.button("Show List"):
#     st.write("Number of models:", len(model_list))
    
#     # Create a table to display the list
#     model_table = "<table><tr><th>Model ID</th></tr>"
#     for model_id in model_list:
#         model_table += f"<tr><td>{model_id}</td></tr>"
#     model_table += "</table>"
    
#     # Render the table
#     st.markdown(model_table, unsafe_allow_html=True)


st.title('All models available at OpenAI')

# Fetch model data
data = openai.Model.list()
model_list = [entry["id"] for entry in data["data"]]

# Add a toggle button to show/hide the list
show_list = st.checkbox("Show List")

if show_list:
    st.write("Number of models:", len(model_list))
    
    # Create a table to display the list
    model_table = "<table><tr><th>Model ID</th></tr>"
    for model_id in model_list:
        model_table += f"<tr><td>{model_id}</td></tr>"
    model_table += "</table>"
    
    # Render the table
    st.markdown(model_table, unsafe_allow_html=True)