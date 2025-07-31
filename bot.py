import os
import subprocess
import sys
import platform

# Gói cần cài
REQUIREMENTS = [
    "telebot", "flask", "aiogram", "pyTelegramBotAPI", "python-telegram-bot",
    "pymongo", "aiohttp", "psutil", "motor", "pytz", "asyncssh",
    "pytesseract", "pillow"
]

def install_python_packages():
    print("📦 Đang cài đặt thư viện Python...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", *REQUIREMENTS])

def install_tesseract_linux():
    if platform.system().lower() == "linux":
        print("🔧 Đang cập nhật hệ thống và cài đặt tesseract-ocr...")
        subprocess.call(["sudo", "apt", "update"])
        subprocess.call(["sudo", "apt", "install", "tesseract-ocr", "-y"])
    else:
        print("⚠️ Tesseract chỉ tự động cài trên Linux. Hãy tự cài trên Windows hoặc macOS nếu cần.")

def run_cuong_py():
    if os.path.exists("cuong.py"):
        print("🚀 Đang chạy cuong.py...")
        subprocess.call([sys.executable, "cuong.py"])
    else:
        print("❌ Không tìm thấy file cuong.py")

def make_all_executable():
    print("🔓 Đang gán quyền chmod +x cho tất cả các file...")
    subprocess.call(["chmod", "+x", "*"])

if __name__ == "__main__":
    try:
        install_python_packages()
        install_tesseract_linux()
        make_all_executable()
        run_cuong_py()
    except Exception as e:
        print(f"❌ Có lỗi xảy ra: {e}")
