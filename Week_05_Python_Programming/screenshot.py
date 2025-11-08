import pyautogui
import time
from datetime import datetime
import os
import tkinter as tk
from tkinter import messagebox

# Create the Pictures/AutomatedS folder if it doesn't exist
screenshot_folder = os.path.join(os.path.expanduser("~"), "Pictures", "AutomatedS")
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)
    print(f"Created folder: {screenshot_folder}")

def ask_screenshot():
    """Show popup asking if user wants to take a screenshot"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.attributes('-topmost', True)  # Keep on top
    
    response = messagebox.askyesno(
        "Screenshot Timer", 
        "15 minutes have passed!\n\nDo you want to take a screenshot of your lab work?",
        icon='question'
    )
    
    root.destroy()
    return response

def take_screenshot():
    """Take and save screenshot"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(screenshot_folder, f"lab_{timestamp}.png")
    
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    
    # Show confirmation
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    messagebox.showinfo("Screenshot Saved", f"Screenshot saved to:\n{filename}")
    root.destroy()
    
    print(f"📸 Screenshot saved: {filename}")

def main():
    print("Screenshot automation started!")
    print(f"Screenshots will be saved to: {screenshot_folder}")
    print("You'll be asked every 15 minutes if you want to take a screenshot.")
    print("Press Ctrl+C to stop.\n")
    
    interval = 15 * 60  
    
    try:
        while True:
            print(f"Waiting 15 minutes... (Next prompt at {datetime.now().strftime('%H:%M:%S')})")
            time.sleep(interval)
            
            
            if ask_screenshot():
                take_screenshot()
            else:
                print("Screenshot skipped.")
    
    except KeyboardInterrupt:
        print("\n\nScreenshot automation stopped.")

if __name__ == "__main__":
    main()