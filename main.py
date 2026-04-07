import logging
import os
import json
from pica_punch import PicaPuncher
from jm_punch import JmPuncher

# 日志格式设置
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

def parse_accounts_config():
    """
    解析 JSON 格式的账号配置
    """
    accounts_json = os.getenv("ACCOUNTS_CONFIG")
    
    if not accounts_json:
        logging.error("❌ 未找到 ACCOUNTS_CONFIG 环境变量")
        logging.error("   请在 GitHub Secrets 中配置 ACCOUNTS_CONFIG")
        exit(1)
    
    try:
        config = json.loads(accounts_json)
        pica_accounts = config.get("pica", [])
        jm_accounts = config.get("jm", [])
        proxy = config.get("proxy", "")
        
        logging.info(f"📋 加载配置: {len(pica_accounts)} 个 Pica 账号, {len(jm_accounts)} 个 JM 账号")
        return pica_accounts, jm_accounts, proxy
    except json.JSONDecodeError as e:
        logging.error(f"❌ JSON 配置解析失败: {e}")
        exit(1)

if __name__ == "__main__":
    logging.info("=" * 50)
    logging.info("🚀 ComicsPuncher 启动")
    logging.info("=" * 50)
    
    # 解析配置
    pica_accounts, jm_accounts, proxy = parse_accounts_config()
    
    # 检查配置
    if not pica_accounts and not jm_accounts:
        logging.error("❌ 配置中没有任何账号信息！")
        logging.error("   请在 ACCOUNTS_CONFIG 中至少配置一个平台的账号")
        exit(1)
    
    # 执行哔咔打卡
    if pica_accounts:
        logging.info(f"\n🎨 开始执行 Pica 签到 ({len(pica_accounts)} 个账号)")
        for idx, account in enumerate(pica_accounts, 1):
            logging.info(f"\n--- Pica 账号 {idx}/{len(pica_accounts)} ---")
            pica = PicaPuncher(account["user"], account["password"], proxy)
            pica.run()
    else:
        logging.info("\n⏭️  未配置 Pica 账号，跳过")

    # 执行 JM 打卡
    if jm_accounts:
        logging.info(f"\n📚 开始执行 JM 签到 ({len(jm_accounts)} 个账号)")
        for idx, account in enumerate(jm_accounts, 1):
            logging.info(f"\n--- JM 账号 {idx}/{len(jm_accounts)} ---")
            jm = JmPuncher(account["user"], account["password"], proxy)
            jm.run()
    else:
        logging.info("\n⏭️  未配置 JM 账号，跳过")
    
    logging.info("\n" + "=" * 50)
    logging.info("✅ 所有任务执行完毕")
    logging.info("=" * 50)
