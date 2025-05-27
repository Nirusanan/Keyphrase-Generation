FROM python:3.11.12-bullseye

WORKDIR /app

# Copy requirements.txt first
COPY requirements.txt /app/

# Install needed packages and dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Now copy the rest of your application files
COPY main.py /app/

COPY /keywordsGeneration-model/config.json /app/keywordsGeneration-model/
COPY /keywordsGeneration-model/vocab.txt /app/keywordsGeneration-model/
COPY /keywordsGeneration-model/model.safetensors /app/keywordsGeneration-model/
COPY /keywordsGeneration-model/tokenizer.json /app/keywordsGeneration-model/
COPY /keywordsGeneration-model/tokenizer_config.json /app/keywordsGeneration-model/
COPY /keywordsGeneration-model/special_tokens_map.json /app/keywordsGeneration-model/

# Expose the port
EXPOSE 80

# Command to run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8007"]