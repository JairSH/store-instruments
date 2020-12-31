from django.urls import path
from .views import home , registro_usuario, guitars, bass,keyboards,drums,accordion, categories, ready_to_pick

urlpatterns = [
    path('', home, name = "home"),
    path('registro-usuario/',registro_usuario,name = "registro_usuario"),
    path('guitars/',guitars, name = "guitars"),
    path('bass/',bass, name = "bass"),
    path('keyboards/',keyboards, name = "keyboards"),
    path('drums/',drums, name = "drums"),
    path('accordion/',accordion, name = "accordion"),
    path('categories/',categories, name = "categories"),
    path('ready-to-pick/',ready_to_pick, name = "ready_to_pick"),
]