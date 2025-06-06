from __future__ import unicode_literals

from django.urls import path

from admin_page_lock.views import ClosePageConnection, GetPageInfo, OpenPageConnection

urlpatterns = [
    # Close Page Connection.
    path(
        "close_page_connection/",
        ClosePageConnection.as_view(),
        name="page_lock_close_page_connection",
    ),
    # Get Page Info.
    path("get_page_info/", GetPageInfo.as_view(), name="page_lock_get_page_connection"),
    # Open Page Connection.
    path(
        "open_page_connection/",
        OpenPageConnection.as_view(),
        name="page_lock_open_page_connection",
    ),
]
