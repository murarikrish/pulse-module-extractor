# Pulse – Module Extraction AI Agent

This project automatically extracts **Modules, Sub-Modules, and Descriptions** from online product documentation or Help-Center websites.  
It crawls documentation pages, parses content, and produces a structured JSON hierarchy that can be used for knowledge organization, analytics, or navigation systems.

---

## 🚀 Features

- Crawls documentation websites safely
- Extracts:
  - Modules
  - Sub-modules
  - Descriptive summaries
- Two execution modes:
  - Streamlit Web UI
  - Command-Line Interface (CLI)
- Saves structured results to `output/result.json`
- Handles large / restricted documentation pages gracefully

---

## 🏗️ System Architecture

Input URLs
↓
Crawler → HTML Parser → Section Extractor
↓
Hierarchy Builder / Inference Logic
↓
JSON Output (Modules + Sub-modules + Descriptions)



**Core Components**

- `crawler.py` – Fetches documentation pages and parses sections  
- `pipeline.py` – Orchestrates the extraction workflow  
- `inference.py` – Builds hierarchical module structure  
- `app.py` – Streamlit user interface  
- `module_extractor.py` – CLI execution script  

---

## 🧩 Tech Stack

- Python  
- Requests  
- BeautifulSoup4  
- Streamlit  
- JSON Processing  

---

## 📦 Installation

### 1️⃣ Clone the Repository
git clone https://github.com/murarikrish/pulse-module-extractor
cd pulse-module-extractor

shell
Copy code

### 2️⃣ Create & Activate Virtual Environment
python -m venv venv
.\venv\Scripts\Activate

shell
Copy code

### 3️⃣ Install Dependencies
pip install -r requirements.txt


---

## 🖥️ Run Using Streamlit (Recommended)

streamlit run app.py

markdown
Copy code

Steps:

1. Enter one or more documentation URLs
2. Click **Extract Modules**
3. View JSON output in the UI
4. Result is saved automatically to:

output/result.json



---

## 🧑‍💻 Run Using CLI Mode

python module_extractor.py --urls https://help.zluri.com/



Output prints in terminal and also saves JSON to `output/result.json`.

---

## 🧾 Example Output

[
{
"module": "Help Center",
"Description": "Explore our Help Center...",
"Submodules": {
"Getting Started": "...",
"Application Management": "...",
"User Management": "..."
}
}
]



---

## 🎥 Demo Video

👉 **Project Demo:** [https://drive.google.com/file/d/1yvBOf2R8xFF0FSDEjKozUFTUhXsgkTja/view?usp=drivesdk]


---

## 📂 Repository Structure

pulse-module-extractor
│
├── app.py
├── module_extractor.py
├── requirements.txt
├── output/
│ └── result.json
│
└── module_extractor/
├── crawler.py
├── pipeline.py
├── inference.py
├── utils.py
└── init.py



---

## ⚠️ Limitations

- Works best on text-based documentation pages  
- Some websites may block automated crawling  
- Highly dynamic JavaScript pages may return limited content  

---

## 🚀 Future Enhancements

- Multi-page crawling with link traversal  
- ML-based description summarization  
- Language support for multilingual documentation  
- Export options (CSV / Excel formats)  

---

## 📝 Author

**Kesaboyina Murari Krishna**  
Project developed as part of the **Pulse AI Assignment**.
