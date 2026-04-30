"""Custom exceptions for mongo_agg_profiler."""

from __future__ import annotations


class MongoAggProfilerError(Exception):
    """Base exception for all MongoAggProfiler errors.

    Attributes:
        message: Human-readable error description.
        code: Optional machine-readable error code.
    """

    def __init__(self, message: str, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class ConfigurationError(MongoAggProfilerError):
    """Raised when the SDK is misconfigured."""


class ValidationError(MongoAggProfilerError):
    """Raised when input validation fails."""


class TimeoutError(MongoAggProfilerError):
    """Raised when an operation exceeds its time limit."""
