from django.urls import path
from bookingAPI.views.all_avl_seats_of_show import AllSeatsofAShow
from bookingAPI.views.all_shows_of_movie import ShowsOfMovieInCity
from bookingAPI.views.book_seat_of_a_show import BookSeatOfAShow
from bookingAPI.views.get_cinemas_in_city_view import CinemasInCity, ShowsInCinemas
from bookingAPI.views.cities_view import Cities

urlpatterns = [
    path('city/<int:pk>/cinemas',CinemasInCity.as_view(),name="Cinemas in city"),
    path('city/',Cities.as_view(),name="Cinemas in city"),
    path('city/<int:pk>',Cities.as_view(),name="Cinemas in city"),
    path('cinemas/',CinemasInCity.as_view(),name="Cinemas in city"),
    path('city/<int:pk>/cinemas/<int:cpk>/shows',ShowsInCinemas.as_view(),name="Cinemas in city"),    
    path('city/<int:cpk>/movie/<int:mpk>/',ShowsOfMovieInCity.as_view(),name="Shows in city"),    
    path('show/<int:spk>/avlseats/',AllSeatsofAShow.as_view(),name="All seats of a show"),   
    path('book/show/<int:shpk>/seat/<int:sepk>',BookSeatOfAShow.as_view(),name="Book seat of a show"),   

]

