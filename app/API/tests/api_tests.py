import pytest

import main
from main import app


class TestApi:

    post_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    @pytest.fixture
    def app_instance(self):
        app = main.app
        test_client = app.test_client()
        return test_client

    def test_all_post_correct_status(self, app_instance):
        result = app_instance.get('/api/posts', follow_redirects=True)
        assert result.status_code == 200

    def test_all_post_correct_keys(self, app_instance):
        result = app_instance.get('/api/posts', follow_redirects=True)
        list_of_post = result.get_json()
        for post in list_of_post:
            assert set(post.keys()) == self.post_keys

    def test_one_post_correct_status(self, app_instance):
        result = app_instance.get('/api/posts/1', follow_redirects=True)
        assert result.status_code == 200

    def test_one_post_correct_keys(self, app_instance):
        result = app_instance.get('/api/posts/1', follow_redirects=True)
        post = result.get_json()
        keys = set(post.keys())
        assert keys == self.post_keys

