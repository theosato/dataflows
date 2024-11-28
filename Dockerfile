# Base Airflow image
FROM apache/airflow:2.7.3

# Switch to root user for installations
USER root

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends vim \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy necessary files and folders into the container
COPY dags/ /opt/airflow/dags/
COPY plugins/ /opt/airflow/plugins/
COPY scripts/ /opt/airflow/scripts/
COPY data/ /opt/airflow/data/

# Set ownership to airflow user
RUN chown -R airflow: /opt/airflow/

# Switch back to airflow user
USER airflow

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
