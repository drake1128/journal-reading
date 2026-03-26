# Claude Code Tutorial

**整理：謝慕揚 MD, PhD, FESC**
**日期：2026-03-26**

---

Best Practices and Tips for AI-Powered Coding
Based on Builder.io Video Tutorial
January 28, 2026
Abstract
This tutorial provides a comprehensive guide to using Claude Code, Anthropic’s offi-
cial CLI tool for AI-assisted coding. Based on real-world experience from developers who
have switched from other AI coding tools, this guide covers installation, configuration, best
practices, and advanced features to maximize your productivity with Claude Code. Contents
Introduction
1.1
Why Claude Code? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Installation and Setup
2.1
VS Code Extension . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2
Automatic Context . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Terminal Interface Basics
3.1
Essential Keyboard Shortcuts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2
File and Image Handling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.1
Dragging Files
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.2
Pasting Images . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Model Selection
4.1
Available Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2
Switching Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3
Model Comparison . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Essential Slash Commands
5.1
The /clear Command
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2
Common Slash Commands
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Permission Management
6.1
The Permission Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2
Dangerously Skip Permissions Mode . . . . . . . . . . . . . . . . . . . . . . . . . 6.3
Recommended Workflow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . GitHub Integration
7.1
Installing the GitHub App . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2
Configuring Code Reviews . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.3
Benefits of AI Code Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


Claude Code Tutorial
Contents
Message Queuing
8.1
How Queuing Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2
Example Workflow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.3
Benefits Over Traditional Workflow . . . . . . . . . . . . . . . . . . . . . . . . . . Custom Configuration
9.1
The CLAUDE.md File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.2
Custom Hooks
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.3
Custom Slash Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.3.1
Command File Structure
. . . . . . . . . . . . . . . . . . . . . . . . . . . 9.4
Memory Management
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 Pricing and Plans
10.1 Subscription Tiers
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10.2 Value Proposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10.3 Why Direct Pricing Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 Why Claude Code Excels
11.1 Technical Advantages
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11.2 Real-World Performance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11.3 Compared to Other Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 Visual Interface Alternative
12.1 Fusion by Builder.io
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12.2 Use Cases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 Best Practices Summary
13.1 Daily Workflow Checklist
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13.2 Productivity Tips . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13.3 Common Pitfalls to Avoid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14 Quick Reference Card
15 Conclusion
Additional Resources


Claude Code Tutorial
Terminal Interface Basics
Introduction
Claude Code is a terminal-based AI coding assistant developed by Anthropic. Unlike other AI
coding tools that support multiple models, Claude Code is built specifically for Claude models,
allowing for deep integration and optimization between the tool and the underlying AI. Info
Claude Code works directly with Anthropic’s models, eliminating the middleman and
providing maximum performance at competitive pricing. 1.1
Why Claude Code?
Key advantages of Claude Code include:
• Large File Handling: Reliably updates files with 18,000+ lines of code
• Complex Codebase Navigation: Excellent at searching patterns and understanding re-
lationships
• Consistency: Rarely gets stuck compared to other AI coding tools
• Direct Integration: Built by the same team that creates the underlying models
• Cost Efficiency: No middleman markup on API costs
Installation and Setup
2.1
VS Code Extension
Claude Code has an official extension that works with:
• Visual Studio Code
• Cursor
• Windsurf
• Other VS Code forks
Tip
The extension makes it easy to launch Claude Code directly in your IDE. You can have
multiple Claude Code panes open simultaneously to work on different parts of your code-
base in parallel. 2.2
Automatic Context
When you have a file open in your editor, Claude Code automatically pulls it into the context. This seamless integration reduces the friction of manually specifying which files to work with. Terminal Interface Basics
Claude Code uses a terminal UI, which may seem unfamiliar at first but offers powerful func-
tionality once mastered.


Claude Code Tutorial
Model Selection
3.1
Essential Keyboard Shortcuts
Shortcut
Action
Escape
Stop Claude’s current operation
Escape (twice)
View list of previous messages
Up Arrow
Navigate to past chats (including prior sessions)
Shift + Enter
Add new lines in your message
Ctrl + V
Paste images from clipboard
Shift + Drag
Drag files into the terminal
Ctrl + C (twice)
Exit Claude Code (careful!)
Table 1: Essential Claude Code Keyboard Shortcuts
Warning
Do not use Ctrl + C to stop Claude’s work—this will exit the application. Use Escape
instead. 3.2
File and Image Handling
3.2.1
Dragging Files
In VS Code/Cursor, dragging a file normally opens it in a new tab. To reference a file in Claude
Code:
1. Hold Shift
2. Drag the file into the Claude Code terminal
3. The file will be referenced in your conversation
3.2.2
Pasting Images
Standard Cmd + V (Mac) does not paste images. Instead:
Use Ctrl + V to paste
images
from
clipboard
Model Selection
4.1
Available Models
Claude Code supports multiple Claude models:
• Opus: The most capable model, recommended for complex tasks
• Sonnet: More cost-efficient, good for general tasks
4.2
Switching Models
Use the /model command to switch between models:
/model
opus
/model
sonnet


Claude Code Tutorial
Permission Management
Tip
The default behavior uses Opus until you reach 50% of your usage limits, then switches
to Sonnet. For most users, this automatic switching is recommended. 4.3
Model Comparison
Aspect
Opus
Sonnet
Capability
Highest
Very Good
Speed
Fast
Fast
Cost
Higher
More Efficient
Use Case
Complex tasks
General tasks
Table 2: Claude Model Comparison
Essential Slash Commands
Claude Code provides numerous slash commands for various operations. 5.1
The /clear Command
/clear
Tip
Clear every time you start something new! You don’t need old chat history con-
suming tokens, and avoiding compaction (which runs additional LLM calls to summarize
history) saves time. 5.2
Common Slash Commands
Command
Description
/clear
Clear conversation history
/model
Switch between AI models
/help
Show available commands
/terminal-setup
Configure terminal settings
Table 3: Common Slash Commands
Permission Management
6.1
The Permission Problem
By default, Claude Code asks for permission to:
• Edit files
• Run bash commands


Claude Code Tutorial
GitHub Integration
• Execute lint/build commands
This can be frustrating when you return to find Claude waiting for permission. 6.2
Dangerously Skip Permissions Mode
To bypass permission prompts:
claude
--dangerously -skip -permissions
Warning
This mode (similar to Cursor’s “YOLO mode”) carries a minor risk of running unexpected
commands. However, in practice, destructive agent behavior is extremely rare. Use at
your own discretion. 6.3
Recommended Workflow
1. Open Claude Code terminal
2. Press Ctrl + C to stop default launch
3. Run: claude –dangerously-skip-permissions
4. Continue with your work uninterrupted
GitHub Integration
7.1
Installing the GitHub App
Claude Code can integrate with GitHub to automatically review pull requests. /install -github -app
7.2
Configuring Code Reviews
After installation, Claude creates a claude-code-review.yaml file. The default configuration
can be verbose, so customize it:
# claude -code -review.yaml
# Focus on what
matters
most
instructions: |
Look for bugs and
security
issues. Only
report on bugs and
potential
vulnerabilities . Be concise. Tip
AI code reviews can catch bugs that humans miss because they apply consistent effort to
every line of code, while humans may skim through familiar patterns.


Claude Code Tutorial
Message Queuing
7.3
Benefits of AI Code Review
• Catches real bugs that humans might miss
• Consistent review quality regardless of PR volume
• Identifies security vulnerabilities
• Reduces nitpicking on style issues (when configured properly)
Message Queuing
One of Claude Code’s most powerful features is the ability to queue messages. 8.1
How Queuing Works
1. Send your first message
2. While Claude is working, type additional messages
3. Messages are queued and processed in order
4. Claude intelligently determines when to process queued items
8.2
Example Workflow
You: Add
comments to the utility
functions
[Claude
starts
working ...]
You: Also add
comments to the main JSX chunks
[Message
queued]
You: And add
comments to the
computed
values
[Message
queued]
[Claude
processes
all tasks
sequentially]
Tip
Claude is smart about queuing—if it needs feedback from you, it won’t automatically
process queued messages. Check in periodically to see if input is needed. 8.3
Benefits Over Traditional Workflow
• No need for a separate notepad to track pending tasks
• Agent doesn’t sit idle waiting for your next prompt
• More efficient use of time—queue tasks and check back later


Claude Code Tutorial
Custom Configuration
Custom Configuration
9.1
The CLAUDE.md File
Create a CLAUDE.md file in your project root to provide Claude with:
• Project overview
• Key commands (build, lint, test)
• Project-specific conventions
# CLAUDE.md
## Project
Overview
This is a React
application
using
TypeScript. ## Key
Commands
- Build: ‘npm run build ‘
- Lint: ‘npm run lint ‘
- Test: ‘npm run test ‘
## Conventions
- Use
functional
components
- Use
Tailwind
CSS for
styling
Tip
CLAUDE.md files can be hierarchical. Place one at the project level and additional ones in
nested directories. Claude prioritizes the most specific (deepest nested) file when relevant. 9.2
Custom Hooks
Hooks allow you to run commands automatically at specific points:
# Before
edits are
accepted
- Run
Prettier on the
specific
file
# After
edits
- Run type
checking on modified
files
9.3
Custom Slash Commands
Create custom commands by adding markdown files to .claude/commands/:
.claude/
commands/
test.md
-> /test
builder/
plugin.md
-> /builder
plugin
9.3.1
Command File Structure


Claude Code Tutorial
Pricing and Plans
# .claude/commands/test.md
Write
unit
tests for the
following
file: $ARGUMENTS
Follow our
testing
conventions:
- Use Jest
- Include
edge
cases
- Mock
external
dependencies
Usage:
/test src/utils/helpers.ts
9.4
Memory Management
Add memories using the # symbol:
#always use Mobx
components
for new stuff
Memory types:
• Global User Memory: Preferences applied everywhere
• Local Project Memory: Project-specific memories (git-ignored)
• CLAUDE.md: Shared project documentation
Pricing and Plans
10.1
Subscription Tiers
Claude Code supports standard Anthropic pricing plans:
• Standard: Basic access with usage limits
• Max: Enhanced limits and Opus access ($100/month)
10.2
Value Proposition
Info
Consider the cost of human engineering time. Even at competitive global rates, AI as-
sistance at $100/month provides extraordinary value compared to the cost per hour of
human engineering work. 10.3
Why Direct Pricing Works
• No middleman markup
• Direct from model creators
• Anthropic can offer maximum model access
• Sustainable pricing model


Claude Code Tutorial
Visual Interface Alternative
Why Claude Code Excels
11.1
Technical Advantages
1. Single Model Focus: Only needs to support Claude models
2. Deep Integration: Tool and model optimized together
3. Continuous Improvement: Model improvements directly benefit Claude Code
4. Expert Knowledge: Built by the team that knows the model best
11.2
Real-World Performance
• Handles 18,000+ line files without issues
• Excellent pattern recognition across large codebases
• Understands relationships between components, state, and files
• Rarely gets stuck or requires babysitting
11.3
Compared to Other Tools
Other AI coding tools:
• Must support multiple models (added complexity)
• Have additional teams and layers
• Don’t control the core AI models
• Must make their own margin on top of API costs
Visual Interface Alternative
For users who prefer a graphical interface, Builder.io offers a visual alternative. 12.1
Fusion by Builder.io
Access at: fusion.builder.io
Features:
• Visual chat interface
• Live preview of changes
• Design mode with Figma-style editing
• Pull request creation from the browser
• Same underlying agent mechanics as Claude Code


Claude Code Tutorial
Conclusion
12.2
Use Cases
• Team members creating prototypes
• Visual editing of UI components
• Bridging design and code workflows
• Browser-based development
Best Practices Summary
13.1
Daily Workflow Checklist
1. Use /clear when starting new tasks
2. Consider using –dangerously-skip-permissions for uninterrupted work
3. Queue multiple related tasks
4. Leverage Opus for complex tasks, Sonnet for simpler ones
5. Configure CLAUDE.md for project-specific context
13.2
Productivity Tips
Tip
• Run multiple Claude Code panes for parallel work on different files
• Use the up arrow to access previous sessions
• Configure GitHub integration for automated PR reviews
• Create custom slash commands for repetitive tasks
• Use message queuing to batch tasks and check back later
13.3
Common Pitfalls to Avoid
Warning
• Don’t use Ctrl + C to stop work (use Escape)
• Don’t keep extensive chat history (use /clear)
• Don’t forget to check queued tasks periodically
• Don’t use Cmd + V for images (use Ctrl + V)
Quick Reference Card
Conclusion
Claude Code represents a significant advancement in AI-assisted coding tools. By combining
deep model integration, powerful terminal-based workflows, and thoughtful features like message
queuing, it enables developers to work more efficiently than ever before.


Claude Code Tutorial
Conclusion
Task
Command/Action
Clear history
/clear
Change model
/model opus or /model sonnet
Skip permissions
claude –dangerously-skip-permissions
Stop Claude
Escape
Exit application
Ctrl + C (twice)
Previous messages
Escape (twice)
Past chats
Up Arrow
New line in message
Shift + Enter
Paste image
Ctrl + V
Drag file in
Shift + Drag
Add memory
#your memory here
Custom command
/command-name arguments
Table 4: Quick Reference Card
The key to success with Claude Code is:
1. Understanding the terminal interface quirks
2. Configuring your environment properly
3. Leveraging advanced features like queuing and custom commands
4. Using the right model for each task
Whether you prefer the terminal interface or a visual alternative, the underlying Claude
technology provides reliable, capable AI assistance for even the most complex coding tasks. Happy coding with Claude!
Additional Resources
• Builder.io Blog: Full list of Claude Code tips
• Fusion Visual Interface: fusion.builder.io
• Claude Code Documentation: docs.anthropic.com
• GitHub: Report issues and feedback
