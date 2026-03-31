#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生姜价格数据更新脚本
读取爬虫数据并更新 data.js 文件
"""

import json
import os
import re
from datetime import datetime, timedelta
from crawler import crawl_all_data

# 数据文件路径
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.js")

def build_new_data_js(crawl_result):
    """构建新的 data.js 文件内容"""

    today = datetime.now()

    # 1. 生成 history 数组
    history_lines = []
    for item in crawl_result["history"]:
        history_lines.append(f"        ['{item['date']}', {item['national']}, {item['yishui']}]")
    history_js = ",\n".join(history_lines)

    # 2. 生成 regions 数组
    regions_js = {}
    for region_key, region_data in crawl_result["regional"].items():
        items = []
        for item in region_data:
            items.append(f"            {{ name: '{item['name']}', price: {item['price']}, change: {item['change']} }}")
        regions_js[region_key] = ",\n".join(items)

    # 3. 生成 forecast 数组
    forecast_7_nat = ", ".join([str(v) for v in crawl_result["forecast_7"]["national"]])
    forecast_7_yi = ", ".join([str(v) for v in crawl_result["forecast_7"]["yishui"]])
    forecast_30_nat = ", ".join([str(v) for v in crawl_result["forecast_30"]["national"]])
    forecast_30_yi = ", ".join([str(v) for v in crawl_result["forecast_30"]["yishui"]])

    # 读取原文件保留其他内容
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # 提取需要保留的部分
    # todayDetail
    today_detail_match = re.search(r"todayDetail: \{[\s\S]*?\n    \}", content)
    today_detail = today_detail_match.group(0) if today_detail_match else "todayDetail: {}"

    # marketAnalysis
    market_match = re.search(r"marketAnalysis: \{[\s\S]*?\n    \}", content)
    market_analysis = market_match.group(0) if market_match else "marketAnalysis: {}"

    # 90 天预测（保留空数组）
    forecast_90 = "90: {\n            national: [],\n            yishui: []\n        }"

    # 构建新文件
    new_content = f'''// 生姜价格数据 - 手动更新文件
// 更新时间：修改下方的 lastUpdateTime
// 数据来源：我的钢铁网 Mysteel / 中姜网 / 产区经纪人报价

const GingerData = {{
    // 最后更新时间（格式：YYYY-MM-DD HH:mm）
    lastUpdateTime: '{today.strftime('%Y-%m-%d %H:%M')}',

    // 全国主产区价格（单位：元/斤）
    // 每天更新各产区的主流成交价
    regions: {{
        shandong: [
{regions_js['shandong']}
        ],
        hebei: [
{regions_js['hebei']}
        ],
        yunnan: [
{regions_js['yunnan']}
        ],
        other: [
{regions_js['other']}
        ]
    }},

    // 30 天历史价格（用于走势图）
    // 格式：[日期字符串，全国均价，沂水价格]
    // 每天添加一条新记录
    history: [
{history_js}
    ],

    // 价格预测（用于预测图表）
    // 格式：{{ days: 预测天数，national: 全国预测 [], yishui: 沂水预测 [] }}
    forecast: {{
        7: {{
            national: [{forecast_7_nat}],
            yishui: [{forecast_7_yi}]
        }},
        30: {{
            national: [{forecast_30_nat}],
            yishui: [{forecast_30_yi}]
        }},
        {forecast_90}
    }},

    {today_detail[6:]},  // 移除开头的"    "

    {market_analysis[6:]}  // 移除开头的"    "
}};
'''

    return new_content


def update_data_file(crawl_result):
    """更新 data.js 文件"""

    today = datetime.now()

    # 构建新文件内容
    new_content = build_new_data_js(crawl_result)

    # 写回文件
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✓ 数据已更新至今日 ({today.strftime('%Y-%m-%d %H:%M')})")
    print(f"  全国均价：¥{crawl_result['national_avg']}/斤")
    print(f"  沂水价格：¥{crawl_result['yishui_price']}/斤")
    print(f"  历史数据：{len(crawl_result['history'])} 条")


def main():
    """主函数"""
    print("=" * 50)
    print("生姜价格数据自动更新")
    print("=" * 50)

    # 爬取数据
    print("\n[1/3] 正在爬取数据...")
    crawl_result = crawl_all_data()

    # 保存详细结果供调试
    with open("crawl_result.json", "w", encoding="utf-8") as f:
        json.dump(crawl_result, f, ensure_ascii=False, indent=2)
    print(f"\n     详细数据已保存至 crawl_result.json")

    # 更新 data.js
    print("\n[2/3] 正在更新 data.js...")
    update_data_file(crawl_result)

    # 显示更新摘要
    print("\n[3/3] 更新摘要:")
    print("-" * 40)
    history = crawl_result["history"]
    if len(history) >= 2:
        old_nat = history[-2]["national"]
        new_nat = history[-1]["national"]
        old_yi = history[-2]["yishui"]
        new_yi = history[-1]["yishui"]

        nat_change = ((new_nat - old_nat) / old_nat) * 100
        yi_change = ((new_yi - old_yi) / old_yi) * 100

        print(f"  全国均价：¥{old_nat} → ¥{new_nat} ({'↑' if nat_change > 0 else '↓'}{abs(nat_change):.1f}%)")
        print(f"  沂水价格：¥{old_yi} → ¥{new_yi} ({'↑' if yi_change > 0 else '↓'}{abs(yi_change):.1f}%)")

    print("\n✓ 更新完成！")
    print("\n下一步:")
    print("  git add data.js")
    print('  git commit -m "chore: 自动更新生姜价格数据至 $(date +%Y-%m-%d)"')
    print("  git push")


if __name__ == "__main__":
    main()
