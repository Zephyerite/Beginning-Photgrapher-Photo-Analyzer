import exifread

def convert_fraction(value):

    value = str(value)

    if "/" in value:

        num, den = value.split("/")

        return round(
            float(num) / float(den),
            2
        )

    return round(
        float(value),
        2
    )

def extract_metadata(image_path):

    metadata = {
        "camera_maker": "Unknown",
        "camera_model": "Unknown",
        "lens_model": "Unknown",
        "f_stop": "Unknown",
        "shutter_speed": "Unknown",
        "iso_speed": "Unknown",
        "focal_length": "Unknown",

        # raw values for future rules
        "iso_value": None,
        "f_stop_value": None,
        "shutter_value": None,
        "focal_length_value": None
    }

    try:

        with open(image_path, "rb") as f:

            tags = exifread.process_file(f)

            # print("FNumber =", tags.get("EXIF FNumber"))
            # print("ExposureTime =", tags.get("EXIF ExposureTime"))
            # print("FocalLength =", tags.get("EXIF FocalLength"))

        # Camera Maker

        if "Image Make" in tags:

            metadata["camera_maker"] = str(
                tags["Image Make"]
            )

        # Camera Model

        if "Image Model" in tags:

            metadata["camera_model"] = str(
                tags["Image Model"]
            )

        # Lens Model

        if "EXIF LensModel" in tags:

            metadata["lens_model"] = str(
                tags["EXIF LensModel"]
            )

        # ISO

        if "EXIF ISOSpeedRatings" in tags:

            iso = int(
                str(tags["EXIF ISOSpeedRatings"])
            )

            metadata["iso_value"] = iso

            metadata["iso_speed"] = (
                f"ISO-{iso}"
            )

        # print("FOUND FNUMBER:",
        #       tags.get("EXIF FNumber"))

        # print("FOUND SHUTTER:",
        #       tags.get("EXIF ExposureTime"))

        # print("FOUND FOCAL:",
        #       tags.get("EXIF FocalLength"))
        
        # F-Stop

        if "EXIF FNumber" in tags:

            f_stop = convert_fraction(
                tags["EXIF FNumber"]
            )

            metadata["f_stop_value"] = f_stop

            metadata["f_stop"] = (
                f"f/{f_stop:g}"
            )

        # Shutter Speed

        if "EXIF ExposureTime" in tags:

            shutter = convert_fraction(
                tags["EXIF ExposureTime"]
            )

            metadata["shutter_value"] = shutter

            if shutter >= 1:

                metadata["shutter_speed"] = (
                    f"{shutter:g} sec"
                )

            else:

                metadata["shutter_speed"] = (
                    f"1/{round(1/shutter)} sec"
                )

        # Focal Length

        if "EXIF FocalLength" in tags:

            focal = convert_fraction(
                tags["EXIF FocalLength"]
            )

            metadata["focal_length_value"] = focal

            metadata["focal_length"] = (
                f"{round(focal)} mm"
            )

    except Exception as e:

        print(
            "Metadata error:",
            e
        )

    return metadata


def format_metadata(metadata):

    lines = []

    lines.append("")

    # lines.append(
    #     f"Camera Maker: "
    #     f"{metadata['camera_maker']}"
    # )

    # lines.append(
    #     f"Camera Model: "
    #     f"{metadata['camera_model']}"
    # )

    lines.append(
        f"Lens Model: "
        f"{metadata['lens_model']}"
    )

    lines.append(
        f"F-Stop (Aperture): "
        f"{metadata['f_stop']}"
    )

    lines.append(
        f"Exposure Time (Shutter Speed): "
        f"{metadata['shutter_speed']}"
    )

    lines.append(
        f"ISO Speed: "
        f"{metadata['iso_speed']}"
    )

    lines.append(
        f"Focal Length for shot: "
        f"{metadata['focal_length']}"
    )

    return "\n".join(lines)