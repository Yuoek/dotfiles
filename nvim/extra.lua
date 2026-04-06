return {

  -- 19. todo-comments
  {
  "folke/todo-comments.nvim",
  lazy = false,
  dependencies = { "nvim-lua/plenary.nvim" },
    opts = {
      -- your configuration comes here
      -- or leave it empty to use the default settings
      -- refer to the configuration section below
    }
  },

  -- 18. llm
  {
    "Kurama622/llm.nvim",
    -- If code completion uses Codeium, it requires `Exafunction/codeium.nvim`; otherwise, it does not.
    dependencies = { "nvim-lua/plenary.nvim", "MunifTanjim/nui.nvim", "Exafunction/codeium.nvim" },
    cmd = { "LLMSessionToggle", "LLMSelectedTextHandler", "LLMAppHandler" },
    config = function()
      local tools = require("llm.tools")
      -- vim.api.nvim_set_hl(0, "Query", { fg = "#6aa84f", bg = "NONE" })
      require("llm").setup({
        -- enable_trace = true,
        -- -- [[ cloudflare ]]     params: api_type =  "workers-ai" | "openai" | "zhipu" | "ollma"
        -- -- model = "@cf/qwen/qwen1.5-14b-chat-awq",
        -- model = "@cf/google/gemma-7b-it-lora",
        -- api_type = "workers-ai",
        -- fetch_key = function()
        --   return vim.env.WORKERS_AI_KEY
        -- end,

        -- [[ openrouter]]
        -- url = "https://openrouter.ai/api/v1/chat/completions",
        -- model = "google/gemini-2.0-flash-exp:free",
        -- max_tokens = 4096,
        -- api_type = "openai",
        -- fetch_key = function()
        --   return vim.env.OPENROUTER_KEY
        -- end,

        -- [[ GLM ]]
        -- url = "https://open.bigmodel.cn/api/paas/v4/chat/completions",
        -- model = "glm-4-flash",
        -- max_tokens = 8000,
        -- fetch_key = function()
        --   return vim.env.GLM_KEY
        -- end,

        -- [[ kimi ]]
        -- url = "https://api.moonshot.cn/v1/chat/completions",
        -- model = "moonshot-v1-8k", -- "moonshot-v1-8k", "moonshot-v1-32k", "moonshot-v1-128k"
        -- api_type = "openai",
        -- max_tokens = 4096,
        -- fetch_key = function()
        --   return vim.env.KIMI_KEY
        -- end,
        -- -- streaming_handler = kimi_handler,

        -- [[ ollma ]]
        -- url = "http://localhost:11434/api/chat",
        -- model = "llma3.2:1b",
        -- api_type = "ollma",
        -- fetch_key = function()
        --   return vim.env.LOCAL_LLM_KEY
        -- end,

        -- [[ local llm ]]
        -- url = "your url",
        -- model = "your model name",
        -- streaming_handler = local_llm_streaming_handler,
        -- parse_handler = local_llm_parse_handler,

        -- [[ Github Models ]]
        -- url = "https://models.inference.ai.azure.com/chat/completions",
        -- model = "gpt-4o",
        -- api_type = "openai",
        -- -- max_tokens = 4096,
        -- max_tokens = 8000,
        -- -- model = "gpt-4o-mini",
        -- fetch_key = function()
        --   return vim.env.GITHUB_TOKEN
        -- end,

        -- [[deepseek]]
        -- url = "https://api.deepseek.com/chat/completions",
        -- model = "deepseek-chat",
        -- api_type = "openai",
        -- max_tokens = 4096,
        -- fetch_key = function()
        --   return vim.env.LLM_KEY
        -- end,

        -- [[ siliconflow ]]
        -- model = "THUDM/glm-4-9b-chat",
        -- model = "01-ai/Yi-1.5-9B-Chat-16K",
        -- model = "google/gemma-2-9b-it",
        -- model = "meta-llma/Meta-llma-3.1-8B-Instruct",
        -- model = "Qwen/Qwen2.5-Coder-7B-Instruct",
        -- model = "internlm/internlm2_5-7b-chat",
        -- [optional: fetch_key]
        url = "https://api.siliconflow.cn/v1/chat/completions",
        api_type = "openai",
        max_tokens = 4096,
        model = "Qwen/Qwen2.5-7B-Instruct",
        fetch_key = function()
          return vim.env.SILICONFLOW_TOKEN
        end,

        temperature = 0.3,
        top_p = 0.7,

        prompt = "You are a helpful chinese assistant.",

        spinner = {
          text = {
            "󰧞󰧞",
            "󰧞󰧞",
            "󰧞󰧞",
            "󰧞󰧞",
          },
          hl = "Title",
        },

        prefix = {
          -- 
          user = { text = "😃 ", hl = "Title" },
          assistant = { text = "  ", hl = "Added" },
        },

        display = {
          diff = {
            layout = "vertical", -- vertical|horizontal split for default provider
            opts = { "internal", "filler", "closeoff", "algorithm:patience", "followwrap", "linematch:120" },
            provider = "mini_diff", -- default|mini_diff
          },
        },
        -- style = "right",
        --[[ custom request args ]]
        -- args = [[return {url, "-N", "-X", "POST", "-H", "Content-Type: application/json", "-H", authorization, "-d", vim.fn.json_encode(body)}]],
        -- history_path = "/tmp/llm-history",
        save_session = true,
        max_history = 15,
        max_history_name_length = 20,

        -- stylua: ignore
        -- popup window options
        popwin_opts = {
          relative = "cursor", enter = true,
          focusable = true, zindex = 50,
          position = { row = -7, col = 15, },
          size = { height = 15, width = "50%", },
          border = { style = "single",
            text = { top = " Explain ", top_align = "center" },
          },
          win_options = {
            winblend = 0,
            winhighlight = "Normal:Normal,FloatBorder:FloatBorder",
          },
        },

        -- stylua: ignore
        keys = {
          -- The keyboard mapping for the input window.
          ["Input:Submit"]      = { mode = "n", key = "<cr>" },
          ["Input:Cancel"]      = { mode = {"n", "i"}, key = "<C-c>" },
          ["Input:Resend"]      = { mode = {"n", "i"}, key = "<C-r>" },

          -- only works when "save_session = true"
          ["Input:HistoryNext"] = { mode = {"n", "i"}, key = "<C-j>" },
          ["Input:HistoryPrev"] = { mode = {"n", "i"}, key = "<C-k>" },

          -- The keyboard mapping for the output window in "split" style.
          ["Output:Ask"]        = { mode = "n", key = "i" },
          ["Output:Cancel"]     = { mode = "n", key = "<C-c>" },
          ["Output:Resend"]     = { mode = "n", key = "<C-r>" },

          -- The keyboard mapping for the output and input windows in "float" style.
          ["Session:Toggle"]    = { mode = "n", key = "<leader>llac" },
          ["Session:Close"]     = { mode = "n", key = {"<esc>", "Q"} },

          -- Scroll [default]
          ["PageUp"]            = { mode = {"i","n"}, key = "<C-b>" },
          ["PageDown"]          = { mode = {"i","n"}, key = "<C-f>" },
          ["HalfPageUp"]        = { mode = {"i","n"}, key = "<C-u>" },
          ["HalfPageDown"]      = { mode = {"i","n"}, key = "<C-d>" },
          ["JumpToTop"]         = { mode = "n", key = "gg" },
          ["JumpToBottom"]      = { mode = "n", key = "G" }
        },

        app_handler = {
          OptimizeCode = {
            handler = tools.side_by_side_handler,
            opts = {
              -- streaming_handler = local_llm_streaming_handler,
              left = {
                focusable = false,
              },
            },
          },
          TestCode = {
            handler = tools.side_by_side_handler,
            prompt = [[Write some test cases for the following code, only return the test cases.
            Give the code content directly, do not use code blocks or other tags to wrap it.]],
            opts = {
              right = {
                title = " Test Cases ",
              },
            },
          },
          OptimCompare = {
            handler = tools.action_handler,
            opts = {
              fetch_key = function()
                return vim.env.LLM_KEY
              end,
              url = "https://api.deepseek.com/chat/completions",
              model = "deepseek-chat",
              api_type = "openai",
              max_tokens = 4096,
              language = "Chinese",
            },
          },

          DocString = {
            prompt = [[You are an AI programming assistant. You need to write a really good docstring that follows a best practice for the given language.

Your core tasks include:
- parameter and return types (if applicable).
- any errors that might be raised or returned, depending on the language.

You must:
- Place the generated docstring before the start of the code.
- Follow the format of examples carefully if the examples are provided.
- Use Markdown formatting in your answers.
- Include the programming language name at the start of the Markdown code blocks.]],
            handler = tools.action_handler,
            opts = {
              fetch_key = function()
                return vim.env.LLM_KEY
              end,
              url = "https://api.deepseek.com/chat/completions",
              model = "deepseek-chat",
              api_type = "openai",
              max_tokens = 4096,
              only_display_diff = true,
              templates = {
                lua = [[- For the Lua language, you should use the LDoc style.
- Start all comment lines with "---".
]],
              },
            },
          },
          Translate = {
            handler = tools.qa_handler,
            opts = {
              fetch_key = function()
                return vim.env.LLM_KEY
              end,
              url = "https://api.deepseek.com/chat/completions",
              model = "deepseek-chat",
              api_type = "openai",
              max_tokens = 4096,

              component_width = "60%",
              component_height = "50%",
              query = {
                title = " 󰊿 Trans ",
                hl = { link = "Define" },
              },
              input_box_opts = {
                size = "15%",
                win_options = {
                  winhighlight = "Normal:Normal,FloatBorder:FloatBorder",
                },
              },
              preview_box_opts = {
                size = "85%",
                win_options = {
                  winhighlight = "Normal:Normal,FloatBorder:FloatBorder",
                },
              },
            },
          },

          -- check siliconflow's balance
          -- UserInfo = {
          --   handler = function()
          --     local key = os.getenv("LLM_KEY")
          --     local res = tools.curl_request_handler(
          --       "https://api.siliconflow.cn/v1/user/info",
          --       { "GET", "-H", string.format("'Authorization: Bearer %s'", key) }
          --     )
          --     if res ~= nil then
          --       print("balance: " .. res.data.balance)
          --     end
          --   end,
          -- },
          WordTranslate = {
            handler = tools.flexi_handler,
            prompt = [[You are a translation expert. Your task is to translate all the text provided by the user into Chinese.

          NOTE:
          - All the text input by the user is part of the content to be translated, and you should ONLY FOCUS ON TRANSLATING THE TEXT without performing any other tasks.
          - RETURN ONLY THE TRANSLATED RESULT.]],
            -- prompt = "Translate the following text to English, please only return the translation",
            opts = {
              fetch_key = function()
                return vim.env.LLM_KEY
              end,
              url = "https://api.deepseek.com/chat/completions",
              model = "deepseek-chat",
              api_type = "openai",
              -- args = [=[return string.format([[curl %s -N -X POST -H "Content-Type: application/json" -H "Authorization: Bearer %s" -d '%s']], url, LLM_KEY, vim.fn.json_encode(body))]=],
              exit_on_move = true,
              enter_flexible_window = false,
            },
          },
          CodeExplain = {
            handler = tools.flexi_handler,
            prompt = "Explain the following code, please only return the explanation, and answer in Chinese",
            opts = {
              fetch_key = function()
                return vim.env.LLM_KEY
              end,
              url = "https://api.deepseek.com/chat/completions",
              model = "deepseek-chat",
              api_type = "openai",
              enter_flexible_window = true,
            },
          },
          CommitMsg = {
            handler = tools.flexi_handler,
            prompt = function()
              -- Source: https://andrewian.dev/blog/ai-git-commits
              return string.format(
                [[You are an expert at following the Conventional Commit specification. Given the git diff listed below, please generate a commit message for me:
      1. First line: conventional commit format (type: concise description) (remember to use semantic types like feat, fix, docs, style, refactor, perf, test, chore, etc.)
      2. Optional bullet points if more context helps:
        - Keep the second line blank
        - Keep them short and direct
        - Focus on what changed
        - Always be terse
        - Don't overly explain
        - Drop any fluffy or formal language

      Return ONLY the commit message - no introduction, no explanation, no quotes around it.

      Examples:
      feat: add user auth system

      - Add JWT tokens for API auth
      - Handle token refresh for long sessions

      fix: resolve memory leak in worker pool

      - Clean up idle connections
      - Add timeout for stale workers

      Simple change example:
      fix: typo in README.md

      Very important: Do not respond with any of the examples. Your message must be based off the diff that is about to be provided, with a little bit of styling informed by the recent commits you're about to see.

      Based on this format, generate appropriate commit messages. Respond with message only. DO NOT format the message in Markdown code blocks, DO NOT use backticks:

      ```diff
      %s
      ```
      ]],
                vim.fn.system("git diff --no-ext-diff --staged")
              )
            end,

            opts = {
              fetch_key = function()
                return vim.env.LLM_KEY
              end,
              url = "https://api.deepseek.com/chat/completions",
              model = "deepseek-chat",
              api_type = "openai",
              enter_flexible_window = true,
              apply_visual_selection = false,
              win_opts = {
                relative = "editor",
                position = "50%",
              },
              accept = {
                mapping = {
                  mode = "n",
                  keys = "<cr>",
                },
                action = function()
                  local contents = vim.api.nvim_buf_get_lines(0, 0, -1, true)
                  vim.api.nvim_command(string.format('!git commit -m "%s"', table.concat(contents, '" -m "')))

                  -- just for lazygit
                  vim.schedule(function()
                    vim.api.nvim_command("LazyGit")
                  end)
                end,
              },
            },
          },
          Ask = {
            handler = tools.disposable_ask_handler,
            opts = {
              position = {
                row = 2,
                col = 0,
              },
              title = " Ask ",
              inline_assistant = true,
              language = "Chinese",
              url = "https://api.deepseek.com/chat/completions",
              model = "deepseek-chat",
              api_type = "openai",
              fetch_key = function()
                return vim.env.LLM_KEY
              end,
              display = {
                mapping = {
                  mode = "n",
                  keys = { "d" },
                },
                action = nil,
              },
              accept = {
                mapping = {
                  mode = "n",
                  keys = { "Y", "y" },
                },
                action = nil,
              },
              reject = {
                mapping = {
                  mode = "n",
                  keys = { "N", "n" },
                },
                action = nil,
              },
              close = {
                mapping = {
                  mode = "n",
                  keys = { "<esc>" },
                },
                action = nil,
              },
            },
          },
          AttachToChat = {
            handler = tools.attach_to_chat_handler,
            opts = {
              is_codeblock = true,
              inline_assistant = true,
              language = "Chinese",
            },
          },

        FormulaRecognition = {
          handler = "images_handler",
          prompt = "Please convert the formula in the image to LaTeX syntax, and only return the syntax of the formula.",
          opts = {
            url = "https://api.siliconflow.cn/v1/chat/completions",
            model = "Qwen/Qwen2.5-VL-72B-Instruct",
            fetch_key = vim.env.SILICONFLOW_TOKEN,
            api_type = "openai",
            -- 图片选择器（保持不变）
            picker = {
              cmd = "fd . ~/ScreenShots/ | xargs -d '\n' ls -t | fzf --no-preview",
              mapping = {
                mode = "i",
                keys = "<C-f>",
              },
            },
            use_base64 = true,
            detail = "low", -- 低精度提升速度，公式识别足够用
            max_tokens = 8096,
            temperature = 0.0, -- 公式识别用0温度保证准确性
          },
        },
          Completion = {
            handler = tools.completion_handler,
            opts = {
              -------------------------------------------------
              ---                  ollma
              -------------------------------------------------
              -- -- url = "http://localhost:11434/api/generate",
              -- url = "http://localhost:11434/v1/completions",
              -- model = "qwen2.5-coder:1.5b",
              -- api_type = "ollma",

              -------------------------------------------------
              ---                 deepseek
              -------------------------------------------------
              url = "https://api.deepseek.com/beta/completions",
              model = "deepseek-chat",
              api_type = "deepseek",
              fetch_key = function()
                return vim.env.LLM_KEY
              end,

              -------------------------------------------------
              ---                 codeium
              -------------------------------------------------
              -- api_type = "codeium",
              -- style = "virtual_text",

              n_completions = 1,
              context_window = 512,
              max_tokens = 256,
              filetypes = { sh = false },
              default_filetype_enabled = true,
              auto_trigger = true,
              style = "blink.cmp",
              -- style = "nvim-cmp",
              -- style = "virtual_text",
              keymap = {
                toggle = {
                  mode = "n",
                  keys = "<leader>llcp",
                },
                virtual_text = {
                  accept = {
                    mode = "i",
                    keys = "<A-a>",
                  },
                  next = {
                    mode = "i",
                    keys = "<A-n>",
                  },
                  prev = {
                    mode = "i",
                    keys = "<A-p>",
                  },
                },
              },
            },
          },
        },
      })

    end,
    keys = {
      { "<leader>llmc", mode = "n", "<cmd>LLMSessionToggle<cr>", desc = " Toggle LLM Chat" },
      { "<leader>llmp", mode = "n", "<cmd>LLMAppHandler FormulaRecognition<cr>", desc = " FormulaRecognition" },
      { "<leader>llms", mode = "x", "<cmd>LLMAppHandler WordTranslate<cr>", desc = " Word Translate" },
      { "<leader>llme", mode = "v", "<cmd>LLMAppHandler CodeExplain<cr>", desc = " Explain the Code" },
      { "<leader>llmt", mode = "n", "<cmd>LLMAppHandler Translate<cr>", desc = " AI Translator" },
      { "<leader>llmC", mode = "x", "<cmd>LLMAppHandler TestCode<cr>", desc = " Generate Test Cases" },
      { "<leader>llmo", mode = "x", "<cmd>LLMAppHandler OptimCompare<cr>", desc = " Optimize the Code" },
      -- { "<leader>llau", mode = "n", "<cmd>LLMAppHandler UserInfo<cr>", desc = " Check Account Information" },
      { "<leader>llmg", mode = "n", "<cmd>LLMAppHandler CommitMsg<cr>", desc = " Generate AI Commit Message" },
      { "<leader>llmd", mode = "v", "<cmd>LLMAppHandler DocString<cr>", desc = " Generate a Docstring" },
      { "<leader>llmk", mode = { "v", "n" }, "<cmd>LLMAppHandler Ask<cr>", desc = " Ask LLM" },
      { "<leader>llma", mode = { "v", "n" }, "<cmd>LLMAppHandler AttachToChat<cr>", desc = " Ask LLM (multi-turn)" },
      -- { "<leader>llao", mode = "x", "<cmd>LLMAppHandler OptimizeCode<cr>" },
      -- { "<leader>llae", mode = "v", "<cmd>LLMSelectedTextHandler 请解释下面这段代码<cr>" },
      -- { "<leader>llts", mode = "x", "<cmd>LLMSelectedTextHandler 英译汉<cr>" },
    },
  },
  "saghen/blink.cmp",
  optional = true,
  dependencies = { "saghen/blink.compat", "Kurama622/llm.nvim" },
  opts = {
    completion = {
      menu = {
        scrollbar = false,
        border = "rounded",
        winhighlight = "Normal:BlinkCmpMenu,FloatBorder:FloatBorder",

        draw = {
          components = {
            kind_icon = {
              ellipsis = false,
              text = function(ctx)
                local mini_icons = require("mini.icons")
                local kind_name = ctx.item.kind_name or "lsp"

                local success, kind_icon, _, _ = pcall(mini_icons.get, kind_name, ctx.kind)
                if not success then
                  kind_icon = " "
                end
                return kind_icon
              end,

              -- Optionally, you may also use the highlights from mini.icons
              highlight = function(ctx)
                local mini_icons = require("mini.icons")
                local kind_name = ctx.item.kind_name or "lsp"

                local success, _, hl, _ = pcall(mini_icons.get, kind_name, ctx.kind)
                if not success then
                  hl = "BlinkCmpKindSnippet"
                end
                return hl
              end,
            },
          },
        },
      },
      documentation = { window = { border = "rounded" } },
      trigger = {
        prefetch_on_insert = false,
        show_on_blocked_trigger_characters = {},
      },
    },

    keymap = {
      ["<C-y>"] = {
        function(cmp)
          cmp.show({ providers = { "llm" } })
        end,
      },
    },

    sources = {
      -- if you want to use auto-complete
      default = { "llm" },
      providers = {
        llm = {
          name = "LLM",
          module = "llm.common.completion.frontends.blink",
          timeout_ms = 10000,
          score_offset = 100,
          async = true,
        },
      },
    },
  },

  -- 17. trans
 {
    "JuanZoran/Trans.nvim",
    build = function () require'Trans'.install() end,
    keys = {
    -- 可以换成其他你想映射的键
        { 'mm', mode = { 'n', 'x' }, '<Cmd>Translate<CR>', desc = '󰊿 Translate' },
        { 'mk', mode = { 'n', 'x' }, '<Cmd>TransPlay<CR>', desc = ' Auto Play' },
        -- 目前这个功能的视窗还没有做好，可以在配置里将view.i改成hover
        { 'mi', '<Cmd>TranslateInput<CR>', desc = '󰊿 Translate From Input' },
    },
    dependencies = { 'kkharji/sqlite.lua', },
    opts = {
        -- your configuration there
    }
  },

  -- 16. dadbod-ui
  {
    'kristijanhusak/vim-dadbod-ui',
    dependencies = {
      { 'tpope/vim-dadbod', lazy = true },
      { 'kristijanhusak/vim-dadbod-completion', ft = { 'sql', 'mysql', 'plsql' }, lazy = true }, -- Optional
    },
    cmd = {
      'DBUI',
      'DBUIToggle',
      'DBUIAddConnection',
      'DBUIFindBuffer',
    },
    init = function()
      -- Your DBUI configuration
      vim.g.db_ui_use_nerd_fonts = 1
    end,
  },

  -- 15. dab-ui
  {
    "mfussenegger/nvim-dap",
    dependencies = {
      "rcarriga/nvim-dap-ui",
      "theHamsta/nvim-dap-virtual-text",
      "nvim-neotest/nvim-nio",
    },

    -- 快捷键映射
    keys = {
      { "<leader>dB", function() require("dap").set_breakpoint(vim.fn.input('Breakpoint condition: ')) end, desc = "Breakpoint Condition" },
      { "<leader>db", function() require("dap").toggle_breakpoint() end, desc = "Toggle Breakpoint" },
      { "<leader>dc", function() require("dap").continue() end, desc = "Run/Continue" },
      { "<leader>dC", function() require("dap").run_to_cursor() end, desc = "Run to Cursor" },
      { "<leader>di", function() require("dap").step_into() end, desc = "Step Into" },
      { "<leader>do", function() require("dap").step_out() end, desc = "Step Out" },
      { "<leader>dO", function() require("dap").step_over() end, desc = "Step Over" },
      { "<leader>dt", function() require("dap").terminate() end, desc = "Terminate" },
      -- 一键编译并调试 (修复版)
      { "<leader>dd", function()
        local filetype = vim.bo.filetype
        if not (filetype == 'c' or filetype == 'cpp') then
          vim.notify('Not a C/C++ file!', vim.log.levels.WARN)
          return
        end

        -- 固定你的项目目录 (核心修复)
        local proj_dir = "/data/data/com.termux/files/home/.yuoek/code"
        local filename = vim.fn.expand('%:t')  -- 仅文件名 test.c
        local src_path = proj_dir .. "/" .. filename
        local exe_path = proj_dir .. "/" .. vim.fn.expand('%:t:r')

        -- 强制使用 GCC 编译，关闭优化
        local compile_cmd = filetype == 'c' 
          and string.format('gcc -g -O0 "%s" -o "%s"', src_path, exe_path)
          or string.format('g++ -g -O0 "%s" -o "%s"', src_path, exe_path)

        -- 执行编译
        local compile_result = vim.fn.system(compile_cmd)
        if vim.v.shell_error ~= 0 then
          vim.notify('Compilation failed:\n' .. compile_result, vim.log.levels.ERROR)
          return
        end

        -- 启动调试，强制指定源码目录
        require('dap').run({
          type = 'gdb',
          request = 'launch',
          name = 'Launch C/C++ (Fixed)',
          program = exe_path,
          cwd = proj_dir,
          stopOnEntry = false,
          args = {},
          setupCommands = {
            -- 强制绑定你的源码目录，彻底解决 No source file 问题
            { text = "directory " .. proj_dir, ignoreFailures = false },
            { text = "-enable-pretty-printing", ignoreFailures = false },
          },
        })
      end, desc = "Debug current C/C++ file" },
    },

    config = function()
      local dap = require("dap")

      -- --------------------------
      -- Python 调试配置 (Termux)
      -- --------------------------
      dap.configurations.python = {
        {
          type = "python",
          request = "launch",
          name = "Launch file",
          program = "${file}",
          pythonPath = function()
            return "/data/data/com.termux/files/usr/bin/python3"
          end,
        },
      }

      dap.adapters.python = {
        type = "executable",
        command = "python3",
        args = { "-m", "debugpy.adapter" },
      }

      -- --------------------------
      -- C/C++ 调试配置 (gdb, Termux)
      -- --------------------------
      dap.adapters.gdb = {
        type = "executable",
        command = "gdb",
        args = { "-q", "-i", "dap" }, -- 静默启动，去除版权信息
        name = "gdb",
      }

      -- 手动启动调试的配置 (同样加入了路径修复)
      dap.configurations.c = {
        {
          name = "Launch (Fixed Path)",
          type = "gdb",
          request = "launch",
          program = function()
            return vim.fn.input("Path to executable: ", "/data/data/com.termux/files/home/.yuoek/code", "file")
          end,
          cwd = "/data/data/com.termux/files/home/.yuoek/code",
          stopOnEntry = false,
          args = {},
          setupCommands = {
            { text = "directory /data/data/com.termux/files/home/.yuoek/code", ignoreFailures = false },
            { text = "-enable-pretty-printing", ignoreFailures = false },
          },
        },
      }

      dap.configurations.cpp = dap.configurations.c

      -- --------------------------
      -- 高亮与图标
      -- --------------------------
      vim.api.nvim_set_hl(0, "DapStoppedLine", { default = true, link = "Visual" })

      local signs = {
        Breakpoint = "",
        BreakpointCondition = "",
        BreakpointRejected = "",
        LogPoint = "",
        Stopped = "",
      }
      for name, sign in pairs(signs) do
        vim.fn.sign_define(
          "Dap" .. name,
          { text = sign, texthl = name == "Stopped" and "DiagnosticSignInfo" or "DiagnosticSignError", linehl = "", numhl = "" }
        )
      end
    end,
  },

  {
    "rcarriga/nvim-dap-ui",
    dependencies = { "nvim-neotest/nvim-nio" },
    keys = {
      { "<leader>du", function() require("dapui").toggle({}) end, desc = "Dap UI" },
      { "<leader>de", function() require("dapui").eval() end, desc = "Eval", mode = {"n", "x"} },
    },
    config = function(_, opts)
      local dap = require("dap")
      local dapui = require("dapui")
      dapui.setup(opts)
      
      dap.listeners.after.event_initialized["dapui_config"] = function()
        dapui.open({})
      end
      dap.listeners.before.event_terminated["dapui_config"] = function()
        dapui.close({})
      end
      dap.listeners.before.event_exited["dapui_config"] = function()
        dapui.close({})
      end
    end,
  },

  {
    "theHamsta/nvim-dap-virtual-text",
    opts = {
      show_type = true,
    },
  },

  -- 14. diffview
  -- TODO

  -- 13. browser

  {                                                                         
    'claydugo/browsher.nvim',                                               
    event = "VeryLazy",                                                     
    config = function()                                                     
      -- Specify empty to use below default options                         
      require('browsher').setup()                                           
    end                                                                     
  },                                                                       

  -- 12. lazygit.nvim
  {                                                                  
      "kdheepak/lazygit.nvim",                                              
      lazy = true,                                                          
      cmd = {                                                               
          "LazyGit",                                                        
          "LazyGitConfig",                                                  
          "LazyGitCurrentFile",                                             
          "LazyGitFilter",                                                  
          "LazyGitFilterCurrentFile",                                       
      },                                                                    
      -- optional for floating window border decoration                     
      dependencies = {                                                      
          "nvim-lua/plenary.nvim",                                          
      },                                                                    
      -- setting the keybinding for LazyGit with 'keys' is recommended in   
      -- order to load the plugin when the command is run for the first time
      keys = {                                                              
          { "<leader>lg", "<cmd>LazyGit<cr>", desc = "LazyGit" }            
      }                                                                     
  },                                                                         

  -- 11. vimtex
 {
  "lervag/vimtex",
    lazy = false,     -- we don't want to lazy load VimTeX
    -- tag = "v2.15", -- uncomment to pin to a specific release
    init = function()
      -- VimTeX configuration goes here, e.g.
      vim.g.vimtex_view_method = "default"
    end
  },

  -- 10. lilypond
  { 
  "martineausimon/nvim-lilypond-suite",
  event = "VeryLazy",
    opts = {
      -- edit config here (see "Customize default settings" in wiki)
    }
  },

  -- 9. url-open
  {
      "sontungexpt/url-open",
      event = "VeryLazy",
      cmd = "URLOpenUnderCursor",
      config = function()
          local status_ok, url_open = pcall(require, "url-open")
          if not status_ok then
              return
          end
          url_open.setup ({})
      end,
  },

  -- 8. veen
  {
    "jbyuki/venn.nvim",
    lazy = true,
    keys = {
      -- 移除范围标记，直接绑定 VBox 命令（适配 Termux 环境）
      { "<leader>ve", ":VBox<CR>", desc = "Draw Venn box", mode = "x", silent = true },
      -- 普通模式画线快捷键（保留）
      { "J", "<C-v>j:VBox<CR>", mode = "n", silent = true },
      { "K", "<C-v>k:VBox<CR>", mode = "n", silent = true },
      { "H", "<C-v>h:VBox<CR>", mode = "n", silent = true },
      { "L", "<C-v>l:VBox<CR>", mode = "n", silent = true },
    },
    config = function()
      -- 强制开启自由光标，确保选中区域可超出文本长度
      vim.api.nvim_create_autocmd("BufEnter", {
        callback = function()
          vim.wo.virtualedit = "all"
        end,
      })
    end,
  },

  -- 7. screenkey
  {
    "NStefan002/screenkey.nvim",
      lazy = false,
      version = "*", -- or branch = "main", to use the latest commit
  },

  -- 6. markdown-toc
  {
  "hedyhli/markdown-toc.nvim",
    ft = "markdown",  -- Lazy load on markdown filetype
    cmd = { "Mtoc" }, -- Or, lazy load on "Mtoc" command
    opts = {
      -- Your configuration here (optional)
    },
  },

  -- 5. flash
  {
  "folke/flash.nvim",
    event = "VeryLazy",
    ---@type Flash.Config
    opts = {},
    keys = {
      { "s", mode = { "n", "x", "o" }, function() require("flash").jump() end, desc = "Flash" },
      { "S", mode = { "n", "x", "o" }, function() require("flash").treesitter() end, desc = "Flash Treesitter" },
      { "r", mode = "o", function() require("flash").remote() end, desc = "Remote Flash" },
      { "R", mode = { "o", "x" }, function() require("flash").treesitter_search() end, desc = "Treesitter Search" },
      { "<c-s>", mode = { "c" }, function() require("flash").toggle() end, desc = "Toggle Flash Search" },
    },
  },

  -- 4. yazi
  --@type LazySpec
  {
    "mikavilpas/yazi.nvim",
    version = "*", -- use the latest stable version
    event = "VeryLazy",
    dependencies = {
      { "nvim-lua/plenary.nvim", lazy = true },
    },
    keys = {
      -- 👇 in this section, choose your own keymappings!
      {
        "<leader>-",
        mode = { "n", "v" },
        "<cmd>Yazi<cr>",
        desc = "Open yazi at the current file",
      },
      {
        -- Open in the current working directory
        "<leader>cw",
        "<cmd>Yazi cwd<cr>",
        desc = "Open the file manager in nvim's working directory",
      },
      {
        "<c-up>",
        "<cmd>Yazi toggle<cr>",
        desc = "Resume the last yazi session",
      },
    },
    ---@type YaziConfig | {}
    opts = {
      -- if you want to open yazi instead of netrw, see below for more info
      open_for_directories = false,
      keymaps = {
        show_help = "<f1>",
      },
    },
    -- 👇 if you use `open_for_directories=true`, this is recommended
    init = function()
      -- mark netrw as loaded so it's not loaded at all.
      --
      -- More details: https://github.com/mikavilpas/yazi.nvim/issues/802
      vim.g.loaded_netrwPlugin = 1
    end,
  },
  
  -- 3. eskk
  {
    "vim-skk/eskk.vim",
    lazy = false,
    dependencies = { "delphinus/skkeleton_indicator.nvim" },
    config = function()
      -- 本地词库路径，避免网络问题
      local eskk_dir = vim.fn.expand("~/Yu/db/eskk")
      vim.fn.mkdir(eskk_dir, "p")
      vim.g["eskk#directory"] = eskk_dir
      vim.g["eskk#dictionary"] = {
        path = eskk_dir .. "/my_jisyo",
        sorted = 1,
        encoding = "utf-8",
      }
      -- 禁用自动下载大词库，手动准备更可靠
      vim.g["eskk#large_dictionary"] = {
        path = eskk_dir .. "/SKK-JISYO.L", -- 需手动下载：https://skk-dev.github.io/dict/SKK-JISYO.L
        sorted = 1,
        encoding = "euc-jp",
      }
      vim.g["eskk#user_dictionary"] = {
        path = eskk_dir .. "/user_jisyo",
        sorted = 0,
        encoding = "utf-8",
      }

      -- 基础设置
      vim.g["eskk#initial_mode"] = "hira"
      vim.g["eskk#keep_state"] = 0
      vim.g["eskk#egg_like_newline"] = 1
      vim.g["eskk#show_annotation"] = 1

      -- 冲突率低的快捷键：Insert/Command模式按<C-j>切换
      vim.keymap.set({"i", "c"}, "<C-\\>", "<Plug>(eskk:toggle)", { noremap = false, silent = true })

      -- 状态指示器
      if pcall(require, "skkeleton_indicator") then
        require("skkeleton_indicator").setup()
      end
    end,
  },

  -- 2. cmp-english
  {
    "hrsh7th/nvim-cmp",
    version = false,
    event = "InsertEnter",
    dependencies = {
      "hrsh7th/cmp-nvim-lsp",
      "hrsh7th/cmp-buffer",
      "hrsh7th/cmp-path",
      "hrsh7th/cmp-cmdline",
      "uga-rosa/cmp-dictionary",
      "hrsh7th/cmp-emoji", -- 这里加了 emoji
      "L3MON4D3/LuaSnip",
      "saadparwaiz1/cmp_luasnip",
      "rafamadriz/friendly-snippets",
    },

    config = function()
      local cmp = require("cmp")
      local luasnip = require("luasnip")

      -- 字典配置
      local dict = {
        ["*"] = { vim.fn.expand("~/Yu/db/english-words/words.txt") },
        ft = {
          lua = { vim.fn.expand("~/Yu/db/english-words/words.txt") },
          python = { vim.fn.expand("~/Yu/db/english-words/words.txt") },
        },
      }

      require("cmp_dictionary").setup({
        paths = dict["*"],
        exact_length = 2,
      })

      vim.api.nvim_create_autocmd("BufEnter", {
        pattern = "*",
        callback = function()
          local paths = dict.ft[vim.bo.filetype] or {}
          vim.list_extend(paths, dict["*"])
          require("cmp_dictionary").setup({ paths = paths })
        end,
      })

      local opts = {
        completion = {
          completeopt = "menu,menuone,noselect",
        },
        snippet = {
          expand = function(args)
            luasnip.lsp_expand(args.body)
          end,
        },
        window = {
          completion = cmp.config.window.bordered({
            border = "rounded",
            winhighlight = "Normal:NormalFloat,FloatBorder:FloatBorder,CursorLine:PmenuSel,Search:None",
          }),
          documentation = cmp.config.window.bordered(),
        },
        mapping = cmp.mapping.preset.insert({
          ["<C-n>"] = cmp.mapping.select_next_item({ behavior = cmp.SelectBehavior.Insert }),
          ["<C-p>"] = cmp.mapping.select_prev_item({ behavior = cmp.SelectBehavior.Insert }),
          ["<C-b>"] = cmp.mapping.scroll_docs(-4),
          ["<C-f>"] = cmp.mapping.scroll_docs(4),
          ["<C-Space>"] = cmp.mapping.complete(),
          ["<C-e>"] = cmp.mapping.abort(),
          ["<CR>"] = cmp.mapping.confirm({ select = true }),
          ["<Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then
              cmp.select_next_item()
            elseif luasnip.expand_or_jumpable() then
              luasnip.expand_or_jump()
            else
              fallback()
            end
          end, { "i", "s" }),
          ["<S-Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then
              cmp.select_prev_item()
            elseif luasnip.jumpable(-1) then
              luasnip.jump(-1)
            else
              fallback()
            end
          end, { "i", "s" }),
        }),
        sources = cmp.config.sources({
          { name = "nvim_lsp" },
          { name = "luasnip" },
          { name = "buffer" },
          { name = "path" },
          { name = "dictionary", keyword_length = 2 },
          { name = "emoji" }, -- 启用 emoji
        }),
        experimental = {
          ghost_text = true,
        },
      }

      cmp.setup(opts)

      cmp.setup.cmdline(":", {
        mapping = cmp.mapping.preset.cmdline(),
        sources = cmp.config.sources({
          { name = "path" },
          { name = "cmdline" },
        }),
      })
    end,
  },

  -- 1. render-markdown
  {
      "MeanderingProgrammer/render-markdown.nvim",
      lazy = false,
      dependencies = {
        {
          "nvim-treesitter/nvim-treesitter",
          branch = "main",
          config = function()
            vim.api.nvim_create_autocmd("FileType", {
              pattern = { "llm", "markdown" },
              callback = function()
                vim.treesitter.start(0, "markdown")
              end,
            })
          end,
        },
        "nvim-mini/mini.icons",
      }, -- if you use standalone mini plugins
      ft = { "markdown", "llm" },

      config = function()
        require("render-markdown").setup({
          restart_highlighter = true,
          heading = {
            enabled = true,
            sign = false,
            position = "overlay", -- inline | overlay
            icons = { "󰎤 ", "󰎧 ", "󰎪 ", "󰎭 ", "󰎱 ", "󰎳 " },
            signs = { "󰫎 " },
            width = "block",
            left_margin = 0,
            left_pad = 0,
            right_pad = 0,
            min_width = 0,
            border = false,
            border_virtual = false,
            border_prefix = false,
            above = "▄",
            below = "▀",
            backgrounds = {},
            foregrounds = {
              "RenderMarkdownH1",
              "RenderMarkdownH2",
              "RenderMarkdownH3",
              "RenderMarkdownH4",
              "RenderMarkdownH5",
              "RenderMarkdownH6",
            },
          },
          dash = {
            enabled = true,
            icon = "─",
            width = 0.5,
            left_margin = 0.5,
            highlight = "RenderMarkdownDash",
          },
          code = { style = "normal" },
        })
      end,
    }
}
