from flask_restful import Resource
from restapi.util import jsonify

class UserResource(Resource):

	def get(self, user_id=None):
		"""
		GET /users --> Get list of users.
		GET /users/<user_id> --> Get the user.
		"""
		if user_id is None:
			return jsonify({
			"users": "test without user_id"
			})
		else:
			return jsonify({
			"users": "test with user_id"
			})

	def post(self):
		"""
		POST /users --> Create new user.
		POST /users/<user_id> --> Not allowed.
		"""
		pass

	def patch(self, user_id):
		"""
		PATCH /users --> Not allowed.
		PATCH /users/<user_id> --> Update the user.
		"""
		pass

	def delete(self, user_id):
		"""
		DELETE /users --> Not allowed.
		DELETE /users/<user_id> --> Delete the user.
		"""
		pass