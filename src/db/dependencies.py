from src.db.session import AsyncSessionLocal


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            print("DB Session Error", e)

        finally:
            await session.close()
