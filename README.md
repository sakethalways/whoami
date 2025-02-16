# Who Am I?

A Flask web application that uses machine learning to find which Bollywood actor you look like!

## Features
- Upload your photo and get matched with a Bollywood actor
- Attractive web interface
- Real-time image processing and comparison
- Displays your photo alongside the matched actor's photo

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Place actor images in `static/actors/` directory, organized by actor name:
   ```
   static/actors/
   ├── Actor1/
   │   ├── image1.jpg
   │   ├── image2.jpg
   ├── Actor2/
   │   ├── image1.jpg
   │   ├── image2.jpg
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and visit `http://localhost:5000`

## Technologies Used
- Flask (Web Framework)
- TensorFlow (Machine Learning)
- MobileNetV2 (Feature Extraction)
- HTML/CSS (Frontend)
