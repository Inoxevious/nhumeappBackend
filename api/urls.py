from django.urls import path
from django.conf.urls import include,url
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from .views import *

urlpatterns = [
    # Rides Urls
    url(r'^rides/$',ride_list),
    url(r'^rides/(?P<pk>[0-9]+)$',ride_detail),
    path('upload/', FileUploadView.as_view()),
    url(r'^carimages/$',carimages),

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
    
]