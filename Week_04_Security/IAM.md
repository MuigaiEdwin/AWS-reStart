# AWS Identity and Access Management (IAM) Lab

A hands-on lab exploring user management, access control, and policy enforcement in AWS using Identity and Access Management (IAM).

## Overview

This project demonstrates the implementation of access control and authentication procedures in AWS environments. The lab covers creating custom password policies, managing IAM users and user groups, and applying granular permissions through IAM policies to control access to AWS resources like EC2 and S3.

## Technologies Used

- **AWS IAM** - Identity and Access Management for user and permission management
- **AWS EC2** - Elastic Compute Cloud for compute resource testing
- **AWS S3** - Simple Storage Service for storage resource testing
- **IAM Policies** - Managed and inline policies for access control
- **IAM User Groups** - Logical grouping for efficient permission management

## Lab Objectives

- ✅ Create and apply a custom IAM password policy
- ✅ Explore pre-created IAM users and user groups
- ✅ Inspect IAM policies applied to user groups
- ✅ Add users to user groups with specific capabilities
- ✅ Locate and use the IAM sign-in URL
- ✅ Experiment with the effects of policies on service access

## Architecture

### IAM Structure

```
AWS Account
├── Password Policy (Custom)
├── Users
│   ├── user-1 → S3-Support Group
│   ├── user-2 → EC2-Support Group
│   └── user-3 → EC2-Admin Group
└── User Groups
    ├── S3-Support (AmazonS3ReadOnlyAccess)
    ├── EC2-Support (AmazonEC2ReadOnlyAccess)
    └── EC2-Admin (EC2-Admin-Policy - Inline)
```

## Business Scenario

The lab simulates a growing company using AWS services with different staff roles requiring varying levels of access:

| User | Group | Permissions |
|------|-------|-------------|
| user-1 | S3-Support | Read-only access to Amazon S3 |
| user-2 | EC2-Support | Read-only access to Amazon EC2 |
| user-3 | EC2-Admin | View, start, and stop EC2 instances |

## Key Concepts

### IAM Components

**IAM Users**
- Individual identities with unique security credentials
- Can be assigned individual permissions or group memberships

**IAM User Groups**
- Collections of users requiring access to the same resources
- Efficiently distribute privileges to entire groups
- Changes to group permissions automatically apply to all members

**IAM Policies**
- Define allowed or denied actions for AWS resources
- Two types: Managed policies and Inline policies

### Policy Types

**Managed Policies**
- Pre-built policies (AWS-managed or customer-managed)
- Can be attached to multiple users and groups
- Updates automatically apply to all attached entities

**Inline Policies**
- Custom policies assigned to a single user or group
- Used for one-off permission requirements
- Directly embedded in the user or group

## Lab Tasks

### Task 1: Create Account Password Policy

Configured a custom password policy with enhanced security requirements:

```
Requirements:
✓ Minimum password length: 10 characters (increased from 8)
✓ Require at least one uppercase letter
✓ Require at least one lowercase letter
✓ Require at least one number
✓ Require at least one non-alphanumeric character
✓ Enable password expiration: 90 days
✓ Prevent password reuse: 5 passwords
✗ Password expiration requires administrator reset (disabled)
```

### Task 2: Explore Users and User Groups

Examined pre-created IAM resources:

**Users Created:**
- user-1, user-2, user-3 (all with console passwords)

**User Groups and Policies:**

1. **EC2-Support Group**
   - Policy: `AmazonEC2ReadOnlyAccess` (Managed)
   - Permissions: List and describe EC2, ELB, CloudWatch, Auto Scaling
   - Use case: Support role with view-only access

2. **S3-Support Group**
   - Policy: `AmazonS3ReadOnlyAccess` (Managed)
   - Permissions: Get and list S3 resources
   - Use case: Storage support with read-only access

3. **EC2-Admin Group**
   - Policy: `EC2-Admin-Policy` (Inline)
   - Permissions: View, start, and stop EC2 instances
   - Use case: EC2 administrator with limited control actions

### Task 3: Add Users to User Groups

Assigned users to appropriate groups based on job function:

```bash
# User assignments
user-1 → S3-Support group
user-2 → EC2-Support group
user-3 → EC2-Admin group
```

### Task 4: Sign In and Test User Permissions

Verified permission enforcement through hands-on testing:

#### Test Results

**user-1 (S3-Support)**
- ✅ Can view S3 buckets and contents
- ❌ Cannot view EC2 instances
- Error: "You are not authorized to perform this operation"

**user-2 (EC2-Support)**
- ✅ Can view EC2 instances
- ❌ Cannot stop EC2 instances
- ❌ Cannot view S3 buckets
- Error: "Failed to stop the instance"

**user-3 (EC2-Admin)**
- ✅ Can view EC2 instances
- ✅ Can stop EC2 instances
- ✅ Successfully stopped instance

## IAM Policy Structure

```json
{
  "Effect": "Allow | Deny",
  "Action": [
    "service:Action"
  ],
  "Resource": "arn:aws:service:region:account:resource"
}
```

### Policy Components

| Element | Description | Example |
|---------|-------------|---------|
| **Effect** | Whether to Allow or Deny permissions | `Allow`, `Deny` |
| **Action** | API calls allowed against AWS service | `cloudwatch:ListMetrics` |
| **Resource** | Scope of entities covered by the rule | `*`, specific ARN |

## IAM Sign-In Process

1. Locate IAM sign-in URL in IAM Dashboard
   ```
   Format: https://[ACCOUNT-ID].signin.aws.amazon.com/console
   ```

2. Open private/incognito browser window

3. Navigate to sign-in URL

4. Enter IAM credentials:
   - IAM user name
   - Password

## Security Best Practices Implemented

- ✅ Strong password policy with complexity requirements
- ✅ Principle of least privilege (minimal necessary permissions)
- ✅ Group-based permission management for scalability
- ✅ Separation of duties (different access levels by role)
- ✅ Regular password expiration and reuse prevention
- ✅ Read-only access for support roles
- ✅ Limited administrative privileges

## Use Cases

### When to Use IAM User Groups

✅ **Use Groups When:**
- Multiple users need identical permissions
- Role-based access control is required
- Permissions need centralized management
- Organization has defined job functions

❌ **Use Individual Permissions When:**
- One-time special access is needed
- User requires unique permission set
- Temporary exception to group policy

### Managed vs. Inline Policies

**Managed Policies:**
- Reusable across multiple users/groups
- Easier to manage at scale
- Version controlled by AWS
- Best for standard permissions

**Inline Policies:**
- Strict one-to-one relationship
- Deleted when user/group is deleted
- Best for exceptional situations
- More granular control

## Common IAM Errors

| Error | Cause | Solution |
|-------|-------|----------|
| "You are not authorized to perform this operation" | Missing required permissions | Add user to appropriate group or attach policy |
| "Failed to stop the instance" | Read-only access only | Grant additional permissions or change to admin group |
| "You don't have permissions to list buckets" | No S3 permissions | Add S3 policy to user or group |

## Learning Outcomes

Through this lab, I gained hands-on experience with:
- Creating and enforcing password policies at the AWS account level
- Understanding the difference between managed and inline IAM policies
- Implementing group-based access control for efficient permission management
- Testing and verifying permission boundaries through practical scenarios
- Applying the principle of least privilege in AWS environments
- Managing access control for multiple AWS services (EC2, S3)
- Troubleshooting authorization issues in AWS

## Prerequisites

- AWS Account with IAM administrative access
- Basic understanding of AWS services (EC2, S3)
- Understanding of access control concepts
- Web browser supporting private/incognito mode

## Duration

Approximately 60 minutes

## Cleanup

To avoid charges (if running outside lab environment):
- Remove test users
- Delete custom user groups
- Remove inline policies
- Reset password policy to defaults

## References

- [AWS IAM Documentation](https://docs.aws.amazon.com/iam/)
- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [IAM Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)
- [AWS Security Best Practices](https://aws.amazon.com/architecture/security-identity-compliance/)

## Related Labs

- AWS Organizations and Multi-Account Management
- AWS Single Sign-On (SSO) Configuration
- AWS Security Token Service (STS) and Temporary Credentials
- AWS CloudTrail for IAM Activity Monitoring

## License

This is an educational lab project for learning AWS Identity and Access Management.

---

**Note**: This lab was completed as part of AWS training. Users, groups, and permissions shown are for demonstration purposes in a controlled lab environment. Always follow your organization's security policies when implementing IAM in production.