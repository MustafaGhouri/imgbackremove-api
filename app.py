from flask import Flask, request, jsonify
from PIL import Image
import os

app = Flask(__name__)

def convert_image(input_path, output_path, output_format):
    try:
        image = Image.open(input_path)
        image.save(output_path, format=output_format)
        return True, None
    except Exception as e:
        return False, str(e)

@app.route('/convert', methods=['POST'])
def image_converter():
    input_image_format = request.form.get('input_format', 'JPEG')
    output_image_format = request.form.get('output_format', 'PNG')

    input_image_file = request.files['image']
    input_image_path = 'input_image_temp'
    input_image_file.save(input_image_path)

    output_image_path = 'output_image_temp.' + output_image_format.lower()
    success, error_message = convert_image(input_image_path, output_image_path, output_image_format)

    if success:
        return jsonify({"message": "Conversion successful.", "output_image_path": output_image_path}), 200
    else:
        return jsonify({"error": "Conversion failed.", "message": error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)
