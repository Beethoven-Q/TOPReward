"""Model clients package public API — lazy imports to avoid missing deps."""

from topreward.clients.base import BaseModelClient

def __getattr__(name):
    if name == "QwenClient":
        from topreward.clients.qwen import QwenClient
        return QwenClient
    elif name == "GeminiClient":
        from topreward.clients.gemini import GeminiClient
        return GeminiClient
    elif name == "GemmaClient":
        from topreward.clients.gemma import GemmaClient
        return GemmaClient
    elif name == "GLMClient":
        from topreward.clients.glm import GLMClient
        return GLMClient
    elif name == "KimiThinkingClient":
        from topreward.clients.kimi import KimiThinkingClient
        return KimiThinkingClient
    elif name == "Molmo2Client":
        from topreward.clients.molmo import Molmo2Client
        return Molmo2Client
    elif name == "OpenAIClient":
        from topreward.clients.openai import OpenAIClient
        return OpenAIClient
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    "BaseModelClient",
    "GLMClient",
    "GeminiClient",
    "GemmaClient",
    "KimiThinkingClient",
    "Molmo2Client",
    "OpenAIClient",
    "QwenClient",
]
