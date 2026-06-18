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

st.title("Beginner Photographer Photo Coach")
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

    **Current Limitations:**
    - Best results come from standard JPG and JPEG images
    - Advanced techniques such as long exposures, light trails,
      waterfalls, and some night photography may trigger warnings
      that can be ignored if the effect was intentional
    - Some camera models provide more metadata than others
    - This tool is designed primarily for beginner photographers

    **Help Improve Photo Coach**
    If the tool misses something important, please use the
    feedback section below. New features and improvements are
    added based on user suggestions.
    """
)


st.info(
    "Tip: Upload a photo you think didn't turn out well. "
    "The tool is most useful when diagnosing photography mistakes."
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

# ========================
# ABOUT SECTION
# ========================

st.divider()

st.subheader("Why I Built This")

st.write(
    """
    My mom wanted to learn photography but found books,
    videos, and camera settings overwhelming.

    The biggest problem wasn't a lack of information.
    There are thousands of photography books, YouTube
    videos, blogs, and courses available.

    The problem was that none of them explained *her*
    photo.

    A book might explain motion blur, but not why her
    bird photo was blurry. A YouTube video might talk
    about exposure settings for a cloudy day, while she
    was shooting in bright sunlight. Most photography
    advice is general, but beginners usually want to
    know what happened in the specific photo they just
    took.

    She kept asking me questions about settings,
    exposure, blur, and why certain photos didn't turn
    out the way she expected.

    So I built this tool to explain photography
    mistakes in plain English and help beginners
    understand what their camera settings are actually
    doing using the photo they just uploaded.

    If it helps other photographers learn too,
    that's even better.

    And Mom, if you're reading this, you can always
    ask me in person or over the phone as well,
    don't worry :)
    """
)