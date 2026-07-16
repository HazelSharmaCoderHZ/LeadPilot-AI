from __future__ import annotations

import logging
import time
from abc import ABC, abstractmethod
from datetime import datetime,UTC

from app.schemas.state import LeadPilotState, WorkflowStatus

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """
    Base class for all LeadPilot AI agents.
    """

    def __init__(self):
        self.name = self.__class__.__name__

    def execute(self, state: LeadPilotState) -> LeadPilotState:
        """Public entry point for every agent."""

        self.validate_state(state)

        if state.execution.status is WorkflowStatus.FAILED:
            logger.warning(
                "[%s] Skipped because workflow has already failed",
                self.name,
            )
            return state

        state.execution.current_agent = self.name
        state.execution.status = WorkflowStatus.RUNNING

        start_time = time.perf_counter()

        logger.info("[%s] Started", self.name)

        try:
            self.before_execute(state)

            state = self.run(state)

            self.after_execute(state)

            elapsed = time.perf_counter() - start_time

            state.execution.status = WorkflowStatus.COMPLETED
            state.metadata.completed_at = datetime.now(UTC)

            # Optional: if you add execution_time to MetadataState
            # state.metadata.execution_time = elapsed

            logger.info(
                "[%s] Finished in %.2fs",
                self.name,
                elapsed,
            )

            return state

        except Exception as e:
            return self.handle_error(state, e)

    def validate_state(self, state: LeadPilotState):
        """Ensure every agent receives a LeadPilotState."""

        if not isinstance(state, LeadPilotState):
            raise TypeError(
                f"{self.name} expected LeadPilotState, got {type(state)}"
            )

    def before_execute(self, state: LeadPilotState):
        """Optional hook."""
        pass

    @abstractmethod
    def run(self, state: LeadPilotState) -> LeadPilotState:
        """Implement agent logic."""
        ...

    def after_execute(self, state: LeadPilotState):
        """Optional hook."""
        pass

    def handle_error(
        self,
        state: LeadPilotState,
        error: Exception,
    ) -> LeadPilotState:

        logger.exception("[%s] Failed: %s", self.name, error)

        state.execution.status = WorkflowStatus.FAILED
        state.execution.current_agent = self.name
        state.execution.errors.append(str(error))

        return state
