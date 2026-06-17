def shutter_to_float(shutter):

    if shutter is None:
        return None

    shutter = str(shutter)

    try:

        if "/" in shutter:

            num, den = shutter.split("/")

            return float(num) / float(den)

        return float(shutter)

    except:

        return None

def generate_recommendations(
    metadata,
    blur,
    exposure,
    noise
):

    recs = []

    iso = metadata.get(
        "iso_value"
    )

    focal = metadata.get(
        "focal_length_value"
    )

    aperture = metadata.get(
        "f_stop_value"
    )

    shutter = metadata.get(
        "shutter_value"
    )

    shutter_seconds = shutter_to_float(
        shutter
    )

    # ----------------------------------
    # BLUR
    # ----------------------------------

    if blur["result"] == "Very Blurry":

        if shutter_seconds is not None:

            if shutter_seconds >= 1:

                recs.append(
                    f"Your shutter speed was {shutter} second(s), which is extremely slow for most handheld photography. Camera movement is likely causing the blur. Try using a tripod or a much faster shutter speed."
                )

            elif shutter_seconds > 1/20:

                recs.append(
                    f"Your shutter speed was {shutter}. This is relatively slow and may cause blur from camera movement. Try using 1/60 or faster."
                )

            elif shutter_seconds > 1/60:

                recs.append(
                    f"Your shutter speed was {shutter}. This may still cause blur depending on subject movement. Try 1/125 or faster for moving subjects."
                )

            else:

                recs.append(
                    f"The image appears blurry even though your shutter speed was {shutter}. Focus accuracy or subject movement may be contributing."
                )

        else:

            recs.append(
                "The image appears blurry. Try using a faster shutter speed or stabilizing the camera."
            )

    # ----------------------------------
    # NOISE
    # ----------------------------------

    if noise["result"] == "High Noise":

        recs.append(
            f"Your ISO was ISO-{iso}, which is quite high and may be causing visible digital grain. Lower ISO settings usually produce cleaner images."
        )

    elif noise["result"] == "Moderate Noise":

        recs.append(
            f"Your ISO was ISO-{iso}. Some digital grain may be visible. If lighting allows, try lowering ISO."
        )

    # ----------------------------------
    # OVEREXPOSURE
    # ----------------------------------

    if exposure["result"] == "Overexposed":

        if iso and iso > 800:

            recs.append(
                f"Your ISO was ISO-{iso}, which may be contributing to the image being too bright. Consider lowering ISO."
            )

        if shutter_seconds and shutter_seconds > 1/60:

            recs.append(
                f"Your shutter speed was {shutter}, allowing a large amount of light into the camera. A faster shutter speed may reduce overexposure."
            )

        if aperture and aperture <= 4:

            recs.append(
                f"Your aperture was f/{aperture:g}, which is a wide aperture that allows a lot of light into the camera. A larger F-Stop number may help reduce brightness."
            )

    # ----------------------------------
    # UNDEREXPOSURE
    # ----------------------------------

    if exposure["result"] == "Underexposed":

        if iso and iso < 400:

            recs.append(
                f"Your ISO was ISO-{iso}. Increasing ISO may help brighten the image."
            )

        if shutter_seconds and shutter_seconds < 1/500:

            recs.append(
                f"Your shutter speed was {shutter}, which is very fast and may be making the image too dark. A slower shutter speed may help."
            )

        if aperture and aperture >= 11:

            recs.append(
                f"Your aperture was f/{aperture:g}, which limits the amount of light entering the camera. A smaller F-Stop number may brighten the image."
            )

    # ----------------------------------
    # FOCAL LENGTH RULE
    # ----------------------------------

    if (
        blur["result"] != "Sharp"
        and focal
        and shutter_seconds
    ):

        recommended = 1 / focal

        if shutter_seconds > recommended:

            recs.append(
                f"You used a focal length of {int(focal)} mm. A common guideline is to use at least 1/{int(focal)} second when shooting handheld. Your shutter speed of {shutter} may be too slow."
            )

    # ----------------------------------
    # NOTHING FOUND
    # ----------------------------------

    if len(recs) == 0:

        recs.append(
            "No major technical issues were detected in this image."
        )

    return recs