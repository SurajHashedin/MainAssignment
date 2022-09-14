from enum import Enum

class Issue_Type(str,Enum):
  BUG = 'BUG'
  TASK = 'TASK'
  STORY = 'STORY'
  EPIC = 'EPIC'

  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

class Status_Type(str,Enum):
  Open = 'Open'
  InProgress = 'InProgress'
  InReview = 'In Review'
  CodeComplete = 'Code Complete'
  Done = 'Done'
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]