from flask import Flask, request, jsonify
from rembg import remove
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/remove_background', methods=['POST'])
def remove_background():
    try:
        # Get the image from the request
        image = request.files['image']
        
        # Process the image using rembg
        image = remove(image.read())
        
        # Return the processed image
        response = app.response_class(response=image, content_type='image/png')
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
