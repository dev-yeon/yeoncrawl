# sample_swagger/open_api_params.py

from drf_yasg import openapi

get_params = [
	openapi.Parameter(
        "img_url",
        openapi.IN_QUERY,
        description="img_url",
        type=openapi.TYPE_STRING,
        default=""
    ),
    openapi.Parameter(
        "img_alt",
        openapi.IN_QUERY,
        description="img_alt",
        type=openapi.TYPE_STRING,
        default=""
    ),
	openapi.Parameter(
        "img_tag",
        openapi.IN_QUERY,
        description="img_tag",
        type=openapi.TYPE_STRING,
        default=""
    )
]