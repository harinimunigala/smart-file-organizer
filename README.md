# Smart File Organizer 🗂️

A **beginner-friendly Python tool** that automatically organizes your messy file folders into neat categories (Images, Documents, Videos, Audio, Code, etc.).

**Stop wasting time manually sorting files — let the bot do it!**

---

## ✨ Features

- ✅ **Automatically categorizes files** by type (Images, Documents, Videos, Audio, Archives, Code, etc.)
- ✅ **Creates folders on-the-fly** if they don't exist
- ✅ **Handles 50+ common file types** (.pdf, .jpg, .mp4, .py, .zip, etc.)
- ✅ **Works on Windows, Mac, and Linux**
- ✅ **Beginner-friendly** — No dependencies, pure Python
- ✅ **Safe & non-destructive** — Never deletes files, only moves them

---

## 🛠️ Built With

- **Python 3.6+** (No external libraries required!)

---

## 📦 Installation

### Option 1: Clone the Repository
```bash
git clone https://github.com/harinimunigala/smart-file-organizer.git
cd smart-file-organizer
```

### Option 2: Download ZIP
- Click **Code** → **Download ZIP** on GitHub
- Extract the folder

---

## 🚀 Quick Start

### Step 1: Prepare Your Test Folder
Create a test folder with some messy files:
```
test_folder/
├── photo.jpg
├── document.pdf
├── song.mp3
├── video.mp4
├── script.py
└── archive.zip
```

### Step 2: Run the Script
```bash
python main.py
```

### Step 3: Enter Folder Path
When prompted, enter the path to your test folder:
```
Enter the folder path to organize: /Users/yourname/Desktop/test_folder
```

### Step 4: ✨ Done!
Your folder is now organized:
```
test_folder/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── document.pdf
├── Audio/
│   └── song.mp3
├── Videos/
│   └── video.mp4
├── Code/
│   └── script.py
└── Archives/
    └── archive.zip
```

---

## 📋 File Categories Supported

| Category | File Types |
|----------|-----------|
| **Images** | .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp |
| **Documents** | .pdf, .doc, .docx, .txt, .xls, .xlsx, .ppt, .pptx |
| **Videos** | .mp4, .mkv, .avi, .mov, .flv, .wmv, .webm |
| **Audio** | .mp3, .wav, .flac, .aac, .m4a, .ogg, .wma |
| **Code** | .py, .js, .html, .css, .java, .cpp, .c, .rb, .go |
| **Archives** | .zip, .rar, .7z, .tar, .gz, .iso |
| **Other** | Everything else |

---

## 💻 How It Works (Technical)

The script:
1. Scans all files in the specified folder
2. Reads the file extension
3. Maps the extension to a category
4. Creates the category folder if it doesn't exist
5. Moves the file to the appropriate folder

**No files are deleted — only organized!**

---

## 🎯 Use Cases

✓ Clean up **Downloads folder**  
✓ Organize **project files**  
✓ Sort **shared drive folders**  
✓ Backup **media collections**  
✓ Automate **routine file management**

---

## 🚧 Future Improvements (Roadmap)

- [ ] 🎨 **GUI version** (Tkinter interface)
- [ ] 📊 **Logging system** (track what was moved)
- [ ] ⚙️ **Config file** (customize categories)
- [ ] 🔄 **Undo functionality** (reverse operations)
- [ ] 📦 **Pip package** (install via `pip install smart-file-organizer`)

---

## 📝 Example Usage

```bash
# Terminal example
$ python main.py
Enter the folder path to organize: /Users/john/Downloads
✅ 47 files organized successfully!
```

---

## ⚠️ Important Notes

- **Backup first** — Test on a small folder before using on important files
- **Admin rights** — You need write permission in the folder
- **Hidden files** — Are NOT organized (system protection)
- **Duplicates** — If a file exists in the target category folder, a number is appended (e.g., `photo(1).jpg`)

---

## 🤝 Contributing

Found a bug? Want to add a feature? **I'd love your help!**

1. Fork the repository
2. Create a branch (`git checkout -b feature/awesome-feature`)
3. Commit changes (`git commit -m 'Add awesome feature'`)
4. Push to branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the LICENSE file for details.

---

## 👤 Author

**Harini Munigala**  
*BTech IT Student | Python Developer | Open Source Enthusiast*

- 🌐 [GitHub](https://github.com/harinimunigala)
- 💼 [LinkedIn](https://linkedin.com/in/harinimunigala)


---

## 💬 Questions? Issues?

- 📮 Open an **Issue** on GitHub
- 💭 Start a **Discussion**
- 🐛 Found a bug? Report it [here](https://github.com/harinimunigala/smart-file-organizer/issues)

---

⭐ **If this helped you, please star the repository!** ⭐
