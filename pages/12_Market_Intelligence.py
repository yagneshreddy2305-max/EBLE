import streamlit as st
import requests

st.set_page_config(
    page_title="Market Intelligence",
    page_icon="📰",
    layout="wide"
)
st.markdown("""
<div style="
padding:30px;
border-radius:20px;
background:linear-gradient(90deg,#00E5FF,#0066FF);
color:white;
">

<h1>🚀 EBLE</h1>

<h3>Empowering Every Business to Level Up</h3>

<p>
AI-Powered Business Intelligence Platform
for Small Businesses, Vendors and Retailers.
</p>

</div>
""", unsafe_allow_html=True)

st.title("📰 Market Intelligence")

try:
    API_KEY = st.secrets["NEWS_API_KEY"]
except:
    st.error("❌ NEWS_API_KEY not found in secrets.toml")
    st.stop()

query = st.selectbox(
    "Select News Category",
    [
        "small business",
        "MSME India",
        "retail business",
        "startup India",
        "business finance"
    ]
)

url = (
    f"https://newsapi.org/v2/everything?"
    f"q={query}&"
    f"sortBy=publishedAt&"
    f"pageSize=10&"
    f"language=en&"
    f"apiKey={API_KEY}"
)

with st.spinner("Loading latest news..."):
    response = requests.get(url)

if response.status_code != 200:
    st.error(f"API Error: {response.status_code}")
    st.write(response.text)
    st.stop()

data = response.json()

st.write("API Status:", data.get("status"))

articles = data.get("articles", [])

if len(articles) == 0:
    st.warning("No articles found.")
    st.write(data)
    st.stop()

st.success(f"Found {len(articles)} articles")

for article in articles:

    st.markdown("---")

    st.subheader(
        article.get("title", "No Title")
    )

    st.write(
        article.get(
            "description",
            "No Description Available"
        )
    )

    st.caption(
        article.get(
            "publishedAt",
            ""
        )
    )

    st.link_button(
        "Read Full Article",
        article.get("url", "")
    )

    from utils.theme import apply_theme

apply_theme()