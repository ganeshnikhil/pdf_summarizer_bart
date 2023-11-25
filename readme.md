<h1 align="center">Text-to-Speech Summarizer 📚🔊</h1>

<p align="center">
  <img src="https://img.shields.io/badge/language-python-blue.svg" alt="Language">
  <img src="https://img.shields.io/github/license/your-username/your-repository.svg" alt="License">
</p>

<p align="center">
  <strong>An intelligent Python script to extract text from PDF files, generate summaries using Hugging Face's BART model, and convert them into speech.</strong>
</p>

## Table of Contents
- [Prerequisites](#prerequisites)
- [Features](#features)
- [Usage](#usage)
- [Limitations](#limitations)
- [Contributors](#contributors)
- [License](#license)

## Prerequisites 🛠️

Before running the script, ensure you have the required Python libraries installed:

```bash
pip install pytorch transformers pyttsx3 PyPDF2 psutil playsound gTTS
```
OR 
```bash
pip install -r requirements.txt
```
## Features 🚀

- **PDF Text Extraction:** Extracts text from PDF files.
- **Intelligent Summarization:** Generates concise summaries using Hugging Face's BART model.
- **Text-to-Speech:** Converts the summary into speech using either `pyttsx3` or Google Text-to-Speech (gtts).

## Usage 📖

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd pdf_summarizer_bart
   ```

3. **Run the script with the path to the PDF file as an argument:**

   ```bash
   python main.py /path/to/your/file.pdf
   ```

## Limitations ⚠️

- **Input Text Limit:** The script may limit the number of input chunks to prevent excessive resource usage.
- **CPU Usage Monitoring:** The script monitors CPU usage; if it exceeds 95%, it terminates to prevent resource overload.

## Contributors 🤝

- [cythonboy](https://github.com/ganeshnikhil)
## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to further customize the README to better fit your project's style and add any additional information you find relevant.
