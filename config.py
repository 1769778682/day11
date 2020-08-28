import logging.handlers

# 发布文章标题
PUB_ARITCAL_TITLE = None


def log_base_config():
    logger = logging.getLogger()# 不能加参数
    logger.setLevel(level=logging.INFO)

    ls = logging.StreamHandler()
    la = logging.handlers.TimedRotatingFileHandler("./log/hmtt.log", when="midnight", interval=1, backupCount=2,
                                                   encoding="utf-8")
    formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')
    ls.setFormatter(formatter)
    la.setFormatter(formatter)
    logger.addHandler(ls)
    logger.addHandler(la)
