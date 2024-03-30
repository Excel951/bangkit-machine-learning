import cv2
import argparse

def detect_blur_and_hd(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is HD
    height, width = image.shape[:2]
    if width == 1280 and height == 720 or width == 1920 and height == 1080:
        hd_text = "HD"
    else:
        hd_text = "Not HD"

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Laplacian filter for edge detection
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)

    # Calculate maximum intensity and variance
    _, max_val, _, _ = cv2.minMaxLoc(gray)
    binary_variance = gray.var()
    laplacian_variance = laplacian.var()

    # Initialize result variables
    blur_text = "Not Blurry"
    bright_spot_text = "No Bright Spot"

    # Check blur condition based on variance of Laplacian image
    if laplacian_variance < 100:
        blur_text = "Blurry"

    # Check bright spot condition based on variance of binary image
    if 5000 < binary_variance < 8500:
        bright_spot_text = "Bright Spot"

    # Add labels to the image
    cv2.putText(image, hd_text, (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.putText(image, blur_text, (15, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.putText(image, bright_spot_text, (15, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 3)

    # Display the image
    cv2.imshow("Image", image)
    cv2.waitKey(0)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", required=True, help="input image path")
    args = parser.parse_args()

    # Detect blur and bright spot
    detect_blur_and_hd(args.i)

if __name__ == "__main__":
    main()