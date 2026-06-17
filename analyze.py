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


def main():

    #image_path = sys.argv[1]
    #image_path = input("Enter image path: ")
    image_path = r"C:\Users\Marlow\Downloads\lll\Coding\Photo Analyzer for beginning photgraphers\test photos\test_exposure.jpg"

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

    print("========================")
    print("PHOTO ANALYSIS REPORT")
    print("========================")

    print("\nMetadata (Camera Settings):")
    print(format_metadata(metadata))

    print("\n------------------------")
    print(format_blur(blur))
    print()
    print("\n------------------------")
    print(format_exposure(exposure))
    print()
    print("\n------------------------")
    print(format_noise(noise))
    print()
    print("\n------------------------")
    print(format_contrast(contrast))
    print()
    print("\n------------------------")
    print(format_white_balance(wb))
    print()
    print("")
    print("========================")
    print("TOP RECOMMENDATIONS - FOR THIS PICTURE")
    print("========================")

    for r in recommendations:
        print("-", r)
        print("")


if __name__ == "__main__":
    main()