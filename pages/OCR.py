import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="OCR Scanner",
    page_icon="📷",
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
st.title("📷 OCR Receipt Scanner")

uploaded_file = st.file_uploader(
    "Upload Receipt",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Receipt",
        use_container_width=True
    )

    st.success(
        "Receipt Uploaded Successfully"
    )

    st.markdown("---")

    st.subheader("📄 OCR Output (Demo)")

    st.text_area(
        "Extracted Text",
        """
Shop: Balaji Kirana Store

Rice ₹500
Oil ₹250
Sugar ₹180

Total Amount: ₹930

Date: 15-06-2026
        """,
        height=250
    )

    st.success(
        "Future Version: Real OCR extraction using AI Vision."
    )
