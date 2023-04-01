from restapi.app import apiv1 as api
from restapi.resource.apiv1.user import UserResource

api.add_resource(
	UserResource,
	"/users",
	methods=["GET", "POST"],
	endpoint="users"  # It will be shown in response as key name.
)
api.add_resource(
	UserResource,
	"/users/<user_id>",
	methods=["GET", "PATCH", "DELETE"],
	endpoint="user" # It will be shown in response as key name.
)
