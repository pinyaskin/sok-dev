from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('web_api.urls'), name='web'),
    path('', include('main_table.urls'))
]
