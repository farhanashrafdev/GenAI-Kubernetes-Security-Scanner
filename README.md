# GenAI-Powered Kubernetes Security Scanner

This repository contains a Kubernetes security scanner powered by Generative AI (GenAI) for detecting, analyzing, and remediating security risks in Kubernetes pods. The scanner uses AWS Bedrock's Large Language Models (LLMs) to analyze pod configurations and identify security issues in real-time.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Scanner](#running-the-scanner)
- [Example Usage](#example-usage)
- [Deployment](#deployment)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [License](#license)

## Features
- Real-time pod scanning
- Context-aware security analysis
- Human-readable risk summaries and remediation advice
- Integration with AWS Bedrock for AI-driven security analysis

## Prerequisites
Before running the scanner, ensure you have the following:
- A Kubernetes cluster
- Python 3.8+ installed
- AWS account with Bedrock access
- `kubectl` configured to interact with your Kubernetes cluster

## Installation

### Clone the Repository
```bash
git clone https://github.com/farhanashrafdev/k8s-genai-scanner
cd k8s-genai-scanner

### Set Up the Python Environment
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies
``` 
pip install -r requirements.txt
```

## Running GenAI Analyzer 

### Set Up AWS Credentials

Make sure your AWS credentials are set up to access Bedrock:

``` 
aws configure 
```

### You can test the GenAI analyzer independently with a pod specification:

```
from genai_analyzer import GenAIAnalyzer

analyzer = GenAIAnalyzer()

pod_spec = {
    # Example pod spec here
}

analysis = await analyzer.analyze_pod(pod_spec)
print(analysis)
```


