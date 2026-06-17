import cv2


def analyze_blur(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    score = cv2.Laplacian(
        gray,
        cv2.CV_64F
    ).var()

    if score < 50:
        result = "Very Blurry"

    elif score < 150:
        result = "Slightly Blurry"

    else:
        result = "Sharp"

    return {
        "score": round(float(score), 2),
        "result": result
    }

def format_blur(blur):

    lines = []

    lines.append(
        "Sharpness (Focus & Blur)"
    )

    lines.append("")

    lines.append(
        f"Result: {blur['result']}"
    )

    lines.append("")

    lines.append(
        "What This Means:"
    )

    if blur["result"] == "Sharp":

        lines.append(
            "The image appears sharp with clear details."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- Camera was stable"
        )

        lines.append(
            "- Focus was placed correctly"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- No changes needed"
        )

    elif blur["result"] == "Slightly Blurry":

        lines.append(
            "The image appears slightly soft and may be missing some detail."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- Minor camera movement"
        )

        lines.append(
            "- Subject movement"
        )

        lines.append(
            "- Focus slightly missed the subject"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- Use a faster shutter speed"
        )

        lines.append(
            "- Hold the camera steadier"
        )

        lines.append(
            "- Double check focus before taking the photo"
        )

    else:

        lines.append(
            "The image appears blurry and lacks detail."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- Camera movement while taking the photo"
        )

        lines.append(
            "- Subject movement"
        )

        lines.append(
            "- Focus missed the subject"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- Use a faster shutter speed"
        )

        lines.append(
            "- Use a tripod or stabilize the camera"
        )

        lines.append(
            "- Make sure focus is on the subject"
        )

    return "\n".join(lines)