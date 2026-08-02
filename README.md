# 📥 AegisFetch-CLI v3.5 (Pro Edition)

**AegisFetch-CLI** হলো টার্মিনাল (Termux/Linux/Windows)-ভিত্তিক একটি অ্যাডভান্সড, মাল্টি-প্ল্যাটফর্ম মিডিয়া ডাউনলোডার ও সিকিউরিটি টুল। Python ও `yt-dlp` লাইব্রেরির ওপর ভিত্তি করে তৈরি এই টুলের মাধ্যমে YouTube, Facebook, Instagram, TikTok সহ ১,০০০+ ওয়েবসাইট থেকে ভিডিও বা অডিও সরাসরি স্মার্টফোনের রুট ইন্টারনাল স্টোরেজে ডাউনলোড করা যায়। 

এতে রয়েছে **In-Code Auto-Updating SHA-256 Security** সিস্টেম, যা কোনো এক্সটার্নাল ফাইল ছাড়াই অ্যাডমিন পাসওয়ার্ড স্বয়ংক্রিয়ভাবে এনক্রিপ্ট করে কোডের ভেতরে আপডেট করে নেয়।

---

## ✨ মেইন ফিচারসমূহ (Key Features)

- **🎨 Terminal Box Art UI:** আকর্ষণীয় ব্যানার ও কালারফুল সিএলআই ইন্টারফেস।
- **📂 Root Internal Storage Save:** ফাইল ডাউনলোড হয়ে সরাসরি ফোনের মূল মেমোরিতে (`/sdcard/AegisDownloads/`) জমা হয়।
- **🔐 Protected Security & History Menu:** পাসওয়ার্ড দ্বারা সুরক্ষিত সিকিউরিটি ও ডিলিট অপশন।
- **⚡ In-Code Auto-Updating SHA-256 Hash:** পাসওয়ার্ড চেঞ্জ করলে কোড নিজে থেকেই হ্যাশ আপডেট করে নেয়।
- **🛡️ URL Sanitization & Injection Protection:** ক্ষতিকারক লিঙ্ক ও কমান্ড ইনজেকশন প্রতিরোধ ব্যবস্থা।
- **⏸️ Resumable Downloads:** ইন্টারনেট কেটে গেলে পরবর্তীতে আবার সেখান থেকেই ডাউনলোড শুরু করার সুবিধা।

---

## 🎛️ ডাউনলোডিং মোডসমূহ (Modes)

1. **🎬 Best Quality Mode:** সর্বোচ্চ রেজুলেশনে (Auto Best Video + Best Audio) MP4 ভিডিও ডাউনলোড।
2. **🎵 Audio Extraction Mode:** ভিডিও থেকে শুধুমাত্র হাই-কোয়ালিটি MP3 অডিও আলাদা করে সেভ করা।
3. **⚙️ Custom Quality Mode:** পছন্দমতো রেজুলেশন (1080p, 720p, 480p, 360p) সিলেক্ট করার সুবিধা।
4. **📋 Bulk / Batch Mode:** `links.txt` ফাইল থেকে একসংগে একাধিক লিঙ্ক অটোমেটিক ডাউনলোড।

---

## 📁 প্রজেক্ট ফাইল স্ট্রাকচার (File Structure)

```text
aegisfetch-cli/
├── aegisfetch.py              # প্রধান পাইথন সোর্স কোড (Main Application)
├── aegis_fetch_history.json   # ডাউনলোড হিস্ট্রি লগার (Auto-generated)
├── requirements.txt
├── links.txt                  # বাল্ক ডাউনলোডের জন্য ইউআরএল লিস্ট (Optional)
└── README.md                  # প্রজেক্টের অফিসিয়াল ডকুমেন্টেশন

📦 প্রয়োজনীয় প্যাকেজ ও ইনস্টলেশন (Package Management)
​প্রোগ্রামটি রান করার আগে সিস্টেমে Python, FFmpeg এবং প্রয়োজনীয় লাইব্রেরি ইনস্টল থাকতে হবে।
​টার্মাক্স (Termux)-এর জন্য:
# সিস্টেম আপডেট ও প্রয়োজনীয় প্যাকেজ ইনস্টল
pkg update && pkg upgrade -y
pkg install python ffmpeg -y

# পাইথন প্যাকেজ ইনস্টল
pip install yt-dlp colorama

🚀 ব্যবহার করার নিয়ম (How to Use)
​১. স্টোরেজ পারমিশন দিন (প্রথমবার ব্যবহারের জন্য):
termux-setup-storage

২. প্রোগ্রামটি রান করুন:
python aegis-fetch3.5.py

৩. মেনু ব্যবহার নিয়ম:
​মেনু থেকে পছন্দমতো মোড (1-4) সিলেক্ট করুন।
​সামাজিক যোগাযোগ মাধ্যম বা ভিডিও প্ল্যাটফর্ম থেকে যেকোনো লিঙ্ক কপি করে পেস্ট করুন।
​সিকিউরিটি ও হিস্ট্রি মেনুতে ঢুকতে 5 চাপুন (ডিফল্ট এডমিন পাসওয়ার্ড: admin123)।

​👨‍💻 ডেভলপার তথ্য (Developer Info)
​Developer: MD IMRAN HOSSEN (Rana)
​GitHub: RanaCoding-cs
​WhatsApp: +8801636690865
