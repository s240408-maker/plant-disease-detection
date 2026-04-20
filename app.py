```python
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import gdown
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Plant Doctor",
    page_icon="🌿",
    layout="centered"
)

# ---------- HIDE STREAMLIT HEADER ----------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------- LIGHT NATURE CSS ----------
st.markdown("""
<style>
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
}

.stApp {
    background: #f4fff6;
}

.title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #2e7d32;
    margin-bottom: 10px;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-top: 10px;
}

.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    height: 45px;
    width: 100%;
    font-size: 16px;
}

.result-box {
    background-color: #c8e6c9;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    font-size: 18px;
    color: #1b5e20;
    margin-top: 15px;
}

.conf-box {
    background-color: #bbdefb;
    padding: 12px;
    border-radius: 10px;
    text-align: center;
    margin-top: 10px;
    color: #0d47a1;
}
</style>
""", unsafe_allow_html=True)

# ---------- SESSION STATE ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------- LOGIN ----------
def login():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title"> Login</div>', unsafe_allow_html=True)

    st.text_input("Username", key="username")
    st.text_input("Password", type="password", key="password")

    if st.button("Login"):
        if (
            st.session_state.username == "admin"
            and st.session_state.password == "1234"
        ):
            st.session_state.logged_in = True
            st.success("Login Successful ✅")
            st.rerun()
        else:
            st.error("Invalid Username or Password")

    st.markdown('</div>', unsafe_allow_html=True)

if not st.session_state.logged_in:
    login()
    st.stop()

# ---------- MENU ----------
col1, col2 = st.columns([8,2])

with col2:
    menu = st.selectbox("☰ Menu", ["Home", "About Us", "Logout"])

if menu == "Logout":
    st.session_state.logged_in = False
    st.rerun()

# ---------- LOAD MODEL ----------
@st.cache_resource
def load_model():
    MODEL_PATH = "model/plant_model.h5"

    os.makedirs("model", exist_ok=True)

    file_id = "1izlzNjTNlOtVTG00rjrdt4xi-NmbLDNo"
    url = f"https://drive.google.com/uc?id={file_id}"

    if not os.path.exists(MODEL_PATH):
        with st.spinner("Downloading model..."):
            gdown.download(url, MODEL_PATH, quiet=False)

    return tf.keras.models.load_model(MODEL_PATH, compile=False)

model = load_model()

# ---------- CLASSES ----------
classes = [
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites",
    "Tomato___Target_Spot",
    "Tomato___Yellow_Leaf_Curl_Virus",
    "Tomato___healthy"
]

# ---------- HOME ----------
if menu == "Home":

    st.image("https://cdn-icons-png.flaticon.com/512/2909/2909763.png", width=90)

    st.markdown('<div class="title">Plant Disease Detection</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    option = st.radio("Choose Input Method", ["Upload Image", "Use Camera"])

    file = None

    if option == "Upload Image":
        file = st.file_uploader("Upload Leaf Image", type=["jpg","png","jpeg"])

    elif option == "Use Camera":
        file = st.camera_input("Capture Leaf Image")

    if file is not None:

        img = Image.open(file).convert("RGB")
        st.image(img, caption="Input Image", use_column_width=True)

        img = img.resize((128,128))
        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        with st.spinner("Analyzing Image..."):
            pred = model.predict(img)

        index = np.argmax(pred)
        conf = np.max(pred)

        name = classes[index].replace("___", " - ").replace("_", " ").title()

        st.markdown(f'<div class="result-box">Disease: {name}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="conf-box">Confidence: {conf*100:.2f}%</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- ABOUT ----------
elif menu == "About Us":

    st.markdown('<div class="title">About Us</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>Plant Disease Detection App</h3>
    <p>This app uses Deep Learning (CNN) to detect plant diseases.</p>

    <h4>Developed By:</h4>
    <p>
    • Sanika G. Bharankar<br>
    • Kadambari V. Sawant<br>
    • Ifrah J. Solkar
    </p>
    </div>
    """, unsafe_allow_html=True)
```
