from PIL import Image
import numpy as np
import os 
import zipfile

# Load the image from the specified filename
def loadImage(filename):
    return np.array(Image.open(filename))

# Save the image to the specified filename
def saveImage(image, filename):
    Image.fromarray(image).save(filename)

# Ask the user if they want to encrypt the entire image or a specific area
def desiredSize():
    wholeImage = input("Do you want to encrypt the entire image? (y/n): ").lower() == 'y'
    if not wholeImage:
        x1 = int(input("Enter the x1 coordinate: "))
        y1 = int(input("Enter the y1 coordinate: "))
        x2 = int(input("Enter the x2 coordinate: "))
        y2 = int(input("Enter the y2 coordinate: "))
        area = (x1, y1, x2, y2)
        return area
    else:
        return None

# Implement the Vernam cipher
def vernamCipher(image, key):
    return image ^ key

# Encrypt the image using the Vernam cipher
def encryptImage(image, output, key, area=None):
    if area is not None:
        x1, y1, x2, y2 = area
        encrypted_area = vernamCipher(image[y1:y2, x1:x2], key[:y2-y1, :x2-x1])
        image[y1:y2, x1:x2] = encrypted_area
    else:
        image = vernamCipher(image, key)
    saveImage(image, output)


# Decrypt the image using the Vernam cipher
def decryptImage(image, output, key, area=None):
    encryptImage(image, output, key, area)

# Generate a random key with the same shape as the image
def generateKeyShape(shape, area=None):
    if area is None:
        return np.random.randint(0, 256, shape, dtype=np.uint8)
    else:
        x1, y1, x2, y2 = area
        key_shape = list(shape)
        key_shape[0] = y2 - y1
        key_shape[1] = x2 - x1
        return np.random.randint(0, 256, key_shape, dtype=np.uint8)


path_color = "Color Images.zip"
path_gray = "Grayscale Images.zip"

output_path_encrypted = "output_encrypt"
output_path_decrypted = "output_decrypt"

if not os.path.exists(output_path_encrypted):
    os.makedirs(output_path_encrypted)

if not os.path.exists(output_path_decrypted):
    os.makedirs(output_path_decrypted)

def main():
    try:
        # Extract color images from ZIP
        with zipfile.ZipFile(path_color, 'r') as zip_ref:
            zip_ref.extractall("color_images")

        # Extract grayscale images from ZIP
        with zipfile.ZipFile(path_gray, 'r') as zip_ref:
            zip_ref.extractall("gray_images")

        # Load and process color images
        for filename in os.listdir("color_images"):
            if filename.endswith(".tif"):
                image_path = os.path.join("color_images", filename)
                image = loadImage(image_path)
                area = desiredSize()
                key = generateKeyShape(image.shape)
                encryptImage(image, os.path.join(output_path_encrypted, f"{filename}_encrypted.tif"), key, area)
                decryptImage(loadImage(os.path.join(output_path_encrypted, f"{filename}_encrypted.tif")), os.path.join(output_path_decrypted, f"{filename}_decrypted.tif"), key, area)

        # Load and process grayscale images
        for filename in os.listdir("gray_images"):
            if filename.endswith((".gif", ".bmp", ".jpeg", ".png")):
                image_path = os.path.join("gray_images", filename)
                image = loadImage(image_path)
                area = desiredSize()
                key = generateKeyShape(image.shape)
                print(f"Encrypting {filename}...")
                encryptImage(image, os.path.join(output_path_encrypted, f"{filename}_encrypted.png"), key, area)
                decryptImage(loadImage(os.path.join(output_path_encrypted, f"{filename}_encrypted.png")), os.path.join(output_path_decrypted, f"{filename}_decrypted.png"), key, area)

    except Exception as e:
        print("An error occurred:", e)
            

if __name__ == "__main__":
    main()
