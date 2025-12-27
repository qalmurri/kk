from .user import UserReadSerializer
from .activity import ActivityReadSerializer
from .common import (
    SizeReadSerializer,
    InstituteReadSerializer,
)
from .cover import CoverReadSerializer
from .description import (
    TextDescriptionReadSerializer, 
    SectionDescriptionReadSerializer,
    DescriptionReadSerializer
)
from .flag import (
    PartReadSerializer,
    FlagReadSerializer
)
from .isbn import (
    TypeIsbnReadSerializer,
    IsbnReadSerializer
)
from .note import (
    TextNoteReadSerializer,
    SectionNoteReadSerializer,
    NoteReadSerializer
)
from .orderer import (
    OrdererReadSerializer,
    ScriptOrdererReadSerializer
)
from .scripts import ScriptsReadSerializer
from .scriptsprocess import (
    SectionReadSerializer,
    ByReadSerializer,
    ScriptProcessReadSerializer
)
from .status import (
    LabelStatusReadSerializer,
    SectionStatusReadSerializer,
    StatusReadSerializer
)