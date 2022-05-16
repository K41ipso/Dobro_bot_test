@echo off

call %~dp0dobr\venv\Scripts\activate

cd %~dp0dobr

set TOKEN=5396831775:AAFP5MU48mlc_HrX3C546bJ6i_LrE4GdNso

python dobr_bot.py

pause