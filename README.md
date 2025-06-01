# pdf_extractor
PDF information extractor prototype




## installation

Ubuntu/Debian
```bash
apt update && apt install -y poppler-utils tesseract-ocr

```


Alpine Linux
```bash
apk add poppler-utils
```
## Documentation 


### Official Documentation & Resources

#### Core Libraries

| Tool              | Purpose                                               | Docs                                                                                       |
| ----------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **pytesseract**   | Python wrapper for Tesseract OCR                      | [https://pypi.org/project/pytesseract/](https://pypi.org/project/pytesseract/)             |
| **Tesseract OCR** | Core OCR engine (C++ binary)                          | [https://tesseract-ocr.github.io/](https://tesseract-ocr.github.io/)                       |
| **pdf2image**     | Convert PDF pages to images                           | [https://pdf2image.readthedocs.io/en/latest/](https://pdf2image.readthedocs.io/en/latest/) |
| **Poppler**       | PDF rendering backend for `pdf2image`                 | [https://poppler.freedesktop.org/](https://poppler.freedesktop.org/)                       |
| **fpdf2**         | Generate PDFs with modern Unicode support             | [https://pyfpdf.github.io/fpdf2/](https://pyfpdf.github.io/fpdf2/)                         |
| **pdfplumber**    | (Optional) extract structured text directly from PDFs | [https://github.com/jsvine/pdfplumber](https://github.com/jsvine/pdfplumber)               |

---

## What to Learn

Here’s a breakdown of relevant knowledge to move from prototype to production:

---

#### 1. **Image Preprocessing for Better OCR**

* **Why**: OCR results improve dramatically with clean, high-contrast images.
* **Topics**:

  * Convert to grayscale
  * Resize / DPI tuning (300 DPI recommended)
  * Binarization (thresholding)
  * Denoising
* **Tools**: `Pillow`, `OpenCV`
* Guide: [Improving OCR accuracy with image preprocessing](https://nanonets.com/blog/ocr-with-tesseract/#improving-the-ocr-accuracy-using-preprocessing)

---

#### 2. **Tesseract Tuning & Configuration**

* **Why**: Tesseract has config options like page segmentation modes, OCR engine modes, and custom whitelist/blacklist characters.
* Official guide: [https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html)
* Topics to explore:

  * `--psm` (page segmentation mode)
  * `--oem` (OCR engine mode)
  * Language packs and dictionaries
  * Custom training (if ever needed)

---

#### 3. **Error Handling & Logging**

* Add:

  * Try/except blocks
  * Logging (using `logging` module, not `print`)
  * Fallback mechanisms
* Python Logging Basics: [https://docs.python.org/3/library/logging.html](https://docs.python.org/3/library/logging.html)

---

#### 4. **Packaging as a CLI Tool or Module**

* Use `argparse` for CLI
* Structure code for reusability: `src/pdf_extractor/`
* Use `setup.cfg` / `pyproject.toml`
* RealPython guide: [Python Application Layouts](https://realpython.com/python-application-layouts/)

---

#### 5. **Testing**

* Unit tests for:

  * OCR output parsing (with mock OCR input)
  * Regex robustness
* Tools: `pytest`
* Guide: [https://docs.pytest.org/en/latest/](https://docs.pytest.org/en/latest/)


