from fastapi import APIRouter

alarms = APIRouter()

@alarms.get("/api/alarms")
def getTodaySummary(): 