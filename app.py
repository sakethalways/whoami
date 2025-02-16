from flask import Flask, render_template, request, redirect, url_for
import os
from model import predict_similar_actor
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    name = request.form['name']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Get prediction
            actor_name, actor_image = predict_similar_actor(filepath)
            
            # Debug print statements
            print(f"User image: {filename}")
            print(f"Actor name: {actor_name}")
            print(f"Actor image path: {actor_image}")
            
            return render_template('result.html', 
                                user_name=name,
                                user_image=filename,
                                actor_name=actor_name,
                                actor_image=actor_image)
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return redirect(request.url)
    
    return redirect(request.url)

if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)