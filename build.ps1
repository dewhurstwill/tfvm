# Ensure C:\Users\YOUR_USER\AppData\Local\Programs\Python\Python39
# and
# C:\Users\YOUR_USER\AppData\Local\Programs\Python\Python39\Scripts are in PATH
 
pip install pyinstaller
pip install -r src/requirements.txt
pyinstaller --onefile src/tfvm.py
