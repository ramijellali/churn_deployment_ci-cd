.PHONY: all data_processing train evaluate deploy clean

# Define the Python interpreter (modify if needed)
PYTHON = python

# Default command to run all steps
all: data_processing train evaluate deploy

# Run data processing
data_processing:
	@echo "Running data processing..."
	@$(PYTHON) data_processing.py

# Train the model
train:
	@echo "Training the model..."
	@$(PYTHON) train_model.py

# Evaluate the model
evaluate:
	@echo "Evaluating the model..."
	@$(PYTHON) evaluate_model.py

# Deploy the model
deploy:
	@echo "Deploying the model..."
	@$(PYTHON) deploy_model.py

# Clean temporary files (optional)
clean:
	@echo "Cleaning temporary files..."
	rm -rf __pycache__
