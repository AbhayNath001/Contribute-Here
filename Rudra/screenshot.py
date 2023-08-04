import pyautogui                #pip install PyAutoGUI

def take_screenshot():
    try:
        im = pyautogui.screenshot()
        print('Screenshot captured.')
        filename = input("Please enter a name for the screenshot (without extension): ")
        im.save(f"{filename}.png")
        print(f"Screenshot saved as '{filename}.png' successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

# Example usage:
take_screenshot()
