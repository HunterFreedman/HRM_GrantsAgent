
from fastapi import FastAPI, Request
from pydantic import BaseModel
from export_manager import export_to_all
import datetime

app = FastAPI()

class GrantRequest(BaseModel):
    funding_agency: str
    proposal_focus: str
    target_audience: str
    budget_range: str

@app.post("/draft/proposal")
async def draft_proposal(req: GrantRequest):
    # Generate draft
    content = f"""Proposal for {req.funding_agency}
Focus: {req.proposal_focus}
Target Audience: {req.target_audience}
Requested Budget: {req.budget_range}

This proposal outlines the application of Harmonic Resonance Master’s AI-powered music therapy platform to address trauma in vulnerable populations. The approach integrates biometric feedback, neuroadaptive models, and therapeutic soundscapes to deliver scalable care for PTSD and emotional dysregulation.

Impact: High relevance to NIH/NIMH, DoD, SAMHSA, VA Hospital networks, and digital public health innovation funding pathways.
"""
    # Export content
    filename = f"HRM_GrantDraft_{req.funding_agency.replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.docx"
    export_to_all(filename=filename, content=content, tags=["grant", "proposal", req.funding_agency])
    return {"status": "Draft created and exported", "filename": filename}
