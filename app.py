import streamlit as st
import tempfile

from analyze import analyze_photo
from create_analytics import log_event

# st.title()
# st.header()
# st.markdown()
# st.columns()
# st.image()
# st.button()
# st.text_area()
# st.divider()


# ========================
# PAGE SETTINGS
# ========================

st.set_page_config(
    page_title="Photo Coach",
    layout="centered"
)


# ========================
# HEADER
# ========================

st.title("Photo Coach")

st.write(
    """
    Upload a photo and get beginner-friendly feedback about
    camera settings and common photography mistakes.
    """
)


# ========================
# PHOTO UPLOAD
# ========================


## will need ot make avail for .arw, .cr2, .nef, .dng ..etc later

uploaded_file = st.file_uploader(
    "Choose a JPG or JPEG image",
    type=["jpg", "jpeg"]
)


# ========================
# ANALYSIS SECTION
# ========================

if uploaded_file is not None:

    log_event("Upload")

    st.image(
        uploaded_file,
        caption="Uploaded Photo",
        use_container_width=True
    )

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as tmp_file:

        tmp_file.write(
            uploaded_file.getvalue()
        )

        image_path = tmp_file.name

    with st.spinner(
        "Analyzing photo..."
    ):

        report = analyze_photo(
            image_path
        )

    st.divider()

    #st.subheader("Photo Analysis Report")

    st.text(report)


# ========================
# FEEDBACK SECTION
# ========================

st.divider()

st.subheader("Was this feedback helpful?")

col1, col2 = st.columns(2)

with col1:
    if st.button("👍 Yes"):

        log_event("Helpful")

        st.success(
            "Thanks for the feedback!"
        )

with col2:
    if st.button("👎 No"):

        log_event("Not Helpful")

        st.success(
            "Thanks for the feedback!"
        )


feedback = st.text_area(
    "Anything confusing or missing?"
)

if st.button("Submit Feedback"):

    if feedback.strip():

        log_event(
            "Feedback",
            feedback
        )

        st.success(
            "Feedback submitted!"
        )


# ========================
# ABOUT SECTION
# ========================

st.divider()

st.subheader("Why I Built This")

st.write(
    """
    My mom wanted to learn photography but found books,
    videos, and camera settings overwhelming.

    She kept asking me questions about settings,
    exposure, blur, and why certain photos didn't turn
    out the way she expected.

    So I built this tool to explain photography
    mistakes in plain English and help beginners
    understand what their camera settings are actually
    doing.

    If it helps other photographers learn too,
    that's even better.
    """
)