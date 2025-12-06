# app/domains/auth/state.py
from dataclasses import dataclass

from fastapi_opinionated.http.state import State

@dataclass
class AuthState(State):
    current_user: dict
    referer: str
