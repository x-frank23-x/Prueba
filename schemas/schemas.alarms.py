from datetime import datetime 
from typing import Literal
from pydantic import BaseModel, ConfigDict

CriticalType = Literal["NORMAL","WARN","CRITICAL"]

class AlarmBase(BaseModel):
    id_alarm:int
    tec2g: int
    tec3g: int
    tec4g: int
    date_create:datetime
    muni:str
    depa:str
    noti:str
    
class AlarmResponse(AlarmBase):
    id:int
    timeHours:float
    timeText:str
    critical:CriticalType
    model_config = ConfigDict(from_attributes=True)
    
class ImportResponse(BaseModel):
    fileName:str
    totalProcessed:int
    items:list[AlarmResponse]
    
class HourlyCount(BaseModel):
    hour:str
    amount:int
    
class DailySummaryResponse(BaseModel):
    date:str
    totalDay:int
    perHour:list[HourlyCount]