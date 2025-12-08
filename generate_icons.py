import os
from PIL import Image

def generate_icons(source_path, output_dir):
    try:
        img = Image.open(source_path)
        
        # Ensure output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save as PNG (Master)
        png_path = os.path.join(output_dir, "defendly-logo.png")
        img.save(png_path, "PNG")
        print(f"Generated: {png_path}")

        # Generate ICO
        # ICO usually contains multiple sizes: 16, 32, 48, 64, 128, 256
        icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        ico_path = os.path.join(output_dir, "Defendly.ico")
        img.save(ico_path, sizes=icon_sizes)
        print(f"Generated: {ico_path}")

        # Generate ICNS
        # Pillow might not support saving ICNS directly on all platforms/versions without extensions.
        # We will try, if it fails, we will skip it and warn.
        try:
            icns_path = os.path.join(output_dir, "Defendly.icns")
            # ICNS support in Pillow is read-only or limited. 
            # However, we can try saving it. If Pillow doesn't support it, it will raise an error.
            # Standard Pillow does NOT support writing ICNS. 
            # We will skip ICNS generation via Pillow and note it.
            # BUT, we can generate the PNGs needed for ICNS if we were using a tool like iconutil (macOS).
            # Since we are on Windows, we can't use iconutil.
            # We will try to save it, just in case this version has support, otherwise we print a warning.
            img.save(icns_path, format='ICNS', sizes=icon_sizes)
            print(f"Generated: {icns_path}")
        except Exception as e:
            print(f"Warning: Could not generate ICNS file directly. Pillow might not support writing ICNS. Error: {e}")
            # Fallback: We can't easily generate ICNS on Windows without specific libraries.
            # We will just proceed with ICO and PNG.

    except Exception as e:
        print(f"Error generating icons: {e}")

if __name__ == "__main__":
    source_image = r"C:/Users/DELL/.gemini/antigravity/brain/31d00912-3d3c-40ae-9dc1-a3468e05833c/uploaded_image_1764911598549.jpg"
    output_directory = r"c:\Users\DELL\Desktop\R_Zap\defendly-tool\zap\src\main\resources\resource"
    generate_icons(source_image, output_directory)
