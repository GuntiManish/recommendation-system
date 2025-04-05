# app.py
import streamlit as st
import requests

st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")
st.title("🔍 SHL Assessment Recommendation Engine")

query = st.text_area("Enter a job description or query:", height=200)

if st.button("Get Recommendations") and query:
    try:
        response = requests.post("http://localhost:5000/recommend", json={"query": query})
        if response.status_code == 200:
            results = response.json()
            st.markdown("### Recommended Assessments:")
            for res in results:
                st.markdown(f"**[{res['name']}]({res['url']})**")
                st.write(f"- Duration: {res['duration']}")
                st.write(f"- Remote: {res['remote']}, Adaptive: {res['adaptive']}")
                st.write(f"- Type: {res['type']}")
                st.markdown("---")
        else:
            st.error("❌ Error: " + response.text)
    except Exception as e:
        st.error(f"🚫 Server connection failed: {str(e)}")
