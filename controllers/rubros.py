import json
import logging

from dotenv import load_dotenv
from fastapi import HTTPException, Depends
from utils.database import fetch_query_as_json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def fetch_rubros():
    query = f"select * from webapp.rubros order by id desc"

    try:
        logger.info(f"QUERY LIST")
        result_json = await fetch_query_as_json(query)
        result_dict = json.loads(result_json)
        return result_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))