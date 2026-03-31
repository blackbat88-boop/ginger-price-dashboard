# 自动化部署指南

## 启用自动更新

### 步骤 1：推送到 GitHub

```bash
git add .
git commit -m "feat: 添加自动数据更新功能"
git push
```

### 步骤 2：启用 GitHub Actions

1. 进入 GitHub 仓库页面
2. 点击 **Actions** 标签
3. 点击 **I understand my workflows, go ahead and enable them**（如果看到提示）
4. 找到 **生姜价格数据自动更新** 工作流

### 步骤 3：测试工作流

1. 在 Actions 页面点击 **生姜价格数据自动更新**
2. 点击 **Run workflow** 按钮
3. 等待约 1-2 分钟
4. 查看运行日志和 data.js 的变更

## 自定义更新时间

编辑 `.github/workflows/update-price-data.yml`，修改 cron 表达式：

```yaml
schedule:
  #  cron: '分 时 日 月 星期'  (UTC 时间)
  # 每天早上 8:00 (UTC 0:00 = 北京 8:00)
  - cron: '0 0 * * *'
```

### 常用时间设置

| 北京时间 | cron 表达式 |
|---------|-------------|
| 早上 6:00 | `0 22 * * *` |
| 早上 8:00 | `0 0 * * *` |
| 中午 12:00 | `0 4 * * *` |
| 下午 6:00 | `0 10 * * *` |

## 注意事项

1. **GitHub Actions 免费额度**：每月 2000 分钟，本项目每次运行约 30 秒，每天运行足够
2. **爬虫稳定性**：如果目标网站改版，爬虫可能失效，需要更新 `crawler.py`
3. **数据校验**：建议定期检查自动更新的数据是否准确

## 手动运行爬虫（本地测试）

```bash
# 安装依赖
pip install -r requirements.txt

# 运行爬虫
python update_data.py

# 查看 data.js 是否更新
cat data.js | head -30
```

## 故障排查

### 工作流运行失败

1. 检查 `.github/workflows/update-price-data.yml` 语法
2. 查看 Actions 日志输出
3. 确认 `crawler.py` 和 `update_data.py` 没有语法错误

### 数据未更新

1. 检查 `git diff` 是否有实际变更（无变更时不会提交）
2. 确认 `data.js` 中的数据格式正确
3. 查看爬虫日志输出

## 添加更多数据源

编辑 `crawler.py`，在 `crawl_price_data()` 函数中添加新的数据抓取逻辑：

```python
def crawl_price_data():
    # 现有抓取逻辑
    data = fetch_from_site_a()
    
    # 添加新数据源
    data_b = fetch_from_site_b()
    if data_b:
        data.update(data_b)
    
    return data
```
