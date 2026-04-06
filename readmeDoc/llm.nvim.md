
  English |                                                                   
    简体中文                                                                  
  --------                                                                    
                                                                              
  | [!IMPORTANT]                                                              
  | A large language model(LLM) plugin that allows you to interact with LLM in
  | Neovim.                                                                   
  |                                                                           
  | 1. Supports any LLM, such as GPT, GLM, Kimi, DeepSeek, Gemini, Qwen or    
  | local LLMs (such as ollama).                                              
  | 2. Allows you to define your own AI tools, with different tools able to   
  use                                                                         
  | different models.                                                         
  | 3. Most importantly, you can use free models provided by any platform     
  (such                                                                       
  | as Copilot, GitHub models, SiliconFlow, openrouter, Cloudflare or other   
  | platforms).                                                               
                                                                              
  | [!NOTE]                                                                   
  | The configurations of different LLMs (such as **ollama**, **deepseek**),  
  UI                                                                          
  | configurations, and AI tools (including **code completion**) should be    
  | checked in the examples                                                   
  | https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples first. 
  | Here you will find most of the information you want to know. Additionally,
  | before using the plugin, you should ensure that your LLM_KEY is **valid** 
  | and that the environment variable is in effect.                           
  |                                                                           
  | Additionally, you should also take a look at wiki                         
  | https://github.com/Kurama622/llm.nvim/wiki and docs                       
  | https://raw.githubusercontent.com/Kurama622/llm.nvim/main/docs/.          
                                                                              
  # Contents                                                                  
                                                                              
  • Screenshots                                                               
      • Chat                                                                  
      • Quick Translation                                                     
      • Explain Code                                                          
      • Ask                                                                   
      • Attach To Chat                                                        
      • Optimize Code                                                         
      • Generate Test Cases                                                   
      • AI Translation                                                        
      • Image Recognition                                                     
      • Generate Git Commit Message                                           
      • Generate Doc String                                                   
      • Web Search                                                            
      • Diagnostic                                                            
      • Lsp                                                                   
  • Installation                                                              
      • Dependencies                                                          
      • Preconditions                                                         
          • Websites of different AI platforms                                
      • Minimal installation example                                          
  • Configuration                                                             
      • Commands                                                              
      • Model Parameters                                                      
      • keymaps                                                               
      • Tool                                                                  
      • UI                                                                    
      • Custom parsing function                                               
  • TODO List                                                                 
  • Author's configuration                                                    
  • Acknowledgments                                                           
      • Special thanks                                                        
                                                                              
                                                                              
  ## Screenshots                                                              
                                                                              
  ### Chat                                                                    
                                                                              
  models                                                                      
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/chat/ |  
  UI https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/ui/   
                                                                              
  **Press **?** can display the shortcut key help window**                    
                                                                              
  • Float-UI                                                                  
                                                                              
  • Split-UI                                                                  
                                                                              
  ### Quick Translation                                                       
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/ai-      
  tools/Word-Translate/config.lua                                             
                                                                              
  enable_cword_context = true: Translate the text under the cursor in normal  
  mode.                                                                       
                                                                              
  ### Explain Code                                                            
                                                                              
  Streaming output                                                            
  https://raw.githubusercontent.com/Kurama622/llm.                            
  nvim/main/examples/chat/deepseek/config.lua#L52                             
  | Non-streaming output                                                      
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/ai-      
  tools/Code-Explain/config.lua                                               
                                                                              
  ### Ask                                                                     
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/ai-      
  tools/Ask/config.lua                                                        
                                                                              
  | One-time, no history retained.                                            
                                                                              
  You can configure inline_assistant                                          
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/ai-      
  tools/Ask/config.lua to decide whether to display diffs (default: show by   
  pressing 'd').                                                              
                                                                              
  ### Attach To Chat                                                          
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/ai-      
  tools/Attach-To-Chat/config.lua                                             
                                                                              
  You can configure inline_assistant                                          
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/ai-      
  tools/Attach-To-Chat/config.lua to decide whether to display diffs (default:
  show by pressing 'd').                                                      
                                                                              
  ### Optimize Code                                                           
                                                                              
  • **Display side by side** https://raw.githubusercontent.com/Kurama622/llm. 
  nvim/main/examples/ai-tools/Optimize-Code/config.lua                        
                                                                              
  • **Display in the form of a diff** https://raw.githubusercontent.          
  com/Kurama622/llm.nvim/main/examples/ai-tools/Optimize-Code-and-Display-    
  Diff/config.lua                                                             
                                                                              
  ### Generate Test Cases                                                     
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/ai-      
  tools/Generate-Test-Cases/config.lua                                        
                                                                              
  ### AI Translation                                                          
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/ai-      
  tools/AI-Translate/config.lua                                               
                                                                              
  ### Image Recognition                                                       
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/ai-      
  tools/Formula-Recognition/README.md                                         
                                                                              
  ### Generate Git Commit Message                                             
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/ai-      
  tools/AI-Commit-Messages/config.lua                                         
                                                                              
  ### Generate Doc String                                                     
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/ai-      
  tools/Generate-Docstring/config.lua                                         
                                                                              
  ### Web Search                                                              
  https://raw.githubusercontent.com/Kurama622/llm.                            
  nvim/main/docs/functions/README.md#web_search                               
                                                                              
  /buffer                                                                     
  https://raw.githubusercontent.com/Kurama622/llm.                            
  nvim/main/docs/functions/README.md#buffers                                  
  | /file                                                                     
  https://raw.githubusercontent.com/Kurama622/llm.                            
  nvim/main/docs/functions/README.md#files                                    
  | @web_search                                                               
  https://raw.githubusercontent.com/Kurama622/llm.                            
  nvim/main/docs/functions/README.md#web_search                               
                                                                              
  ### Diagnostic                                                              
                                                                              
  Both disposable_ask_handler, attach_to_chat_handler, side_by_side_handler   
  and action_handler can enable diagnostic features:                          
                                                                              
    diagnostic = { min = vim.diagnostic.severity.HINT },                      
    -- or                                                                     
    -- diagnostic = { vim.diagnostic.severity.WARN, vim.diagnostic.severity.  
  ERROR },                                                                    
    -- see `:h diagnostic-severity`                                           
                                                                              
  ### Lsp                                                                     
                                                                              
  | [!NOTE]                                                                   
  | New features, still in continuous iteration.                              
                                                                              
  Both disposable_ask_handler, attach_to_chat_handler, and action_handler can 
  enable lsp features:                                                        
                                                                              
    lsp = {                                                                   
      cpp = { methods = { "definition", "declaration" } },                    
      python = { methods = { "definition" } },                                
      lua = { methods = { "definition", "declaration" } },                    
                                                                              
      root_dir = { {'pyproject.toml', 'setup.py' }, ".git" },                 
    },                                                                        
                                                                              
  ⬆ back to top                                                               
                                                                              
  ## Installation                                                             
                                                                              
  ### Dependencies                                                            
                                                                              
  • curl                                                                      
  • fzf >= 0.37.0: Optional. Split style preview of session history and image 
  recognition tool image selection depends on fzf(The author's development    
  environment is 0.39.0)                                                      
  • render-markdown.nvim: Optional. Better Markdown preview depends on this   
  plugin.                                                                     
                                                                              
    {                                                                         
        "MeanderingProgrammer/render-markdown.nvim",                          
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
                                                                              
  ### Preconditions                                                           
                                                                              
  1. Register on the official website and obtain your API Key (Cloudflare     
  needs to obtain an additional account).                                     
  2. Set the LLM_KEY (Cloudflare needs to set an additional ACCOUNT)          
  environment variable in your zshrc or bashrc.                               
                                                                              
    export LLM_KEY=<Your API_KEY>                                             
    export ACCOUNT=<Your ACCOUNT> # just for cloudflare                       
                                                                              
  #### Websites of different AI platforms                                     
  Expand the table.                                                           
   Platform               | Link to obtain api key             | Note         
  ------------------------|------------------------------------|------------  
   Cloudflare             | https://dash.cloudflare.com/[1]    | You can      
                          |                                    | see all of   
                          |                                    | Cloudflare   
                          |                                    | 's models    
                          |                                    | here[2],     
                          |                                    | with the     
                          |                                    | ones         
                          |                                    | marked as    
                          |                                    | beta being   
                          |                                    | free         
                          |                                    | models.      
   ChatGLM(智谱清言)      | https://open.bigmodel.cn/[3]       |              
   Kimi(月之暗面)         | Moonshot AI 开放平台[4]            |              
   Github Models          | Github Token[5]                    |              
   siliconflow (硅基流动) | siliconflow[6]                     | You can      
                          |                                    | see all      
                          |                                    | models on    
                          |                                    | Siliconflo   
                          |                                    | w here[7],   
                          |                                    | and select   
                          |                                    | 'Only        
                          |                                    | Free' to     
                          |                                    | see all      
                          |                                    | free         
                          |                                    | models.      
   Deepseek               | https://platform.deepseek.com/api_ |              
                          | keys[8]                            |              
   Openrouter             | https://openrouter.ai/[9]          |              
   Chatanywhere           | https://api.chatanywhere.org/v1/oa | 200 free     
                          | uth/free/render[10]                | calls to     
                          |                                    | GPT-4o-      
                          |                                    | mini are     
                          |                                    | available    
                          |                                    | every day.   
                                                                              
   [1]: https://dash.cloudflare.com/ https://dash.cloudflare.com/             
   [2]: here https://developers.cloudflare.com/workers-ai/models/             
   [3]: https://open.bigmodel.cn/ https://open.bigmodel.cn/                   
   [4]: Moonshot AI 开放平台 https://login.moonshot.cn/?source=https%3A%2F%2F…
   [5]: Github Token https://github.com/settings/tokens                       
   [6]: siliconflow https://account.siliconflow.cn/login?redirect=https%3A%2F…
   [7]: here https://cloud.siliconflow.cn/models                              
   [8]: https://platform.deepseek.com/api_keys https://platform.deepseek.com/…
   [9]: https://openrouter.ai/ https://openrouter.ai/                         
  [10]: https://api.chatanywhere.org/v1/oauth/free/render https://api.chatany…
                                                                              
  **For local llms, Set **LLM_KEY** to **NONE** in your **zshrc** or          
  **bashrc**.**                                                               
                                                                              
  ⬆ back to top                                                               
                                                                              
  ### Minimal installation example                                            
                                                                              
  • lazy.nvim                                                                 
                                                                              
      {                                                                       
        "Kurama622/llm.nvim",                                                 
        dependencies = { "nvim-lua/plenary.nvim", "MunifTanjim/nui.nvim"},    
        cmd = { "LLMSessionToggle", "LLMSelectedTextHandler", "LLMAppHandler" 
  },                                                                          
        config = function()                                                   
          require("llm").setup({                                              
            url = "https://models.inference.ai.azure.com/chat/completions",   
            model = "gpt-4o-mini",                                            
            api_type = "openai"                                               
          })                                                                  
        end,                                                                  
        keys = {                                                              
          { "<leader>ac", mode = "n", "<cmd>LLMSessionToggle<cr>" },          
        },                                                                    
      }                                                                       
                                                                              
  • Mini.deps                                                                 
                                                                              
    require("mini.deps").setup()                                              
    MiniDeps.add({                                                            
            source = "Kurama622/llm.nvim",                                    
            depends = { "nvim-lua/plenary.nvim", "MunifTanjim/nui.nvim" },    
            cmd = { "LLMSessionToggle", "LLMSelectedTextHandler",             
  "LLMAppHandler" },                                                          
    })                                                                        
                                                                              
    require("llm").setup({                                                    
            url = "https://models.inference.ai.azure.com/chat/completions",   
            model = "gpt-4o-mini",                                            
            api_type = "openai"                                               
    })                                                                        
                                                                              
  Configure template                                                          
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/basic_template.lua
                                                                              
  ## Configuration                                                            
                                                                              
  ### Commands                                                                
                                                                              
   Cmd                    | Description                                       
  ------------------------|-------------------------------------------------  
   LLMSessionToggle       | Open/hide the Chat UI                             
   LLMSelectedTextHandler | Handle the selected text, the way it is           
                          | processed depends on the prompt words you input   
   LLMAppHandler          | Call AI tools                                     
                                                                              
  ### Model Parameters                                                        
  Expand the table.                                                           
   Parameter         | Description                         | Value            
  -------------------|-------------------------------------|----------------  
   url               | Model entpoint                      | String           
   model             | Model name                          | String           
   api_type          | Result parsing format               | workers-ai |     
                     |                                     | zhipu|openai |   
                     |                                     | ollama|deepsee   
                     |                                     | k | copilot      
                     |                                     | |lmstudio        
   timeout           | The maximum timeout for a response  | Number           
                     | (in seconds)                        |                  
   proxy             | Curl request proxy                  | String           
                     |                                     | (noproxy|<ip>:   
                     |                                     | <port>) | nil    
   fetch_key         | API key string or Function that     | Function |       
                     | returns the API key                 | String           
   max_tokens        | Limits the number of tokens         | Number           
                     | generated in a response.            |                  
   temperature       | From 0 to 1.The lower the number    | Number           
                     | is, the more deterministic the      |                  
                     | response will be.The higher the     |                  
                     | number is the more creative the     |                  
                     | response will be, but moe likely to |                  
                     | go off topic if it's too high       |                  
   top_p             | A threshold(From 0 to 1).The higher | Number           
                     | the threshold is the more diverse   |                  
                     | and the less repetetive the         |                  
                     | response will be.(But it could also |                  
                     | lead to less likely tokens which    |                  
                     | also means: off-topic responses.)   |                  
   enable_thinking   | Activate the model's deep thinking  | Boolean          
                     | ability (The model itself needs to  |                  
                     | ensure this feature.)               |                  
   thinking_budget   | The maximum length of the thinking  | Number           
                     | process only takes effect when      |                  
                     | enable_thinking is true.            |                  
   schema            | Function-calling required function  | Table            
                     | parameter description               |                  
   functions_tbl     | Function dict required for          | Table            
                     | Function-calling                    |                  
   keep_alive        | Maintain connection (usually for    | see              
                     | ollama)                             | keep_alive/OLL   
                     |                                     | AMA_KEEP_ALIVE   
                     |                                     | [1]              
   streaming_handler | Customize the parsing format of the | Function         
                     | streaming output                    |                  
   parse_handler     | Customize the parsing format for    | Function         
                     | non-streaming output                |                  
                                                                              
  [1]: keep_alive/OLLAMA_KEEP_ALIVE https://github.com/ollama/ollama/blob/c02…
                                                                              
  ### keymaps                                                                 
  Expand the table.                                                           
   Style       | Keyname      | Description   | Default: [mo… | Window        
  -------------|--------------|---------------|---------------|-------------  
   float       | Input:Submit | Submit your   | [i] ctrl+g    | Input         
               |              | question      |               |               
   float       | Input:Cancel | Cancel dialog | [i] ctrl+c    | Input         
               |              | response      |               |               
   float       | Input:Resend | Rerespond to  | [i] ctrl+r    | Input         
               |              | the dialog    |               |               
   float       | Input:Histor | Select the    | [i] ctrl+j    | Input         
               | yNext        | next session  |               |               
               |              | history       |               |               
   float       | Input:Histor | Select the    | [i] ctrl+k    | Input         
               | yPrev        | previous      |               |               
               |              | session       |               |               
               |              | history       |               |               
   float       | Input:Models | Select the    | [i]           | Input         
               | Next         | next model    | ctrl+shift+j  |               
   float       | Input:Models | Select the    | [i]           | Input         
               | Prev         | previous      | ctrl+shift+k  |               
               |              | model         |               |               
   split       | Output:Ask   | Open the      | [n] i         | Output        
               |              | input boxIn   |               |               
               |              | the normal    |               |               
               |              | mode of the   |               |               
               |              | input box,    |               |               
               |              | press Enter   |               |               
               |              | to submit     |               |               
               |              | your          |               |               
               |              | question)     |               |               
   split       | Output:Cance | Cancel dialog | [n] ctrl+c    | Output        
               | l            | response      |               |               
   split       | Output:Resen | Rerespond to  | [n] ctrl+r    | Output        
               | d            | the dialog    |               |               
   float/split | Session:Togg | Toggle        | [n]           | Input+Outpu   
               | le           | session       | <leader>ac    | t             
   float/split | Session:Clos | Close session | [n] <esc>     | float:        
               | e            |               |               | Input+Outpu   
               |              |               |               | tsplit:       
               |              |               |               | Output        
   float/split | Session:New  | Create a new  | [n] <C-n>     | float:        
               |              | session       |               | Input+Outpu   
               |              |               |               | tsplit:       
               |              |               |               | Output        
   float/split | Session:Mode | Open the      | [n] ctrl+m    | float: App    
               | ls           | model-list    |               | input         
               |              | window        |               | windowsplit   
               |              |               |               | : Output      
   split       | Session:Hist | Open the      | [n] ctrl+h    | Output        
               | ory          | history       |               |               
               |              | windowmove:   |               |               
               |              | same as fzf   |               |               
               |              | configuration |               |               
               |              | <cr>:         |               |               
               |              | select<esc>:  |               |               
               |              | close         |               |               
   float       | Focus:Input  | Jump from the | -             | Output        
               |              | output window |               |               
               |              | to the input  |               |               
               |              | window        |               |               
   float       | Focus:Output | Jump from the | -             | Input         
               |              | input window  |               |               
               |              | to the output |               |               
               |              | window        |               |               
   float       | PageUp       | Output Window | [n/i] Ctrl+b  | Input         
               |              | page up       |               |               
   float       | PageDown     | Output window | [n/i] Ctrl+f  | Input         
               |              | page down     |               |               
   float       | HalfPageUp   | Output Window | [n/i] Ctrl+u  | Input         
               |              | page up       |               |               
               |              | (half)        |               |               
   float       | HalfPageDown | Output window | [n/i] Ctrl+d  | Input         
               |              | page down     |               |               
               |              | (half)        |               |               
   float       | JumpToTop    | Jump to the   | [n] gg        | Input         
               |              | top (output   |               |               
               |              | window)       |               |               
   float       | JumpToBottom | Jump to the   | [n] G         | Input         
               |              | bottom        |               |               
               |              | (output       |               |               
               |              | window)       |               |               
                                                                              
  ### Tool                                                                    
                                                                              
   Handler name           | Description                                       
  ------------------------|-------------------------------------------------  
   side_by_side_handler   | Display results in two windows side by side       
   action_handler         | Display results in the source file in the form    
                          | of a diff                                         
   qa_handler             | AI for single-round dialogue                      
   flexi_handler          | Results will be displayed in a flexible window    
                          | (window size is automatically calculated based    
                          | on the amount of output text)                     
   disposable_ask_handler | Flexible questioning, you can choose a piece of   
                          | code to ask about, or you can ask directly (the   
                          | current buffer is the context)                    
   attach_to_chat_handler | Attach the selected content to the context and    
                          | ask a question.                                   
   completion_handler     | Code completion                                   
   curl_request_handler   | The simplest interaction between curl and LLM     
                          | is generally used to query account balance or     
                          | available model lists, etc.                       
                                                                              
  **Each handler's parameters can be referred to **here                       
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/docs/tools**.**   
                                                                              
  Examples can be seen AI Tools Configuration                                 
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/ai-tools/
                                                                              
  ### UI                                                                      
                                                                              
  See UI Configuration                                                        
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/examples/ui/ and  
  nui/popup                                                                   
  https://github.com/MunifTanjim/nui.nvim/blob/main/lua/nui/popup/README.md   
                                                                              
  ⬆ back to top                                                               
                                                                              
  ### Custom parsing function                                                 
                                                                              
  For streaming output, we use our custom streaming_handler; for AI tools that
  return output results in one go, we use our custom parse_handler.           
                                                                              
  Below is an example of ollama running llama3.2:1b.                          
  Expand the code.                                                            
    local function local_llm_streaming_handler(chunk, ctx, F)                 
      if not chunk then                                                       
        return ctx.assistant_output                                           
      end                                                                     
      local tail = chunk:sub(-1, -1)                                          
      if tail:sub(1, 1) ~= "}" then                                           
        ctx.line = ctx.line .. chunk                                          
      else                                                                    
        ctx.line = ctx.line .. chunk                                          
        local status, data = pcall(vim.json.decode, ctx.line)                 
        if not status or not data.message.content then                        
          return ctx.assistant_output                                         
        end                                                                   
        ctx.assistant_output = ctx.assistant_output .. data.message.content   
        F.WriteContent(ctx.bufnr, ctx.winid, data.message.content)            
        ctx.line = ""                                                         
      end                                                                     
      return ctx.assistant_output                                             
    end                                                                       
                                                                              
    local function local_llm_parse_handler(chunk)                             
      local assistant_output = chunk.message.content                          
      return assistant_output                                                 
    end                                                                       
                                                                              
    return {                                                                  
      {                                                                       
        "Kurama622/llm.nvim",                                                 
        dependencies = { "nvim-lua/plenary.nvim", "MunifTanjim/nui.nvim" },   
        cmd = { "LLMSessionToggle", "LLMSelectedTextHandler" },               
        config = function()                                                   
          require("llm").setup({                                              
            url = "http://localhost:11434/api/chat", -- your url              
            model = "llama3.2:1b",                                            
                                                                              
            streaming_handler = local_llm_streaming_handler,                  
            app_handler = {                                                   
              WordTranslate = {                                               
                handler = tools.flexi_handler,                                
                prompt = "Translate the following text to Chinese, please only
  return the translation",                                                    
                opts = {                                                      
                  parse_handler = local_llm_parse_handler,                    
                  exit_on_move = true,                                        
                  enter_flexible_window = false,                              
                },                                                            
              },                                                              
            }                                                                 
          })                                                                  
        end,                                                                  
        keys = {                                                              
          { "<leader>ac", mode = "n", "<cmd>LLMSessionToggle<cr>" },          
        },                                                                    
      }                                                                       
    }                                                                         
                                                                              
  ⬆ back to top                                                               
                                                                              
  ## TODO List                                                                
                                                                              
  todo-list https://github.com/Kurama622/llm.nvim/issues/44                   
                                                                              
  ⬆ back to top                                                               
                                                                              
  ## Author's configuration                                                   
                                                                              
  plugins/llm https://github.com/Kurama622/.lazyvim/blob/main/lua/plugins/llm 
                                                                              
  ## Acknowledgments                                                          
                                                                              
  We would like to express our heartfelt gratitude to the contributors of the 
  following open-source projects, whose code has provided invaluable          
  inspiration and reference for the development of llm.nvim:                  
                                                                              
  • olimorris/codecompanion.nvim https://github.com/olimorris/codecompanion.  
  nvim: Diff style and prompt.                                                
  • SmiteshP/nvim-navbuddy https://github.com/SmiteshP/nvim-navbuddy: UI.     
  • milanglacier/minuet-ai.nvim https://github.com/milanglacier/minuet-ai.    
  nvim: Code completions.                                                     
                                                                              
  ### Special thanks                                                          
                                                                              
  ACKNOWLEDGMENTS                                                             
  https://raw.githubusercontent.com/Kurama622/llm.nvim/main/ACKNOWLEDGMENTS.md

