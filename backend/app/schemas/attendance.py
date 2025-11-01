from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AttendanceBase(BaseModel):
    """Base attendance schema"""
    session_id: int
    child_id: int
    present: bool
    notes: Optional[str] = None


class AttendanceCreate(AttendanceBase):
    """Schema for creating attendance record"""
    coach_id: int


class AttendanceUpdate(BaseModel):
    """Schema for updating attendance"""
    present: Optional[bool] = None
    notes: Optional[str] = None


class Attendance(AttendanceBase):
    """Schema for reading attendance"""
    id: int
    coach_id: int
    marked_at: datetime

    class Config:
        from_attributes = True


class AttendanceBulkCreate(BaseModel):
    """Schema for bulk creating attendance records"""
    session_id: int
    coach_id: int
    attendance_records: list[dict]  # [{child_id: int, present: bool, notes: str}]
