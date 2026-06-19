import json
from datetime import datetime

SITE_RECORDS = [
    {
        "title": "华体会体育入口",
        "url": "https://site-index-hth.com.cn",
        "keywords": ["华体会", "体育入口", "即时比分", "在线投注"],
        "tags": ["体育", "博彩", "华体会"],
        "description": "华体会体育官方入口平台，提供足球篮球赛事直播与投注服务。"
    },
    {
        "title": "华体会电竞专区",
        "url": "https://site-index-hth.com.cn/esports",
        "keywords": ["华体会", "电竞", "英雄联盟", "DOTA2"],
        "tags": ["电竞", "华体会", "游戏"],
        "description": "华体会电竞比赛专区，覆盖主流电竞赛事与实时赔率。"
    },
    {
        "title": "华体会新闻中心",
        "url": "https://site-index-hth.com.cn/news",
        "keywords": ["华体会", "体育新闻", "赛事分析", "实时资讯"],
        "tags": ["新闻", "华体会", "体育"],
        "description": "华体会官方新闻资讯板块，提供最新体育动态与深度分析。"
    }
]

def build_summary(records):
    """组装结构化摘要"""
    summary_lines = []
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary_lines.append(f"站点资料摘要 (生成时间: {now_str})")
    summary_lines.append("=" * 50)

    for idx, site in enumerate(records, 1):
        title = site.get("title", "未知")
        url = site.get("url", "#")
        keywords = ", ".join(site.get("keywords", []))
        tags = ", ".join(site.get("tags", []))
        desc = site.get("description", "")

        summary_lines.append(f"\n--- 站点 {idx} ---")
        summary_lines.append(f"名称: {title}")
        summary_lines.append(f"URL: {url}")
        summary_lines.append(f"关键词: {keywords}")
        summary_lines.append(f"标签: {tags}")
        summary_lines.append(f"说明: {desc}")

    summary_lines.append("\n" + "=" * 50)
    summary_lines.append(f"共 {len(records)} 条记录")
    return "\n".join(summary_lines)

def generate_json_summary(records):
    """以 JSON 格式返回摘要数据"""
    output = {
        "generated_at": datetime.now().isoformat(),
        "sources": records,
        "count": len(records)
    }
    return json.dumps(output, ensure_ascii=False, indent=2)

def export_to_markdown(records):
    """将摘要输出为 Markdown 格式"""
    lines = []
    lines.append("# 站点头像 - 结构化摘要")
    lines.append("")
    lines.append(f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    for idx, site in enumerate(records, 1):
        lines.append(f"## {idx}. {site['title']}")
        lines.append("")
        lines.append(f"- **URL**: [{site['url']}]({site['url']})")
        lines.append(f"- **关键词**: {', '.join(site['keywords'])}")
        lines.append(f"- **标签**: {', '.join(site['tags'])}")
        lines.append(f"- **说明**: {site['description']}")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"记录总数: {len(records)}")
    return "\n".join(lines)

if __name__ == "__main__":
    print("===== 纯文本摘要 =====")
    print(build_summary(SITE_RECORDS))

    print("\n\n===== JSON 摘要 =====")
    print(generate_json_summary(SITE_RECORDS))

    print("\n\n===== Markdown 摘要 =====")
    print(export_to_markdown(SITE_RECORDS))