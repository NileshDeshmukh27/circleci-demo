#!/usr/bin/env python3
import aws_cdk as cdk
from stacks.app_stack import AppStack

app = cdk.App()

AppStack(
    app,
    "CircleciDemoDevStack",
    env=cdk.Environment(
        account=None,  # Uses CDK_DEFAULT_ACCOUNT
        region=None,  # Uses CDK_DEFAULT_REGION
    ),
)

app.synth()
