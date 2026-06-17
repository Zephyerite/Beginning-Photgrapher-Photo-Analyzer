import cv2


def analyze_contrast(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    contrast = gray.std()

    if contrast < 40:
        result = "Low Contrast"

    elif contrast > 80:
        result = "High Contrast"

    else:
        result = "Normal Contrast"

    return {
        "score": round(float(contrast), 2),
        "result": result
    }

def format_contrast(contrast):

    lines = []

    lines.append(
        "Contrast (Difference Between Light and Dark Areas, aka Shadows and Highlights)"
    )

    lines.append("")

    lines.append(
        f"Result: {contrast['result']}"
    )

    lines.append("")

    lines.append(
        "What This Means:"
    )

    if contrast["result"] == "Low Contrast":

        lines.append(
            "The image may look flat because bright and dark areas are too similar."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- Cloudy or overcast weather"
        )

        lines.append(
            "- Fog, mist, or haze"
        )

        lines.append(
            "- Flat lighting conditions"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- Increase contrast during editing"
        )

        lines.append(
            "- Photograph in stronger light"
        )

    elif contrast["result"] == "High Contrast":

        lines.append(
            "There is a strong difference between bright and dark areas."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- Direct sunlight"
        )

        lines.append(
            "- Strong shadows"
        )

        lines.append(
            "- Bright highlights next to dark areas"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- Photograph during softer lighting"
        )

        lines.append(
            "- Reduce contrast during editing"
        )

    else:

        lines.append(
            "The balance between bright and dark areas appears normal."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- Balanced lighting conditions"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- No changes needed"
        )

    return "\n".join(lines)