#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)

nonebot.load_plugins("src/plugins")
# nb plugin install nonebot_plugin_test
# 前端测试插件
nonebot.load_plugin("nonebot_plugin_test")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...

if __name__ == "__main__":
    nonebot.run(app="bot:app")
