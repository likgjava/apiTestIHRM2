import logging.handlers
import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("BASE_DIR=", BASE_DIR)


# 项目基本路径
BASE_URL = "http://182.92.81.159"

# 用户令牌（token）
TOKEN = None

# 存放请求头数据
headers_data = {
    "Content-Type": "application/json",
    "Authorization": "Bearer a3ef5095-4798-4f70-90ab-2b3de4a9a6ae"
}


# 初始化日志配置
def init_log_config():
    # 创建日志器对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建控制台处理器
    sh = logging.StreamHandler()

    # 创建文件处理器
    log_file = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_file, when="midnight", interval=1,
                                                   backupCount=7, encoding="UTF-8")

    # 创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt)

    # 把格式化器添加到处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)
