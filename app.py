<<<<<<< HEAD
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import gdown
import os


# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Plant Disease Detection", layout="centered")

# ---------- LIGHT NATURE CSS ----------
st.markdown("""
<style>

/* Remove extra white space */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
}

/* Background */
.stApp {
    background: #f4fff6;
}

/* Title */
.title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #2e7d32;
    margin-bottom: 10px;
}

/* Card */
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-top: 10px;
}

/* Buttons */
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    height: 45px;
    width: 100%;
    font-size: 16px;
}

/* Result */
.result-box {
    background-color: #c8e6c9;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    font-size: 18px;
    color: #1b5e20;
    margin-top: 15px;
}

/* Confidence */
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

# ---------- LOGIN ----------
def login():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title"> Login</div>', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
        else:
            st.error("Invalid Username or Password")

    st.markdown('</div>', unsafe_allow_html=True)

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()

# ---------- RIGHT TOP MENU ----------
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

    return tf.keras.models.load_model(MODEL_PATH)
model = load_model()

# ✅ CORRECT DATASET PATH
dataset_path = "dataset/PlantVillage"

classes = sorted([
    folder for folder in os.listdir(dataset_path)
    if os.path.isdir(os.path.join(dataset_path, folder))
])

# ---------- HOME ----------
if menu == "Home":

    st.markdown('<div class="title">Plant Disease Detection</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # ✅ CLEAN INPUT OPTION (NO CAMERA PREVIEW UNTIL SELECTED)
    option = st.radio("Choose Input Method", ["Upload Image", "Use Camera"])

    file = None

    if option == "Upload Image":
        file = st.file_uploader("Upload Leaf Image", type=["jpg","png","jpeg"])

    elif option == "Use Camera":
        file = st.camera_input("Capture Leaf Image")

    # ---------- PREDICTION ----------
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
    <p>
    This application uses <b>Deep Learning (CNN)</b> to detect plant diseases from leaf images.
    </p>

    <h4>Developed By:</h4>
    <p>
    • Sanika G. Bharankar<br>
    • Kadambari V. Sawant<br>
    • Ifrah J. Solkar
    </p>

    <h4>Technologies Used:</h4>
    <p>
    • Python<br>
    • TensorFlow / Keras<br>
    • Streamlit<br>
    • PlantVillage Dataset
    </p>
    </div>
=======
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import gdown
import os


# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Plant Disease Detection", layout="centered")

# ---------- LIGHT NATURE CSS ----------
st.markdown("""
<style>

/* Remove extra white space */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
}

/* Background */
.stApp {
    background: #f4fff6;
}

/* Title */
.title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #2e7d32;
    margin-bottom: 10px;
}

/* Card */
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-top: 10px;
}

/* Buttons */
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    height: 45px;
    width: 100%;
    font-size: 16px;
}

/* Result */
.result-box {
    background-color: #c8e6c9;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    font-size: 18px;
    color: #1b5e20;
    margin-top: 15px;
}

/* Confidence */
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

# ---------- LOGIN ----------
def login():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title"> Login</div>', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
        else:
            st.error("Invalid Username or Password")

    st.markdown('</div>', unsafe_allow_html=True)

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()

# ---------- RIGHT TOP MENU ----------
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

    return tf.keras.models.load_model(MODEL_PATH)
model = load_model()

# ✅ CORRECT DATASET PATH
dataset_path = "dataset/PlantVillage"

classes = sorted([
    folder for folder in os.listdir(dataset_path)
    if os.path.isdir(os.path.join(dataset_path, folder))
])

# ---------- HOME ----------
if menu == "Home":

    st.markdown('<div class="title">Plant Disease Detection</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # ✅ CLEAN INPUT OPTION (NO CAMERA PREVIEW UNTIL SELECTED)
    option = st.radio("Choose Input Method", ["Upload Image", "Use Camera"])

    file = None

    if option == "Upload Image":
        file = st.file_uploader("Upload Leaf Image", type=["jpg","png","jpeg"])

    elif option == "Use Camera":
        file = st.camera_input("Capture Leaf Image")

    # ---------- PREDICTION ----------
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
    <p>
    This application uses <b>Deep Learning (CNN)</b> to detect plant diseases from leaf images.
    </p>

    <h4>Developed By:</h4>
    <p>
    • Sanika G. Bharankar<br>
    • Kadambari V. Sawant<br>
    • Ifrah J. Solkar
    </p>

    <h4>Technologies Used:</h4>
    <p>
    • Python<br>
    • TensorFlow / Keras<br>
    • Streamlit<br>
    • PlantVillage Dataset
    </p>
    </div>
>>>>>>> d2b87dc07c3ba2ed42c81f24468fc3ebacf1fe77
    """, unsafe_allow_html=True)