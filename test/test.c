
#include <stdio.h>

int main() {
    // 关闭stdout缓冲，确保输出立即显示
    setvbuf(stdout, NULL, _IONBF, 0);
    
    // 直接在循环中声明变量，减少作用域
    for (int i = 0; i < 10; i++) {
        printf("%d\n", i);
    }
    
    return 0;
}


    keys = {
      { "<leader>llmc", mode = "n", "<cmd>LLMSessionToggle<cr>", desc = " Toggle LLM Chat" },
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
                                 
