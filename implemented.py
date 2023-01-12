from const import DB
from dao.pattern import PatternDAO

from service.pattern import PatternService

#Создание связей между слоями service и dao
pattern_dao = PatternDAO(DB)
pattern_service = PatternService(pattern_dao)
