def analyze_noise(metadata):

    iso = metadata.get("iso_value")

    if iso is None:

        return {
            "result": "Unknown"
        }

    if iso <= 800:

        result = "Low Noise"

    elif iso <= 3200:

        result = "Moderate Noise"

    else:

        result = "High Noise"

    return {
        "result": result
    }

def format_noise(noise):

    lines = []

    lines.append(
        "Noise (Digital Grain)"
    )

    lines.append("")

    lines.append(
        f"Result: {noise['result']}"
    )

    lines.append("")

    lines.append(
        "What This Means:"
    )

    if noise["result"] == "Low Noise":

        lines.append(
            "The image appears clean with little visible grain."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- Lower ISO settings"
        )

        lines.append(
            "- Good lighting conditions"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- No changes needed"
        )

    elif noise["result"] == "Moderate Noise":

        lines.append(
            "Some digital grain may be visible."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- Medium ISO settings"
        )

        lines.append(
            "- Lower light conditions"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- Lower ISO if possible"
        )

        lines.append(
            "- Increase available light"
        )

    elif noise["result"] == "High Noise":

        lines.append(
            "Noticeable digital grain may reduce image quality."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- High ISO settings"
        )

        lines.append(
            "- Very low light conditions"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- Lower ISO"
        )

        lines.append(
            "- Use a tripod and slower shutter speed"
        )

        lines.append(
            "- Increase available light"
        )

    else:

        lines.append(
            "Noise level could not be determined."
        )

        lines.append("")

        lines.append(
            "Common Causes:"
        )

        lines.append(
            "- Metadata may be missing"
        )

        lines.append("")

        lines.append(
            "Suggested Fixes:"
        )

        lines.append(
            "- Try another image"
        )

    return "\n".join(lines)