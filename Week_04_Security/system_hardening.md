# AWS Systems Manager Patch Manager Lab

## Overview

This lab demonstrates how to use AWS Systems Manager Patch Manager to automate patch management across multiple EC2 instances running different operating systems. The lab covers creating custom patch baselines, using patch groups, and verifying compliance across both Linux and Windows instances.

## Lab Objectives

- Patch Linux instances using default baselines
- Create custom patch baselines for Windows instances
- Use patch groups to organize and patch instances
- Verify patch compliance across the infrastructure

## Environment

The lab environment includes:
- **6 EC2 Instances**:
  - 3 Linux instances (Amazon Linux 2)
  - 3 Windows instances (Windows Server 2019)
- Pre-configured IAM roles for Systems Manager access
- Organized using patch groups: `LinuxProd` and `WindowsProd`

## Architecture

```
AWS Systems Manager
    ├── Patch Manager
    │   ├── Linux Instances (LinuxProd)
    │   │   └── Default Baseline: AWS-AmazonLinux2DefaultPatchBaseline
    │   └── Windows Instances (WindowsProd)
    │       └── Custom Baseline: WindowsServerSecurityUpdates
    ├── Fleet Manager (Node Management)
    └── Run Command (Execution)
```

## Tasks Completed

### Task 1: Patching Linux Instances

Used the default AWS patch baseline to patch Linux instances:
- **Baseline**: AWS-AmazonLinux2DefaultPatchBaseline
- **Operation**: Scan and install
- **Target**: Instances tagged with `Patch Group: LinuxProd`
- **Reboot**: If needed

### Task 2: Creating Custom Windows Patch Baseline

Created a custom patch baseline for Windows security updates:

**Baseline Name**: `WindowsServerSecurityUpdates`

**Approval Rules**:
1. **Critical Security Updates**
   - Product: Windows Server 2019
   - Severity: Critical
   - Classification: SecurityUpdates
   - Auto-approval: 3 days
   - Compliance: Critical

2. **Important Security Updates**
   - Product: Windows Server 2019
   - Severity: Important
   - Classification: SecurityUpdates
   - Auto-approval: 3 days
   - Compliance: High

### Task 3: Patching Windows Instances

Tagged Windows instances and applied the custom patch baseline:
- Tagged all Windows instances with `Patch Group: WindowsProd`
- Associated the custom baseline with the patch group
- Executed scan and install operation
- Monitored execution through Run Command

### Task 4: Compliance Verification

Verified patch compliance across all instances:
- Reviewed compliance dashboard showing all 6 instances as compliant
- Checked compliance reporting for detailed status
- Examined individual patch details and installation times

## Key Concepts

### Patch Baselines
Define which patches should be approved for installation on your instances. AWS provides default baselines, or you can create custom baselines for specific requirements.

### Patch Groups
Tag-based grouping system that associates instances with specific patch baselines, enabling organized patch management across different environments or OS types.

### Compliance Reporting
Tracks and reports on:
- Critical noncompliant count
- Security noncompliant count
- Other noncompliant count
- Last operation date
- Baseline ID used

## AWS Services Used

- **AWS Systems Manager**
  - Patch Manager
  - Fleet Manager
  - Run Command
  - State Manager
- **Amazon EC2**
- **AWS IAM** (for Systems Manager permissions)

## Results

✅ All 6 instances successfully patched and compliant
- 3 Linux instances patched with default baseline
- 3 Windows instances patched with custom security baseline
- Zero noncompliant instances
- Automated patch deployment with minimal manual intervention

## Best Practices Demonstrated

1. **Separation of Concerns**: Different patch baselines for different operating systems
2. **Automation**: Using patch groups and tags for automated targeting
3. **Security Focus**: Custom baseline prioritizing security updates
4. **Compliance Tracking**: Regular monitoring and reporting of patch status
5. **Controlled Rollout**: Auto-approval delays allowing for testing periods

## Lab Duration

Approximately 60 minutes

## Prerequisites

- AWS account with appropriate permissions
- Basic understanding of AWS Systems Manager
- Familiarity with EC2 instances
- Understanding of patch management concepts

## Notes

- The lab uses pre-configured IAM roles that grant Systems Manager the necessary permissions to manage EC2 instances
- Patch Manager leverages the Run Command feature to execute the `PatchBaselineOperations` SSM document
- Instances are automatically rebooted if needed after patching

## Cleanup

When finished with the lab, ensure to:
- Stop or terminate EC2 instances to avoid charges
- Remove custom patch baselines if no longer needed
- Delete any associated SSM documents or maintenance windows

## Additional Resources

- [AWS Systems Manager Documentation](https://docs.aws.amazon.com/systems-manager/)
- [Patch Manager Documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)
- [SSM Best Practices](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-best-practices.html)

---

**Lab Completed**: Successfully demonstrated enterprise-level patch management using AWS Systems Manager