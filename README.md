
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

### Step 2: Install Dependencies
Install the required Python packages using the requirements.txt file:
``` bash
pip install -r requirements.txt
```

### Step 3: Download Model weight 

 I use VGG16 as the base model, download the model weight and store in the model directory. link to the model https://huggingface.co/matthias-wright/vgg/blob/main/vgg16_weights.h5


### Step 3: Train the Model
 The model can be train in two ways
1.Using the /notebooks/Chessman_Classification.ipynb notebook ; make sure to load the path to the VGG16 weights before running the notebook.\n
2.Running the Src/ (data_processing.py,model.py,train.py,evaluate.py) script to start the pipelines in that  order which is more structed and production friendly 




Proof of concept link : https://drive.google.com/file/d/1IqXkpU8tcyTwnbRIPdjbxqe6TpGUcb91/view?usp=sharing