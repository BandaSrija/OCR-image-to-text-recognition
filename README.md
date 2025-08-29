# 📝 OCR Image to Text Recognition

This project is a **Python-based OCR (Optical Character Recognition) application** that converts text from images into editable digital text using **Tesseract OCR** and **Tkinter** for a simple GUI.

---

## ✨ Features
- 📷 Upload an image and extract text instantly  
- 🔍 Uses **Tesseract OCR** for high-quality recognition  
- 🖼️ Supports common image formats (`.jpg`, `.png`, `.jpeg`)  
- 💻 Simple and lightweight **Tkinter GUI**  
- 📄 Save extracted text into a `.txt` file  

---

## 📂 Project Structure
OCR-image-to-text-recognition/
│── ocrrr.py # Main Python script (GUI + OCR logic)
│── requirements.txt # Python dependencies
│── README.md # Project documentation


---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/BandaSrija/OCR-image-to-text-recognition.git
cd OCR-image-to-text-recognition
```

### 2. Create Virtual Environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Tesseract OCR

Windows: Download here and install.

Linux (Ubuntu/Debian): sudo apt-get install tesseract-ocr

Mac (Homebrew): brew install tesseract


⚠️ Don’t forget to add Tesseract to your PATH or configure it in ocrrr.py:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

### ▶️ Usage

Run the app:
```bash
python ocrrr.py
```

### Steps:

Click Upload Image to choose a file

The extracted text will appear in the text box

Optionally, save the text into a file

### 📌 Example

Input image:

Extracted text:

This is an OCR text extraction example.

### 🛠️ Tech Stack

Python 3.x

Tkinter (GUI)

Pillow (Image processing)

Pytesseract (OCR wrapper)

Tesseract OCR Engine

### 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.


### 👩‍💻 Author: Srija B


---

Would you like me to also create a **`requirements.txt`** file for your repo (with the exact Python dependencies like `pytesseract`, `Pillow`, `tkinter`)? That way, others can install everything in one go.

---