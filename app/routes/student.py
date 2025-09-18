from fastapi import APIRouter
from datetime import datetime
import zoneinfo

router = APIRouter()


@router.get("/student/{student_id}")
def get_student_info(student_id: int):
    timezone = zoneinfo.ZoneInfo("America/Mexico_City")
    current_time = datetime.now(tz=timezone)
    return {
        "student_id": student_id,
        "message": f"Student information for ID {student_id}",
        "timestamp": current_time.isoformat(),
    }
