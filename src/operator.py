import kopf
import kubernetes
from genai_analyzer import GenAIAnalyzer

analyzer = GenAIAnalyzer()

@kopf.on.create('pods')
async def scan_pod(spec, name, namespace, **kwargs):
    """
    Scan newly created pods using GenAI analysis
    """
    try:
        analysis = await analyzer.analyze_pod(spec)
        
        if has_critical_risks(analysis):
            return {
                'status': 'denied',
                'reason': format_risk_message(analysis)
            }
        
        store_analysis_results(name, namespace, analysis)
        
        return {'status': 'allowed'}
        
    except Exception as e:
        kopf.info(body, reason='Error', message=str(e))
        return {'status': 'error'}

def has_critical_risks(analysis):
    return any(
        risk['severity'] == 'Critical'
        for risk in analysis['risks']
    )

def format_risk_message(analysis):
    risks = analysis['risks']
    return "\n".join([
        f"- {risk['severity']}: {risk['description']}"
        for risk in risks
    ])