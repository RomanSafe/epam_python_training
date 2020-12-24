import pytest

from lecture_10.homework10.task.task import main


@pytest.mark.asyncio
async def test_main(event_loop):
    event_loop.run_until_complete(main())
