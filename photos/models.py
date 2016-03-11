from __future__ import unicode_literals

from django.db import models

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENCES = (
    (COPYLEFT, 'Copyleft'),
    (COPYRIGHT, 'Copyright'),
    (CREATIVE_COMMONS, 'Commons')
)

class Photo(models.Model):

    name = models.CharField(max_length=50)
    url = models.URLField()
    description = models.TextField(blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha automatica de agregado
    modified_at = models.DateTimeField(auto_now=True)  # Fecha automatica de modificacion
    license = models.CharField(max_length=3, choices=LICENCES)