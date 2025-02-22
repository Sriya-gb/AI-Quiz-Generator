
# **AI-Powered Quiz Generator**  

## **Project Overview**  
The AI-Powered Quiz Generator is a tool that automatically generates multiple-choice questions (MCQs) from any given text using Natural Language Processing (NLP) and AI models. It extracts key information from the input text and formulates structured MCQs with:  
- One correct answer  
- Three incorrect but plausible distractors  

This project is designed for educators, students.  

---

## **Features**  
- Automatic MCQ generation from any text input  
- AI-powered distractor selection to ensure meaningful incorrect answers  
- Simple UI using Streamlit for easy interaction  
- FastAPI backend for handling model inference   

---

## **Technology Stack**  

### **Libraries & Models**  
- Hugging Face Transformers – Pretrained models for text generation  
- PyTorch/TensorFlow – Model fine-tuning and inference  

### **Frameworks**  
- Streamlit – UI for quiz generation  
- FastAPI – Backend for AI model inference  
- Hugging Face Spaces

---

## **Setup & Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/YOUR_USERNAME/AI-Quiz-Generator.git
cd AI-Quiz-Generator
```

### **2. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3. Run the FastAPI Backend**  
```bash
uvicorn api.endpoints:app --host 0.0.0.0 --port 8000 --reload
```

### **4. Run the Streamlit UI**  
```bash
streamlit run app/main.py

``

