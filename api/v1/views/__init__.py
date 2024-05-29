#!/usr/bin/python3
"""init file for the blueprint"""

from flask import Blueprint


# instance of Blueprint (url prefix must be /api/v1)
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# wildcard import of everything in the package api.v1.views.index
from api.v1.views.index import *