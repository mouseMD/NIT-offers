from sanic.response import json
from offers.tables import offers_table
from sanic.exceptions import InvalidUsage


def setup_routes(app):

    @app.post("/offer/create")
    async def create_offer(request):
        payload = request.json
        try:
            user_id = int(payload['user_id'])
            title = payload['title']
            text = payload['text']
        except Exception:
            raise InvalidUsage("Invalid message format")

        # add order to db
        query = offers_table.insert().values(
            user_id=user_id,
            title=title,
            text=text
        )
        await request.app.ctx.db.execute(query)
        return json({}, status=201)

    @app.post("/offer/")
    async def get_offers(request):
        payload = request.json
        if "offer_id" in payload:
            try:
                offer_id = int(payload["offer_id"])
            except ValueError:
                raise InvalidUsage("Invalid message format")
            query = offers_table.select().where(offers_table.c.id == offer_id)
            row = await request.app.ctx.db.fetch_one(query)
            if row is None:
                return json([])
            return json({'user_id': row[1], 'title': row[2], 'text': row[3]})
        elif "user_id" in payload:
            try:
                user_id = int(payload["user_id"])
            except ValueError:
                raise InvalidUsage("Invalid message format")
            query = offers_table.select().where(offers_table.c.user_id == user_id)
            rows = await request.app.ctx.db.fetch_all(query)
            if rows is None:
                return json([])
            return json([{'offer_id': row[0],  'title': row[2], 'text': row[3]} for row in rows])
        else:
            raise InvalidUsage("Invalid message format")
