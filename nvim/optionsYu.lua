
-- add yours here!

-- local o = vim.o
-- o.cursorlineopt ='both' -- to enable cursorline!

-- 启用所有模式下的虚拟编辑 (virtualedit=all)
vim.opt.virtualedit = 'all'

-- ## 录音
-- pkg install mpv
local api = vim.api
local keymap = vim.keymap.set
local fn = vim.fn

-- ===================== 配置 =====================
local config = {
  record_dir = fn.expand("~/Yu/db/recordings/"),
  leader     = " ",
}
-- ===============================================

_G.rec = {
  recoding = false,
  file     = nil,
  start_at = 0,
  ts_list  = {},
}

fn.mkdir(config.record_dir, "p")

-- ——————————————————————————————————————————————
-- <leader>ar 开始录音
-- ——————————————————————————————————————————————
keymap("n", "<leader>ar", function()
  if rec.recoding then
    vim.notify("已在录音", 3)
    return
  end

  local now = fn.strftime("%Y-%m-%d_%H-%M-%S")
  rec.file = config.record_dir .. "rec_" .. now .. ".m4a"
  rec.recoding = true
  rec.start_at = os.time()
  rec.ts_list = {}

  fn.system(("termux-microphone-record -f %s -e m4a &"):format(fn.shellescape(rec.file)))
  vim.notify("🎙 开始录音: " .. fn.fnamemodify(rec.file, ":t"), 2)
end, { desc = "开始录音" })

-- ——————————————————————————————————————————————
-- <leader>aa 插入时间戳
-- ——————————————————————————————————————————————
keymap("n", "<leader>aa", function()
  if not rec.recoding then
    vim.notify("未录音", 4)
    return
  end

  local sec = os.time() - rec.start_at
  local h = math.floor(sec / 3600)
  local m = math.floor((sec % 3600) / 60)
  local s = sec % 60
  local ts = ("%02d:%02d:%02d"):format(h, m, s)

  local line = ("[%s] %s"):format(ts, fn.fnamemodify(rec.file, ":t"))
  api.nvim_put({ line }, "l", false, true)

  table.insert(rec.ts_list, {
    ts   = ts,
    sec  = sec,
    file = rec.file,
  })
  vim.notify("✅ 时间戳: " .. ts, 2)
end, { desc = "插入时间戳" })

-- ——————————————————————————————————————————————
-- <leader>as 停止录音
-- ——————————————————————————————————————————————
keymap("n", "<leader>as", function()
  if not rec.recoding then
    vim.notify("未录音", 4)
    return
  end

  fn.system("termux-microphone-record -q")
  rec.recoding = false

  local md = api.nvim_buf_get_name(0)
  local f = io.open(md .. ".ts", "w")
  if f then
    f:write(vim.inspect(rec.ts_list))
    f:close()
  end

  vim.notify("🛑 录音结束", 2)
end, { desc = "停止录音" })

-- ——————————————————————————————————————————————
-- 加载时间戳
-- ——————————————————————————————————————————————
api.nvim_create_autocmd("BufEnter", {
  pattern = "*.md",
  callback = function()
    local md = api.nvim_buf_get_name(0)
    local ts_file = md .. ".ts"
    if fn.filereadable(ts_file) == 1 then
      local f = io.open(ts_file, "r")
      local data = f:read("*a")
      f:close()
      rec.ts_list = loadstring("return " .. data)() or {}
    end
  end,
})

-- ——————————————————————————————————————————————
-- 获取当前行时间戳
-- ——————————————————————————————————————————————
local function get_cur()
  local line = api.nvim_get_current_line()
  local ts = line:match("%[(%d+:%d+:%d+)%]")
  if not ts then return nil end

  local fname = line:match("(rec_%d+-%d+-%d+_%d+-%d+-%d+%.m4a)")
  if not fname then return nil end

  local h, m, s = ts:match("(%d+):(%d+):(%d+)")
  local sec = h * 3600 + m * 60 + s
  local file = config.record_dir .. fname

  return file, sec
end

-- ——————————————————————————————————————————————
-- <leader>ap 从时间戳播放
-- ——————————————————————————————————————————————
keymap("n", "<leader>ap", function()
  local file, sec = get_cur()
  if not file or fn.filereadable(file) == 0 then
    vim.notify("无效录音行", 4)
    return
  end

  fn.system("pkill -9 mpv 2>/dev/null")

  local cmd = (
    "nohup mpv --no-video --ao=opensles --start=%d %s >/dev/null 2>&1 &"
  ):format(sec, fn.shellescape(file))

  fn.system(cmd)
  vim.notify(("▶️ 从 %d 秒播放"):format(sec), 2)
end, { desc = "从时间戳播放" })

-- ——————————————————————————————————————————————
-- <leader>ak 停止播放（新加）
-- ——————————————————————————————————————————————
keymap("n", "<leader>ak", function()
  fn.system("pkill -9 mpv 2>/dev/null")
  fn.system("termux-media-player stop 2>/dev/null")
  vim.notify("⏹️ 播放已停止", 2)
end, { desc = "停止播放" })


local keymap = vim.keymap.set
local fn = vim.fn
local api = vim.api

-- ## 拍照

-- ===================== 拍照 / 截图 插入 MD（最终版）=====================
-- 拍照：<leader>ac
keymap("n", "<leader>ac", function()
  local img_dir = fn.expand("~/storage/shared/Pictures/")
  fn.system("mkdir -p " .. fn.shellescape(img_dir))

  local now = fn.strftime("%Y-%m-%d_%H-%M-%S")
  local img_name = "photo_" .. now .. ".jpg"
  local img_path = img_dir .. img_name

  vim.notify("📷 正在调用相机拍照…", vim.log.levels.INFO)
  local cmd = string.format("termux-camera-photo -c 0 %s", fn.shellescape(img_path))
  fn.system(cmd)

  vim.defer_fn(function()
    if fn.filereadable(img_path) == 0 then
      vim.notify("❌ 拍照失败：未生成图片文件", vim.log.levels.ERROR)
      return
    end
    local md_line = string.format("![photo](%s)", img_path)
    api.nvim_put({ md_line }, "l", false, true)
    vim.notify("✅ 拍照已插入：" .. img_name, vim.log.levels.INFO)
  end, 1500)
end, { desc = "拍照并插入Markdown" })

-- 截图：<leader>ad
keymap("n", "<leader>ad", function()
  local img_dir = fn.expand("~/storage/shared/Pictures/")
  fn.system("mkdir -p " .. fn.shellescape(img_dir))

  local now = fn.strftime("%Y-%m-%d_%H-%M-%S")
  local img_name = "screen_" .. now .. ".png"
  local img_path = img_dir .. img_name

  vim.notify("🖥️  正在截图…", vim.log.levels.INFO)
  local cmd = string.format("termux-screenshot -o %s", fn.shellescape(img_path))
  fn.system(cmd)

  vim.defer_fn(function()
    if fn.filereadable(img_path) == 0 then
      vim.notify("❌ 截图失败：未生成图片文件", vim.log.levels.ERROR)
      return
    end
    local md_line = string.format("![screen](%s)", img_path)
    api.nvim_put({ md_line }, "l", false, true)
    vim.notify("✅ 截图已插入：" .. img_name, vim.log.levels.INFO)
  end, 1000)
end, { desc = "截图并插入Markdown" })

-- ===================== <leader>ax 专用：摄像头0拍照 =====================
keymap("n", "<leader>ax", function()
  local img_dir = fn.expand("~/storage/shared/Pictures/")
  fn.system("mkdir -p " .. fn.shellescape(img_dir))

  local now = fn.strftime("%Y-%m-%d_%H-%M-%S")
  local img_name = "camera0_" .. now .. ".jpg"
  local img_path = img_dir .. img_name

  vim.notify("📸 正在使用摄像头拍照…", vim.log.levels.INFO)
  -- 你要的命令：termux-camera-photo -c 0
  local cmd = string.format("termux-camera-photo -c 1 %s", fn.shellescape(img_path))
  fn.system(cmd)

  vim.defer_fn(function()
    if fn.filereadable(img_path) == 0 then
      vim.notify("❌ 拍照失败", vim.log.levels.ERROR)
      return
    end
    local md_line = string.format("![camera0](%s)", img_path)
    api.nvim_put({ md_line }, "l", false, true)
    vim.notify("✅ 已插入摄像头0照片", vim.log.levels.INFO)
  end, 1500)
end, { desc = "摄像头0拍照插入md" })


-- ## 插入图片
-- Image Insert--
-- Markdown：<leader>aj 插图片 <leader>ak 插视频 <leader>al feh自适应预览
vim.api.nvim_create_autocmd("FileType", {
  pattern = "markdown",
  callback = function()
    -- 获取最新文件
    local function get_latest_file(dir, exts)
      local path = vim.fn.expand(dir)
      if vim.fn.isdirectory(path) == 0 then return nil end

      local files = {}
      for _, ext in ipairs(exts) do
        local matched = vim.fn.glob(path .. "/**/*." .. ext, false, true)
        vim.list_extend(files, matched)
      end

      if #files == 0 then return nil end
      table.sort(files, function(a, b)
        return vim.fn.getftime(a) > vim.fn.getftime(b)
      end)
      return files[1]
    end

    -- 复制文件
    local function copy_file(src, dest_dir)
      local dest_path = vim.fn.expand(dest_dir)
      if vim.fn.isdirectory(dest_path) == 0 then
        vim.fn.mkdir(dest_path, "p")
      end
      local name = vim.fn.fnamemodify(src, ":t")
      local dest = dest_path .. "/" .. name
      vim.fn.system(string.format("cp -f '%s' '%s'", src, dest))
      return dest
    end

    -- 提取当前行 MD 图片路径
    local function get_image_path()
      local line = vim.api.nvim_get_current_line()
      local path = line:match("%((.-)%)")
      if not path then return nil end
      return vim.fn.expand(path)
    end

    local source_dir = "~/storage/shared/Pictures/"
    local target_dir = "~/Yu/db/screenShots"

    -- <leader>aj 插入最新图片
    vim.keymap.set("n", "<leader>aj", function()
      local src = get_latest_file(source_dir, {"png", "jpg", "jpeg", "webp", "gif"})
      if not src then return end
      local dest = copy_file(src, target_dir)
      local line = string.format("![%s](%s)", vim.fn.fnamemodify(dest, ":t:r"), dest)
      vim.api.nvim_put({line}, "l", false, true)
      vim.notify("✅ 已插入图片：" .. vim.fn.fnamemodify(dest, ":t"), vim.log.levels.INFO)
    end, { buffer = true, desc = "插入最新图片" })

    -- <leader>ak 插入最新视频
    vim.keymap.set("n", "<leader>av", function()
      local src = get_latest_file(source_dir, {"mp4", "mkv", "mov", "avi", "webm"})
      if not src then return end
      local dest = copy_file(src, target_dir)
      local line = string.format("<video src=\"%s\" controls></video>", dest)
      vim.api.nvim_put({line}, "l", false, true)
      vim.notify("✅ 已插入视频：" .. vim.fn.fnamemodify(dest, ":t"), vim.log.levels.INFO)
    end, { buffer = true, desc = "插入最新视频" })

    -- ==============================================
    -- <leader>al：feh 完美自适应预览（核心修改）
    -- ==============================================
    vim.keymap.set("n", "<leader>al", function()
      local p = get_image_path()
      if not p then
        vim.notify("❌ 未找到图片路径", vim.log.levels.WARN)
        return
      end
      if vim.fn.filereadable(p) == 0 then
        vim.notify("❌ 图片不存在：" .. p, vim.log.levels.WARN)
        return
      end
      -- 最优自适应参数：自动缩放、保持比例、无边框、黑背景
      vim.fn.system(("feh --scale-down --auto-zoom -x -B black '%s' &"):format(p))
      vim.notify("🖼️ 已自适应预览", vim.log.levels.INFO)
    end, { buffer = true, desc = "feh 自适应预览当前图片" })

-- <leader>a; 图片预览：Termux 无乱码终极版
vim.keymap.set('n', '<leader>a;', function()
    -- 1. 提取图片路径（优先匹配 Markdown 链接）
    local line = vim.api.nvim_get_current_line()
    local img_path = line:match("!%[.-%]%((.-)%)")

    -- 2. 回退到行内路径/当前文件
    if not img_path then
        img_path = line:match("(%S+%.(png|jpg|jpeg|gif|webp|bmp))")
    end
    if not img_path then
        local bufname = vim.api.nvim_buf_get_name(0)
        local ext = vim.fn.fnamemodify(bufname, ':e'):lower()
        local is_img = {png=true, jpg=true, jpeg=true, gif=true, webp=true, bmp=true}
        if not is_img[ext] then
            vim.notify("❌ 未找到有效图片路径", vim.log.levels.WARN)
            return
        end
        img_path = bufname
    end

    -- 3. 兼容旧版 Neovim 的绝对路径判断
    local function is_abs(path) return path:sub(1,1) == "/" end
    local current_dir = vim.fn.fnamemodify(vim.api.nvim_buf_get_name(0), ':h')
    if not is_abs(img_path) then
        img_path = current_dir .. "/" .. img_path
    end

    -- 4. 校验文件存在
    if vim.fn.filereadable(img_path) == 0 then
        vim.notify("❌ 图片不存在: " .. img_path, vim.log.levels.ERROR)
        return
    end

    -- 5. 创建悬浮窗口
    local width = math.floor(vim.o.columns * 0.8)
    local height = math.floor(vim.o.lines * 0.8)
    local win_w = math.min(120, width)
    local win_h = math.min(36, height)

    local buf = vim.api.nvim_create_buf(false, true)
    local win = vim.api.nvim_open_win(buf, true, {
        relative = "editor",
        width = win_w, height = win_h,
        col = math.floor((vim.o.columns - win_w)/2),
        row = math.floor((vim.o.lines - win_h)/2),
        style = "minimal", border = "rounded"
    })

    -- 6. 核心修复：纯 ASCII 字符 + 安全参数，彻底杜绝乱码
    vim.fn.termopen(string.format(
        'chafa --size=%dx%d --align=center --fill=none "%s"',
        win_w, win_h, img_path
    ))
    vim.cmd.startinsert()

    -- 7. 关闭快捷键
    vim.keymap.set('n', 'q', function() vim.api.nvim_win_close(win, true) end, {buffer=buf, nowait=true})
    vim.keymap.set('t', '<ESC>', function() vim.api.nvim_win_close(win, true) end, {buffer=buf, nowait=true})
end, { desc = 'Chafa 图片预览' })
  end,
})


-- ## 硅基流动生成图片
-- ====================== 全局环境变量 ======================
local SILICONFLOW_TOKEN = vim.env.SILICONFLOW_TOKEN or ""
local SAVE_DIR = vim.fn.expand("~/Yu/db/silionflow")
vim.fn.mkdir(SAVE_DIR, "p") -- 自动创建目录

-- 工具函数：生成时间戳文件名
local function gen_filename(ext)
  return string.format("%s/%s.%s", SAVE_DIR, os.date("%Y%m%d_%H%M%S"), ext)
end

-- ====================== <leader>pp：生图 (正常可用) ======================
vim.keymap.set("n", "<leader>pp", function()
  local line = vim.api.nvim_get_current_line()
  if line == "" then return end

  local body = { model = "Kwai-Kolors/Kolors", prompt = line, image_size = "1024x1024", num_images = 1 }
  vim.notify("🔄 生成图片中...")

  vim.fn.jobstart({
    "curl", "-s", "-H", "Authorization: Bearer " .. SILICONFLOW_TOKEN,
    "-H", "Content-Type: application/json", "-d", vim.json.encode(body),
    "https://api.siliconflow.cn/v1/images/generations"
  }, {
    on_stdout = function(_, data)
      local ok, res = pcall(vim.json.decode, table.concat(data))
      if not ok or not res.images then return end
      
      local save_path = gen_filename("png")
      vim.fn.jobstart({"wget", "-O", save_path, res.images[1].url}, {
        on_exit = function()
          local img_link = string.format("![%s](%s)", line, save_path)
          local row = vim.api.nvim_win_get_cursor(0)[1]
          vim.api.nvim_buf_set_lines(0, row, row, false, {img_link})
          vim.notify("✅ 图片已保存插入")
        end
      })
    end
  })
end)

