from pydantic import BaseModel, Field, computed_field,field_validator
#for example mumbia input de rahe but we need in title cas elike Mumbia (phele capital)
#then we use feild validator (campus x V8)
from typing import Literal,Annotated

#pydantic model (To validate Incoming data)
class UserInput(BaseModel):
    src_bytes: Annotated[int, Field(..., ge=0, description="Bytes sent from source to destination", example=491)]
    dst_bytes: Annotated[int, Field(..., ge=0, description="Bytes sent from destination to source", example=0)]
    count: Annotated[int, Field(..., ge=0, description="Number of connections to same host in past 2 seconds", example=2)]
    srv_count: Annotated[int, Field(..., ge=0, description="Number of connections to same service in past 2 seconds", example=2)]
    num_failed_logins: Annotated[int, Field(..., ge=0, description="Number of failed login attempts", example=0)]
    num_compromised: Annotated[int, Field(..., ge=0, description="Number of compromised conditions", example=0)]
    serror_rate: Annotated[float, Field(..., ge=0, le=1, description="% of connections with SYN errors (0-1)", example=0.0)]
    rerror_rate: Annotated[float, Field(..., ge=0, le=1, description="% of connections with REJ errors (0-1)", example=0.0)]
    num_file_creations: Annotated[int, Field(..., ge=0, description="Number of file creation operations", example=0)]
    num_shells: Annotated[int, Field(..., ge=0, description="Number of shell prompts", example=0)]