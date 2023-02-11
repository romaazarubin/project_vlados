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

    async def add_good(self, user_id, name_tg, name_good, quantity,currency, rate, wallet):
        return await self.pool.execute("INSERT INTO good (user_id, name_tg, name_good, quantity,currency, rate, wallet, status) "
                                       "VALUES ($1,$2,$3,$4,$5,$6,$7,$8)", str(user_id), name_tg, name_good, int(quantity),
                                       currency, rate, wallet, False)

    async def presence_user(self, user_id):
        return await self.pool.fetchval("SELECT login FROM tt WHERE user_id = $1", str(user_id))

    async def confirmation(self, user_id, name_good, boolean):
        return await self.pool.execute("UPDATE good SET status = $3 WHERE user_id = $1 and name_good = $2",
                                       str(user_id), name_good, boolean)

    async def cart(self, user_id):
        return await self.pool.fetch("SELECT name_good, quantity, currency, rate, status FROM good WHERE user_id = $1",
                                     str(user_id))

    async def delete_product(self, user_id, name_good):
        return await self.pool.execute("DELETE FROM good WHERE user_id=$1 and name_good=$2", str(user_id), name_good)

    async def good(self, name_tg):
        return await self.pool.fetch(
            "SELECT user_id, name_good, quantity, rate, status, wallet FROM good WHERE name_tg = $1", name_tg)

    async def edit_value_buyer(self, user_id, name_good, value):
        return await self.pool.execute("UPDATE good SET quantity = quantity - $1 WHERE user_id = $2 and name_good = $3",
                                       int(value), str(user_id), name_good)

    async def check_value(self, user_id, name_good):
        return await self.pool.fetchval("SELECT quantity FROM good WHERE user_id = $1 and name_good = $2",
                                        str(user_id),
                                        name_good)
    async def add_buyer(self, user_id, name_tg, wallet):
        return await self.pool.execute("INSERT INTO buyer (user_id, name_tg, wallet_buyer) "
                                       "VALUES ($1, $2, $3)", str(user_id), name_tg, wallet)

    async def wallet_user(self, user_id):
        return await self.pool.fetchval("SELECT wallet_buyer FROM buyer WHERE user_id = $1", str(user_id))

    async def wallet_sellers_currency(self, user_id, name_good):
        return await self.pool.fetch("SELECT wallet, currency FROM good WHERE user_id = $1 and name_good = $2", str(user_id), name_good)

    async def update_buyer(self, user_id, name_tg, wallet):
        return await self.pool.execute('UPDATE buyer SET name_tg=$2, wallet_buyer=$3 where user_id=$1',str(user_id), name_tg, str(wallet))

    async def edit_value_seller(self, user_id, name_good, value):
        return await self.pool.execute("UPDATE good SET quantity = quantity + $1 WHERE user_id = $2 and name_good = $3",
                                       int(value), str(user_id), name_good)
    async def edit_wallet_admin(self, admin_id, wallet):
        return await self.pool.execute('UPDATE admin SET wallet_admin=$1 where user_id=$2', str(wallet), str(admin_id))

    async def wallet_admun(self, admin_id):
        return await self.pool.fetchval("SELECT wallet_admin FROM admin WHERE user_id = $1", str(admin_id))

    async def edit_price_admin(self, admin_id, price, currency):
        return await self.pool.execute('UPDATE admin SET price=$1, currency=$2 where user_id=$3', price, currency,str(admin_id))

    async def take_price(self, admin_id):
        return await self.pool.fetch('SELECT price, currency FROM admin WHERE user_id=$1', str(admin_id))

    async def add_admin(self, admin_id):
        return await self.pool.execute("INSERT INTO admin(user_id) VALUES ($1)", str(admin_id))