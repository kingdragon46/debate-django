from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls"), name='home'), # Website routes
    # path("master/", include("Master.urls")), # Master routes
    # path("employee/", include("Employee.urls")), # Volunteer Panel routes
    # path("donor/", include("Donor.urls")), # Donor Panel routes
    # path("beneficiary/", include("Beneficiary.urls")), # Beneficiary Panel routes
    # path('oauth/', include('social_django.urls', namespace='social')),  # <-- Social here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
