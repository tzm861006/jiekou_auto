import time

import pytest
from datetime import datetime
from util.logging_util import logger

@pytest.fixture(scope="session",autouse=True)
def setup_class():
    strart_timer = time.time()
    start_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    logger.debug(f"用例开始了，当前时间为{start_time}")
    yield
    end_timer = time.time()
    end_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    logger.debug(f"用例结束了了，当前时间为{end_time}")
    logger.debug(f"一共耗时{strart_timer-end_timer}")


