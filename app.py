import streamlit as st
import json

from query_parser import parse_query
from company_finder import search_companies
from qualifier import qualifies
from email_generator import generate_email

st.title("🤖 Focus Softnet AI Sales Agent")

query = st.text_input("Enter your search request")

if st.button("Find Leads"):

    parsed = parse_query(query)
    st.write("🔍 Parsed Query:", parsed)

    # For demo (simplified)
    solution = "WMS"

    companies = search_companies(query)

    st.subheader("🎯 Potential Leads")

    for company in companies[:5]:

        st.write("---")
        st.write("🏢", company["name"])

        decision = qualifies(company["name"], solution)
        st.write("🧠 AI Decision:", decision)

        email = generate_email(company, solution)

        st.text_area(
            f"Email to {company['name']}",
            email,
            height=200
        )

        if st.button(f"Send to {company['name']}"):
            st.success("Email sent (demo)")