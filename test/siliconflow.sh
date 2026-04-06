#!/data/data/com.termux/files/usr/bin/bash
TOKEN="sk-psbulfyeksopdecegacsawiimusfpjdxoqkxudhivqnjbaim"
TMP_JSON=$(mktemp /data/data/com.termux/files/home/Yu/db/siliconflow.XXXXXX.json)
# "model": "Wan-AI/Wan2.2-T2V-A14B",
#!/data/data/com.termux/files/usr/bin/bash
# TOKEN="sk-psbulfyeksopdecegacsawiimusfpjdxoqkxudhivqnjbaim"
# TMP_JSON=$(mktemp /data/data/com.termux/files/home/Yu/db/siliconflow.XXXXXX.json)

#!/data/data/com.termux/files/usr/bin/bash

# 1. 配置区
TOKEN="sk-psbulfyeksopdecegacsawiimusfpjdxoqkxudhivqnjbaim"
SAVE_DIR="/data/data/com.termux/files/home/Yu/db/silionflow"
PROMPT="天气晴朗的一天，男生在食堂坐着敲键盘，侧对窗户，穿黑色衣服，年轻阳光，画面流畅, 2秒"
# 超时时间（秒），避免无限循环
TIMEOUT=1000

# 2. 构造 JSON
TMP_JSON=$(mktemp /data/data/com.termux/files/home/Yu/db/siliconflow.XXXXXX.json)
cat > "$TMP_JSON" << EOF
{
  "model": "Wan-AI/Wan2.2-T2V-A14B",
  "prompt": "$PROMPT",
  "image_size": "1280x720",
  "duration": 4
}
EOF

# 3. 提交任务
echo "🔄 提交文生视频任务..."
RESPONSE=$(curl -s -w "\n%{http_code}" -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  --data-binary "@$TMP_JSON" \
  https://api.siliconflow.cn/v1/video/submit)

HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
RESP_BODY=$(echo "$RESPONSE" | head -n -1)
rm -f "$TMP_JSON"

# 4. 验证提交
if [ "$HTTP_CODE" -ne 200 ]; then
  echo "❌ 提交失败 (HTTP $HTTP_CODE): $RESP_BODY"
  exit 1
fi

# 5. 解析任务ID（兼容requestId/task_id）
TASK_ID=$(echo "$RESP_BODY" | grep -o '"requestId":"[^"]*"' | cut -d'"' -f4)
if [ -z "$TASK_ID" ]; then
  TASK_ID=$(echo "$RESP_BODY" | grep -o '"task_id":"[^"]*"' | cut -d'"' -f4)
fi
if [ -z "$TASK_ID" ]; then
  echo "❌ 未获取到ID: $RESP_BODY"
  exit 1
fi

echo "✅ 任务提交成功，ID: $TASK_ID，开始轮询（超时${TIMEOUT}秒）"
START_TIME=$(date +%s)

# 6. 轮询（修复状态解析+增加超时）
while true; do
  # 超时检查
  CURRENT_TIME=$(date +%s)
  if [ $((CURRENT_TIME - START_TIME)) -gt $TIMEOUT ]; then
    echo "❌ 轮询超时，任务ID: $TASK_ID"
    exit 1
  fi

  # 查询任务状态
  RESULT=$(curl -s "https://api.siliconflow.cn/v1/video/query?task_id=$TASK_ID" \
    -H "Authorization: Bearer $TOKEN")
  
  # 【修复点】用jq精准解析（Termux可安装pkg install jq），彻底解决grep匹配问题
  # 备选：如果没装jq，用下面的grep方式
  # STATUS=$(echo "$RESULT" | python3 -c "import json, sys; print(json.load(sys.stdin).get('status', ''))")
  STATUS=$(echo "$RESULT" | jq -r '.status' 2>/dev/null)
  
  # 兼容旧版status字段
  if [ -z "$STATUS" ] || [ "$STATUS" = "null" ]; then
    STATUS=$(echo "$RESULT" | grep -o '"status":"[^"]*"' | cut -d'"' -f4)
  fi

  if [ "$STATUS" = "success" ] || [ "$STATUS" = "succeeded" ]; then
    # 提取视频URL
    VIDEO_URL=$(echo "$RESULT" | jq -r '.video_url' 2>/dev/null)
    if [ -z "$VIDEO_URL" ] || [ "$VIDEO_URL" = "null" ]; then
      VIDEO_URL=$(echo "$RESULT" | grep -o '"video_url":"[^"]*"' | cut -d'"' -f4)
    fi

    SAVE_PATH="$SAVE_DIR/$(date +%Y%m%d_%H%M%S).mp4"
    echo "✅ 生成成功，下载中..."
    curl -s -o "$SAVE_PATH" "$VIDEO_URL"
    
    if [ $? -eq 0 ]; then
      echo "✅ 视频已保存: $SAVE_PATH"
    else
      echo "❌ 下载失败"
    fi
    break
  elif [ "$STATUS" = "failed" ]; then
    echo "❌ 生成失败: $RESULT"
    break
  else
    # 【修复点】只打印一次，不刷屏
    echo -ne "\r⏳ 生成中... 已等待$((CURRENT_TIME - START_TIME))秒"
    sleep 2
  fi
done

echo -e "\n✅ 流程结束"
