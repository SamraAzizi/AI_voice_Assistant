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

    
    @llm.ai_callable(description="get the temperature in specific room!")

    def get_temperature(self, zone:Annotated[Zone, llm.TypeInfo(description="the specific info")]):
        logger.info("get-temp %s", zone)

        temp = self._temperature[Zone(zone)]

        return f"the temperature in the {zone} is {temp}C"
    

    @llm.ai_callable(description="set the temperature in specific room!")

    def set_temperature(self, zone:Annotated[Zone, llm.TypeInfo(description="the specific info")], temp:Annotated[int,llm.TypeInfo(description="the temperature to set")]):
        logger.info("set-temp-info %s and temp is %s", zone, temp)
        self._temperature[Zone(zone)] = temp

        return f"the temperature in {zone} is now {temp}C"
