import exifread

image_path = r"C:\Users\Marlow\Downloads\lll\Coding\Photo Analyzer for beginning photgraphers\test photos\test_exposure.jpg"

with open(image_path, "rb") as f:

    tags = exifread.process_file(f)

    print("\n===== EXIF DATA =====\n")

    for tag in sorted(tags.keys()):
        print(f"{tag}: {tags[tag]}")