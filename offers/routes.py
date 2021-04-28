from sanic.response import json
from offers.tables import offers_table
from sanic.exceptions import Unauthorized, InvalidUsage


def setup_routes(app):
    pass
    # @app.post("/offer/create")
    # async def create_offer(request):
    #     payload = request.json
    #     try:
    #         username = payload['username']
    #         email = payload['email']
    #         password = payload['password']
    #     except KeyError:
    #         raise InvalidUsage("Invalid message format")
    #
    #     query = users_table.insert().values(
    #         username=username,
    #         email=email,
    #         password=sha256_crypt.hash(password)
    #     )
    #     try:
    #         await request.app.ctx.db.execute(query)
    #     except UniqueViolationError:
    #         raise InvalidUsage("User already exists")   # or 409?
    #     return json({}, status=201)
    #
    # @app.post("/offer/")
    # async def get_offers(request):
    #     payload = request.json
    #     try:
    #         username = payload['username']
    #         password = payload['password']
    #     except KeyError:
    #         raise InvalidUsage("Invalid message format")
    #     #query = users.select([users.c.id, users.c.password]) #.where(users.c.username == 'user')
    #     query = users_table.select().where(users_table.c.username == username)
    #     row = await request.app.ctx.db.fetch_one(query)
    #     if row is None:
    #         raise Unauthorized("Invalid credentials")
    #     user_id, hash_pass = row[0], row[3]
    #     if sha256_crypt.verify(password, hash_pass):
    #         token = await generate_token(user_id)
    #     else:
    #         raise Unauthorized("Invalid credentials")
    #     return json({'user_id': user_id, 'token': token})
    #
    #
    # @app.route("/")
    # async def test(request):
    #     query = users_table.select()
    #     rows = await request.app.ctx.db.fetch_all(query)
    #     return json([{'id': row[0], 'username': row[1], 'email': row[2], 'password': row[3]} for row in rows])
