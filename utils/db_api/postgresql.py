import asyncio
import asyncpg
from config import ip, PGUSER, PGPASSWORD, DATABASE


class DataBase:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(
                database=DATABASE,
                user=PGUSER,
                password=PGPASSWORD,
                host=ip,
                port='5432'

            )
        )

    async def add_user(self, user_id, name_tg):
        return await self.pool.execute("INSERT INTO seller (user_id, name_tg, premium) "
                                        "VALUES ($1, $2, $3)", str(user_id), name_tg, False)

    async def add_good(self, user_id, name_tg, name_good, quantity, rate, wallet):
        return await self.pool.execute("INSERT INTO good (user_id, name_tg, name_good, quantity, rate, status, wallet) "
                                       "VALUES ($1,$2,$3,$4,$5,$6,$7)", str(user_id), name_tg, name_good, int(quantity), rate, False, wallet)

    async def presence_user(self, user_id):
         return await self.pool.fetchval("SELECT login FROM tt WHERE user_id = $1", str(user_id))
    #
    # async def registration_user(self, user_id, username, login, password):
    #     return await self.pool.execute("INSERT INTO tt (user_id, name_tg, login, password, premium) "
    #                                    "VALUES ($1,$2,$3,$4,$5)", str(user_id), username, str(login), password, False)
    #
    # async def sel(self, user_id):
    #     return await self.pool.fetchval("SELECT password FROM tt WHERE user_id = $1", str(user_id))
