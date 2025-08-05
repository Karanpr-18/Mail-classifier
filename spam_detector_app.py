import streamlit as st
from streamlit_extras.st_modal import st_modal
import joblib

st.set_page_config(page_title="Spam Detection App", page_icon="📧", layout="centered")

# Add your background as usual
st.markdown("""
    <style>
        header, [data-testid="stSidebar"], #MainMenu, footer {display: none !important;}
        .stApp {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;}
    </style>
""", unsafe_allow_html=True)

# --- Only show the modal on the first load
if "show_menu" not in st.session_state:
    st.session_state["show_menu"] = True

if st.session_state["show_menu"]:
    with st_modal("ℹ️ About This App", key="modal1"):
        st.markdown("""
            <h2 style="color:#64ffda;text-align:center;margin-top:0;">About This App</h2>
            <p style="text-align:center;font-size:1.1rem;">
            This application uses machine learning to detect spam messages.<br>
            Simply paste your text and get instant results!
            </p>
            <h3 style="font-size:1.1rem;color:#fff;">Features:</h3>
            <ul>
                <li>🤖 AI-powered detection</li>
                <li>⚡ Instant results</li>
                <li>🎯 High accuracy</li>
                <li>🔒 Privacy focused</li>
            </ul>
            <div style="margin-top:12px;text-align:center;">
                <a style="
                    color:#fff;background:#23272b;border-radius:19px;
                    padding:4px 15px;text-decoration:none;font-weight:600;
                    border:2px solid #64ffda;box-shadow:0 0 7px #764ba2c0;
                    display:inline-flex;align-items:center;" 
                    href="https://github.com/Karanpr-18" target="_blank">
                    <img style="width:24px;height:24px;margin-right:7px;border-radius:50%;border:1.5px solid #64ffda;background:#fff;" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub"> Account
                </a>
                <div style="color:rgba(255,255,255,0.68);font-size:0.99rem;margin-top:6px;">
                  Built with 💜 using Streamlit by <a href="https://github.com/Karanpr-18" style="color:#64ffda;text-decoration:none;" target="_blank">Karan</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
    st.session_state["show_menu"] = False  # Only open once

# --- Main app streamlit content
model = joblib.load("spam_classifier_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.markdown("<h1 style='margin-bottom:1.2rem;'>📧 Spam Detection App</h1>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <p style="color: rgba(255,255,255,0.89); font-size: 1.2rem; font-weight: 300;">
            Check if your message is spam using AI-powered detection
        </p>
    </div>
""", unsafe_allow_html=True)

user_input = st.text_area(
    "Enter your text here:",
    height=150,
    placeholder="Paste your email or message content here..."
)

col1, col2, col3 = st.columns([1,1,1])
with col2:
    check_button = st.button("🔎 Check for Spam")

if check_button:
    if not user_input.strip():
        st.warning("⚠️ Please enter some text to analyze!")
    else:
        with st.spinner("Analyzing your text..."):
            X = vectorizer.transform([user_input])
            prediction = model.predict(X)
        if prediction[0] == 1:
            st.error("🚫 This text is classified as **SPAM**.")
            st.balloons()
        else:
            st.success("✅ This text is **NOT spam**.")
