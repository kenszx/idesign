# Pipeline Workspace — 临时工作区

> 此目录内容为每次运行的临时产物，已在 .gitignore 中排除。
> 但 `iteration_log.md` 保留以支持跨会话断点续传。

## 目录说明

| 文件 | 来源 | 说明 |
|------|------|------|
| `current_design.json` | Planner Agent | 设计蓝图（配色/字体/页大纲） |
| `selected_theme.css` | Phase 1 | 用户选择的 tokens.css |
| `output.md` / `output.html` | Executor Agent | Marp/HTML 源码 |
| `screenshot.png` | Playwright | 供 Critic 审查 |
| `review_result.json` | Critic Agent | PASS 或修改指令 |
| `final_output.pptx` | Marp CLI | 最终交付的 PPTX |
| `iteration_log.md` | 全部 | **跨会话断点续传日志** |
