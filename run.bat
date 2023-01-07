@echo off
setlocal
pip install -r requirements.txt
cls
if exist "%PROGRAMFILES(X86)%" ansicon64 python ShopeeFlashSale.py else ansicon python ShopeeFlashSale.py
pause
endlocal