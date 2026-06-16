"""Tests for signup endpoints."""

import pytest


class TestSignupForActivity:
    """Tests for the POST /activities/{activity_name}/signup endpoint."""

    def test_signup_returns_200_for_valid_activity(self, client, existing_activity, sample_email):
        """Test that signup returns status code 200 for valid activity."""
        response = client.post(
            f"/activities/{existing_activity}/signup",
            params={"email": sample_email}
        )
        assert response.status_code == 200

    def test_signup_returns_success_message(self, client, existing_activity, sample_email):
        """Test that signup returns a success message."""
        response = client.post(
            f"/activities/{existing_activity}/signup",
            params={"email": sample_email}
        )
        assert response.status_code == 200
        assert "message" in response.json()
        assert sample_email in response.json()["message"]
        assert existing_activity in response.json()["message"]

    def test_signup_for_non_existing_activity_returns_404(self, client, non_existing_activity, sample_email):
        """Test that signup for non-existing activity returns 404."""
        response = client.post(
            f"/activities/{non_existing_activity}/signup",
            params={"email": sample_email}
        )
        assert response.status_code == 404
        assert "detail" in response.json()

    def test_signup_duplicate_returns_400(self, client, existing_activity):
        """Test that signing up the same student twice returns 400."""
        # Get existing participant from the activity
        response = client.get("/activities")
        activities = response.json()
        existing_participant = activities[existing_activity]["participants"][0]
        
        # Try to sign up again
        response = client.post(
            f"/activities/{existing_activity}/signup",
            params={"email": existing_participant}
        )
        assert response.status_code == 400
        assert "detail" in response.json()
        assert "already signed up" in response.json()["detail"]

    def test_signup_adds_participant_to_activity(self, client, existing_activity):
        """Test that signup actually adds participant to activity."""
        new_email = "newstudent@mergington.edu"
        
        # Get current participant count
        response = client.get("/activities")
        activities_before = response.json()
        count_before = len(activities_before[existing_activity]["participants"])
        
        # Signup new participant
        client.post(
            f"/activities/{existing_activity}/signup",
            params={"email": new_email}
        )
        
        # Check if participant was added
        response = client.get("/activities")
        activities_after = response.json()
        count_after = len(activities_after[existing_activity]["participants"])
        assert count_after == count_before + 1
        assert new_email in activities_after[existing_activity]["participants"]

    def test_signup_multiple_students_different_activities(self, client):
        """Test that multiple students can signup for different activities."""
        email1 = "student1@mergington.edu"
        email2 = "student2@mergington.edu"
        activity1 = "Chess Club"
        activity2 = "Soccer Team"
        
        response1 = client.post(
            f"/activities/{activity1}/signup",
            params={"email": email1}
        )
        response2 = client.post(
            f"/activities/{activity2}/signup",
            params={"email": email2}
        )
        
        assert response1.status_code == 200
        assert response2.status_code == 200
        
        # Verify both were added
        response = client.get("/activities")
        activities = response.json()
        assert email1 in activities[activity1]["participants"]
        assert email2 in activities[activity2]["participants"]
