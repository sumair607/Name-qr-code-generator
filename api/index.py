from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import qrcode
from PIL import Image
import io
import base64
import os
import logging

app = Flask(__name__, template_folder='../templates')
CORS(app, origins=['*'])

# Security configurations
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1MB limit
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate-qr', methods=['POST'])
def generate_qr():
    try:
        # Input validation
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
            
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON data'}), 400
            
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({'error': 'Please enter text or URL'}), 400
            
        # Security: Limit text length
        if len(text) > 2000:
            return jsonify({'error': 'Text too long (max 2000 characters)'}), 400
        
        # Generate QR code with proper error handling
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        
        # Create QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert to base64 with proper resource management
        img_buffer = io.BytesIO()
        try:
            img.save(img_buffer, format='PNG')
            img_buffer.seek(0)
            img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
            
            return jsonify({
                'success': True,
                'qr_code': f'data:image/png;base64,{img_base64}'
            })
        finally:
            img_buffer.close()  # Ensure resource cleanup
    
    except ValueError as e:
        app.logger.error(f'Validation error: {str(e)}')
        return jsonify({'error': 'Invalid input data'}), 400
    except Exception as e:
        app.logger.error(f'QR generation error: {str(e)}')
        return jsonify({'error': 'QR generation failed'}), 500

# Vercel serverless handler
def handler(request):
    return app(request.environ, lambda *args: None)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)