import streamlit as st
import json
# REMOVED the "modules." prefix because your files are in the same directory
from query_parser import parse_query
from company_finder import search_companies
from qualifier import qualifies
from email_generator import generate_email

st.set_page_config(page_title="Focus Softnet AI Sales Agent", page_icon="🤖")
st.title("🤖 Focus Softnet AI Sales Agent")

# Initialize session state to store results so they don't vanish on rerun
if "leads" not in st.session_state:
    st.session_state.leads = []

query = st.text_input("Enter your search request (e.g., 'Software companies in Dubai')")

if st.button("Find Leads"):
    with st.spinner("Analyzing query and finding companies..."):
        # 1. Parse Query
        parsed_str = parse_query(query)
        # Note: You might need json.loads(parsed_str) here if query_parser doesn't return a dict
        
        # 2. Search
        # For demo, using the raw query; in production, use parsed keywords
        companies = search_companies(query)
        
        results = []
        for company in companies[:5]:
            # 3. Qualify
            decision = qualifies(company["name"], "Focus Softnet Solutions")
            # 4. Generate Email
            email_body = generate_email(company, "Focus Softnet ERP")
            
            results.append({
                "name": company["name"],
                "decision": decision,
                "email": email_body
            })
        
        st.session_state.leads = results

# Display Results from Session State
for idx, lead in enumerate(st.session_state.leads):
    with st.container():
        st.write("---")
        st.subheader(f"🏢 {lead['name']}")
        st.info(f"🧠 **AI Qualification:** {lead['decision']}")
        
        new_email = st.text_area(f"Edit Email for {lead['name']}", lead['email'], height=200, key=f"email_{idx}")
        
        if st.button(f"Send to {lead['name']}", key=f"btn_{idx}"):
            st.success(f"✅ Email sent to {lead['name']}!")