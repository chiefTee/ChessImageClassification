# chessmanclassification

markdown
Copy code
# Chess Piece Classification Project

## Project Structure

chessman_classification/
├── data/
│ └── Chessman/
│ ├── Bishop/
│ ├── King/
│ ├── Knight/
│ ├── Pawn/
│ ├── Queen/
│ └── Rook/
├── notebooks/
│ └── best_model.keras
├── src/
│ ├── init.py
│ ├── api.py
│ ├── app.py
│ ├── data_preprocessing.py
│ ├── evaluate.py
│ ├── model.py
│ └── train.py
├── docker/
│ ├── Dockerfile.api
│ ├── Dockerfile.streamlit
│ └── docker-compose.yml
├── requirements.txt
├── README.md
└── report/
└── report.pdf

markdown
Copy code

## Objective

Develop a sophisticated image classification model that can identify different chess pieces using the Chessman Image Dataset. This project covers data preprocessing, model training, evaluation, deployment, and Docker containerization. The project includes a REST API and a Streamlit interface for user interaction.

## Prerequisites

Ensure you have the following installed on your machine:

- Docker
- Docker Compose
- Python 3.12
- Git

## Setup Instructions

### Step 1: Clone the Repository

Clone the project repository from GitHub:

```bash
git clone <repository_url>
cd chessman_classification
```
### Step 2: Prepare the Data

Place the Chessman Image Dataset in the data directory. The dataset should be organized into subdirectories for each chess piece (Bishop, King, Knight, Pawn, Queen, Rook).

Step 3: Build and Run Docker Containers
Navigate to the docker/ directory and run Docker Compose to build and start the containers:

bash
Copy code
cd docker
docker-compose up --build
This will create and start the following services:

chessman_api: Runs the FastAPI server.
chessman_streamlit: Runs the Streamlit interface.
Step 4: Access the Streamlit Interface
Once the containers are up and running, access the Streamlit interface by opening a web browser and navigating to:

arduino
Copy code
http://localhost:8501
Step 5: Using the Streamlit Interface
Upload an Image: Use the file uploader to select and upload an image of a chess piece.
Predict: Click the "Predict" button to get the classification result.
Step 6: REST API Endpoints
You can also interact with the model through the REST API. The API is accessible at:

arduino
Copy code
http://localhost:8000
API Endpoints
POST /predict: Predict the class of the uploaded chess piece image.

Example using curl:

bash
Copy code
curl -X POST "http://localhost:8000/predict" -F "file=@path_to_your_image.jpg"
Detailed Docker Configuration
Dockerfile.api
Dockerfile
Copy code
# Dockerfile.api

# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY ../requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY ../src/ ./src/
COPY ../data/ ./data/
COPY ../notebooks/best_model.keras ./notebooks/best_model.keras

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI server
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
Dockerfile.streamlit
Dockerfile
Copy code
# Dockerfile.streamlit

# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY src/ ./src/
COPY data/ ./data/

# Expose the port the app runs on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "src/app.py"]
docker-compose.yml
yaml
Copy code
version: '3.8'

services:
  chessman_api:
    build:
      context: ..
      dockerfile: docker/Dockerfile.api
    container_name: chessman_api
    ports:
      - "8000:8000"
    networks:
      - chessman_net

  chessman_streamlit:
    build:
      context: ..
      dockerfile: docker/Dockerfile.streamlit
    container_name: chessman_streamlit
    ports:
      - "8501:8501"
    networks:
      - chessman_net

networks:
  chessman_net:
    driver: bridge
Potential Issues and Troubleshooting
Docker Network Issues: If the containers cannot communicate, ensure they are on the same Docker network.
File Not Found Errors: Ensure all paths in the Dockerfiles are correct and files are properly copied into the containers.
Streamlit Interface Not Loading: Ensure the Streamlit container is running and accessible at the specified port.
Conclusion
This project involves building and deploying a machine learning model for chess piece classification using Docker. The REST API and Streamlit interface provide an accessible way to interact with the model. Follow the steps outlined above to set up and run the project successfully. For more details, refer to the report in the report/ directory and the code documentation.

