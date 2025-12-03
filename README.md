# Abhishek Flask Portfolio API 🚀

This project demonstrates a **serverless Flask application** deployed on **AWS Lambda + API Gateway** using **Zappa**.

## 🔗 Live Demo
Public Endpoint:  
`https://9cf4adms0h.execute-api.ap-south-1.amazonaws.com/dev`

### Available Routes
- `/health` → Health check
- `/about` → About info
- `/projects` → Project showcase

## ⚙️ Tech Stack
- Python 3.12
- Flask
- Zappa
- AWS Lambda + API Gateway
- S3 for deployment package

## 📝 Deployment Commands
```bash
zappa deploy dev     # First deployment
zappa update dev     # Update after code changes
zappa undeploy dev   # Remove deployment
