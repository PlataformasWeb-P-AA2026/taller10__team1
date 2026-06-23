from django import forms
from ordenamiento.models import Parroquia, Barrio


class ParroquiaForm(forms.ModelForm):
    """Formulario base para la entidad Parroquia."""
    class Meta:
        model = Parroquia
        fields = ['nombre', 'ubicacion', 'tipo']


class BarrioForm(forms.ModelForm):
    """Formulario base para la entidad Barrio."""
    class Meta:
        model = Barrio
        fields = ['nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales', 'parroquia']



# Formulario que cree una parroquia
class ParroquiaCrearForm(ParroquiaForm):
    pass


# Formulario que edite una parroquia
class ParroquiaEditarForm(ParroquiaForm):
    pass


# Formulario que cree un barrio
class BarrioCrearForm(BarrioForm):
    pass


# Formulario que edite un barrio
class BarrioEditarForm(BarrioForm):
    pass
