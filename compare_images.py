from PIL import Image, ImageChops

def compare_images(img1_path, img2_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    
    diff = ImageChops.difference(img1, img2)
    
    if diff.getbbox() is None:
        print("same")
        exit(0)
    else:
        print("different")
        exit(132)

if __name__ == "__main__":
    compare_images('./scripts/Untitled.png', 'Resources/graph_20240730_143149.png')