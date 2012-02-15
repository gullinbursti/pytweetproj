from django.conf.urls.defaults import *
from twitterPanel.views import *

urlpatterns = patterns( '',
    url( r'^$', index, name = 'twitterPanel_index' ),
    url( r'^panel/$', panel, name = 'twitterPanel_panel' ),
    url( r'^update/$', update, name = 'twitterPanel_update' ),
)