# QR Code Generator

A secure, fast, and privacy-focused QR code generator with colorful options.

## Features
- 🔒 **Secure**: No data storage, privacy-focused
- 🎨 **Colorful**: 8 color options available
- 📱 **Mobile-friendly**: Responsive design
- ⚡ **Fast**: Instant QR code generation
- 🆓 **Free**: No registration required

## Security Features
- Input validation and sanitization
- Resource leak prevention
- Secure error handling
- Production-ready configuration

## Deployment Options

### 1. Heroku (Recommended)
```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create app
heroku create your-qr-generator

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key-here
heroku config:set FLASK_ENV=production

# Deploy
git add .
git commit -m "Deploy QR Generator"
git push heroku main
```

### 2. Vercel (Serverless)
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

### 3. Netlify (Static + Functions)
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
netlify deploy --prod --dir .
```

### 4. Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export SECRET_KEY=dev-secret-key
export FLASK_ENV=development

# Run locally
python api/index.py
```

## Environment Variables
- `SECRET_KEY`: Flask secret key (required for production)
- `FLASK_ENV`: Set to 'production' for production deployment
- `PORT`: Port number (default: 5000)

## Security Considerations
- All packages updated to secure versions
- Input validation implemented
- Resource management optimized
- Debug mode disabled in production
- CORS properly configured

## License
© 2025 QR Generator. All rights reserved.