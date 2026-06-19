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
st.caption(
    "Free • No signup required • Photos are not stored"
)

st.write(
    """
    Upload a photo and get beginner-friendly feedback about
    camera settings and common photography mistakes.

    **Best For:**
    - Landscapes
    - Wildlife
    - Birds
    - Travel photos
    - Family photos
    - Everyday photography
    """
)


st.info(
    "Tip: The most useful feedback comes from photos that didn't turn out the way you expected."
)

# ========================
# PHOTO UPLOAD
# ========================


## will need ot make avail for .arw, .cr2, .nef, .dng ..etc later

uploaded_file = st.file_uploader(
    "Choose a JPG or JPEG image - please upload ONE image at a time",
    type=["jpg", "jpeg"]
)


# ========================
# ANALYSIS SECTION
# ========================

if "last_upload" not in st.session_state:

    st.session_state.last_upload = None


if uploaded_file is not None:

    if uploaded_file.name != st.session_state.last_upload:

        log_event("Upload")

        st.session_state.last_upload = (
            uploaded_file.name
        )

    st.image(
        uploaded_file,
        caption="Uploaded Photo",
        width="stretch"
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

st.divider()

st.subheader("Current Limitations")

st.write(
    """
    - Only supports JPG and JPEG images
    - Advanced techniques such as long exposures, light trails,
      waterfalls, and some night photography may trigger warnings
      that can be ignored if the effect was intentional
    - Some camera models provide more metadata than others
    - This tool is designed primarily for beginner photographers
    """
)

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
    "Anything confusing, incorrect, or missing? Tell me what you'd like the tool to explain better or add in a future update."
)
st.caption(
    "Examples: composition analysis, RAW support, iPhone photos, editing suggestions, horizon detection, etc."
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
# PRIVACY
# ========================

st.divider()

st.subheader("Your Photos Stay Yours")

st.write(
    """
    I built this tool to help beginners learn photography.

    Uploaded photos are analyzed and then discarded.

    I do not save, sell, share, or use your photos for AI training.

    I only collect anonymous statistics such as:

    - Number of uploads
    - Helpful / Not Helpful ratings
    - Written feedback that users choose to submit

    No images are permanently stored.
    """
)

st.divider()

st.subheader("How Photo Coach Works")

st.write(
    """
    Photo Coach does not use AI to judge your photos.

    Instead, it analyzes information contained within
    the image itself, including camera settings used and
    measurable image characteristics such as brightness,
    blur, contrast, noise, and color balance.

    Feedback is generated using basic photography rules and
    image analysis rather than subjective opinions.

    The goal is to explain *why* a photo may have turned
    out a certain way and help beginners understand what
    their camera settings were doing.
    """
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

The problem wasn't that information didn't exist.
There are thousands of photography books, YouTube
videos, and tutorials available online.

The problem was that none of them were helping in
the moment.

A video might explain settings for a cloudy day
while she was shooting in bright sunlight. A book
might explain shutter speed, but it couldn't look
at her actual photo and tell her what went wrong.

She kept asking me questions about exposure, blur,
focus, and why certain photos didn't turn out the
way she expected.

After answering the same questions over and over,
I realized there should be an easier way for
beginners to understand what their camera settings
are actually doing.

So I built Photo Coach.

The goal is simple:

Upload a photo, get beginner-friendly feedback,
and learn from your own images instead of generic
examples.

If it helps other photographers learn too, that's
even better.

And Mom, if you're reading this, you can still
call me to ask your questions.
"""

)
