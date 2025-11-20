import pyautogui
import time
from datetime import datetime
import os
import tkinter as tk
from tkinter import messagebox
import pygetwindow as gw


screenshot_folder = os.path.join(os.path.expanduser("~"), "Pictures", "AutomatedS")
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)
    print(f"Created folder: {screenshot_folder}")

def ask_screenshot():
    """Show popup asking if user wants to take a screenshot"""
    root = tk.Tk()
    root.withdraw()  
    root.attributes('-topmost', True) 
    
    response = messagebox.askyesno(
        "Screenshot Timer", 
        "5 minutes have passed!\n\nDo you want to take a screenshot of your lab work?",
        icon='question'
    )
    
    root.destroy()
    return response

def take_screenshot():
    """Take and save screenshot of active window only with automatic naming"""
    try:
        # Get active window
        active_window = gw.getActiveWindow()
        
        if active_window:
            # Get window position and size
            x, y, width, height = active_window.left, active_window.top, active_window.width, active_window.height
            
            # Extract window title for naming
            window_title = active_window.title
            keywords = window_title.lower().replace('-', ' ').replace('|', ' ').split()
            stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'brave', 'chrome', 'firefox', 'safari', 'edge'}
            meaningful_words = [w for w in keywords if w not in stop_words and len(w) > 2][:3]
            
            name_part = "_".join(meaningful_words) if meaningful_words else "window"
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(screenshot_folder, f"{name_part}_{timestamp}.png")
            
            # Capture only the window region
            screenshot = pyautogui.screenshot(region=(x, y, width, height))
            screenshot.save(filename)
            
            # Show confirmation
            root = tk.Tk()
            root.withdraw()
            root.attributes('-topmost', True)
            messagebox.showinfo("Screenshot Saved", f"Screenshot saved to:\n{filename}")
            root.destroy()
            
            print(f"📸 Screenshot saved: {filename}")
        else:
            print("⚠️ No active window detected")
            
    except Exception as e:
        print(f"❌ Error taking screenshot: {e}")
        # Fallback to full screen screenshot
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(screenshot_folder, f"lab_{timestamp}.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(filename)
            print(f"📸 Fallback screenshot saved: {filename}")
        except Exception as fallback_error:
            print(f"❌ Fallback also failed: {fallback_error}")

def main():
    print("🚀 Screenshot automation started!")
    print(f"📁 Screenshots will be saved to: {screenshot_folder}")
    print("⏰ You'll be asked every 5 minutes if you want to take a screenshot.")
    print("🛑 Press Ctrl+C to stop.\n")
    
    interval = 5 * 60  # 5 minutes in seconds
    
    try:
        while True:
            next_time = datetime.now()
            next_time = next_time.replace(second=0, microsecond=0)
            next_time = next_time.replace(minute=next_time.minute + 5)
            
            print(f"⏳ Waiting 5 minutes... (Next prompt at {next_time.strftime('%H:%M:%S')})")
            time.sleep(interval)
            
            if ask_screenshot():
                take_screenshot()
            else:
                print("⏭️ Screenshot skipped.")
    
    except KeyboardInterrupt:
        print("\n\n✅ Screenshot automation stopped.")

if __name__ == "__main__":
    main()