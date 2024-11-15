#!/bin/bash

# Check if WSL is available
if ! command -v powershell.exe &> /dev/null
then
    echo "PowerShell is not available. Please make sure you are running under WSL or have PowerShell installed."
    exit 1
fi

# Path to registry keys
KEY_PATH="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens"
REG_FILE_ORIG="voices_backup_orig.reg"

# Export current voice registry
echo "Exporting current voices registry to: $REG_FILE_ORIG"
powershell.exe -Command "reg export '$KEY_PATH' '$REG_FILE_ORIG' /y"

# Modify registry file using bash commands
# This will replace the first and second paths to unlock voices system-wide
echo "Modifying registry file..."

sed \
-e 's|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens|g' \
-e 's|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens|HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\SPEECH\Voices\Tokens|g' \
"$REG_FILE"

# Import the modified registry data
echo "Importing modified registry..."
echo powershell.exe -Command "reg import '$REG_FILE'"

# Suggest restarting or signing off
echo "To finalize the changes, please sign off and sign back in, or restart the PC."
