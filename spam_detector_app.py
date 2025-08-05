import streamlit as st
import joblib

# Page configuration
st.set_page_config(page_title="Spam Detection App", page_icon="📧", layout="centered")

# Load your trained model and vectorizer
model = joblib.load("spam_classifier_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Custom CSS to remove Streamlit's default top menu and footer, and style the page
st.markdown("""
    <style>
        /* Hide Streamlit's default menu and footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            background-attachment: fixed;
        }
        
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        
        h1 {
            color: #ffffff !important;
            text-align: center;
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .stTextArea > div > div > textarea {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: #ffffff !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 10px !important;
            backdrop-filter: blur(5px);
        }
        
        .stButton > button {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 25px !important;
            padding: 0.75rem 2rem !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3) !important;
        }
        
        .stAlert {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: #ffffff !important;
            border-radius: 10px !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            backdrop-filter: blur(5px) !important;
        }
        
        .sidebar .sidebar-content {
            background: rgba(255, 255, 255, 0.05) !important;
            backdrop-filter: blur(10px) !important;
        }
        
        .sidebar h2 {
            color: #ffffff !important;
        }
        
        .sidebar p {
            color: rgba(255, 255, 255, 0.8) !important;
        }
        
        /* Style for text area label */
        .stTextArea label {
            color: #ffffff !important;
            font-weight: 500 !important;
        }
        
        /* Style for warning/success messages */
        .stSuccess {
            background-color: rgba(76, 175, 80, 0.2) !important;
            color: #ffffff !important;
            border: 1px solid rgba(76, 175, 80, 0.4) !important;
        }
        
        .stError {
            background-color: rgba(244, 67, 54, 0.2) !important;
            color: #ffffff !important;
            border: 1px solid rgba(244, 67, 54, 0.4) !important;
        }
        
        .stWarning {
            background-color: rgba(255, 152, 0, 0.2) !important;
            color: #ffffff !important;
            border: 1px solid rgba(255, 152, 0, 0.4) !important;
        }

        /* Clickable GitHub profile link styling */
        .github-profile-link {
            color: rgba(255, 255, 255, 0.8) !important;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        
        .github-profile-link:hover {
            color: #64ffda !important;
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# App title with attractive styling
st.markdown("<h1>📧 Spam Detection App</h1>", unsafe_allow_html=True)

# Subtitle
st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <p style="color: rgba(255, 255, 255, 0.8); font-size: 1.2rem; font-weight: 300;">
            Check if your message is spam using AI-powered detection
        </p>
    </div>
""", unsafe_allow_html=True)

# Text input area
user_input = st.text_area(
    "Enter your text here:", 
    height=150,
    placeholder="Paste your email or message content here..."
)

# Center the button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    check_button = st.button("🔎 Check for Spam")

# Spam detection logic
if check_button:
    if not user_input.strip():
        st.warning("⚠️ Please enter some text to analyze!")
    else:
        # Show a spinner while processing
        with st.spinner("Analyzing your text..."):
            X = vectorizer.transform([user_input])
            prediction = model.predict(X)
            
        if prediction[0] == 1:  # spam
            st.error("🚫 This text is classified as **SPAM**.")
            st.balloons()
        else:  # not spam
            st.success("✅ This text is **NOT spam**.")

# Sidebar with information
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h2>About This App</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <p style="color: rgba(255, 255, 255, 0.8);">
        This application uses machine learning to detect spam messages. 
        Simply paste your text and get instant results!
        </p>
        
        <h3 style="color: #ffffff; margin-top: 2rem;">Features:</h3>
        <ul style="color: rgba(255, 255, 255, 0.8);">
            <li>🤖 AI-powered detection</li>
            <li>⚡ Instant results</li>
            <li>🎯 High accuracy</li>
            <li>🔒 Privacy focused</li>
        </ul>
        
        <div style="margin-top: 2rem; text-align: center;">
            <p style="color: rgba(255, 255, 255, 0.6);">
            Built with 💜 using Streamlit by 
            <a href="https://github.com/Karanpr-18" target="_blank" class="github-profile-link"> Karan </a>
            </p>
        </div>
    """, unsafe_allow_html=True)
