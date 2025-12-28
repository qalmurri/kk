from .common import (
    SizeCommandRepository,
    InstituteCommandRepository
)
from .cover import (
    CoverBookCommandRepository
)
from .description import (
    DescriptionCommandRepository,
    DescriptionPartCommandRepository,
    TextCommandRepository
)
from .flag import (
    FlagCommandRepository,
    PartCommandRepository
)
from .isbn import (
    TypeIsbnCommandRepository,
    IsbnCommandRepository,

)
from .note import (
    SectionNoteCommandRepository,
    TextNoteCommandRepository,
    NoteCommandRepository
)
from .orderer import (
    OrdererCommandRepository,
    ScriptsOrdererCommandRepository
)
from .scripts import (
    ScriptsCommandRepository
)
from .scriptsprocess import (
    SectionCommandRepository,
    ByCommandRepository,
    ScriptsProcessCommandRepository
)
from .status import (
    LabelCommandRepository,
    ScriptsStatusCodeCommandRepository,
    StatusCommandRepository
)