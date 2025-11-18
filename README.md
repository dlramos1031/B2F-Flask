# Bottle2Filament - Local Website (Offline Version)

**No internet needed • Works on your laptop first • Later copy to Raspberry Pi**

This is the website for our capstone project.  
It runs completely offline — perfect for testing on your laptop before we move to the Pi.

### FOR PEOPLE WHO HATE READING (LIKE YOU)

JUST DOUBLE-CLICK → `RUN ME - Start Website.bat`  
→ Wait 5 seconds → Open browser → type `http://127.0.0.1:5000` → Done!

Still not working? Follow the steps below (with pictures in your mind).

### STEP-BY-STEP (Windows Only)

#### 1. You Must Have These (One-Time Only)
- Python installed → https://www.python.org/downloads/  
  → During install: **TICK "Add Python to PATH"** ← VERY IMPORTANT!
- This whole folder (bottle2filament) — don’t delete anything!

#### 2. How to Start the Website (Every Time)

**EASY WAY (RECOMMENDED):**
1. Open the folder `bottle2filament`
2. **Double-click this file →** `RUN ME - Start Website.bat`
3. A black window will open → wait until you see:
   
   ```
   * Running on http://0.0.0.0:5000
   ```

4. Open Chrome/Edge → type → `http://127.0.0.1:5000`
5. Enjoy!

**If the .bat file doesn’t work (some laptops block it):**

1. Press `Windows + R` → type `cmd` → Enter
2. Type these commands one by one (copy-paste):

```cmd
cd C:\bottle2filament
venv\Scripts\activate
python run.py
```

→ When you see the line with `http://127.0.0.1:5000` → open browser → go to that address.

### How to Stop
Just close the black window (or press Ctrl + C)

### Common Problems & Fixes

| Problem                            | Fix                                                                 |
|------------------------------------|----------------------------------------------------------------------|
| "python is not recognized"         | You forgot to tick "Add to PATH" → Reinstall Python and tick it!     |
| Black window closes immediately    | Double-click `RUN ME - Start Website.bat` instead of run.py directly |
| Website says "template not found"  | Don’t move or rename folders! Everything must stay as-is            |
| Port 5000 already in use           | Close other black windows or change port in run.py (ask the coder)   |

### For Future (When We Get the Raspberry Pi)
1. Copy this entire folder to USB
2. Paste on Pi → open terminal → run the same `RUN ME - Start Website.bat` (we’ll make a Pi version later)

### Credits
Made with love by Dave Lester Ramos
USTP Cagayan de Oro • 2025  
No internet? No problem!

**JUST DOUBLE-CLICK THE .BAT FILE. THAT’S IT.**
