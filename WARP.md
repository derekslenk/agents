# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This repository contains 83 specialized AI subagents for Claude Code, providing domain-specific expertise across software development, infrastructure, and business operations. Each agent is a Markdown file with frontmatter defining its capabilities, model assignment, and system prompt.

## Common Development Tasks

### Basic Repository Operations
```bash
# Clone the repository to Claude agents directory
cd ~/.claude
git clone https://github.com/derekslenk/agents.git

# View all available agents
ls *.md | grep -v README | grep -v WARP

# Count agents by category
find . -name "*.md" -not -name "README.md" -not -name "WARP.md" | wc -l

# Search for agents by capability
grep -l "description.*API" *.md
grep -l "model: sonnet" *.md
```

### Agent Development and Validation
```bash
# Validate agent frontmatter format
head -10 *.md | grep -E "^---$|^name:|^description:|^model:"

# Check for consistent naming convention
ls *.md | grep -v "^[a-z].*-[a-z].*\.md$"

# Find agents missing model specifications
grep -L "model:" *.md

# Validate agent descriptions for clarity
grep "description:" *.md | head -20
```

### Git Workflow Commands
```bash
# Create new agent (use template approach)
cp backend-architect.md new-agent.md
# Edit frontmatter and content

# Check changes before commit
git diff --name-only
git diff *.md

# Commit with descriptive message
git add new-agent.md
git commit -m "Add new-agent for [specific domain]"
```

## Architecture and Structure

### Agent File Structure
Each agent follows this standardized format:
```markdown
---
name: agent-name
description: Activation criteria and capabilities summary
model: haiku|sonnet|opus
tools: optional_tool_restrictions
---

System prompt defining expertise, capabilities, and behavioral traits
```

### Model Distribution Strategy
The repository uses a three-tier model assignment strategy:

**Haiku (11 agents)**: Quick, focused tasks
- Context management, reference building
- SEO optimization tasks
- Simple automation and search

**Sonnet (63 agents)**: Standard development and analysis tasks
- Language-specific programming agents
- Frontend/UI development
- Infrastructure and testing
- Business operations
- Documentation and content creation
- Database operations and optimization

**Opus (9 agents)**: Complex reasoning and critical analysis
- Core system architecture (backend-architect, cloud-architect)
- Critical security analysis (security-auditor, code-reviewer)
- Advanced AI/ML engineering (ai-engineer, prompt-engineer, mlops-engineer)
- Production incident response (incident-responder)
- Financial modeling and quantitative analysis (quant-analyst)

### Agent Categories Architecture

**Specialization Hierarchy:**
1. **Core Architecture** - System and API design agents
2. **Programming Languages** - Technology-specific implementation agents  
3. **Infrastructure & Operations** - DevOps, deployment, and monitoring agents
4. **Quality Assurance** - Testing, security, and performance agents
5. **Data & AI** - Machine learning and data engineering agents
6. **Documentation** - Technical writing and API documentation agents
7. **Business Operations** - Analytics, marketing, and legal agents
8. **Specialized Domains** - Niche technology and industry-specific agents

### Multi-Agent Orchestration Patterns

**Sequential Processing:** `backend-architect → frontend-developer → test-automator → security-auditor`

**Parallel Execution:** `performance-engineer + database-optimizer → Merged analysis`

**Conditional Routing:** `debugger → [backend-architect | frontend-developer | devops-troubleshooter]`

**Validation Pipeline:** `payment-integration → security-auditor → Validated implementation`

## Agent Usage Guidelines

### Automatic Agent Selection
Claude Code automatically selects appropriate agents based on:
- Task context and domain
- Technology stack mentioned
- Complexity requirements
- Quality standards needed

### Explicit Agent Invocation
Use specific agent names for targeted expertise:
```bash
# Security-focused code review
"Use security-auditor to analyze this authentication implementation"

# Performance optimization
"Have performance-engineer profile this database query"

# Architecture validation
"Get architect-reviewer to validate this microservice design"
```

### Common Agent Combinations

**Full-Stack Feature Development:**
```bash
"Implement user authentication system"
# Activates: backend-architect → frontend-developer → test-automator → security-auditor
```

**Production Incident Response:**
```bash
"Debug high memory usage in production"
# Activates: incident-responder → devops-troubleshooter → error-detective → performance-engineer
```

**ML Pipeline Setup:**
```bash
"Build ML pipeline with monitoring" 
# Activates: mlops-engineer → ml-engineer → data-engineer → observability-engineer
```

## Development Best Practices

### Agent Creation Guidelines
- Use lowercase, hyphen-separated naming (`new-agent-name.md`)
- Write clear activation criteria in description
- Assign appropriate model based on task complexity
- Define 8-12 specific capability areas
- Include behavioral traits and response patterns
- Provide concrete examples and use cases

### Agent Maintenance
- Keep expertise current with 2024/2025 practices
- Maintain consistency with existing agent patterns  
- Test activation criteria with realistic scenarios
- Update model assignments based on performance
- Validate frontmatter format and required fields

### Quality Assurance
- Ensure agent descriptions clearly define when to activate
- Verify no overlap in primary specializations
- Test multi-agent workflows for coordination
- Validate model assignments match complexity
- Check examples reflect real-world usage

## Integration with Claude Code

### Commands Integration
This repository integrates with [Claude Code Commands](https://github.com/wshobson/commands) for sophisticated multi-agent orchestration:

```bash
/full-stack-feature   # Coordinates 8+ agents for complete feature development
/incident-response    # Activates incident management workflow  
/ml-pipeline         # Sets up end-to-end ML infrastructure
/security-hardening  # Implements security best practices across stack
```

### Agent Activation Context
Agents activate based on:
- Technology keywords in requests
- Problem domain indicators
- Task complexity signals
- Quality requirement mentions
- Explicit agent naming

### TDD Workflow Support
Special support for Test-Driven Development via:
- `tdd-orchestrator` for workflow management
- `test-automator` for test generation
- Language-specific agents for implementation
- `code-reviewer` for refactoring guidance

## Project-Specific Rules

### Agent Selection Priority
1. **Domain Specificity** - Choose most specialized agent for the task
2. **Technology Alignment** - Match agent expertise to tech stack
3. **Complexity Matching** - Use appropriate model tier for task difficulty
4. **Quality Requirements** - Engage security/performance agents as needed

### Multi-Agent Coordination
- Trust automatic orchestration for complex tasks
- Use explicit combinations for specialized workflows
- Allow agents to coordinate context and handoffs
- Review integration points between agent outputs

### Performance Optimization
- Monitor agent selection effectiveness for your use cases
- Refine request phrasing to improve automatic selection
- Use direct naming when automatic selection fails
- Track which agent combinations work best for your projects

## Troubleshooting

### Agent Not Activating
- Check if request clearly indicates the target domain
- Include specific technology or problem type keywords  
- Try explicit agent naming: "Use [agent-name] to..."

### Unexpected Agent Selection
- Provide more context about technology stack and requirements
- Use explicit agent invocation for precise control
- Consider if the unexpected agent might have relevant expertise

### Agent Conflicts or Inconsistencies
- Normal behavior - specialists have different priorities and approaches
- Request reconciliation between specific agents when needed
- Consider trade-offs based on your specific project requirements

### Missing Context Between Agents
- Include background information and project constraints in requests
- Reference previous work or established patterns
- Provide examples of desired outcomes and approaches