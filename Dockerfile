FROM python:3.10

WORKDIR /automation

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    python -m playwright install-deps && \
    python -m playwright install

# Copy the automation code
COPY . .

