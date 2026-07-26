from typing import Any
from mcdreforged import *

def on_load(server: PluginServerInterface, _old: Any) -> None:
    server.loggger.info("Plugin loaded!")

def on_unload(server: PluginServerInterface) -> None:
    server.logger.info("Plugin unloaded!")
