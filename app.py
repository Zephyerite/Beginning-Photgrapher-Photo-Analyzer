import tempfile
import streamlit as st

from analyze import analyze_photo


st.set_page_config(
    page_title="Photo Coach",
    layout="centered"
)

st.title("Photo Coach")

st.write(
    """
    Upload a photo and receive beginner-friendly
    feedback about camera settings and common
    photography mistakes.
    """
)

uploaded_file = st.file_uploader(
    "Upload a JPG image",
    type=["jpg", "jpeg"]
)

if uploaded_file is not None:

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

    st.subheader(
        "Analysis Report"
    )

    st.text(report)