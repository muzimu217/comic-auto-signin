import logging
from jmcomic import JmOption, JmModuleConfig


class JmPuncher:
    """
    禁漫天堂自动签到类
    基于 jmcomic 库实现，模拟移动端 API 登录
    """

    def __init__(self, username, password, proxy=None):
        self.username = username
        self.password = password
        self.proxy = proxy

    def _clear_global_cookies(self):
        """清除 jmcomic 全局 cookies 缓存，避免多账号间 session 复用"""
        if hasattr(JmModuleConfig, 'APP_COOKIES'):
            delattr(JmModuleConfig, 'APP_COOKIES')

    def run(self):
        try:
            # 清除全局 cookies 缓存，确保每个账号使用独立 session
            self._clear_global_cookies()

            # 构造禁漫配置
            option = JmOption.construct(
                {
                    "client": {
                        "username": self.username,
                        "password": self.password,
                        "proxies": {"http": self.proxy, "https": self.proxy}
                        if self.proxy
                        else None,
                    }
                }
            )
            client = option.build_jm_client()

            logging.info(f"正在尝试登录 JM (账号: {self.username})...")
            # 登录接口返回的数据包含完整用户信息
            resp = client.login(self.username, self.password)
            user_data = resp.res_data

            # 验证登录返回的用户名是否与请求账号一致
            actual_username = user_data.get("username", "")
            if actual_username != self.username:
                logging.error("=" * 20)
                logging.error("❌ JM 登录验证失败！")
                logging.error(f"   期望账号: {self.username}")
                logging.error(f"   实际登录: {actual_username}")
                logging.error("   可能原因: 会话缓存导致登录了错误账号")
                logging.error("=" * 20)
                return False

            logging.info("=" * 20)
            logging.info("🎉 JM 登录活跃成功！")
            logging.info(f"登录账号: {self.username}")
            logging.info(f"显示用户名: {actual_username}")
            logging.info(f"金币余额: {user_data.get('coin')}")
            logging.info("=" * 20)
            return True

        except Exception as e:
            logging.error(f"JM 运行异常: {e}")
            return False
