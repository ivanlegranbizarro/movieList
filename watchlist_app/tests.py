from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from watchlist_app import models


class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testUser', password='testPassword')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamingPlatform.objects.create(
            name='Netflix', about='My Streaming Platform', website='www.netflix.com')

    def test_streamplatform_create(self):
        data = {
            'name': 'Netflix',
            'about': 'My Streaming Platform',
            'website': 'www.netflix.com'
        }
        response = self.client.post(reverse('router-movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('router-movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_ind(self):
        response = self.client.get(
            reverse('router-movie-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WatchListTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='testUser', password='testPassword')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        self.stream = models.StreamingPlatform.objects.create(
            name='HBO', about='My favorite platform', website='www.hbo.com')
        self.watchlist = models.WatchList.objects.create(
            platform=self.stream, title='Example Movie', storyline='Example storyline', active=True)

    def test_watchlist_create(self):
        data = {
            'platform': self.stream,
            'title': 'Example Movie',
            'storyline': 'Example storyline',
            'active': True
        }

        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_ind(self):
        response = self.client.get(
            reverse('movie-details', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, 'Example Movie')
