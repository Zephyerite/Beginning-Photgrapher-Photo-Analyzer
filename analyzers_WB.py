import cv2
import numpy as np


def analyze_white_balance(image_path):

    image = cv2.imread(image_path)

    b, g, r = cv2.split(image)

    r_mean = np.mean(r)
    g_mean = np.mean(g)
    b_mean = np.mean(b)

    if b_mean > r_mean + 15:
        result = "Cool Cast"

    elif r_mean > b_mean + 15:
        result = "Warm Cast"

    else:
        result = "Neutral"

    return {
        "result": result
    }

def format_white_balance(wb):

    lines = []

    lines.append(
        "White Balance (Overall Color Tone)"
    )

    lines.append("")

    lines.append(
        f"Result: {wb['result']}"
    )

    lines.append("")

    lines.append(
        "What This Means:"
    )

    if wb["result"] == "Warm Cast":

        lines.append(
            "The image contains more yellow, orange, or golden tones."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- Golden hour lighting"
        )

        lines.append(
            "- Sunsets"
        )

        lines.append(
            "- Indoor tungsten lighting"
        )

        lines.append(
            "- White balance setting too warm"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- Leave it if the warm look was intentional"
        )

        lines.append(
            "- Use a cooler white balance setting"
        )

        lines.append(
            "- Adjust color temperature during editing"
        )

    elif wb["result"] == "Cool Cast":

        lines.append(
            "The image contains more blue tones."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- Shade"
        )

        lines.append(
            "- Cloudy weather"
        )

        lines.append(
            "- Blue hour lighting"
        )

        lines.append(
            "- White balance setting too cool"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- Leave it if the cool look was intentional"
        )

        lines.append(
            "- Use a warmer white balance setting"
        )

        lines.append(
            "- Adjust color temperature during editing"
        )

    else:

        lines.append(
            "The image appears to have a neutral color balance."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- White balance appears properly adjusted"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- No changes needed"
        )

    return "\n".join(lines)