from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Get the segments from the user
def get_segments(file_name):
    # Read the image using the Image class from the PIL library
    img = Image.open(file_name)

    # Convert the image to a Numpy array
    img_array = np.array(img)

    # Divide the image into segments of size 50x50
    segment_size = 100
    segments = [img_array[i:i + segment_size, j:j + segment_size] for i in range(0, img_array.shape[0], segment_size) for j in range(0, img_array.shape[1], segment_size)]

    return segments

# Store the password
def set_password():
    # Get the file name of the image from the user
    file_name = input("Enter the file name of the image: ")

    # Get the segments from the image
    segments = get_segments(file_name)

    # Store the segments in a file on the disk
    with open("password.txt", "w") as f:
        for segment in segments:
            np.savetxt(f, segment, delimiter=",")
    print("Password set successfully")

# Verify the password
def verify_password():
    # Get the file name of the image from the user
    file_name = input("Enter the file name of the image: ")

    # Get the segments from the image
    segments = get_segments(file_name)

    # Load the password from the file
    with open("password.txt", "r") as f:
        password = [np.loadtxt(f, delimiter=",") for i in range(len(segments))]

    # Compare the segments with the password
    if segments == password:
        print("Authentication succeeded")
        return True
    else:
        print("Authentication failed")
        return False

# Main function
if __name__ == "__main__":
    # Get the action from the user
    action = input("Enter 'set' to set the password or 'verify' to verify the password: ")

    if action == 'set':
        set_password()
    elif action == 'verify':
        if verify_password():
            # Access granted
            pass
        else:
            # Access denied
            pass
    else:
        print("Invalid action")



# can you write a program in python for shortest path question 