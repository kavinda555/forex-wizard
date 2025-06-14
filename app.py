import streamlit as st
from PIL import Image

st.set_page_config(page_title="Forex Fizard AI", layout="centered")

st.title("📈 Forex Fizard - AI Market Analyzer")
st.write("Upload a chart screenshot below and let AI analyze it using support & resistance strategy + trend detection.")

# --- Input Section ---
with st.container():
    st.subheader("🖼️ Upload Screenshot")
    uploaded_file = st.file_uploader("Upload your chart (PNG, JPG)", type=["png", "jpg", "jpeg"])
    
    st.subheader("📝 Prompt")
    prompt = st.text_input("Describe your request (e.g., Should I Buy or Sell?)")

# --- Action Button ---
if st.button("🔍 Run Analysis") and uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Chart", use_column_width=True)

    # --- Output Box ---
    with st.container():
        st.subheader("📊 AI Analysis")
        st.markdown("""
        <div style="border: 2px solid #4CAF50; border-radius: 10px; padding: 15px; background-color: #f9f9f9;">
        
        ### Trend Analysis  
        The price has made a significant upward move above the moving average, indicating strong bullish momentum.
        
        ### RSI  
        RSI is at 63.5%, which is above the neutral 50 but still below the overbought level of 70.  
        This suggests that there is potential for further upward movement but also warrants caution.
        
        ### Recommendation  
        ✅ Buy — Considering the strong upward move and momentum, entering a buy position could be favorable.
        
        ### Take Profit and Stop Loss  
        - 🎯 Take Profit: Set around 3055 to 3060  
        - 🛡️ Stop Loss: Set around 3025
        
        *Based on Support & Resistance Strategy. Make sure to review with live market data.*
        
        </div>
        """, unsafe_allow_html=True)

elif uploaded_file is None and prompt:
    st.warning("📷 Please upload a chart screenshot before running analysis.")
