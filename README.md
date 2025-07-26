# Flask Projects

This repository contains two Flask applications:

## Project 1: Flask API
A simple Flask API that serves JSON data from a backend file.

### Setup
1. Navigate to the project directory:
   ```bash
   cd project-1
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Access the API at: http://127.0.0.1:5000/api

## Project 2: Flask Form with MongoDB Atlas
A Flask application with a form that submits data to MongoDB Atlas.

### Prerequisites
- MongoDB Atlas account
- Database user with read/write permissions
- Network access configured (IP whitelist)

### Setup
1. Navigate to the project directory:
   ```bash
   cd project-2
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Copy `env_template.txt` to `.env`
   - Update the `.env` file with your MongoDB Atlas credentials:
     ```
     MONGO_URI=mongodb+srv://your_username:your_password@your_cluster_url/your_database?retryWrites=true&w=majority
     MONGO_DB=your_database_name
     MONGO_COLLECTION=your_collection_name
     ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the form at: http://127.0.0.1:5000

### Security Notes
- Never commit your `.env` file to version control
- The `.gitignore` file is configured to exclude sensitive files
- Use environment variables for all credentials

## Features
- **Project 1**: RESTful API serving JSON data
- **Project 2**: Web form with MongoDB integration, error handling, and success redirects

## Screenshots
Include screenshots of:
- Terminal running Flask applications
- Browser showing API responses
- Form submission and success pages
- Error handling (if applicable) 