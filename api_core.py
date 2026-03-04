from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from scanner_engine import RapidScanner
from vuln_scanner import CyberSentinelExploiter
import uvicorn

app = FastAPI(title="Apex Sentinel AI Control Hub")

# তোমার নিজস্ব ফিঙ্গারপ্রিন্ট বা সিক্রেট কি (sayan9168 Exclusive)
API_KEY = "SAYAN_AI_9168_SECURE_ACCESS"
api_key_header = APIKeyHeader(name="X-AI-Fingerprint")

def verify_token(token: str = Depends(api_key_header)):
    if token != API_KEY:
        raise HTTPException(status_code=403, detail="AI Fingerprint Identity Mismatch")
    return token

class ScanRequest(BaseModel):
    target: str

@app.get("/")
def home():
    return {"status": "Sentinel Engine Online", "owner": "sayan9168"}

@app.post("/scan", dependencies=[Depends(verify_token)])
async def start_scan(request: ScanRequest):
    """
    মোবাইল অ্যাপ থেকে কল করলে এটি Masscan + Nmap স্ক্যান শুরু করবে।
    """
    scanner = RapidScanner(request.target)
    results = scanner.run_scan()
    return {"target": request.target, "vulnerabilities": results}

@app.post("/terminate", dependencies=[Depends(verify_token)])
async def terminate_service(request: ScanRequest):
    """
    চুক্তি বাতিল হলে সার্ভিস শাটডাউন করার সেই ফিচার।
    """
    exploiter = CyberSentinelExploiter()
    status = exploiter.kill_connection(request.target)
    return {"target": request.target, "action": "Service Severed", "log": status}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
  
