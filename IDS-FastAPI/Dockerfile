FROM python:3.11-slim

# Set working directory
WORKDIR /app


#saare requirements ko app directory mai install kiya 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#sab remaining files app , predict etc etc sab ko directory mai copy kiya 
COPY . .

# Expose the application port
EXPOSE 8000

# Command to start FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
#ye 0.0.0.0 ka matlab kisse pe ip adress pe request aayegi toh wo accept krni hai