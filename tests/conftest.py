"""Pytest configuration and fixtures for FastAPI tests."""

import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Provide a test client for the FastAPI application with fresh state."""
    # Reset activities to initial state before each test
    activities.clear()
    activities.update({
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Art Club": {
            "description": "Explore painting, drawing, and creative design",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 15,
            "participants": []
        },
        "Soccer Team": {
            "description": "Competitive soccer team practicing drills and playing matches",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 22,
            "participants": ["liam@mergington.edu"]
        },
        "Swimming Club": {
            "description": "Swim training and recreational laps at the school pool",
            "schedule": "Wednesdays, 5:00 PM - 6:30 PM",
            "max_participants": 18,
            "participants": ["mia@mergington.edu"]
        },
        "Drama Society": {
            "description": "Acting, stagecraft, and production of school plays",
            "schedule": "Mondays and Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 25,
            "participants": ["noah@mergington.edu"]
        },
        "Math Olympiad Club": {
            "description": "Advanced problem solving and competition preparation",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["sophia@mergington.edu"]
        },
        "Debate Team": {
            "description": "Public speaking and competitive debate practice",
            "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": ["ethan@mergington.edu"]
        }
    })
    return TestClient(app)


@pytest.fixture
def sample_email():
    """Provide a sample email for testing."""
    return "test.student@mergington.edu"


@pytest.fixture
def existing_activity():
    """Provide the name of an existing activity."""
    return "Chess Club"


@pytest.fixture
def non_existing_activity():
    """Provide the name of a non-existing activity."""
    return "Non-Existent Club"
