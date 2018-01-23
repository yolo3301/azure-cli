# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import


helps['container'] = """
    type: group
    short-summary: (PREVIEW) Manage Azure Container Instances.
"""

helps['container create'] = """
    type: command
    short-summary: Create a container group.
    examples:
        - name: Create a container in a container group with 1 core and 1Gb of memory.
          text: az container create -g MyResourceGroup --name myalpine --image alpine:latest --cpu 1 --memory 1
        - name: Create a container in a container group that runs Windows, with 2 cores and 3.5Gb of memory.
          text: az container create -g MyResourceGroup --name mywinapp --image winappimage:latest --os-type Windows --cpu 2 --memory 3.5
        - name: Create a container in a container group with public IP address and ports.
          text: az container create -g MyResourceGroup --name myalpine --image alpine:latest --ip-address public --ports 80 443
        - name: Create a container in a container group that invokes a script upon start.
          text: az container create -g MyResourceGroup --name myalpine --image alpine:latest --command-line "/bin/sh -c '/path to/myscript.sh'"
        - name: Create a container in a container group that runs a command and stop the container afterwards.
          text: az container create -g MyResourceGroup --name myalpine --image alpine:latest --command-line "echo hello" --restart-policy Never
        - name: Create a container in a container group with environment variables.
          text: az container create -g MyResourceGroup --name myalpine --image alpine:latest -e key1=value1 key2=value2
        - name: Create a container in a container group using container image from Azure Container Registry.
          text: az container create -g MyResourceGroup --name myalpine --image myAcrRegistry.azurecr.io/alpine:latest --registry-password password
        - name: Create a container in a container group using container image from another private container image registry.
          text: az container create -g MyResourceGroup --name myapp --image myimage:latest --cpu 1 --memory 1.5 --registry-login-server myregistry.com --registry-username username --registry-password password
        - name: Create a container in a container group that mounts an Azure File share as volume.
          text: az container create -g MyResourceGroup --name myapp --image alpine:latest --command-line "cat /mnt/azfile/myfile" --azure-file-volume-share-name myshare --azure-file-volume-account-name mystorageaccount --azure-file-volume-account-key mystoragekey --azure-file-volume-mount-path /mnt/azfile
"""

helps['container delete'] = """
    type: command
    short-summary: Delete a container group.
"""

helps['container list'] = """
    type: command
    short-summary: List container groups.
"""

helps['container show'] = """
    type: command
    short-summary: Get the details of a container group.
"""

helps['container logs'] = """
    type: command
    short-summary: Examine the logs for a container group.
"""

helps['container attach'] = """
    type: command
    short-summary: Attach (not interactively) to a container in a container group.
"""
