import enum 
from typing import Annotated
from livekit.agents import llm
import logging

logger = logging.getLogger("Temperature-Control")
logger.setLevel(logging.INFO)


class Zone(enum.Enum):
    LIVING_ROOM = "living_room"
    BEDROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"


class AssistantFunc(llm.FunctionContext):
    def __init__(self) -> None:
        super().__init__()


        self._temperature= {
            Zone.BATHROOM: 23,
            Zone.BEDROOM: 20,
            Zone.LIVING_ROOM:22,
            Zone.OFFICE:21,
            Zone.KITCHEN:24,
        }

    


        return f"the temperature in {zone} is now {temp}C"
