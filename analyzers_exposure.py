import cv2
import numpy as np


def analyze_exposure(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    brightness = np.mean(gray)

    if brightness < 80:
        result = "Underexposed"

    elif brightness > 180:
        result = "Overexposed"

    else:
        result = "Proper Exposure"

    return {
        "brightness": round(float(brightness), 2),
        "result": result
    }

def format_exposure(exposure):

    lines = []

    lines.append(
        "Exposure (Overall Brightness)"
    )

    lines.append("")

    lines.append(
        f"Result: {exposure['result']}"
    )

    lines.append("")

    lines.append(
        "What This Means:"
    )

    if exposure["result"] == "Underexposed":

        lines.append(
            "The image appears too dark."
        )

        lines.append(
            "Details in darker areas may be difficult to see."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- ISO setting too low"
        )

        lines.append(
            "- Shutter speed too fast"
        )

        lines.append(
            "- Aperture (F-Stop) too narrow (too big F-stop number)"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- Increase ISO"
        )

        lines.append(
            "- Use a slower shutter speed"
        )

        lines.append(
            "- Use a wider aperture (smaller F-Stop number)"
        )

    elif exposure["result"] == "Overexposed":

        lines.append(
            "The image appears too bright."
        )

        lines.append(
            "Some bright areas may have lost detail."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- ISO setting too high"
        )

        lines.append(
            "- Shutter speed too slow"
        )

        lines.append(
            "- Aperture (F-Stop) too wide (too small F-stop number)"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- Lower ISO"
        )

        lines.append(
            "- Use a faster shutter speed"
        )

        lines.append(
            "- Use a narrower aperture (larger F-Stop number)"
        )

    else:

        lines.append(
            "The image brightness appears balanced."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- Camera settings appear well balanced"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- No changes needed"
        )

    return "\n".join(lines)