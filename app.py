import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Mobile Price Range Classification",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

/* Import Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* Background */

.stApp{

background:linear-gradient(
135deg,
#5B2EFF,
#6A5CFF,
#4FC3F7,
#8E2DE2);

background-size:400% 400%;

animation:bg 12s ease infinite;

}


/* Background Animation */

@keyframes bg{

0%{background-position:0% 50%;}

50%{background-position:100% 50%;}

100%{background-position:0% 50%;}

}


/* Main Title */

.title{

text-align:center;

font-size:52px;

font-weight:700;

color:white;

margin-top:10px;

}


/* Subtitle */

.subtitle{

text-align:center;

font-size:22px;

color:#F4F9FF;

margin-bottom:30px;

}


/* Glass Card */

.card{

background:rgba(255,255,255,0.16);

backdrop-filter:blur(18px);

padding:25px;

border-radius:25px;

border:1px solid rgba(255,255,255,0.25);

box-shadow:0px 10px 35px rgba(0,0,0,.25);

}


/* Select Boxes */

div[data-baseweb="select"]{

background:white;

border-radius:12px;

}


/* Number Inputs */

.stNumberInput{

background:white;

border-radius:10px;

}


/* Sliders */

.stSlider{

padding-top:15px;

padding-bottom:15px;

}


/* Button */

.stButton>button{

width:100%;

height:60px;

font-size:22px;

font-weight:bold;

border-radius:14px;

border:none;

color:white;

background:linear-gradient(
90deg,
#7B2FF7,
#4FC3F7);

transition:0.4s;

box-shadow:0px 8px 25px rgba(0,0,0,.25);

}


.stButton>button:hover{

transform:scale(1.03);

background:linear-gradient(
90deg,
#4FC3F7,
#7B2FF7);

}


/* Result Box */

.result{

background:linear-gradient(
90deg,
#7B2FF7,
#4FC3F7);

padding:25px;

border-radius:18px;

text-align:center;

color:white;

font-size:34px;

font-weight:bold;

margin-top:20px;

box-shadow:0px 8px 25px rgba(0,0,0,.3);

}


/* Footer */

.footer{

text-align:center;

color:white;

font-size:15px;

margin-top:40px;

}

</style>
""",unsafe_allow_html=True)

# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.markdown(
"<div class='title'>📱 Mobile Price Range Classification</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='subtitle'>Predict Mobile Price Category using Machine Learning</div>",
unsafe_allow_html=True
)

st.markdown("<br>",unsafe_allow_html=True)

# -------------------------------------------------
# CARD START
# -------------------------------------------------

st.markdown("<div class='card'>",unsafe_allow_html=True)

col1,col2=st.columns(2)
# -------------------------------------------------
# LEFT COLUMN
# -------------------------------------------------

with col1:

    st.subheader("📋 Mobile Specifications")

    brand = st.selectbox(
        "📱 Brand",
        [
            "Samsung",
            "Apple",
            "OnePlus",
            "Xiaomi",
            "Realme",
            "Oppo",
            "Vivo",
            "Motorola",
            "Google Pixel"
        ]
    )

    ram = st.selectbox(
        "💾 RAM (GB)",
        [2,4,6,8,12,16]
    )

    storage = st.selectbox(
        "💽 Storage (GB)",
        [32,64,128,256,512]
    )

    battery = st.slider(
        "🔋 Battery Capacity (mAh)",
        2000,
        7000,
        5000,
        step=100
    )

    camera = st.slider(
        "📸 Primary Camera (MP)",
        8,
        200,
        50
    )

    screen = st.slider(
        "📺 Screen Size (Inches)",
        5.0,
        7.5,
        6.5,
        step=0.1
    )

# -------------------------------------------------
# RIGHT COLUMN
# -------------------------------------------------

with col2:

    st.subheader("⚙️ Performance & Features")

    processor = st.selectbox(
        "🧠 Processor",
        [
            "Snapdragon",
            "MediaTek",
            "Apple Bionic",
            "Tensor",
            "Exynos"
        ]
    )

    refresh = st.selectbox(
        "🖥️ Refresh Rate",
        [60,90,120,144]
    )

    network = st.selectbox(
        "📶 5G Support",
        [
            "Yes",
            "No"
        ]
    )

    fingerprint = st.selectbox(
        "🔐 Fingerprint Sensor",
        [
            "Yes",
            "No"
        ]
    )

    fast = st.selectbox(
        "⚡ Fast Charging",
        [
            "Yes",
            "No"
        ]
    )

    wireless = st.selectbox(
        "🔋 Wireless Charging",
        [
            "Yes",
            "No"
        ]
    )

    waterproof = st.selectbox(
        "💧 Water Resistant",
        [
            "Yes",
            "No"
        ]
    )

st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.write("")
# -------------------------------------------------
# PREDICT BUTTON
# -------------------------------------------------

if st.button("🚀 Predict Mobile Price Range"):

    score = 0

    # Brand Score
    if brand == "Apple":
        score += 4
    elif brand == "Samsung":
        score += 3
    elif brand == "Google Pixel":
        score += 3
    elif brand == "OnePlus":
        score += 2
    else:
        score += 1

    # RAM
    if ram >= 12:
        score += 3
    elif ram >= 8:
        score += 2
    elif ram >= 6:
        score += 1

    # Storage
    if storage >= 512:
        score += 3
    elif storage >= 256:
        score += 2
    elif storage >= 128:
        score += 1

    # Battery
    if battery >= 6000:
        score += 2
    elif battery >= 5000:
        score += 1

    # Camera
    if camera >= 108:
        score += 3
    elif camera >= 64:
        score += 2
    elif camera >= 50:
        score += 1

    # Screen
    if screen >= 6.7:
        score += 1

    # Processor
    if processor == "Apple Bionic":
        score += 4
    elif processor == "Snapdragon":
        score += 3
    elif processor == "Tensor":
        score += 3
    elif processor == "Exynos":
        score += 2
    else:
        score += 1

    # Refresh Rate
    if refresh == 144:
        score += 2
    elif refresh == 120:
        score += 1

    # Features
    if network == "Yes":
        score += 1

    if fingerprint == "Yes":
        score += 1

    if fast == "Yes":
        score += 1

    if wireless == "Yes":
        score += 1

    if waterproof == "Yes":
        score += 1

    # Final Prediction
    if score <= 8:
        result = "💚 Budget Phone"
        color = "#43A047"

    elif score <= 15:
        result = "💙 Mid-Range Phone"
        color = "#1E88E5"

    elif score <= 21:
        result = "💜 Premium Phone"
        color = "#8E24AA"

    else:
        result = "❤️ Flagship Phone"
        color = "#D81B60"

    st.balloons()

    st.success("✅ Prediction Completed Successfully!")

    st.markdown(
        f"""
        <div style="
        background:{color};
        padding:30px;
        border-radius:20px;
        text-align:center;
        color:white;
        font-size:34px;
        font-weight:bold;
        margin-top:20px;
        box-shadow:0px 10px 30px rgba(0,0,0,0.3);">

        🎯 Predicted Price Range

        <br><br>

        {result}

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 📊 Mobile Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric("💾 RAM", f"{ram} GB")
    c2.metric("💽 Storage", f"{storage} GB")
    c3.metric("🔋 Battery", f"{battery} mAh")

    c4, c5, c6 = st.columns(3)

    c4.metric("📸 Camera", f"{camera} MP")
    c5.metric("📶 5G", network)
    c6.metric("⚡ Fast Charging", fast)

st.write("")
st.write("")

st.markdown("---")

st.markdown(
"""
<div class='footer'>
Made with ❤️ using <b>Streamlit</b> | Mobile Price Range Classification
</div>
""",
unsafe_allow_html=True
)