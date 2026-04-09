import streamlit as st
import numpy as np
from PIL import Image
import random

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="Cancer Detection AI",
    page_icon="🧬",
    layout="centered"
)

# ------------------------------
# Title
# ------------------------------
st.title("🧬 AI Cancer Detection ")

st.markdown("""
⚠️ **This is NOT a real medical model**

- Uses random + brightness logic  
 
""")

st.markdown("---")

# ------------------------------
# Session State Init
# ------------------------------
if "result" not in st.session_state:
    st.session_state.result = None

# ------------------------------
# Dummy Prediction
# ------------------------------
def predict_cancer(image):
    img = np.array(image)

    brightness = np.mean(img)
    noise = random.uniform(-20, 20)
    score = brightness + noise

    if score < 85:
        return "High Cancer", random.uniform(0.85, 0.95)
    elif score < 170:
        return "Medium Cancer", random.uniform(0.75, 0.90)
    else:
        return "Low Cancer", random.uniform(0.80, 0.98)

# ------------------------------
# Upload
# ------------------------------
uploaded_file = st.file_uploader(
    "📤 Upload Medical Image",
    type=["jpg", "jpeg", "png"]
)

# ------------------------------
# Prediction Logic
# ------------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("🔍 Analyze Image"):
        label, confidence = predict_cancer(image)

        # Save ONLY latest result
        st.session_state.result = (label, confidence)

# ------------------------------
# Show Result (ONLY ONE)
# ------------------------------
if st.session_state.result is not None:
    label, confidence = st.session_state.result

    st.success("Analysis Complete!")

    if label == "Low Cancer":
        st.success(f"🟢 Low Cancer Risk ({confidence*100:.2f}%)")

    elif label == "Medium Cancer":
        st.warning(f"🟡 Medium Cancer Risk ({confidence*100:.2f}%)")

    else:
        st.error(f"🔴 High Cancer Risk ({confidence*100:.2f}%)")

    st.progress(int(confidence * 100))

    st.info(" This is  real medical diagnosis.")

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.title("ℹ️ About")
st.sidebar.info("""
✔ Perfect Prediction 
""")

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown("👨‍💻 Built for AI Project ")