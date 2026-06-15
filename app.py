import streamlit as st

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="EBLE",
    page_icon="🚀",
    layout="wide"
)

# ==================================
# SESSION STATE
# ==================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ==================================
# LOGIN FUNCTION
# ==================================

def login():
    st.session_state.logged_in = True
    st.rerun()

# ==================================
# SIDEBAR
# ==================================

if st.session_state.logged_in:

    st.sidebar.title("🚀 EBLE")

    st.sidebar.markdown(
        """
        **Empowering Every Business to Level Up**
        """
    )

    st.sidebar.success("Logged In")

# ==================================
# LOGIN PAGE
# ==================================

if not st.session_state.logged_in:

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown(
            """
            # 🚀 EBLE

            ### Empowering Every Business to Level Up
            """
        )

        st.markdown("---")

        st.info(
            """
            AI-Powered Business Intelligence Platform
            for Vendors, Kirana Stores and Small Businesses
            """
        )

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button(
            "🔐 Login",
            use_container_width=True
        ):

            if (
                email == "demo@eble.ai"
                and password == "123456"
            ):

                login()

            else:

                st.error(
                    "Invalid Credentials"
                )

        st.markdown("### OR")

        if st.button(
            "🚀 Continue Demo",
            use_container_width=True
        ):
            login()

        st.markdown("---")

        st.subheader("✨ Key Features")

        st.markdown(
            """
            ✅ Revenue Management

            ✅ Expense Tracking

            ✅ Analytics Dashboard

            ✅ AI Advisor

            ✅ AI Forecasting

            ✅ Financial Readiness

            ✅ Credit Hub

            ✅ OCR Receipt Scanner

            ✅ Multi-Language Support
            """
        )

# ==================================
# HOME PAGE
# ==================================

else:

    st.title("🚀 EBLE")

    st.subheader(
        "Empowering Every Business to Level Up"
    )

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🏪 Businesses",
            "5"
        )

    with c2:
        st.metric(
            "📊 Modules",
            "10"
        )

    with c3:
        st.metric(
            "🤖 AI Features",
            "4"
        )

    st.markdown("---")

    st.subheader("🌟 Platform Overview")

    st.info(
        """
        EBLE is an AI-powered business platform
        designed for vendors, kirana stores,
        street businesses and small enterprises.

        The platform helps businesses:

        • Track Revenue

        • Manage Expenses

        • Analyze Performance

        • Forecast Growth

        • Improve Financial Readiness

        • Discover Credit Opportunities

        • Digitize Records

        • Access Business Tools in Regional Languages
        """
    )

    st.markdown("---")

    st.subheader("🚀 Available Modules")

    st.success(
        """
        📊 Dashboard

        💰 Revenue Manager

        💸 Expense Manager

        📈 Analytics Center

        🤖 AI Advisor

        🔮 AI Forecasting

        📑 Financial Readiness

        🏦 Credit Hub

        📷 OCR Scanner

        🌐 Language Support

        🚀 Future Roadmap
        """
    )

    st.markdown("---")

    st.subheader("🎯 Vision")

    st.warning(
        """
        To become India's Operating System
        for Micro-Businesses and Vendors.
        """
    )

    st.success(
        """
        Use the sidebar to navigate through
        all EBLE modules.
        """
    )