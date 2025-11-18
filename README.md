# Bottle2Filament Website Dashboard

This is the website for our capstone project. It runs completely offline.


### Too Long Didn't Read

JUST DOUBLE-CLICK → `Start Website.bat`  
→ Wait 5 seconds → Open browser → type `http://127.0.0.1:5000` → Done!

Still not working? Follow the steps below (with pictures in your mind).

### STEP-BY-STEP

#### 1. You Must Have These (Requirements)
- Python installed → https://www.python.org/downloads/  
  → During install: **TICK "Add Python to PATH"** ← VERY IMPORTANT!
- This whole folder (bottle2filament) — don’t delete anything!

#### 2. How to Start the Website (Every Time)

**EASY WAY (RECOMMENDED):**
1. Open the folder `bottle2filament`
2. **Double-click this file →** `Start Website.bat`
3. A black window (command line) will open → wait until you see:
   
   ```
   * Running on http://0.0.0.0:5000
   ```

4. Open Chrome/Edge → type → `http://127.0.0.1:5000`
5. Enjoy!

**If the .bat file doesn’t work (some computers block it):**

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
| Black window closes immediately    | Double-click `Start Website.bat` instead of run.py directly |
| Website says "template not found"  | Don’t move or rename folders! Everything must stay as-is            |
| Port 5000 already in use           | Close other black windows or change port in run.py (ask the coder)   |

### Credits
Made with love by Dave Lester Ramos  
USTP Cagayan de Oro • 2025  
No internet? No problem!

**JUST DOUBLE-CLICK THE .BAT FILE. THAT’S IT.**
