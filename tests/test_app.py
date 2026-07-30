import unittest

from fastapi.testclient import TestClient

from src.app import app


class ActivityApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_github_skills_activity_is_available(self) -> None:
        response = self.client.get("/activities")

        self.assertEqual(response.status_code, 200)

        activities = response.json()
        self.assertIn("GitHub Skills", activities)

        github_skills = activities["GitHub Skills"]
        self.assertEqual(
            github_skills["description"],
            "Learn practical coding and collaboration skills through GitHub tools and projects",
        )
        self.assertEqual(github_skills["max_participants"], 25)
        self.assertEqual(github_skills["participants"], [])


if __name__ == "__main__":
    unittest.main()
