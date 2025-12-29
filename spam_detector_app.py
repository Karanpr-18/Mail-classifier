import streamlit as st
import joblib

st.set_page_config(page_title="Spam Detection App", page_icon="📧", layout="wide")

# ─────────────────────────  GLOBAL CSS  ─────────────────────────
st.markdown("""
<style>
header,[data-testid="stSidebar"],#MainMenu,footer{display:none!important;}

.stApp{
    background:linear-gradient(135deg,#667eea 0%,#764ba2 100%)!important;
}

.menu-btn{
    background:#23272b;color:#64ffda;border:2px solid #64ffda;
    border-radius:14px;font-size:1.25rem;font-weight:700;line-height:1;
    padding:8px 18px;box-shadow:0 3px 14px #0004;
    position:fixed;top:8px;left:22px;z-index:3000;
}
.menu-btn:hover{background:#764ba2;color:#fff;}

.sb-card{
    background:rgba(40,41,63,.97);border-radius:22px;
    box-shadow:0 8px 34px #000a,0 0 18px #64ffda55;
    padding:24px 20px 18px 20px;color:#fff;width:350px;max-width:97vw;
}
@media(max-width:600px){
    .sb-card{top:12vw!important;left:2vw!important;width:95vw!important;}
    .menu-btn{left:2vw!important;top:8px!important;}
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────  STATE  ─────────────────────────
if "show_menu" not in st.session_state:
    st.session_state.show_menu = False

# ─────────────────────────  TOGGLE BUTTON  ─────────────────────
label = "☰ Menu" if not st.session_state.show_menu else "✕ Close"
if st.button(label, key="toggle",
             on_click=lambda: st.session_state.update(show_menu=not st.session_state.show_menu),
             help="Open / close info panel"):
    pass

# ─────────────────────────  LAYOUT  ─────────────────────────
menu_w = 2.5 if st.session_state.show_menu else 0.1
menu_col, main_col = st.columns([menu_w, 10 - menu_w], gap="large")

# ─────────────────────────  SIDEBAR CARD  ────────────────────
with menu_col:
    if st.session_state.show_menu:
        st.markdown("""
        <div class="sb-card">
          <h2 style="color:#64ffda;text-align:center;margin:0 0 10px 0;">About This App</h2>
          <p style="text-align:center;font-size:1.05rem;">Uses machine-learning to detect spam messages.</p>
          <h3 style="margin-bottom:6px;">Features</h3>
          <ul>
            <li>🤖 AI-powered detection</li>
            <li>⚡ Instant results</li>
            <li>🎯 High accuracy</li>
            <li>🔒 Privacy-focused</li>
          </ul>
          <div style="text-align:center;margin-top:12px;">
            <a href="https://github.com/Karanpr-18" target="_blank" style="display:inline-flex;align-items:center;background:#23272b;color:#fff;padding:6px 14px;border:2px solid #64ffda;border-radius:18px;font-weight:600;margin-right:10px;text-decoration:none;">
              <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" style="width:22px;height:22px;border-radius:50%;border:1.2px solid #64ffda;background:#fff;margin-right:7px;">
              GitHub
            </a>
            <a href="https://www.linkedin.com/in/karan-bhoriya-b5a3382b7" target="_blank" style="display:inline-flex;align-items:center;background:#0a66c2;color:#fff;padding:6px 14px;border:2px solid #64ffda;border-radius:18px;font-weight:600;text-decoration:none;">
              <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg" style="filter:invert(1);width:22px;height:22px;margin-right:7px;">
              LinkedIn
            </a>
            <div style="font-size:.9rem;color:rgba(255,255,255,.75);margin-top:8px;">
              Built by Karan
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────  MAIN APP  ─────────────────────────
with main_col:
    _, mid, _ = st.columns([1, 4, 1])
    with mid:
        model = joblib.load("spam_classifier_model.pkl")
        vectorizer = joblib.load("vectorizer.pkl")

        st.markdown("<h1 style='margin-bottom:1.1rem;'>📧 Spam Detection App</h1>",
                    unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;color:rgba(255,255,255,.9);font-size:1.15rem;margin-bottom:1.8rem;'>Paste a message to see if it's spam.</p>",
                    unsafe_allow_html=True)

        text = st.text_area("Message", height=140,
                            placeholder="Paste email or chat message here…")

        if st.button("🔎 Check"):
            if not text.strip():
                st.warning("Nothing to analyse.")
            else:
                with st.spinner("Analysing…"):
                    pred = model.predict(vectorizer.transform([text]))[0]
                
                # Fixed: Use proper if-else instead of ternary operator
                if pred == 1:
                    st.error("🚫 Looks like **spam**.")
                    st.balloons()
                else:
                    st.success("✅ Looks **clean**.")
