# Cov-Backend

Backend for X-ray image classification using **Convolutional Neural Networks (CNN)**. This system allows detecting and classifying conditions such as **COVID-19**, **Normal**, and **Viral Pneumonia**, with image preprocessing and predictions performed via pre-trained models.

---

## 🚀 **Technologies Used**
- **Python 3.12**  
- **Flask** (Microframework for APIs)  
- **Torch/PyTorch** (Deep Learning Framework)  
- **Pillow** (Image Processing)  
- **OpenCV** (Image Filters)  
- **Flask-CORS** (Cross-Origin Resource Sharing Management)

---

## 🧩 **Project Structure**

The project is organized as follows:

```
cov-backend/
│
├── controllers/           # API endpoint controllers
│   ├── ImageController.py # Endpoint for image predictions
│   └── MetricsController.py # Endpoint for model metrics (to be implemented)
│
├── models/                # Pre-trained deep learning models
│   ├── model_raw.pt       # Trained model (raw)
│   ├── model_bilateral.pt # Trained model (bilateral filter)
│   └── model_canny.pt     # Trained model (Canny filter)
│
├── services/              # Business logic
│   ├── ModelService.py    # Service to load and predict using models
│   └── PreprocessingService.py # Service to apply image filters
│
├── utils/                 # Utilities
│   ├── ModelLoader.py     # Class to load PyTorch models
│   └── ModelDefinition.py # Model architecture definition
│
├── app.py                 # Main file to run the Flask server
└── requirements.txt       # List of dependencies
```

---

## 📌 **Main Endpoints**

### 1. **Process Image**
- **URL:** `/predict`  
- **Method:** `POST`  
- **Parameters:**
  - **image** (file): Image file in PNG/JPEG format.
  - **method** (string): Preprocessing method (**raw**, **bilateral**, **canny**).
  - **model** (string): Model to use (**raw**, **bilateral**, **canny**).

- **Sample Response:**
```json
{
  "prediction": "COVID-19",
  "processed_image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA..."
}
```

---

## 🛠️ **Setup and Execution**

### **Prerequisites**
- Python 3.12
- Install dependencies:
```bash
pip install -r requirements.txt
```

---

### **Run the Server**
```bash
python app.py
```
The server will be available at:  
`http://localhost:5000`

---

## 💪 **Testing with Postman**

### **Example POST Request**
1. **Endpoint:** `http://localhost:5000/predict`
2. **Parameters:**
   - **image**: Upload image file.
   - **method**: Select "raw", "bilateral", or "canny".
   - **model**: Select "raw", "bilateral", or "canny".

3. **Successful Response:**
```json
{
  "prediction": "NORMAL",
  "processed_image": "data:image/png;base64,...."
}
```

---

## 🛡️ **Security**
- **CORS** is enabled using **Flask-CORS** to allow API access from the frontend.

---

## 🌐 **Deployment**
For production, use **Gunicorn** or another compatible WSGI server:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 🔮 **Next Steps**
- Implement endpoint for model metrics (precision, recall, confusion matrix).
- Add visualization for **Silency Maps** to interpret model predictions.

---

## 📄 **License**
This project is licensed under the MIT License.

---

