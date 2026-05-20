# Enterprise AI RCA Demo

## Overview

This project demonstrates an enterprise-style AI Root Cause Analysis (RCA) system using:

* GitHub
* AWS Lambda + CloudWatch Logs
* JIRA
* Slack

The AI agent correlates evidence across multiple enterprise systems to identify the root cause of production failures.

---

# Scenario

A deployment accidentally changed the AWS deployment region from:

```text
ap-south-1
```

to:

```text
us-east-1
```

The deployment technically succeeded, but production traffic continued hitting the old Lambda.

The AI agent must investigate:

* GitHub commits
* Deployment configuration
* AWS Lambda runtime logs
* JIRA tickets
* Slack discussions

and generate a complete RCA.

---

# Architecture

```text
GitHub Repo
    ↓
Deployment Config Change
    ↓
AWS Lambda Deployment
    ↓
CloudWatch Runtime Failure Logs

Additional Context:
- JIRA contains operational warnings
- Slack contains engineering discussions
```

---

# Repository Structure

```text
enterprise-demo/
│
├── lambda_function.py
├── deploy_config.yml
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml
```

---

# Step 1 — Clone Repository

```bash
git clone <your-repository-url>
cd enterprise-demo
```

---

# Step 2 — Lambda Function

File:

```text
lambda_function.py
```

This Lambda validates whether deployment happened in the correct AWS region.

Expected region:

```text
ap-south-1
```

If deployed incorrectly, the Lambda throws an exception.

---

# Step 3 — Deployment Config

File:

```text
deploy_config.yml
```

Correct configuration:

```yaml
env:
  FUNCTION_NAME: dataset-refresh-prod
  AWS_REGION: ap-south-1
```

Buggy configuration:

```yaml
env:
  FUNCTION_NAME: dataset-refresh-prod
  AWS_REGION: us-east-1
```

This configuration drift becomes the root cause.

---

# Step 4 — Git History

The following commit intentionally introduces the deployment issue:

```bash
git commit -m "chore: simplify deployment config"
```

The AI agent later identifies this commit during RCA.

---

# Step 5 — Create AWS Lambda

Go to AWS Lambda Console.

Create function:

```text
dataset-refresh-prod
```

Runtime:

```text
Python 3.12
```

---

# Step 6 — Package Lambda

```bash
zip function.zip lambda_function.py
```

---

# Step 7 — Configure AWS CLI

```bash
aws configure
```

Provide:

* AWS Access Key
* AWS Secret Key
* Default Region

---

# Step 8 — Deploy Lambda

```bash
aws lambda create-function \
  --function-name dataset-refresh-prod \
  --runtime python3.12 \
  --role YOUR_LAMBDA_ROLE_ARN \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip
```

---

# Step 9 — Introduce Deployment Bug

Update Lambda environment variable:

```bash
aws lambda update-function-configuration \
  --function-name dataset-refresh-prod \
  --environment "Variables={AWS_REGION=us-east-1}"
```

Correct value should be:

```text
ap-south-1
```

---

# Step 10 — Invoke Lambda

```bash
aws lambda invoke \
  --function-name dataset-refresh-prod \
  response.json
```

The Lambda now fails intentionally.

---

# Step 11 — View CloudWatch Logs

```bash
aws logs tail /aws/lambda/dataset-refresh-prod --follow
```

Expected logs:

```text
INFO Running in region: us-east-1
ERROR Wrong region detected: us-east-1
Exception: Expected ap-south-1 but got us-east-1
```

These logs become runtime evidence for RCA.

---

# Step 12 — Create JIRA Tickets

Create these tickets manually.

---

## DEPLOY-221

Title:

```text
Verify deployment region before production rollout
```

Description:

```text
Deployment scripts should always deploy to ap-south-1.
Previous incidents occurred due to incorrect region selection.
```

---

## DEPLOY-233

Title:

```text
Production lambda still serving old traffic
```

Description:

```text
Users report stale responses after latest deployment.
```

---

## DEPLOY-219

Title:

```text
Refactor deployment workflow
```

Description:

```text
Simplify deployment pipeline configuration
for multi-region support.
```

---

# Step 13 — Create Slack Discussion

Channel:

```text
#prod-deployments
```

Messages:

```text
DevOps:
Deployment completed successfully.
```

```text
Engineer:
Then why is prod traffic still hitting old lambda?
```

```text
Lead:
Check deployment region maybe?
```

```text
Engineer:
deploy.yml says us-east-1 now.
```

These messages provide human investigation context.

---

# Example Questions For The AI Agent

```text
Why did deployment succeed but production still fail?
```

```text
What changed before the outage started?
```

```text
Did any tickets predict this issue?
```

```text
Summarize Slack discussions related to the outage.
```

```text
Generate complete RCA with supporting evidence.
```

---

# Expected RCA Output

```text
Root Cause:
Deployment workflow accidentally changed AWS region
from ap-south-1 to us-east-1 during deployment refactor.

Impact:
Production traffic continued routing to old Lambda.

Evidence:
- GitHub deployment config change
- Lambda logs showing runtime in us-east-1
- JIRA warning about deployment region validation
- Slack investigation discussion

Recommended Fix:
Restore deployment region to ap-south-1 and add
region validation checks during deployment.
```

---

# Technologies Used

* GitHub
* AWS Lambda
* CloudWatch Logs
* JIRA
* Slack
* Python

---

# Step-by-Step Execution Flow

Follow these steps in order to reproduce the scenario.

---

## 1. Create GitHub Repository

Create a GitHub repository:

```text
dataset-refresh-service
```

Clone locally:

```bash
git clone <repo-url>
cd dataset-refresh-service
```

---

## 2. Create Lambda Function File

Create:

```text
lambda_function.py
```

Add:

```python
def lambda_handler(event, context):

    customer_id = event.get("customer_id")

    if customer_id is None:
        raise Exception("Invalid payload")

    return {
        "statusCode": 200
    }
```

---

## 3. Initialize Git Repository

```bash
git init
git add .
git commit -m "add dataset refresh lambda"
```

---

## 4. Add Logging Cleanup Commit

Create another commit to simulate observability cleanup:

```bash
git commit --allow-empty -m "cleanup verbose logging"
```

This becomes RCA evidence for the AI agent.

---

## 5. Create AWS Lambda

Open AWS Lambda Console.

Create Lambda:

```text
dataset-refresh-prod
```

Runtime:

```text
Python 3.12
```

---

## 6. Package Lambda

```bash
zip function.zip lambda_function.py
```

---

## 7. Upload Lambda Code

Upload:

```text
function.zip
```

inside AWS Lambda.

---

## 8. Invoke Lambda

Use test payload:

```json
{}
```

This intentionally causes failure.

---

## 9. View CloudWatch Logs

Open CloudWatch Logs for:

```text
/aws/lambda/dataset-refresh-prod
```

Expected output:

```text
Exception: Invalid payload
```

Notice:

* no request tracing
* no customer_id
* no debugging information

This is the observability issue.

---

## 10. Create JIRA Ticket

Create ticket:

### OBS-221

Title:

```text
Reduce excessive Lambda logging costs
```

Description:

```text
Remove unnecessary INFO logs from dataset refresh Lambda.
```

Status:

```text
Done
```

---

## 11. Create Slack Discussion

Channel:

```text
#prod-incidents
```

Messages:

```text
Engineer:
Hard to debug Lambda failures now.
```

```text
SRE:
Looks like logging cleanup removed traces.
```

```text
Lead:
Need important logs restored.
```

---

## 12. Ask AI RCA Questions

Example questions:

```text
Why are Lambda failures difficult to debug?
```

```text
Which recent commit affected observability?
```

```text
Generate complete RCA with supporting evidence.
```

---

# Goal Of This Demo

This project demonstrates how enterprise AI systems can:

* correlate evidence across systems
* perform automated RCA
* understand deployment context
* analyze operational discussions
* generate incident summaries

similar to enterprise observability and incident intelligence platforms.
