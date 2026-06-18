import sys

from analyzers_metadata_extract import (
    extract_metadata,
    format_metadata
)

from analyzers_blur import (
    analyze_blur,
    format_blur
)

from analyzers_exposure import (
    analyze_exposure,
    format_exposure
)

from analyzers_noise import (
    analyze_noise,
    format_noise
)

from analyzers_contrast import (
    analyze_contrast,
    format_contrast
)

from analyzers_WB import (
    analyze_white_balance,
    format_white_balance
)

from rules_recos import generate_recommendations


def analyze_photo(image_path):

    metadata = extract_metadata(image_path)

    blur = analyze_blur(image_path)

    exposure = analyze_exposure(image_path)

    noise = analyze_noise(metadata)

    contrast = analyze_contrast(image_path)

    wb = analyze_white_balance(image_path)

    recommendations = generate_recommendations(
        metadata,
        blur,
        exposure,
        noise
    )

    report = []

    report.append("========================")
    report.append("PHOTO ANALYSIS REPORT")
    report.append("========================")

    report.append("")
    report.append("Metadata (Camera Settings)")
    report.append("")
    report.append(format_metadata(metadata))

    report.append("")
    report.append("------------------------------------------------------------------------")
    report.append(format_blur(blur))

    report.append("")
    report.append("------------------------------------------------------------------------")
    report.append(format_exposure(exposure))

    report.append("")
    report.append("------------------------------------------------------------------------")
    report.append(format_noise(noise))

    report.append("")
    report.append("------------------------------------------------------------------------")
    report.append(format_contrast(contrast))

    report.append("")
    report.append("------------------------------------------------------------------------")
    report.append(format_white_balance(wb))

    report.append("")
    report.append("============================================")
    report.append("TOP RECOMMENDATIONS - FOR THIS PICTURE")
    report.append("============================================")

    for r in recommendations:

        report.append(f"- {r}")
        report.append("")

    return "\n".join(report)


def main():

    # image_path = sys.argv[1]
    # image_path = input("Enter image path: ")
    image_path = r"C:\Users\Marlow\Downloads\lll\Coding\Photo Analyzer for beginning photographers\test photos\test_darkness.jpg"

    report = analyze_photo(image_path)

    print(report)


if __name__ == "__main__":
    main()