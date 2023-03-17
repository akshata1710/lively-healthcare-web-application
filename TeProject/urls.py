
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from SleepApp.views import index,sleep
from FoodApp.views import calorie, food,fruit,vegetables,nuts,dairy
from WorkoutApp.views import workouts, totalwork,absss,arms,legs
from loginapp.views import user_login,user_logout,user_np,user_signup,create,delete,hom
from musics.views import main
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('musics.urls', namespace='music')),
    path('sleep/',sleep,name='sleep'),
    path('chart/',index,name='index'),
    path('food/',food,name='food'),
    path('fruits/',fruit,name='fruits'),
    path('calorie/',calorie,name='calorie'),
    path('vegetables/',vegetables,name='vegetables'),
    path('nuts/',nuts,name='nuts'),
    path('dairy/',dairy,name='dairy'),
    path('workouts/',workouts,name='workouts'),
    path('totalwork/', totalwork, name='totalwork'),
    path('absss/',absss,name='absss'),
    path('arms/',arms,name='arms'),
    path('legs/',legs,name='legs'),
    path("hom/", hom, name="hom"),
    path("user_signup", user_signup, name="user_signup"),
    path("user_login", user_login, name="user_login"),
    path("create", create, name="create"),
    path("user_logout", user_logout, name="user_logout"),
    path("delete/<int:id>", delete, name="delete"),
    path("user_np/",user_np, name="user_np"),
    path("main/",main,name="main"),

]
    



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
