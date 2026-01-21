SCRIPT_INCLUDES = {
    "cover": {
        "serializer": "scripts.serializers.read.script.cover.CoverReadSerializer",
        "source": "scripts_Cover",
        "prefetch": "scripts_Cover",
        "many": True,
    },
    "status": {
        "serializer": "scripts.serializers.read.script.status.StatusReadSerializer",
        "source": "scripts_Status",
        "prefetch": "scripts_Status",
        "many": True,
    },
    "orderers": {
        "serializer": "scripts.serializers.read.script.orderer.ScriptOrdererReadSerializer",
        "source": "scripts_ScriptsOrderer",
        "prefetch": "scripts_ScriptsOrderer__orderer__institute",
        "many": True,
    },
    "process": {
        "serializer": "scripts.serializers.read.script.made.MadeReadSerializer",
        "source": "scripts_ScriptsProcess",
        "prefetch": "scripts_ScriptsProcess",
        "many": True,
    },
}
