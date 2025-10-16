from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
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
        
        # Return success - frontend handles QR generation via API
        return jsonify({
            'success': True,
            'message': 'QR code ready for generation'
        })
    
    except Exception as e:
        app.logger.error(f'Error: {str(e)}')
        return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
