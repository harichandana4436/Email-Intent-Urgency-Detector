import streamlit as st

from prompt import prompt
from model import llm
from email_parser import parser

chain = prompt | llm | parser

st.title("📧 Email Intent & Urgency Detector")

email = st.text_area(
    "Enter Email",
    height=200
)

if st.button("Analyze"):

    if email.strip():

        result = chain.invoke(
            {
                "email": email
            }
        )

        st.json(result)

    else:
        st.warning("Enter email text")