import boto3
import json
from botocore.config import Config

class GenAIAnalyzer:
    def __init__(self):
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name='us-east-1'
        )
    
    async def analyze_pod(self, pod_spec):
        """
        Analyze Kubernetes pod security using Claude
        """
        prompt = self._create_security_prompt(pod_spec)
        
        response = self.bedrock.invoke_model(
            modelId='anthropic.claude-v2',
            body=json.dumps({
                "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
                "max_tokens": 1024,
                "temperature": 0.1
            })
        )
        
        return self._parse_analysis(response)
    
    def _create_security_prompt(self, pod_spec):
        return f"""
        As a Kubernetes security expert, analyze this pod specification for security risks:
        
        {json.dumps(pod_spec, indent=2)}
        
        Provide your analysis in the following format:
        1. List all security risks
        2. Rate each risk (Critical/High/Medium/Low)
        3. Explain the potential impact
        4. Suggest specific remediation steps
        """

    def _parse_analysis(self, response):
        analysis = json.loads(response['body'].read())['completion']
        return {
            'risks': self._extract_risks(analysis),
            'summary': self._generate_summary(analysis),
            'remediation': self._extract_remediation(analysis)
        }