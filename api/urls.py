from django.urls import path
from django.conf.urls import include,url
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAPIView, LogoutUserAPIView



urlpatterns = [
    url(r'^auth/login/$',
        obtain_auth_token,
        name='auth_user_login'),
    url(r'^auth/register/$',
        CreateUserAPIView.as_view(),
        name='auth_user_create'),
    url(r'^auth/logout/$',
        LogoutUserAPIView.as_view(),
        name='auth_user_logout'),
        # Drivers Urls
    url(r'^drivers/$',driver_list),
    url(r'^drivers/(?P<pk>[0-9]+)$',driver_detail),
    # Rides Urls
    url(r'^rides/$',ride_list),
    url(r'^rides/(?P<pk>[0-9]+)$',ride_detail),
    url(r'^getride/$',getride),
    path('upload/', FileUploadView.as_view()),
    url(r'^carimages/$',carimages),
    url(r'^retrieveDriverByEmail/$',retrieveDriverByEmailView.as_view(),name='retrieveDriverByEmailView'),
    url(r'^getDriverRegNumberUrlView/$',retrieveRideByRegNumberView.as_view(),name='retrieveRideByRegNumberView'),

    url(r'^retrieveCarImagesView/$',retrieveCarImagesView.as_view(),name='retrieveCarImagesView'),


    # Users Urls
    # path('users/', UserListCreateView.as_view(), name='users_list'),
    path('users/', usercreate_list, name='usercreate_list'),
    path('user/<uuid:pk>/',  UserDetailView.as_view(), name='user_detail'),
    url(r'^retrieveUserByEmail/$',retrieveUserByEmailView.as_view(),name='retrieveUserByEmail'),
    url(r'^retrievePackageByEmailView/$',retrievePackageByEmailView.as_view(),name='retrievePackageByEmailView'),
    url(r'^retrieveRideByEmailView/$',retrieveRideByEmailView.as_view(),name='retrieveRideByEmailView'),
    # Packages Urls
    url(r'^package/$',packagecreate_list),
    url(r'^userpackages/$',userpackages),
    url(r'^package/(?P<pk>[0-9]+)$',package_detail),
    url(r'^retrievePrimaryDeliveryAddress/$',RetrievePrimaryDeliveryAddressView.as_view(),name='retrievePrimaryDeliveryAddress'),
    url(r'^retrievePackageByReference/$',retrievePackageByReferenceView.as_view(),name='retrievePackageByReference'),
    url(r'^packages/$', PackageListView.as_view(), name='packages_list'),
    path('packageupload/', PackgesFileUploadView.as_view()),
    url(r'^packageimages/$',packageimages),
    url(r'^packageupload/$',packageupload_list),

        # Package Bids
    url(r'^packagebids/$',packagebids_list),
    url(r'^packagebid/(?P<pk>[0-9]+)$',packagebid_detail),
    url(r'^retrievePackageBidsView/$',retrievePackageBidsView.as_view(),name='retrievePackageBidsView'),

        # accepted Bids
    url(r'^acceptedbids/$',acceptedbids_list),
    url(r'^acceptedbid/(?P<pk>[0-9]+)$',acceptedbid_detail),
    url(r'^retrieveAcceptedBidsView/$',retrieveAcceptedBidsView.as_view(),name='retrieveAcceptedBidsView'),
        # accepted Bids
    url(r'^revokedbids/$',revokedbids_list),
    url(r'^revokedbid/(?P<pk>[0-9]+)$',revokedbid_detail),
    url(r'^retrieveRevokedBidsView/$',retrieveRevokedBidsView.as_view(),name='retrieveRevokedBidsView'),

    path('', include(router.urls)),
    # Transactions Urls
    url(r'^createpaymentintent/$',createpaymentintent,name='createpaymentintent'),

    path('appdata/', appdata, name='appdata'),
    url(r'^appDataView/$',appDataView.as_view(),name='appDataView'),

 
    
    
]