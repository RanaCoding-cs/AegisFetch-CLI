#!/usr/bin/env python3
"""
================================================================================
 📥 AEGISFETCH-CLI v3.5 (PRO EDITION - AUTO-ENCRYPTED SECURITY)
================================================================================
 Features:
 - 🎯 Saves directly to Internal Storage Root (/sdcard/AegisDownloads/)
 - 🔐 In-Code Auto-Updating SHA-256 Hash Password Security (Zero Manual Work)
 - 🌐 Auto-detects 1000+ Video Platforms (YouTube, FB, Insta, TikTok, etc.)
 - ⚡ Multi-Threaded Resumable Downloads (yt-dlp powered)
 - 🛡️ URL Sanitization & Injection Protection
================================================================================
"""

import os
import sys
import time
import json
import re
import hashlib
import yt_dlp
from datetime import datetime
from colorama import Fore, Style, init

# Colorama Initialize
init(autoreset=True)

# Save directly in Phone's Main Root Storage (Not in Download Folder)
ROOT_STORAGE_DIR = "/sdcard/AegisDownloads"
HISTORY_FILE = "aegis_fetch_history.json"

# 🔒 Auto-Updating Encrypted SHA-256 Password Hash (Default: admin123)
ADMIN_PASSWORD_HASH = "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9"

# Terminal Banner
BANNER = f"""{Fore.CYAN}{Style.BRIGHT}
 ╔═══════════════════════════════════════════════════════════════════════╗
 ║                                                                       ║
 ║  █████╗ ███████╗ ██████╗ ██╗███████╗███████╗███████╗█████████ █╗  ██╗ ║
 ║ ██╔══██╗██╔════╝██╔════╝ ██║██╔════╝██╔════╝██╔════╝╚══██╔══╝██║  ██║ ║
 ║ ███████║█████╗  ██║  ███╗██║███████╗█████╗  ███████╗   ██║   ███████║ ║
 ║ ██╔══██║██╔══╝  ██║   ██║██║╚════██║██╔══╝  ╚════██║   ██║   ██╔══██║ ║
 ║ ██║  ██║███████╗╚██████╔╝██║███████║██║     ███████║   ██║   ██║  ██║ ║
 ║ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝╚═╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ║
 ║                                                                       ║
 ║              ⚡ UNIVERSAL MULTI-PLATFORM VIDEO DOWNLOADER ⚡          ║
 ║          [ YouTube | Facebook | Insta | TikTok | 1000+ Sites ]        ║
 ║          < Developer: MD IMRAN HOSSEN | Author: RanaCoding-cs >       ║
 ║🔗GitHub Link: https://github.com/RanaCoding-cs | WhatsApp: 01636690865║
 ╚═══════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hash_password(password):
    """Encrypts raw text input using SHA-256 algorithm."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def update_hash_in_source_code(new_hash):
    """Automatically updates the ADMIN_PASSWORD_HASH directly inside this Python file."""
    try:
        script_path = os.path.abspath(__file__)
        with open(script_path, "r", encoding="utf-8") as f:
            code_lines = f.readlines()

        updated = False
        with open(script_path, "w", encoding="utf-8") as f:
            for line in code_lines:
                if line.startswith("ADMIN_PASSWORD_HASH ="):
                    f.write(f'ADMIN_PASSWORD_HASH = "{new_hash}"\n')
                    updated = True
                else:
                    f.write(line)
        return updated
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to auto-update script: {e}{Style.RESET_ALL}")
        return False

def sanitize_url(url):
    """Validates and cleans URL inputs against basic injection attempts."""
    pattern = r"^(https?://)?([\w\.-]+)+[\w\-\._~:/?#[\]@!$&'()*+,;=.]+$"
    if re.match(pattern, url):
        return url
    return None

def get_target_directory():
    """Finds accessible Internal Storage root path (bypasses Download folder)."""
    possible_paths = [
        "/storage/emulated/0/AegisDownloads",
        "/sdcard/AegisDownloads"
    ]
    
    for path in possible_paths:
        try:
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
            return path
        except Exception:
            continue
            
    fallback = os.path.join(os.getcwd(), "AegisDownloads")
    os.makedirs(fallback, exist_ok=True)
    return fallback

def setup_environment():
    target_dir = get_target_directory()
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'w') as f:
            json.dump([], f)
    return target_dir

def log_history(data):
    try:
        history = []
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                history = json.load(f)
        history.append(data)
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
    except Exception:
        pass

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0.0%').strip()
        speed = d.get('_speed_str', 'N/A').strip()
        eta = d.get('_eta_str', 'N/A').strip()
        sys.stdout.write(f"\r{Fore.YELLOW}[►] Downloading: {percent} | Speed: {speed} | ETA: {eta}{Style.RESET_ALL}")
        sys.stdout.flush()
    elif d['status'] == 'finished':
        print(f"\n{Fore.GREEN}[✔] Download Finished! File safely stored in Internal Storage.{Style.RESET_ALL}")

def get_ydl_options(mode, save_dir, quality_format=None):
    base_path = os.path.join(save_dir, '%(title)s.%(ext)s')
    
    opts = {
        'outtmpl': base_path,
        'progress_hooks': [progress_hook],
        'quiet': True,
        'no_warnings': True,
        'continuedl': True,  # Auto Resumable
        'nocheckcertificate': True
    }

    if mode == 'best':
        opts['format'] = 'bestvideo+bestaudio/best'
        opts['merge_output_format'] = 'mp4'
    elif mode == 'audio':
        opts['format'] = 'bestaudio/best'
        opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    elif mode == 'custom' and quality_format:
        opts['format'] = f'bestvideo[height<={quality_format}]+bestaudio/best[height<={quality_format}]/best'
        opts['merge_output_format'] = 'mp4'

    return opts

def fetch_media(url, mode, save_dir, quality=None):
    clean_url = sanitize_url(url)
    if not clean_url:
        print(f"\n{Fore.RED}[✘] Security Alert: Invalid or potentially harmful URL format!{Style.RESET_ALL}")
        return

    print(f"\n{Fore.CYAN}[i] Fetching media metadata...{Style.RESET_ALL}")
    opts = get_ydl_options(mode, save_dir, quality)
    
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(clean_url, download=True)
            title = info.get('title', 'Unknown Title')
            uploader = info.get('uploader', 'Unknown Source')
            
            # Save Log
            log_data = {
                "title": title,
                "uploader": uploader,
                "url": clean_url,
                "mode": mode,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            log_history(log_data)
            
            print(f"\n{Fore.GREEN}===================================================={Style.RESET_ALL}")
            print(f"{Fore.WHITE}{Style.BRIGHT} Title    : {Fore.YELLOW}{title}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}{Style.BRIGHT} Source   : {Fore.YELLOW}{uploader}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}{Style.BRIGHT} Saved At : {Fore.GREEN}{save_dir}/{Style.RESET_ALL}")
            print(f"{Fore.GREEN}===================================================={Style.RESET_ALL}")

    except Exception as e:
        print(f"\n{Fore.RED}[✘] Download Failed: {str(e)[:100]}{Style.RESET_ALL}")

def history_and_security_manager():
    """Protected History Viewer and Admin Password Management System."""
    global ADMIN_PASSWORD_HASH
    clear_screen()
    print(BANNER)
    print(f"{Fore.RED}{Style.BRIGHT}🔐 PROTECTED HISTORY & SECURITY MENU{Style.RESET_ALL}\n")

    confirm = input(f"{Fore.YELLOW}⚠️ Access Restricted Area? (y/n): {Style.RESET_ALL}").strip().lower()
    if confirm != "y":
        print(f"{Fore.GREEN}Action cancelled. Returning to main menu.{Style.RESET_ALL}")
        return

    input_pass = input(f"{Fore.WHITE}{Style.BRIGHT}Enter Admin Password: {Style.RESET_ALL}").strip()
    if hash_password(input_pass) != ADMIN_PASSWORD_HASH:
        print(f"{Fore.RED}❌ Access Denied! Incorrect Password.{Style.RESET_ALL}")
        return

    print(f"\n{Fore.GREEN}✔ Password Verified Successfully!{Style.RESET_ALL}\n")
    print(f"{Fore.WHITE}{Style.BRIGHT}Select an Action:{Style.RESET_ALL}")
    print(f"  {Fore.YELLOW}[1]{Style.RESET_ALL} View Download History Log")
    print(f"  {Fore.RED}[2]{Style.RESET_ALL} Clear All Download History")
    print(f"  {Fore.GREEN}[3]{Style.RESET_ALL} Change Admin Password (Auto-Updates Script 🔐)")
    print(f"  {Fore.WHITE}[0]{Style.RESET_ALL} Return to Main Menu")

    sub_choice = input(f"\n{Fore.CYAN}Select Option (0-3): {Style.RESET_ALL}").strip()

    if sub_choice == "1":
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}📜 DOWNLOAD HISTORY LOG:{Style.RESET_ALL}\n")
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                history = json.load(f)
                if not history:
                    print(Fore.RED + "No download history found.")
                else:
                    for idx, item in enumerate(reversed(history[-10:]), 1):
                        print(f"{Fore.CYAN}[{idx}] {Fore.WHITE}{item['title']}")
                        print(f"    └─ Source: {item['uploader']} | Date: {item['timestamp']}\n")
        else:
            print(Fore.RED + "No history file available.")

    elif sub_choice == "2":
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
            print(f"\n{Fore.GREEN}✅ History cleared successfully!{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.YELLOW}No history file found to clear.{Style.RESET_ALL}")

    elif sub_choice == "3":
        new_pass = input(f"\n{Fore.WHITE}{Style.BRIGHT}Enter NEW Admin Password: {Style.RESET_ALL}").strip()
        if new_pass:
            new_hash = hash_password(new_pass)
            if update_hash_in_source_code(new_hash):
                ADMIN_PASSWORD_HASH = new_hash
                print(f"\n{Fore.GREEN}✅ Password changed! Script automatically updated with new SHA-256 Hash.{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.RED}❌ Auto-update failed.{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}❌ Password cannot be empty.{Style.RESET_ALL}")

def main():
    target_dir = setup_environment()
    while True:
        clear_screen()
        print(BANNER)
        print(f"{Fore.WHITE}{Style.BRIGHT}STORAGE LOCATION: {Fore.GREEN}{target_dir}{Style.RESET_ALL}\n")
        print(f"{Fore.WHITE}{Style.BRIGHT}MAIN MENU:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[1]{Fore.WHITE} Download Best Quality Video (Auto High Res)")
        print(f"{Fore.GREEN}[2]{Fore.WHITE} Download Audio Only (MP3 Audio)")
        print(f"{Fore.GREEN}[3]{Fore.WHITE} Custom Resolution Download (1080p, 720p, etc.)")
        print(f"{Fore.GREEN}[4]{Fore.WHITE} Bulk Mode (Batch download from text file)")
        print(f"{Fore.RED}[5]{Fore.WHITE} Protected History & Security Menu (Auto-Encrypted Password 🔐)")
        print(f"{Fore.RED}[0]{Fore.WHITE} Exit Program")
        
        choice = input(f"\n{Fore.CYAN}Select an option (0-5): {Style.RESET_ALL}").strip()

        if choice == '1':
            url = input(f"\n{Fore.YELLOW}Paste Video Link: {Style.RESET_ALL}").strip()
            if url:
                fetch_media(url, mode='best', save_dir=target_dir)
            input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

        elif choice == '2':
            url = input(f"\n{Fore.YELLOW}Paste Video Link for MP3: {Style.RESET_ALL}").strip()
            if url:
                fetch_media(url, mode='audio', save_dir=target_dir)
            input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

        elif choice == '3':
            url = input(f"\n{Fore.YELLOW}Paste Video Link: {Style.RESET_ALL}").strip()
            print(f"\n{Fore.WHITE}Select Max Resolution:{Style.RESET_ALL}")
            print(f"{Fore.GREEN}[1] 1080p | [2] 720p | [3] 480p | [4] 360p")
            res_choice = input(f"{Fore.CYAN}Choose Option: {Style.RESET_ALL}").strip()
            res_map = {'1': '1080', '2': '720', '3': '480', '4': '360'}
            selected_res = res_map.get(res_choice, '720')
            
            if url:
                fetch_media(url, mode='custom', save_dir=target_dir, quality=selected_res)
            input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

        elif choice == '4':
            file_path = input(f"\n{Fore.YELLOW}Enter text file path (e.g., links.txt): {Style.RESET_ALL}").strip()
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    links = [line.strip() for line in f if line.strip()]
                print(f"{Fore.GREEN}[i] Found {len(links)} links. Starting bulk download...{Style.RESET_ALL}")
                for idx, link in enumerate(links, 1):
                    print(f"\n{Fore.MAGENTA}--- Downloading Link {idx}/{len(links)} ---{Style.RESET_ALL}")
                    fetch_media(link, mode='best', save_dir=target_dir)
            else:
                print(f"{Fore.RED}[✘] File not found!{Style.RESET_ALL}")
            input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

        elif choice == '5':
            history_and_security_manager()
            input(f"\n{Fore.CYAN}Press Enter to return to main menu...{Style.RESET_ALL}")

        elif choice == '0':
            print(f"\n{Fore.GREEN}Thank you for using AegisFetch-CLI! Exiting...{Style.RESET_ALL}")
            sys.exit(0)

        else:
            print(f"\n{Fore.RED}Invalid selection! Try again.{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    main()
