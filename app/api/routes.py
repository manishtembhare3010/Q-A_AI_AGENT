from fastapi import APIRouter, Request, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, Dict, Any
import logging

from app.retrieval.retriever import get_answer, reload_index

# Configure logging
logger = logging.getLogger(__name__)

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str
    
class QuestionResponse(BaseModel):
    question: str
    answer: str
    
class ReloadResponse(BaseModel):
    success: bool
    message: str
    document_count: int

@router.post("/ask", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest):
    """
    Ask a question to the knowledge retrieval system.
    
    Args:
        request: The question request containing the question text
        
    Returns:
        A response containing the question and the answer
    """
    try:
        logger.info(f"Received question: {request.question}")
        
        if not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
            
        answer = get_answer(request.question)
        logger.info(f"Generated answer for: {request.question}")
        
        return QuestionResponse(
            question=request.question,
            answer=answer
        )
        
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing question: {str(e)}")

@router.post("/reload", response_model=ReloadResponse)
async def reload_knowledge_base():
    """
    Reload the knowledge base to include new files.
    
    Returns:
        Status of the reload operation
    """
    try:
        logger.info("Reloading knowledge base...")
        result = reload_index()
        
        if not result["success"]:
            logger.error(f"Failed to reload knowledge base: {result['message']}")
            raise HTTPException(status_code=500, detail=result["message"])
        
        logger.info(f"Knowledge base reloaded: {result['message']}")
        return ReloadResponse(**result)
        
    except HTTPException:
        raise
    except Exception as e:
        err_msg = f"Error reloading knowledge base: {str(e)}"
        logger.error(err_msg)
        raise HTTPException(status_code=500, detail=err_msg)